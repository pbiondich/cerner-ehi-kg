# DM_CONSTRAINT_EXCEPTIONS

> Store row information for constraint violations

**Description:** DM CONSTRAINT EXCEPTONS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONSTRAINT` | VARCHAR(30) |  |  | Constraint name of violating row |
| 2 | `OWNER` | VARCHAR(30) |  |  | Owner of the Table (i.e., V500) |
| 3 | `ROW_ID` | VARCHAR(18) |  |  | ROWID of the violating row. Not a normal ID columns as in Millennium. No sequence. |
| 4 | `TABLE_NAME` | VARCHAR(30) |  |  | Table Name of the violating row |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

