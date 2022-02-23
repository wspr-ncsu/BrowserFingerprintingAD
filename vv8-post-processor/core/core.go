package core

// -------------------------------------------------------------------------------------
// generic vv8 log file parsing and context-awareness framework for aggregation
// -------------------------------------------------------------------------------------

import (
	"bufio"
	"crypto/sha256"
	"database/sql"
	"fmt"
	"io"
	"log"
	"strconv"
	"strings"

	"github.com/lib/pq"

	"golang.org/x/crypto/sha3"
	"gopkg.in/mgo.v2/bson"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "jane_doe"
	password = "never_gonna_give_you_up"
	dbname   = "experiment2"
)

type SourceC struct {
	ScriptName string   `gorm:"type:TEXT"`
	ID         int      `gorm:"type:INT"`
	OriName    string   `gorm:"type:TEXT"`
	DomName    string   `gorm:"type:TEXT"`
	Code       string   `gorm:"type:TEXT"`
	APIs       []string `gorm:"type:TEXT[]"`
}

type SourceList struct {
	sclist []SourceC
}

func (slist *SourceList) appendScirpt(source SourceC) []SourceC {
	slist.sclist = append(slist.sclist, source)
	return slist.sclist
}

func (source *SourceC) appendAPI(api string) []string {
	source.APIs = append(source.APIs, api)
	return source.APIs
}

func (source *SourceC) appendAPIs(apis []string) []string {
	source.APIs = append(source.APIs, apis...)
	return source.APIs
}

// Take a raw log string, expand all escape sequences, and split it into fields
func splitFields(line []byte) []string {
	allFields := make([]string, 0, 8)
	var curField strings.Builder
	var curDigs strings.Builder
	var surrogatePairFirst int

	type State int
	const (
		Copy  State = iota
		Copy2       // Special copy-char state indicating we JUST processed a ':' field separator
		Esc
		Hex
		Uni
	)

	state := Copy
	surrogatePairFirst = -1
	for _, c := range line {
		switch state {
		case Copy:
			if c == '\\' {
				state = Esc
			} else if c == ':' {
				allFields = append(allFields, curField.String())
				curField.Reset()
				state = Copy2
			} else {
				curField.WriteByte(c)
			}
		case Copy2:
			if c == '\\' {
				state = Esc
			} else if c == ':' {
				allFields = append(allFields, "")
			} else {
				curField.WriteByte(c)
				state = Copy
			}
		case Esc:
			if c == 'x' {
				state = Hex
				curDigs.Reset()
			} else if c == 'u' {
				state = Uni
				curDigs.Reset()
			} else {
				curField.WriteByte(c)
				state = Copy
			}
		case Hex:
			curDigs.WriteByte(c)
			if curDigs.Len() == 2 {
				code, _ := strconv.ParseUint(curDigs.String(), 16, 8)
				curField.WriteRune(rune(code))
				state = Copy
			}
		case Uni:
			curDigs.WriteByte(c)
			if curDigs.Len() == 4 {
				// A 16-bit Unicode codepoint--how hard could it be?
				rcode, _ := strconv.ParseUint(curDigs.String(), 16, 16)
				code := int(rcode)

				// Oh the joys of UTF16...
				if surrogatePairFirst >= 0 {
					code = (code - 0xdc00) + surrogatePairFirst + 0x10000
					surrogatePairFirst = -1
				}
				if (code >= 0xd800) && (code <= 0xdfff) {
					surrogatePairFirst = (code - 0xd800) * 0x400
				} else {
					curField.WriteRune(rune(code))
				}
				state = Copy
			}
		}
	}
	// Add on one last field if:
	// * there is trailing data (normal case)
	// * we ended on a ':' separator (corner case)
	if (curField.Len() > 0) || (state == Copy2) {
		allFields = append(allFields, curField.String())
	}

	return allFields
}

// NewLogInfo constructs a fresh LogInfo for the given vv8log Mongo oid (if available) and root log filename (if available)
func NewLogInfo(oid bson.ObjectId, rootName string) *LogInfo {
	return &LogInfo{
		ID:       oid,
		RootName: rootName,
		Isolates: make(map[string]*IsolateInfo),
	}
}

func (ln *LogInfo) changeIsolate(id string) *IsolateInfo {
	iso, ok := ln.Isolates[id]
	if !ok {
		iso = NewIsolateInfo(id)
		ln.Isolates[id] = iso
	}
	ln.World = iso
	ln.World.resetContext()
	return iso
}

func (ln *LogInfo) resetContext() {
	ln.World.resetContext()
}

func (ln *LogInfo) addScript(id int, src string, code string) *ScriptInfo {
	script, ok := ln.World.Scripts[id]
	if !ok {
		script = NewScriptInfo(ln.World, id, code, ln.World.Context.Origin)

		// Determine source: URL or eval-parent?
		parentID, err := strconv.Atoi(src)
		if err != nil {
			// A string
			src, _ = StripQuotes(src)

			// URL-based script
			script.setURL(src)

			// Special case: is this a visible-v8:// script? (or a puppeteer-eval'd script?)
			if strings.HasPrefix(src, "visible-v8://") || strings.HasSuffix(code, "//# sourceURL=__puppeteer_evaluation_script__\n)") {
				script.VisibleV8 = true

				// Special-special case: does this script name end in "/id.js", indicating it's our job id?
				if strings.HasSuffix(src, "/id.js") {
					job := src[13 : len(src)-6]
					if ln.Job != "" {
						panic(fmt.Errorf("new vv8 job ID '%s' (previous one '%s')", job, ln.Job))
					}
					ln.Job = job
					log.Printf("picked up job ID '%s'", job)
					if bson.IsObjectIdHex(job) {
						ln.PageID = bson.ObjectIdHex(job)
						log.Printf("interpreting job ID as PageID (new schema)")
					}
				}
			}
		} else {
			var parentScript *ScriptInfo
			parentScript, ok = ln.World.Scripts[parentID]
			if !ok {
				panic(fmt.Errorf("unknown parent script ID %d in isolate %s", parentID, ln.World.ID))
			}
			script.setEvaledBy(parentScript)
			script.VisibleV8 = parentScript.VisibleV8
		}

		ln.World.Scripts[id] = script
	} else {
		panic(fmt.Errorf("redefining script ID %d in isolate %s", id, ln.World.ID))
	}
	return script
}

func (ln *LogInfo) changeScript(id int) {
	script, ok := ln.World.Scripts[id]
	if !ok {
		panic(fmt.Errorf("changing to undefined script ID %d in isolate %s", id, ln.World.ID))
	}
	ln.World.Context.Script = script
}

func (ln *LogInfo) changeOrigin(url string) {
	ln.World.Context.Origin = url
}

// NewIsolateInfo constructs a fresh, empty IsolateInfo for a given hex-string pointer tag
func NewIsolateInfo(id string) *IsolateInfo {
	return &IsolateInfo{
		ID:      id,
		Scripts: make(map[int]*ScriptInfo)}
}

func (iso *IsolateInfo) resetContext() {
	iso.Context.Script = nil
}

// ScriptHash was originally just an alias for SHA2-256 digest, but then we discovered collisions; now it's a tuple (length, SHA2-256, SHA3-256)
type ScriptHash struct {
	Length int
	SHA2   [sha256.Size]byte
	SHA3   [32]byte
}

// NewScriptHash produces a new (length, SHA2-256, SHA3-256) triple from a JS code string (i.e., a script)
func NewScriptHash(code string) ScriptHash {
	// fmt.Printf("Code: " + string(code) + "\n")
	return ScriptHash{
		Length: len(code),
		SHA2:   sha256.Sum256([]byte(code)),
		SHA3:   sha3.Sum256([]byte(code)),
	}
}

// NewScriptInfo constructs a new script in a given Isolate with the given runtime ID and code body
func NewScriptInfo(iso *IsolateInfo, id int, code string, activeOrigin string) *ScriptInfo {
	return &ScriptInfo{
		Isolate:     iso,
		ID:          id,
		Code:        code,
		CodeHash:    NewScriptHash(code),
		FirstOrigin: activeOrigin,
	}
}

func (script *ScriptInfo) setURL(url string) {
	script.URL = url
}

func (script *ScriptInfo) setEvaledBy(parent *ScriptInfo) {
	script.EvaledBy = parent
}

// IngestStream is the entry point for parsing a given log and feeding the records into zero or more aggregators
func (ln *LogInfo) IngestStream(stream io.Reader, aggs ...Aggregator) error {
	cc := 0
	// Read lines from input
	scan := bufio.NewScanner(stream)

	// Support LOOOONG lines
	scan.Buffer(make([]byte, 0, bufio.MaxScanTokenSize), 128*1024*1024)

	// Start processing log lines
	var lineCount int
	var byteCount int64

	var source_buffer SourceC
	var leftover SourceList
	var domain_name string
	var domain SourceList
	var current_id int
	var buff_origin string
	var buff_code string
	var firstTime int = 1
	var prev_offset string
	var current_ori string
	var prev_ori string
	var prev_line string
	// var flag bool
	for scan.Scan() {

		line := scan.Bytes()
		// fmt.Printf("Line: " + string(line) + "\n")
		lineCount++
		byteCount += int64(len(line)) + 1
		if len(line) > 0 {
			code := line[0]
			fields := splitFields(line[1:])
			switch code {
			case '~':
				ln.changeIsolate(fields[0])
			case '$':
				scriptID, err := strconv.Atoi(fields[0])
				current_id = scriptID

				if err != nil {
					return err
				}
				ln.addScript(scriptID, fields[1], fields[2])

				buff_origin = fields[1]
				buff_code = fields[2]

				// fmt.Println("$BE source_buffer.ID: %d", source_buffer.ID)
				// fmt.Println("$len(source_buffer.APIs): %d", len(source_buffer.APIs))
				if source_buffer.ID != 0 && len(source_buffer.APIs) > 0 {
					if source_buffer.Code == "" && source_buffer.ScriptName == "" {
						leftover.appendScirpt(source_buffer)
					} else {
						source_buffer.OriName = current_ori
						if prev_line[0] == []byte("@")[0] {
							source_buffer.OriName = prev_ori
						}
						domain.appendScirpt(source_buffer)
					}

					source_buffer.APIs = []string{}
					source_buffer.ScriptName = ""
					source_buffer.Code = ""
				}
				source_buffer.ScriptName = buff_origin
				source_buffer.Code = buff_code

				source_buffer.ID = scriptID

			case '!':
				scriptID, err := strconv.Atoi(fields[0])
				// fmt.Println("!ID: %d", scriptID)

				if source_buffer.ID == 0 {
					source_buffer.ID = current_id
				}
				source_buffer.DomName = domain_name
				// fmt.Println("!BE source_buffer.ID: %d", source_buffer.ID)
				// fmt.Println("!len(source_buffer.APIs): %d", len(source_buffer.APIs))
				if len(source_buffer.APIs) > 0 && source_buffer.ID != 0 {
					if source_buffer.Code == "" && source_buffer.ScriptName == "" {
						leftover.appendScirpt(source_buffer)
					} else {
						source_buffer.OriName = current_ori
						if prev_line[0] == []byte("@")[0] {
							source_buffer.OriName = prev_ori
						}
						domain.appendScirpt(source_buffer)
					}
					source_buffer.Code = ""
					source_buffer.ScriptName = ""
					source_buffer.APIs = []string{}
				}
				if len(source_buffer.APIs) == 0 && prev_line[0] != []byte("$")[0] {
					source_buffer.Code = ""
					source_buffer.ScriptName = ""
				}
				source_buffer.ID = scriptID

				if err != nil {
					ln.resetContext()
				} else {
					ln.changeScript(scriptID)
				}
			case '@':
				originString, _ := StripQuotes(fields[0])
				ln.changeOrigin(originString)

				if originString != "null" {
					prev_ori = current_ori
					current_ori = originString
				}
				if firstTime == 2 {
					domain_name = originString
					prev_ori = originString
				}
				firstTime += 1
			default:
				cc++
				offset := line[:strings.IndexByte(string(line), ':')]
				// offset = offset[1:len(offset)]

				for _, agg := range aggs {
					err := agg.IngestRecord(&ln.World.Context, lineCount, code, fields)
					if err != nil {
						return err
					}
				}

				var receiver, member string
				switch code {
				case 'g', 's':
					receiver, _ = StripCurlies(fields[1])
					member, _ = StripQuotes(fields[2])
				case 'n':
					receiver, _ = StripCurlies(fields[1])
					// Eliminate "native" prefix indicator from function names
					if strings.HasPrefix(receiver, "%") {
						receiver = receiver[1:]
					}
				case 'c':
					receiver, _ = StripCurlies(fields[2])
					member, _ = StripQuotes(fields[1])

					// Eliminate "native" prefix indicator from function names
					if strings.HasPrefix(member, "%") {
						member = member[1:]
					}
				default:
					fmt.Println("ERROR")
				}
				var fullName string
				if member != "" {
					fullName = fmt.Sprintf("%s.%s", receiver, member)
				} else {
					fullName = receiver
				}

				// sc_ID := current_id
				// for _, i := range source_code.Scirpt {
				// 	if i.ID == sc_ID {
				// 		csv := string(offset) + "," + fullName
				// 		i.APIs = append(i.APIs, csv)
				// 		fmt.Println(i.APIs)
				// 	}
				// }
				csv := string(offset) + "," + fullName
				if !strings.Contains(csv, "?") && strings.Contains(csv, ".") && !strings.Contains(csv, "-") && !strings.Contains(csv, "<anonymous>") {
					if !(csv[1:] == prev_offset[1:] && csv[0] != prev_offset[0] && string(csv[0]) == "c") {
						source_buffer.APIs = append(source_buffer.APIs, csv)
					}
				}
				prev_offset = csv
			}
		}
		prev_line = string(line)
	}
	if scan.Err() != nil {
		return scan.Err()
	}
	ln.Stats.Lines = lineCount
	ln.Stats.Bytes = byteCount

	for sc, _ := range leftover.sclist {
		for stored_sc, _ := range domain.sclist {
			if leftover.sclist[sc].ID == domain.sclist[stored_sc].ID {
				domain.sclist[stored_sc].appendAPIs(leftover.sclist[sc].APIs)
			}
		}
	}
	// for _, i := range source_code.Scirpt {
	// 	fmt.Println("Scirpt: " + i.ScriptName)
	// 	// fmt.Println("Code: " + i.Code)
	// 	fmt.Println("ID: %d", i.ID)
	// 	fmt.Printf("APIs: ")
	// 	fmt.Printf("%v", i.APIs)
	// }

	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s",
		host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	sqlStatement := "INSERT INTO script (script_name, script_id, ori_name, dom_name, code, APIs) VALUES ($1, $2, $3, $4, $5, $6)"
	for _, s := range domain.sclist {
		_, err = db.Exec(sqlStatement, s.ScriptName, s.ID, s.OriName, s.DomName, s.Code, pq.Array(&s.APIs))
		if err != nil {
			panic(err)
		}
	}
	log.Printf("%d lines (%d bytes) processed\n", ln.Stats.Lines, ln.Stats.Bytes)

	return nil
}
