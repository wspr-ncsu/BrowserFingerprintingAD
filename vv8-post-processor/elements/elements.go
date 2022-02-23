package elements

// ---------------------------------------------------------------------------
// aggregator for tracking DOM element types created by Document.createElement
// ---------------------------------------------------------------------------
import (
	"database/sql"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"strconv"
	"strings"

	"github.com/lib/pq"
	mgo "gopkg.in/mgo.v2"

	"github.ncsu.edu/jjuecks/vv8-post-processor/core"
	"github.ncsu.edu/jjuecks/vv8-post-processor/features"
)

type originCallsite struct {
	Origin string           // what security origin
	Script *core.ScriptInfo // What script
	Offset int              // What location
}

// CreateElementAggregator tracks document.createElement calls and first-arguments (i.e., element type tags)
type CreateElementAggregator struct {
	// IDL feature name normalization database
	idl core.IDLTree

	// track set of (lowercase) tag names Document.createElement()'d by a given originCallsite (origin/script/offset)
	tagMap map[originCallsite]map[string]int
}

// NewCreateElementAggregator constructs a CreateElementAggregator
func NewCreateElementAggregator() (core.Aggregator, error) {
	tree, err := core.LoadDefaultIDLData()
	if err != nil {
		return nil, err
	}
	return &CreateElementAggregator{
		idl:    tree,
		tagMap: make(map[originCallsite]map[string]int),
	}, nil
}

// IngestRecord parses a trace record, looking for document.createElement calls to track
func (agg *CreateElementAggregator) IngestRecord(ctx *core.ExecutionContext, lineNumber int, op byte, fields []string) error {
	if (op == 'c') && (ctx.Script != nil) && !ctx.Script.VisibleV8 && (ctx.Origin != "") {
		offset, err := strconv.Atoi(fields[0])
		if err != nil {
			return fmt.Errorf("%d: invalid script offset '%s'", lineNumber, fields[0])
		}

		rcvr, _ := core.StripCurlies(fields[2])
		name, _ := core.StripQuotes(fields[1])

		// Eliminate "native" prefix indicator from function names
		if strings.HasPrefix(name, "%") {
			name = name[1:]
		}

		// We have some names (V8 special cases, numeric indices) that are never useful
		if features.FilterName(name) {
			return nil
		}

		// Normalize IDL names
		fullName, err := agg.idl.NormalizeMember(rcvr, name)
		if err != nil {
			fullName = fmt.Sprintf("%s.%s", rcvr, name)
		}

		// FINALLY: if we are CALLING "Document.createElement", record the value of the first argument
		if fullName == "Document.createElement" {
			tagName, ok := core.StripQuotes(fields[3])
			if ok {
				cite := originCallsite{ctx.Origin, ctx.Script, offset}
				tagSet := agg.tagMap[cite]
				if tagSet == nil {
					tagSet = make(map[string]int)
					agg.tagMap[cite] = tagSet
				}
				tagSet[strings.ToLower(tagName)]++
			} else {
				log.Printf("bogus argument to Document.createElement: %s\n", tagName)
			}
		}
	}
	return nil
}

// DumpToStream implementation for create-elements
func (agg *CreateElementAggregator) DumpToStream(ctx *core.AggregationContext, stream io.Writer) error {
	jstream := json.NewEncoder(stream)
	if ctx.Formats["create_element"] {
		for cite, tagSet := range agg.tagMap {
			for tagName, tagCount := range tagSet {
				jstream.Encode(core.JSONArray{"create_element", core.JSONObject{
					"script_hash":     hex.EncodeToString(cite.Script.CodeHash.SHA2[:]),
					"script_offset":   cite.Offset,
					"security_origin": cite.Origin,
					"tag_name":        tagName,
					"create_count":    tagCount,
				}})
			}
		}
	}
	return nil
}

type createElementRecord struct {
	origin string
	script *core.ScriptInfo
	offset int
	tag    string
	count  int
}

var elementCreationFields = [...]string{
	"logfile_id",
	"visit_domain",
	"security_origin",
	"script_hash",
	"script_offset",
	"tag_name",
	"create_count",
}

// DumpToMongresql dumps create-element tuple records to Postgres
func (agg *CreateElementAggregator) DumpToMongresql(ctx *core.AggregationContext, mongoDb *mgo.Database, sqlDb *sql.DB) error {
	if ctx.Formats["create_element"] {
		records := make([]createElementRecord, 0, 100)

		for cite, tagSet := range agg.tagMap {
			for tagName, tagCount := range tagSet {
				records = append(records, createElementRecord{
					origin: cite.Origin,
					script: cite.Script,
					offset: cite.Offset,
					tag:    tagName,
					count:  tagCount,
				})
			}
		}

		// Create log record if necessary (need job domain for that)
		visitDomain, err := core.GetRootDomain(mongoDb, ctx.Ln)
		if err != nil {
			return err
		}
		logID, err := features.InsertLogfile(sqlDb, ctx.Ln)
		if err != nil {
			return err
		}

		// Prepare for bulk insertion of script causality tuples
		txn, err := sqlDb.Begin()
		if err != nil {
			return err
		}
		stmt, err := txn.Prepare(pq.CopyIn("create_elements", elementCreationFields[:]...))
		if err != nil {
			txn.Rollback()
			return err
		}

		// Insert actual tuples
		for _, cr := range records {
			log.Printf("CE: origin='%s', script=%p, tag='%s', count=%d\n", cr.origin, cr.script, cr.tag, cr.count)
			_, err = stmt.Exec(
				logID,
				visitDomain,
				cr.origin,
				cr.script.CodeHash.SHA2[:],
				cr.offset,
				cr.tag,
				cr.count)
			if err != nil {
				txn.Rollback()
				return err
			}
		}

		// Finish the bulk insertion and commit everything
		_, err = stmt.Exec()
		if err != nil {
			txn.Rollback()
			return err
		}
		err = stmt.Close()
		if err != nil {
			txn.Rollback()
			return err
		}
		err = txn.Commit()
		if err != nil {
			return err
		}

		// Update the Mongo document store about the completed analysis
		if err := core.MarkVV8LogComplete(mongoDb, ctx.Ln.ID, "create_element"); err != nil {
			return err
		}
	}
	return nil
}
