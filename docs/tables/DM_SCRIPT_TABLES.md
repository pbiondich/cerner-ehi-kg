# DM_SCRIPT_TABLES

> Holds table names used in all parent/request & child objects

**Description:** DM SCRIPT TABLES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SCHEMA_DATE` | DATETIME | NOT NULL |  | Rev date from DM_SCHEMA_VERSION |
| 2 | `SCRIPT_NAME` | VARCHAR(80) | NOT NULL |  | The script name of the object that the table information was generated for |
| 3 | `TABLE_NAME` | VARCHAR(32) | NOT NULL |  | Name of the tables used within a specific object |
| 4 | `USER_NAME` | VARCHAR(30) | NOT NULL |  | Shows what user is accessing the table, either a BATCH or an individual user |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

