# FILL_CYCLE_HX

> Table to store the history of each fill cycle processing and the cycle parameters.

**Description:** fill_cycle_hx  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_ID` | DOUBLE | NOT NULL |  | In case of error, set this value to the order_id of order being processed when failure occurred |
| 2 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | code value of the dispense category |
| 3 | `END_DT_TM` | DATETIME |  |  | date and time processing of this cycle ended |
| 4 | `FILL_CYCLE_ID` | DOUBLE | NOT NULL |  | unique identifier for a fill cycle |
| 5 | `FILL_HX_ID` | DOUBLE | NOT NULL |  | The unique identifier for the parameters defined in this fill run. |
| 6 | `FROM_DT_TM` | DATETIME |  |  | The beginning date and time of the filled cycle range. |
| 7 | `FROM_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 8 | `LAST_OPERATION_FLAG` | DOUBLE |  |  | The operation requested for this cycle. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Code value of the location where meaning = "NURSEUNIT" |
| 10 | `ORDER_COUNT` | DOUBLE |  |  | Numberof orders qualifyingfor this cycle |
| 11 | `START_DT_TM` | DATETIME |  |  | Date and time processing began for this fill cycle |
| 12 | `TO_DT_TM` | DATETIME |  |  | The ending date and time of the filled cycle range |
| 13 | `TO_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

