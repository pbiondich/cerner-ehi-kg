# MLTM_ORDER_SENT

> This table will be used as a load table containing a cumulative list of Multum order sentences. Scripts will be used to compare the data in this table against order sentences currently in Millennium, and will insert valid new order sentences into Millennium.

**Description:** MLTM_ORDER_SENT  
**Table type:** REFERENCE  
**Primary key:** `EXTERNAL_IDENTIFIER`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CKI` | VARCHAR(100) |  |  | Matches the CKI column on the ORDER_CATALOG table. |
| 2 | `CATALOG_CONCEPT_CKI` | VARCHAR(100) |  |  | Matches the CONCEPT_CKI column on the ORDER_CATALOG table. |
| 3 | `CATALOG_DESCRIPTION` | VARCHAR(255) |  |  | Matches the DESCRIPTION column on the ORDER_CATALOG table. |
| 4 | `EXTERNAL_IDENTIFIER` | VARCHAR(100) | NOT NULL | PK | Used here as a unique identifier. Loads the EXTERNAL_IDENTIFIER column on the ORDER_SENTENCE table. |
| 5 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | The Main Multum Drug Code (MMDC) is Multum's designator for groups of similar drug products. This is an extremely important code for developers who are using Multum's database products because it serves as the primary link to all of Multum's tables containing drug product information. An MMDC is assigned to each unique combination of the following fields: active ingredient(s), strength, route of administration, and dosage form. As a result, the MMDC is a very useful field for identifying dru |
| 6 | `MNEMONIC_KEY_CAP` | VARCHAR(255) | NOT NULL |  | Matches the MNEMONIC_KEY_CAP column on the ORDER_CATALOG_SYNONYM table. |
| 7 | `MNEMONIC_TYPE` | VARCHAR(12) |  |  | Used as the MEANING to pull the MNEMONIC_TYPE_CD from the CODE_VALUE table on CODE_SET 6011. |
| 8 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL |  | Matches the ORDER_SENTENCE_ID column on the ORDER_SENTENCE table. |
| 9 | `RX_TYPE_MEAN` | VARCHAR(12) |  |  | Loads the RX_TYPE_MEAN column on the ORDER_SENTENCE table. |
| 10 | `SENTENCE_SCRIPT` | VARCHAR(255) |  |  | Used to give a display of the entire order sentence as defined by the source. |
| 11 | `SYNONYM_CKI` | VARCHAR(100) | NOT NULL |  | Matches the CKI column on the ORDER_CATALOG_SYNONYM table. |
| 12 | `SYNONYM_CONCEPT_CKI` | VARCHAR(100) | NOT NULL |  | Matches the CONCEPT_CKI column on the ORDER_CATALOG_SYNONYM table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `USAGE_FLAG` | DOUBLE | NOT NULL |  | Loads the USAGE_FLAG column on the ORDER_SENTENCE table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_ORDER_SENT_DETAIL](MLTM_ORDER_SENT_DETAIL.md) | `EXTERNAL_IDENTIFIER` |

