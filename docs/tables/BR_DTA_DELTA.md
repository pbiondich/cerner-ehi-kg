# BR_DTA_DELTA

> legacy dta delta information

**Description:** BEDROCK DTA DELTA  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `CHECK_TYPE` | VARCHAR(40) |  |  | The delta check type |
| 3 | `HIGH` | DOUBLE | NOT NULL |  | The delta high value. |
| 4 | `LOW` | DOUBLE | NOT NULL |  | The delta low value. |
| 5 | `MINUTES` | DOUBLE | NOT NULL |  | The delta check minutes |
| 6 | `RRF_ID` | DOUBLE | NOT NULL |  | Reference range ID. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VALUE` | VARCHAR(10) |  |  | The delta value |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

