# DO_CONCEPT_EXPLODE

> Defines a relationship between two concepts in a context version.

**Description:** Discern Ontology Concept Explode  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_CONCEPT1_ID` | DOUBLE | NOT NULL | FK→ | Represents the first concept that has a relationship with another concept in a context release. |
| 2 | `DO_CONCEPT2_ID` | DOUBLE | NOT NULL | FK→ | Represents the second concept in the relationship. |
| 3 | `DO_CONCEPT_EXPLODE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DO_CONCEPT_EXPLODE table. |
| 4 | `DO_CONTEXT_VERSION_ID` | DOUBLE | NOT NULL | FK→ | Represents an ontology context release. |
| 5 | `DO_DISPLAY_SEQ` | DOUBLE |  |  | Represents the display sequence. It is always NULL when the depth is not one. |
| 6 | `DO_RELATIONSHIP_LEVEL_NBR` | DOUBLE | NOT NULL |  | The relationship depth/level between the two concepts. The minimum value is one. |
| 7 | `DO_RELATIONSHIP_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The identification of the relationship type. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_CONCEPT1_ID` | [DO_CONCEPT](DO_CONCEPT.md) | `DO_CONCEPT_ID` |
| `DO_CONCEPT2_ID` | [DO_CONCEPT](DO_CONCEPT.md) | `DO_CONCEPT_ID` |
| `DO_CONTEXT_VERSION_ID` | [DO_CONTEXT_VERSION](DO_CONTEXT_VERSION.md) | `DO_CONTEXT_VERSION_ID` |
| `DO_RELATIONSHIP_TYPE_ID` | [DO_RELATIONSHIP_TYPE](DO_RELATIONSHIP_TYPE.md) | `DO_RELATIONSHIP_TYPE_ID` |

