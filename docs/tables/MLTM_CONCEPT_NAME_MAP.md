# MLTM_CONCEPT_NAME_MAP

> This is a new table for MULTUM allergy mappings. The CONCEPT_DRUG_NAMEs from this table will be used in building MULTUM allergies.

**Description:** MLTM_CONCEPT_NAME_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_CKI` | VARCHAR(50) | NOT NULL |  | MULTUM CONCEPT_CKI |
| 2 | `CONCEPT_DRUG_NAME` | VARCHAR(255) | NOT NULL |  | MULTUM CONCEPT_DRUG_NAME |
| 3 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | MULTUM DRUG_IDENTIFIER |
| 4 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL |  | MULTUM DRUG_SYNONYM_ID |
| 5 | `FUNCTION_IDENT` | DOUBLE | NOT NULL |  | MULTUM FUNCTION_ID |
| 6 | `SOURCE_DISP` | VARCHAR(25) | NOT NULL |  | MULTUM SOURCE_DISP |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

