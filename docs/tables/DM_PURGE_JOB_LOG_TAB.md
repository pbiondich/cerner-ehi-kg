# DM_PURGE_JOB_LOG_TAB

> Table level logging information for purge job runs.

**Description:** DM PURGE JOB LOG TAB  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `JOB_ID` | DOUBLE | NOT NULL |  | Unique id for this purge job. |
| 2 | `LOG_ID` | DOUBLE | NOT NULL |  | Unique id for purge job log. |
| 3 | `NUM_ROWS` | DOUBLE |  |  | Number of rows purged in this table. |
| 4 | `PURGE_FLAG` | DOUBLE |  |  | Mode to run the purge job in - e.g. audit, purge with high or low level logging. |
| 5 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table which was purged. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

