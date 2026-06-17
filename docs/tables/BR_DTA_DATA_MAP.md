# BR_DTA_DATA_MAP

> legacy dta data map

**Description:** BEDROCK DTA DATA MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `DTA_ID` | DOUBLE | NOT NULL |  | Legacy assay id. |
| 3 | `MAX_DIGITS` | DOUBLE | NOT NULL |  | The maximum digits in the data map. |
| 4 | `MIN_DECIMAL_PLACES` | DOUBLE | NOT NULL |  | The minimum decimal places in the data map. |
| 5 | `MIN_DIGITS` | DOUBLE | NOT NULL |  | The minimum digits in the data map. |
| 6 | `SERVICE_RESOURCE` | VARCHAR(40) | NOT NULL |  | The legacy service resource associated to the assay data map. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

