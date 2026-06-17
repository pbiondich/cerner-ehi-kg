# DM_USER_CONS_COLUMNS

> Contains information from USER_CONSTRAINTS and USER_CONS_COLUMNS -- used in the refresh tools

**Description:** Contains information from USER_CONSTRAINTS and USER_CONS_COLUMNS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) |  |  | column name |
| 2 | `CONSTRAINT_NAME` | VARCHAR(30) |  |  | constraint name |
| 3 | `CONSTRAINT_TYPE` | CHAR(1) |  |  | constraint type |
| 4 | `OWNER` | VARCHAR(30) |  |  | table owner (oracle) |
| 5 | `PARENT_TABLE_NAME` | VARCHAR(30) |  |  | parent table name for the constraint |
| 6 | `POSITION` | DOUBLE |  |  | position of the column in the constraint |
| 7 | `R_CONSTRAINT_NAME` | VARCHAR(30) |  |  | parent constraint name |
| 8 | `R_OWNER` | VARCHAR(30) |  |  | owner of the parent constraint |
| 9 | `STATUS` | CHAR(8) |  |  | constraint status |
| 10 | `STATUS_IND` | DOUBLE |  |  | status indicator |
| 11 | `TABLE_NAME` | VARCHAR(30) |  |  | TABLE NAME |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

