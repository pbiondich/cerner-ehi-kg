# CONCEPT_CONCEPT_R

> The Concept Concept Relationship table stores the meaningful relationships between concepts. The most common types of relationships are IS_A and PART_OF.

**Description:** Concept Concept Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 3 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CKI1` | VARCHAR(255) | NOT NULL |  | The first concept in the relationship. |
| 6 | `CKI1_VALUE` | DOUBLE |  |  | Relates to cki1, where the concept for cki1 represents a scalar. This column stores the number associated with the scalar concept. |
| 7 | `CKI2` | VARCHAR(255) | NOT NULL |  | The related concept in the relationship. |
| 8 | `CKI2_VALUE` | DOUBLE |  |  | Relates to cki2, where the concept for cki2 represents a scalar. This column stores the number associated with the scalar concept. |
| 9 | `CONCEPT_CONCEPT_ID` | DOUBLE | NOT NULL |  | Primary key for the table. Uniquely identifies a row within the table. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `INVERSE_RELATION_ID` | DOUBLE | NOT NULL | FK→ | The relationship that is the inverse of the relation_id, e.g. if the relation_id represented PART_OF, then the inverse_relation_id may represent HAS_PART. |
| 12 | `RELATION_ID` | DOUBLE | NOT NULL | FK→ | Represents the kind of relationship between two concepts, e.g. IS_A or PART_OF. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INVERSE_RELATION_ID` | [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_TYPE_ID` |
| `RELATION_ID` | [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_TYPE_ID` |

