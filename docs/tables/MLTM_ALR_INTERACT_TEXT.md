# MLTM_ALR_INTERACT_TEXT

> This table contains a number of template textual descriptions of allergic reactivity appropriate for display to clinical end users. Each of the textual descriptions present in this table is linked to the appropriate variables via the interaction_text_id field.

**Description:** Multum allergy interaction text  
**Table type:** REFERENCE  
**Primary key:** `INTERACTION_TEXT_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERACTION_TEXT` | VARCHAR(2000) |  |  | textual descriptions of allergic reactivity |
| 2 | `INTERACTION_TEXT_ID` | DOUBLE | NOT NULL | PK | Each of the textual descriptions present in this table is linked to the appropriate variables via the interaction_text_id field. |
| 3 | `REV_INTERACTION_TEXT` | VARCHAR(2000) |  |  | Revised Interaction Text |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_ALR_TEXT_MAP](MLTM_ALR_TEXT_MAP.md) | `INTERACTION_TEXT_ID` |

