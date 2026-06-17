# LH_PURGE_HIST

> Stores purge history for lighthouse reporting data - audit purpose

**Description:** LH PURGE HISTORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LH_PURGE_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `PROCESSED_DT_TM` | DATETIME |  |  | The date when the purge script was run by the user |
| 3 | `PURGED_TILL_DT_TM` | DATETIME |  |  | Contains the date till which the rows are removed. ; We will remove rows that have admit_dt_tm < purged_till_dt_tm |
| 4 | `PURGED_USER_NAME` | VARCHAR(50) |  |  | The user Identifier of the person who ran the script |
| 5 | `ROWS_PURGED_COUNT` | DOUBLE |  |  | Contains the number of rows deleted from the table |
| 6 | `TABLE_NAME` | VARCHAR(50) |  |  | Contains the name of the table that is being purged |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | VARCHAR(50) |  |  | Contains the team name and what task has been done (eg : "PIFX stage 1 purge") |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

