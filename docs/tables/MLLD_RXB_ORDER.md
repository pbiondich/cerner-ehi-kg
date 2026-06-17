# MLLD_RXB_ORDER

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_RXB_ORDER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | Drug IdentifierColumn |
| 2 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE |  |  | Main Multum Drug Code. FK from MLTM_NDC_MAIN_DRUG_CODE table |
| 3 | `ORDER_CATEGORY_ID` | DOUBLE | NOT NULL |  | This field contains a unique identifier for each prescription category. |
| 4 | `ORDER_ID_NBR` | DOUBLE | NOT NULL |  | This field contains an identifier that provides uniqueness to a record and along with the drug_id associates a record with a main_Multum_drug_code. |
| 5 | `ORDER_TYPE_ID` | DOUBLE | NOT NULL |  | This field contains a unique identifier for each prescription type. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

