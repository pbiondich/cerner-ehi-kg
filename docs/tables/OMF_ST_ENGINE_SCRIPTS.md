# OMF_ST_ENGINE_SCRIPTS

> Defines scripts called from the summary table engine. These scripts will fill the request structure(s) and perform any qualifications/calculations needed for the summary table fill scripts.

**Description:** Defines scripts called from the summary table engine.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARRAY_STR` | VARCHAR(255) |  |  | Array string. |
| 2 | `CALC_SCRIPT` | VARCHAR(255) |  |  | Script called by the summary table engine to perform calculations on the current transaction. |
| 3 | `CALC_ST_SCRIPT` | VARCHAR(255) |  |  | Summary table fill script called after calculation(s) have been performed. |
| 4 | `CALC_WHEN_QUAL_IND` | DOUBLE |  |  | Defines whether or not a qualification has to occur in order to run the calculation script. Values: 1 - only perform the calculation if the transaction qualifies 0 - perform the calculation on every transaction |
| 5 | `COLUMN_STR` | VARCHAR(255) |  |  | Column string. |
| 6 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Defines the product for which the summary table scripts will be run. |
| 7 | `QUALIFY_MULTIPLE_IND` | DOUBLE |  |  | Defines whether or not the product allows qualifying for multiple qualification records. |
| 8 | `QUALIFY_SCRIPT` | VARCHAR(255) |  |  | The script called by the summary table engine for rule qualification. |
| 9 | `REQUEST_SCRIPT` | VARCHAR(255) |  |  | The script called by the summary table engine in order to fill out the request structure. |
| 10 | `SCRIPT_ORDER` | DOUBLE | NOT NULL |  | The order in which the scripts will be processed for the given product. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

