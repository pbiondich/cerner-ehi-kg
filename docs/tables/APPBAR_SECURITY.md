# APPBAR_SECURITY

> Specifically for use with the application_taskbar

**Description:** Denormaliztion of the application task Security  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NAME` | VARCHAR(200) |  |  | Application Name |
| 2 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Application Number |
| 3 | `APP_GROUP_CD` | DOUBLE | NOT NULL |  | application group code |
| 4 | `OBJECT_NAME` | VARCHAR(60) |  |  | Object name |
| 5 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position Code |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

