# DM_REFCHG_WARNING

> Warnings issued during RDDS data moves

**Description:** Data management reference change warnings  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DML_TXT` | VARCHAR(4000) |  |  | Statement that was run that caused the error to occur. |
| 2 | `DM_REFCHG_WARNING_ID` | DOUBLE | NOT NULL |  | Unique identifier |
| 3 | `ERROR_MSG` | VARCHAR(2000) |  |  | CCL/RDBMS error message |
| 4 | `MESSAGE` | VARCHAR(2000) | NOT NULL |  | Warning message |
| 5 | `ROW_SELECT_TXT` | VARCHAR(2000) |  |  | Statement which will retrieve the rows on the $R table that caused the error to occur. |
| 6 | `SOURCE_ENV_ID` | DOUBLE | NOT NULL |  | Environment id being moved in when the error occurred. This value comes from DM_ENVIRONMENT table in the Admin DB. |
| 7 | `TABLE_NAME` | VARCHAR(30) |  |  | Name of the table that the warning is related to. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `WARNING_TYPE` | VARCHAR(50) | NOT NULL |  | Type of warning - e.g. DUP_BEFORE_CUTOVER |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

