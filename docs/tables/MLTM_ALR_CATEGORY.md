# MLTM_ALR_CATEGORY

> This table assigns a code to each allergy category. It also provides textual descriptions of the category in singular and plural forms.

**Description:** Multum Allergy Category  
**Table type:** REFERENCE  
**Primary key:** `ALR_CATEGORY_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALR_CATEGORY_ID` | DOUBLE | NOT NULL | PK | The ALR category Identifier |
| 2 | `CATEGORY_DESCRIPTION` | VARCHAR(60) |  |  | Textual Description of the alr category |
| 3 | `CATEGORY_DESCRIPTION_PLURAL` | VARCHAR(60) |  |  | Textual descriptions of the category |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MLTM_ALR_CATEGORY_CLASS_MAP](MLTM_ALR_CATEGORY_CLASS_MAP.md) | `ALR_CATEGORY_ID` |
| [MLTM_ALR_CATEGORY_DRUG_MAP](MLTM_ALR_CATEGORY_DRUG_MAP.md) | `ALR_CATEGORY_ID` |
| [MLTM_ALR_TEXT_MAP](MLTM_ALR_TEXT_MAP.md) | `ALR_CATEGORY_ID` |

