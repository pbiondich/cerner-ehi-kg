# BR_DTA_ALPHA_RESPONSES

> legacy dta alpha respones

**Description:** BEDROCK DTA ALPHA RESPONSES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AR` | VARCHAR(40) | NOT NULL |  | The alpha response associated to the legacy assay. |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 3 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Defined as 1 the default indicator is defined. |
| 4 | `REFERENCE_IND` | DOUBLE | NOT NULL |  | Defined as 1 the reference is defined. |
| 5 | `RESULT_PROCESSING_TYPE` | VARCHAR(40) |  |  | Defined as 1 the result processing type is defined. |
| 6 | `RRF_ID` | DOUBLE | NOT NULL |  | Reference range ID. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `USE_UNITS_IND` | DOUBLE | NOT NULL |  | Defined as 1 the use units is defined. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

