# DO_RELATIONSHIP_TYPE

> Defines a discern ontology relationship type.

**Description:** Discern Ontology Relationship Type  
**Table type:** REFERENCE  
**Primary key:** `DO_RELATIONSHIP_TYPE_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_RELATIONSHIP_TYPE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_RELATIONSHIP_TYPE table. |
| 2 | `DO_RELATIONSHIP_TYPE_IDENT` | DOUBLE | NOT NULL |  | Discern Ontology relationship type identifier. It will be consistent across domains. |
| 3 | `DO_RELATIONSHIP_TYPE_MEAN` | VARCHAR(100) | NOT NULL |  | A globally unique identifier for others to write code against. It is like a CDF meaning. |
| 4 | `DO_RELATIONSHIP_TYPE_NAME` | VARCHAR(100) | NOT NULL |  | Name of the relationship type. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DO_CONCEPT_EXPLODE](DO_CONCEPT_EXPLODE.md) | `DO_RELATIONSHIP_TYPE_ID` |

