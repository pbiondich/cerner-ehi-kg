# DM_PC_TEMP

> TEMPORARY WORK TABLE

**Description:** TEMPORARY WORK TABLE FOR DM_PARENT_CHILD TABLE AND ENVIRONMENT MERGE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_TABLE` | VARCHAR(30) |  |  | CHILD TABLE NAME |
| 2 | `LEVEL_IND` | DOUBLE | NOT NULL |  | LEVEL INDICATORColumn |
| 3 | `MAJOR_PARENT_TABLE` | VARCHAR(30) |  |  | MAJOR PARENT TABLE NAME |
| 4 | `MINOR_TABLE` | VARCHAR(30) |  |  | MINOR TABLE NAME |
| 5 | `SEQUENCE` | DOUBLE | NOT NULL |  | SEQUENCE |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

