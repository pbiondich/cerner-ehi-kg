# MIC_REPORT_PARAMETER

> This reference table contains report attributes for use in Microbiology Statistical reporting.

**Description:** Microbiology Report Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MAX_SORT` | DOUBLE | NOT NULL |  | This field identifies the maximum number of sort parameters that can be defined for a specific report. |
| 2 | `MIN_SORT` | DOUBLE | NOT NULL |  | This field identifies the minimum number of sort parameters that must be defined in order to execute a specific report. |
| 3 | `REPORT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of a Microbiology Statistical report. This could be used to join to the CODE_VALUE table. |
| 4 | `TASK_NUMBER` | DOUBLE | NOT NULL |  | This field identifies the task number (Task Security) that must be granted to a user's position in order to execute a specific report. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

