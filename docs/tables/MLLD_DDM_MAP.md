# MLLD_DDM_MAP

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DDM_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ICD_9` | VARCHAR(6) | NOT NULL |  | This field contains the ICD-9-CM code used to classify the disease. ICD-9-CM stands for International Classification of Diseases, Ninth Edition, Clinical Modification. |
| 2 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | The Main Multum Drug Code (MMDC) is Multum's designator for groups of similar drug products. This is an extremely important code for developers who are using Multum's database products because it serves as the primary link to all of Multum's tables containing drug product information. An MMDC is assigned to each unique combination of the following fields: active ingredient(s), strength, route of administration, and dosage form. As a result, the MMDC is a very useful field for identifying dru |
| 3 | `MULTUM_CATEGORY_ID` | DOUBLE | NOT NULL |  | The Category ID from MLTM_DRUG_CATEGORIES table (FK) |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

