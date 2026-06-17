# DO_CODE_SYSTEM

> Discern Ontology Code System

**Description:** DO_CODE_SYSTEM  
**Table type:** REFERENCE  
**Primary key:** `DO_CODE_SYSTEM_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_SOURCE_MEAN` | VARCHAR(12) |  |  | CDF meaning for code set 12100. |
| 2 | `DO_CODE_SYSTEM_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_CODE_SYSTEM table. |
| 3 | `DO_CODE_SYSTEM_IDENT` | DOUBLE | NOT NULL |  | Discern Ontology code system identifier. Will be consistent across domains. |
| 4 | `DO_CODE_SYSTEM_NAME` | VARCHAR(100) | NOT NULL |  | Name of the code system |
| 5 | `SOURCE_VOCABULARY_MEAN` | VARCHAR(12) |  |  | CDF meaning from code set 400. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DO_CODE_SYSTEM_URI](DO_CODE_SYSTEM_URI.md) | `DO_CODE_SYSTEM_ID` |
| [DO_CONCEPT_CODE](DO_CONCEPT_CODE.md) | `DO_CODE_SYSTEM_ID` |

