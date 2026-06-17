# CMT_CONCEPT_HISTORY

> The history table identifies each change in the status of a concept, and relates it to the replacement concept, if any.

**Description:** The history table identifies each change in the status of a concept.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. |
| 2 | `REFERENCE_CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | The concept_cki for the reference concept. |
| 3 | `REFERENCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The indicator of the changed type. For example, 1 - replaced by; 2 - duplicated by; 3 - similar to; 4 - alternative. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |
| `REFERENCE_CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |

