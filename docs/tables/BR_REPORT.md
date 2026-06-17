# BR_REPORT

> bedrock reports

**Description:** BEDROCK REPORT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_REPORT_HISTORY_ID` | DOUBLE | NOT NULL |  | Report history ID |
| 3 | `BR_REPORT_ID` | DOUBLE | NOT NULL |  | unique identifier |
| 4 | `LAST_RUN_DT_TM` | DATETIME |  |  | Date/time the report was accessed |
| 5 | `LAST_RUN_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the user that accessed the report |
| 6 | `LAST_RUN_STATUS_FLAG` | DOUBLE | NOT NULL |  | Status of a digital xray report (good data, incomplete data) |
| 7 | `PROGRAM_NAME` | VARCHAR(50) | NOT NULL |  | name of the ccl program associated with the report |
| 8 | `REFRESH_NBR_OF_DAYS` | DOUBLE | NOT NULL |  | Indicates frequency of report run |
| 9 | `REPORT_NAME` | VARCHAR(100) | NOT NULL |  | name of the report |
| 10 | `REPORT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate the type of report (bedrock audit,digital x-ray) |
| 11 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 12 | `SOLUTION_DISP` | VARCHAR(100) |  |  | Display value of the solution |
| 13 | `SOLUTION_MEAN` | VARCHAR(100) |  |  | Meaning of the solution |
| 14 | `STEP_CAT_MEAN` | VARCHAR(50) | NOT NULL |  | short name of the solution |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

