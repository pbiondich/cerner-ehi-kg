# DM_TABLE_TREE

> CONTAINS USER SCHEMA TREE LIST FOR ALL TABLES

**Description:** ENVIRONMENT MERGE TREE TABLE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | CHILD TABLE NAME |
| 2 | `MAJOR_PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | MAJOR PARENT TABLE NAME |
| 3 | `SEQUENCE` | DOUBLE | NOT NULL |  | SEQUENCE |
| 4 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | TABLE NAMEColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

