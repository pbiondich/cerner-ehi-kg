# OMF_ST_FILL_SCRIPTS

> Defines the scripts called by the summary table engine to fill the summary tables for a given product.

**Description:** Defines the scripts called by the summary table engine to fill smry tbls.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The product for which the summary table fill scripts will be run. |
| 2 | `SCRIPT_ORDER` | DOUBLE | NOT NULL |  | The order in which the summary table fill scripts will be run for a given product. |
| 3 | `ST_FILL_SCRIPT` | VARCHAR(255) | NOT NULL |  | The script called by the summary table engine to fill the summary tables for a given product. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

