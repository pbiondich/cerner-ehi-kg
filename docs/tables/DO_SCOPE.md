# DO_SCOPE

> Defines the scope names and their descriptions.

**Description:** Discern Ontolology Scope  
**Table type:** REFERENCE  
**Primary key:** `DO_SCOPE_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_SCOPE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_SCOPE table. |
| 2 | `DO_SCOPE_IDENT` | DOUBLE | NOT NULL |  | Holds the Ontology Cloud Identifier for the Scope. This is used when synching data between the cloud and Millennium domain. |
| 3 | `DO_SCOPE_NAME` | VARCHAR(1000) | NOT NULL |  | This is the unique name for a scope as defined by FHIR. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DO_SCOPE_ALIAS](DO_SCOPE_ALIAS.md) | `DO_SCOPE_ID` |
| [DO_SCOPE_MAP_SET](DO_SCOPE_MAP_SET.md) | `DO_SCOPE_ID` |
| [DO_SCOPE_NAMESPACE_ALIAS](DO_SCOPE_NAMESPACE_ALIAS.md) | `DO_SCOPE_ID` |

