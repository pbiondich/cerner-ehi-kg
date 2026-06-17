# DO_CONTEXT_VERSION

> Discern Ontology Context Versions

**Description:** DO_CONTEXT_VERSION  
**Table type:** REFERENCE  
**Primary key:** `DO_CONTEXT_VERSION_ID`  
**Columns:** 8  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the DO_CONTEXT table. |
| 2 | `DO_CONTEXT_VERSION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_CONTEXT_VERSION table. |
| 3 | `DO_CONTEXT_VERSION_NBR` | DOUBLE | NOT NULL |  | Number of the context version. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_CONTEXT_ID` | [DO_CONTEXT](DO_CONTEXT.md) | `DO_CONTEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DO_CONCEPT](DO_CONCEPT.md) | `DO_CONTEXT_VERSION_ID` |
| [DO_CONCEPT_ALIAS](DO_CONCEPT_ALIAS.md) | `DO_CONTEXT_VERSION_ID` |
| [DO_CONCEPT_CODE](DO_CONCEPT_CODE.md) | `DO_CONTEXT_VERSION_ID` |
| [DO_CONCEPT_EXPLODE](DO_CONCEPT_EXPLODE.md) | `DO_CONTEXT_VERSION_ID` |

