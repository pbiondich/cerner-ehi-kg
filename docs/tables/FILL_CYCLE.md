# FILL_CYCLE

> Table to store combination of location and dispense category and dispensing parameters

**Description:** Fill Cycle  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_FLAG` | DOUBLE |  |  | Indicator set as the result of cycle processing |
| 2 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Code value for the dispense category |
| 3 | `FILL_CYCLE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 4 | `FROM_DT_TM` | DATETIME |  |  | The beginning date and time of the current fill cycle range being filled in the pharmacy |
| 5 | `FROM_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 6 | `IGNORE_IND` | DOUBLE |  |  | NOT IN USE |
| 7 | `LAST_OPERATION_FLAG` | DOUBLE |  |  | The last operation (might be called the "current state") requested for this cycle. |
| 8 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Code value of the nursing unit where meaning is "NURSEUNIT" |
| 9 | `TO_DT_TM` | DATETIME |  |  | The ending date and time of the current fill cycle range being filled in the pharmacy |
| 10 | `TO_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

