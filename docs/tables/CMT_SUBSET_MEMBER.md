# CMT_SUBSET_MEMBER

> This table contains relationships between concepts / CMTIs within a specific subset. This is to support navigation purposes.

**Description:** CMT SUBSET MEMBER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_CMTI` | VARCHAR(255) |  |  | Global unique identifier. Identifies the child item for the list item. |
| 2 | `CHILD_CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | Child concept_cki from cmt_concept table |
| 3 | `CHILD_SUBSET_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the child subset. |
| 4 | `LIST_SEQUENCE` | DOUBLE |  |  | The sequence of the child item with the parent |
| 5 | `PARENT_CMTI` | VARCHAR(255) |  |  | Global unique identifier. Identifies the parent item for the list item. |
| 6 | `PARENT_CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | Parent concept_cki from cmt_concept table. |
| 7 | `SUBSET_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the subset table. |
| 8 | `SUBSET_MEMBER_ID` | DOUBLE | NOT NULL |  | Unique identifier for the CMT Subset member table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |
| `CHILD_SUBSET_ID` | [CMT_SUBSET](CMT_SUBSET.md) | `SUBSET_ID` |
| `PARENT_CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |
| `SUBSET_ID` | [CMT_SUBSET](CMT_SUBSET.md) | `SUBSET_ID` |

