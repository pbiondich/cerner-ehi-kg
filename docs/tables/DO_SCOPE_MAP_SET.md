# DO_SCOPE_MAP_SET

> Discern Ontology Map Value Sets.

**Description:** Discern Ontology Map Value Sets  
**Table type:** REFERENCE  
**Primary key:** `DO_SCOPE_MAP_SET_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_MAP_SET_ID` | DOUBLE | NOT NULL | FK→ | The associated row from the DO_MAP_SET table. |
| 2 | `DO_SCOPE_ID` | DOUBLE | NOT NULL | FK→ | The associated row from the DO_SCOPE table. |
| 3 | `DO_SCOPE_MAP_SET_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_SCOPE_MAP_SET table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_MAP_SET_ID` | [DO_MAP_SET](DO_MAP_SET.md) | `DO_MAP_SET_ID` |
| `DO_SCOPE_ID` | [DO_SCOPE](DO_SCOPE.md) | `DO_SCOPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DO_SCOPE_VALUE_SET_ALIAS](DO_SCOPE_VALUE_SET_ALIAS.md) | `DO_SCOPE_MAP_SET_ID` |

