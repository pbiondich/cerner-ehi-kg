# MLTM_RXB_ORDER_PRN_MAP

> Multum Rx Builder Order PRN Map Table

**Description:** Multum Rx Builder Order PRN Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL | FK→ | Drug IdentifierColumn |
| 2 | `ORDER_ID_NBR` | DOUBLE | NOT NULL | FK→ | This field contains an identifier that provides uniqueness to a record and along with the drug_id associates a record with a main_Multum_drug_code. |
| 3 | `PRN_DICTIONARY_CKI` | VARCHAR(255) |  |  | CKI Code |
| 4 | `PRN_DICTIONARY_ID` | DOUBLE | NOT NULL | FK→ | This field contains an identifier that represents a prescription PRN description such as "as needed for pain". |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_IDENTIFIER` | [MLTM_RXB_ORDER](MLTM_RXB_ORDER.md) | `DRUG_IDENTIFIER` |
| `ORDER_ID_NBR` | [MLTM_RXB_ORDER](MLTM_RXB_ORDER.md) | `ORDER_ID_NBR` |
| `PRN_DICTIONARY_ID` | [MLTM_RXB_DICTIONARY](MLTM_RXB_DICTIONARY.md) | `DICTIONARY_ID` |

