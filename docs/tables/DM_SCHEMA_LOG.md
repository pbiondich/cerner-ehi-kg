# DM_SCHEMA_LOG

> Log for downtime schema estimates.

**Description:** DM SCHEMA LOG  
**Table type:** ACTIVITY  
**Primary key:** `RUN_ID`  
**Columns:** 4  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEN_DT_TM` | DATETIME |  |  | Date and time downtime estimates were generated. |
| 2 | `OCD` | DOUBLE | NOT NULL |  | OCD number. |
| 3 | `RUN_ID` | DOUBLE | NOT NULL | PK | Primary key. |
| 4 | `SCHEMA_DATE` | DATETIME |  |  | Schema date. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_SCHEMA_OP_LOG](DM_SCHEMA_OP_LOG.md) | `RUN_ID` |

