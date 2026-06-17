# CMT_CONCEPT_EXPLODE_LOAD_NS

> This is a holding table for the cmt_concept_explode to allow faster loading. This table is identical to cmt_concept_explode_load except that the _ns table will not contain any snomed items.

**Description:** CMT_CONCEPT_EXPLODE_LOAD_NS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Flag for determining delete/insert action |
| 2 | `CHILD_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Child Concept CKI. FK from the CMT_CONCEPT table. |
| 3 | `EFFECTIVE_IND` | DOUBLE | NOT NULL |  | The Effective Status of the Relationship |
| 4 | `PARENT_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Parent Concept CKI. FK from the CMT_CONCEPT table. |
| 5 | `SOURCE_VOCABULARY_MEAN` | VARCHAR(12) | NOT NULL |  | Stores a meaning that indicates which vocabulary the row belongs to |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

