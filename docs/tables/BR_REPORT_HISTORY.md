# BR_REPORT_HISTORY

> Stores history data for bedrock reports

**Description:** Bedrock Report History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_REPORT_HISTORY_ID` | DOUBLE | NOT NULL |  | Unique id for the table |
| 3 | `BR_REPORT_ID` | DOUBLE | NOT NULL |  | Unique id from br_report |
| 4 | `RUN_DT_TM` | DATETIME |  |  | Date/time the instance of report was accessed |
| 5 | `RUN_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the user who accessed instance of the report |
| 6 | `RUN_STATUS_FLAG` | DOUBLE | NOT NULL |  | Status of the report?s data when it was accessed |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

