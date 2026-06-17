# DM_SCRIPT_STAT

> Holds statistical information about all parent/request & child objects

**Description:** DM SCRIPT STAT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_NAME` | VARCHAR(60) | NOT NULL |  | Descriptive modifier that further describes the type of the object |
| 2 | `DATA_VALUE` | DOUBLE | NOT NULL |  | Contains a sum of similar data names occurring within the same object |
| 3 | `SCHEMA_DATE` | DATETIME | NOT NULL |  | Rev date from DM_SCHEMA_VERSION |
| 4 | `SCRIPT_NAME` | VARCHAR(80) | NOT NULL |  | The script name of the object that the statistics were generated for |
| 5 | `USER_NAME` | VARCHAR(30) | NOT NULL |  | Shows what user is accessing the table, either a BATCH or an individual user |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

