# ENCNTR_CLIN_REVIEW_ADDNDM

> Stores the addendums of a clinical review for an encounter.

**Description:** Encounter Clinical Review Addendum  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDENDUM_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The comments for the addendum for the clinical review. |
| 2 | `ENCNTR_CLIN_REVIEW_ADDNDM_ID` | DOUBLE | NOT NULL |  | The unique primary key for this table. It is an internally generated number. |
| 3 | `ENCNTR_CLIN_REVIEW_RESULT_ID` | DOUBLE | NOT NULL |  | The Encntr_clin_review_result row for which this addendum belongs. Column is OBSOLETE. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID for the table row which for the table represented by the parent_entity_name. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table which is being referenced. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDENDUM_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

