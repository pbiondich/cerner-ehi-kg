# DM_REF_CONS_COLS

> Work table for recursive merge.

**Description:** Contains referential constraints, indexed by parent table, for Recursive Merge  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COLUMN` | VARCHAR(30) | NOT NULL |  | Column name in the referential constraint. |
| 2 | `CHILD_CONSTRAINT` | VARCHAR(30) | NOT NULL |  | Referential Constraint Name |
| 3 | `CHILD_POSITION` | DOUBLE | NOT NULL |  | Position of the constraint column in the constraint. |
| 4 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | Table name that the constraint is on. |
| 5 | `PARENT_COLUMN` | VARCHAR(30) | NOT NULL |  | Column name in the table that the referential constraint refers to. |
| 6 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | Table name that the referential constraint refers to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

