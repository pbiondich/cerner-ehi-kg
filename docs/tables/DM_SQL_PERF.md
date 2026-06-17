# DM_SQL_PERF

> Data used by trhe CBO Implementer

**Description:** DM SQL PERF  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CCL_QUERY_NBR` | DOUBLE | NOT NULL |  | Cerner Query Number |
| 2 | `CCL_QUERY_NBR_TEXT` | VARCHAR(7) | NOT NULL |  | Cerner query identifier |
| 3 | `CCL_SCRIPT_NAME` | VARCHAR(30) | NOT NULL |  | Cerner Script Name |
| 4 | `COMMENTS` | VARCHAR(255) |  |  | SQL PERF COMMENTS |
| 5 | `DM_SQL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `LAST_TUNING_DT_TM` | DATETIME |  |  | Last Tuning Date and Time |
| 7 | `SQLTEXT_HASH_VALUE` | DOUBLE | NOT NULL |  | Cerner generated hash value on SQL_TEXT from GV$SQL |
| 8 | `TGT_OPT_MODE` | DOUBLE | NOT NULL |  | Cerner Optimizer Mode |
| 9 | `TUNING_STATUS` | VARCHAR(40) | NOT NULL |  | Cerner tuning status |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

