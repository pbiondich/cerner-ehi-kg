# MLLD_RXB_ORD_DOSE_AMOUNT

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_RXB_ORD_DOSE_AMOUNT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOSE_AMOUNT` | DOUBLE | NOT NULL |  | This field contains a numeric amount that represents the amount of drug to prescribe. |
| 2 | `DOSE_QTY_AMOUNT` | DOUBLE | NOT NULL |  | Dose Quantity |
| 3 | `DOSE_QTY_UNIT_DICTIONARY_CKI` | VARCHAR(255) |  |  | CKI Code |
| 4 | `DOSE_QTY_UNIT_DICTIONARY_ID` | DOUBLE | NOT NULL |  | Value from Multum RXB Dictionary |
| 5 | `DOSE_UNIT_DICTIONARY_CKI` | VARCHAR(255) |  |  | CKI code |
| 6 | `DOSE_UNIT_DICTIONARY_ID` | DOUBLE | NOT NULL |  | This field contains an identifier that represents a dosage unit description. |
| 7 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | Drug IdentifierColumn |
| 8 | `MOST_COMMON_IND` | DOUBLE | NOT NULL |  | Designates the data as the most common for the drug_id, order_id combination. |
| 9 | `ORDER_ID_NBR` | DOUBLE | NOT NULL |  | This field contains an identifier that provides uniqueness to a record and along with the drug_id associates a record with a main_Multum_drug_code. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

