# DM_SOFT_CONSTRAINTS

> DM merge table

**Description:** DM table for dynamic soft constraints.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COLUMN` | VARCHAR(30) |  |  | Column name |
| 2 | `CHILD_TABLE` | VARCHAR(30) |  |  | Table name |
| 3 | `CHILD_WHERE` | VARCHAR(255) |  |  | Optional where clause |
| 4 | `CODE_SET` | DOUBLE | NOT NULL |  | code_set for the soft constraint |
| 5 | `EXCLUDE_IND` | DOUBLE |  |  | this constraint should be excluded |
| 6 | `PARENT_COLUMN` | VARCHAR(30) |  |  | Column name |
| 7 | `PARENT_TABLE` | VARCHAR(30) |  |  | Table name |
| 8 | `REFERENCE_IND` | DOUBLE |  |  | constraint is a reference type |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

