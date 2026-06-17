# MLTM_ALR_TEXT_MAP

> This table is intended to locate the most appropriate textual description of an allergy for display to clinical end users. Because certain allergy classifications are associated with specific textual descriptions (i.e., the Narcotic Analgesic Class is associated with different text than other classifications), this table allows association of an interaction type, an allergy classification, and an identifier for a textual description.

**Description:** Multum allergy text map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALR_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | FK from ALR_CATEGORY table. |
| 2 | `INTERACTION_TEXT_ID` | DOUBLE | NOT NULL | FK→ | FK from the ALR INTERACTION TEXT table |
| 3 | `INTERACTION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | FK from the ALR Interction Type table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALR_CATEGORY_ID` | [MLTM_ALR_CATEGORY](MLTM_ALR_CATEGORY.md) | `ALR_CATEGORY_ID` |
| `INTERACTION_TEXT_ID` | [MLTM_ALR_INTERACT_TEXT](MLTM_ALR_INTERACT_TEXT.md) | `INTERACTION_TEXT_ID` |
| `INTERACTION_TYPE_ID` | [MLTM_ALR_INTERACT_TYPE](MLTM_ALR_INTERACT_TYPE.md) | `INTERACTION_TYPE_ID` |

