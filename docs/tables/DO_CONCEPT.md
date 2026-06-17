# DO_CONCEPT

> A unit of meaning within a context. It can be as fine or coarse grained as needed.

**Description:** DISCERN ONTOLOGY  
**Table type:** REFERENCE  
**Primary key:** `DO_CONCEPT_ID`  
**Columns:** 9  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_CONCEPT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_CONCEPT table. |
| 2 | `DO_CONCEPT_NAME` | VARCHAR(100) | NOT NULL |  | Name of the concept. |
| 3 | `DO_CONCEPT_UUID` | VARCHAR(36) | NOT NULL |  | Discern Ontology concept identifier. Will be consistent across domains. |
| 4 | `DO_CONTEXT_VERSION_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifier a single row on the DO_CONTEXT_VERSION table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_CONTEXT_VERSION_ID` | [DO_CONTEXT_VERSION](DO_CONTEXT_VERSION.md) | `DO_CONTEXT_VERSION_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DO_CONCEPT_ALIAS](DO_CONCEPT_ALIAS.md) | `DO_CONCEPT_ID` |
| [DO_CONCEPT_CODE](DO_CONCEPT_CODE.md) | `DO_CONCEPT_ID` |
| [DO_CONCEPT_EXPLODE](DO_CONCEPT_EXPLODE.md) | `DO_CONCEPT1_ID` |
| [DO_CONCEPT_EXPLODE](DO_CONCEPT_EXPLODE.md) | `DO_CONCEPT2_ID` |

