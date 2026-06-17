# CMT_CONCEPT_EXPLODE

> Provides an exploded view of the hierarchies defined in the cmt_concept_reltn table.

**Description:** CMT CONCEPT EXPLODE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | The child concept_cki in the hierarchy. |
| 2 | `EFFECTIVE_IND` | DOUBLE | NOT NULL |  | The Effective Status of the Relationship |
| 3 | `PARENT_CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | The parent concept_cki in the hierarchy. |
| 4 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | Stores a _cd that indicates which vocabulary the row belongs to |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |
| `PARENT_CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |

