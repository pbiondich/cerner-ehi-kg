# DO_SCOPE_VALUE_SET_ALIAS

> Defines an alias for a valueset with in a scope and a mapset combination. The valueset could either be a source or a target.

**Description:** Discern Ontology Scope Value Set Alias  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_SCOPE_MAP_SET_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the scoped map set, a row in the DO_SCOPE_MAP_SET database table. |
| 2 | `DO_SCOPE_VALUE_SET_ALIAS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DO_SCOPE_VALUE_SET_ALIAS table. |
| 3 | `DO_VALUE_SET_ALIAS` | VARCHAR(128) | NOT NULL |  | The Scoped Map Set Alias for a value set. This is the Alias to use when making a map request for a scope. |
| 4 | `DO_VALUE_SET_ID` | DOUBLE | NOT NULL | FK→ | The identifier of a value set definition, a row in the DO_VALUE_SET database table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_SCOPE_MAP_SET_ID` | [DO_SCOPE_MAP_SET](DO_SCOPE_MAP_SET.md) | `DO_SCOPE_MAP_SET_ID` |
| `DO_VALUE_SET_ID` | [DO_VALUE_SET](DO_VALUE_SET.md) | `DO_VALUE_SET_ID` |

