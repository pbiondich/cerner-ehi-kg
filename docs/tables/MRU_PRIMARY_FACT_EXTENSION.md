# MRU_PRIMARY_FACT_EXTENSION

> Associates an mru fact collection to a primary fact to specify what additional data must be considered in addition to the primary fact when making an mru based decision.

**Description:** Most Recently Used Primary Fact Extension  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEST_PRACTICE_IND` | DOUBLE | NOT NULL |  | Best practices are built in - disable community learning and individualized prompting if set. |
| 2 | `MRU_AREA_CD` | DOUBLE | NOT NULL |  | MRU area code |
| 3 | `MRU_FACT_COLLECTION_ID` | DOUBLE | NOT NULL | FK→ | Identify the fact collection associated to this primary mru fact |
| 4 | `MRU_PRIMARY_FACT_EXTENSION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 5 | `PRIMARY_FACT_ID` | DOUBLE | NOT NULL |  | Parent_entity_id for the primary fact |
| 6 | `PRIMARY_FACT_MODIFIER` | VARCHAR(50) | NOT NULL |  | Additional specification for the primary fact |
| 7 | `PRIMARY_FACT_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent entity name for the primary fact |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MRU_FACT_COLLECTION_ID` | [MRU_FACT_COLLECTION](MRU_FACT_COLLECTION.md) | `MRU_FACT_COLLECTION_ID` |

