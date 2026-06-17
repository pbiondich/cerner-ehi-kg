# DM_SQL_SNAPSHOT

> Used to perform analysis on the SQL statements found in the SGA pad

**Description:** Used to analyze SQL statements  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXECUTIONS` | DOUBLE |  |  | Number of times this statement was executed |
| 2 | `FIRST_LOAD_TIME` | DATETIME |  |  | first load time for this SQL |
| 3 | `GETS_EXECUTIONS` | DOUBLE |  |  | This is the ratio of soft_gets/execution |
| 4 | `HARD_GETS` | DOUBLE |  |  | Number of hard i/o buffer gets |
| 5 | `PREV_SNAPSHOT_ID` | DOUBLE |  |  | This is the snapshot id of the most recent snapshot with the same statement |
| 6 | `SCRIPT_NAME` | VARCHAR(80) |  |  | This is the name of the script |
| 7 | `SNAPSHOT_DT_TM` | DATETIME |  |  | This is the date and time that the snapshot occurred |
| 8 | `SNAPSHOT_ID` | DOUBLE | NOT NULL |  | This is the primary key |
| 9 | `SOFT_GETS` | DOUBLE |  |  | Soft i/o buffer gets |
| 10 | `STMT` | LONGTEXT |  |  | This is the text of the actual statement |
| 11 | `STMT_HASH_VALUE` | DOUBLE | NOT NULL |  | This is from the hash_value in the SQL_TEXT table |
| 12 | `TEST_SEQUENCE` | DOUBLE |  |  | Uniquely identifies this snapshot |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

