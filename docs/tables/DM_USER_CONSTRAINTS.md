# DM_USER_CONSTRAINTS

> Similar to the user constraints table

**Description:** DM USER CONSTRAINTS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONSTRAINT_NAME` | VARCHAR(30) | NOT NULL |  | Name of the constraint |
| 2 | `CONSTRAINT_TYPE` | VARCHAR(1) |  |  | The type of the constraint definition |
| 3 | `DELETE_RULE` | VARCHAR(9) |  |  | The Delete rule for a referential constraint; CASCADE, NO ACTION |
| 4 | `OWNER` | VARCHAR(30) | NOT NULL |  | Owner of the constrained definition |
| 5 | `R_CONSTRAINT_NAME` | VARCHAR(30) |  |  | Name of unique constraint definition for referenced table |
| 6 | `R_OWNER` | VARCHAR(30) |  |  | Owner of table used in referential constraint |
| 7 | `STATUS` | VARCHAR(8) |  |  | Status of constraint: ENABLED,DISABLED |
| 8 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name associated with table for constraint definition |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

