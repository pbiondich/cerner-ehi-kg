# BR_DTA_WORK

> legacy dtas

**Description:** BEDROCK DTA WORK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE` | VARCHAR(20) |  |  | Activity type for the assay |
| 2 | `ALIAS` | VARCHAR(40) |  |  | Alias for the assay |
| 3 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 4 | `DTA_ID` | DOUBLE | NOT NULL |  | dta id |
| 5 | `FACILITY` | VARCHAR(50) |  |  | Used to identify individual facility data. |
| 6 | `LONG_DESC` | VARCHAR(60) |  |  | Long description for the assay |
| 7 | `MATCH_DTA_CD` | DOUBLE | NOT NULL |  | Used to match on the DTA code value. |
| 8 | `ORG_EVENT_CODE` | VARCHAR(50) |  |  | Will store event code names |
| 9 | `RESULT_TYPE` | VARCHAR(30) |  |  | Result type for the assay |
| 10 | `SHORT_DESC` | VARCHAR(40) |  |  | Short description for the assay. |
| 11 | `STATUS_IND` | DOUBLE | NOT NULL |  | DTA Status Indicator |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

