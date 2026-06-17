# DM_PARENT_CHILD

> Parent to Child and Child to Parent relationship table

**Description:** Environment Merge Parent Child Relationship Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COL_NAME` | VARCHAR(30) | NOT NULL |  | CHILD TABLE COLUMN NAME |
| 2 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | CHILD TABLE NAME |
| 3 | `PARENT_COL_NAME` | VARCHAR(30) | NOT NULL |  | PARENT TABLE COLUMN NAME |
| 4 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | PARENT TABLE NAME |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

