package mega

import (
	"database/sql"

	"github.ncsu.edu/jjuecks/vv8-post-processor/core"
)

// InsertLogfile inserts (if not present) a record about this log file into PG
func InsertLogfile(sqldb *sql.DB, ln *core.LogInfo) (int, error) {
	_, err := sqldb.Exec(`
INSERT INTO mega_logfile (mongo_oid, root_name, size, lines, page_oid)
	VALUES ($1, $2, $3, $4, $5)
ON CONFLICT DO NOTHING`,
		ln.ID,
		ln.RootName,
		ln.Stats.Bytes,
		ln.Stats.Lines,
		core.NullableMongoOID(ln.PageID),
	)
	if err != nil {
		return 0, err
	}

	// No "RETURNING" clause because in the above "DO NOTHING" case
	// no results will be returned (and "DO UPDATE" without meaningful changes
	// is a bad anti-pattern for Postgres's MVCC).
	// We have a unique key here (the original Mongo OID), so just look it up
	// after the upsert...
	var logID int
	err = sqldb.QueryRow(`SELECT id FROM mega_logfile WHERE mongo_oid = $1`, ln.ID).Scan(&logID)
	if err != nil {
		return 0, err
	}
	return logID, nil
}
