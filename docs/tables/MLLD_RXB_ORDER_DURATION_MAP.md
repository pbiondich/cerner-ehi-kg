# MLLD_RXB_ORDER_DURATION_MAP

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_RXB_ORDER_DURATION_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | Drug IdentifierColumn |
| 2 | `DURATION_AMOUNT` | DOUBLE | NOT NULL |  | Duration AmountColumn |
| 3 | `DURATION_DICTIONARY_CKI` | VARCHAR(255) |  |  | CKI Code |
| 4 | `DURATION_DICTIONARY_ID` | DOUBLE | NOT NULL |  | This field contains an identifier that represents the duration for a prescription, such as hours or days. |
| 5 | `MOST_COMMON_IND` | DOUBLE |  |  | Designates the data as the most common for the drug_id, order_id combination. |
| 6 | `ORDER_ID_NBR` | DOUBLE | NOT NULL |  | This field contains an identifier that provides uniqueness to a record and along with the drug_id associates a record with a main_Multum_drug_code. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

