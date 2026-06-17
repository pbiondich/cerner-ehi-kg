# DM_AUDIT

> used to generically store misc logging information from data management processes

**Description:** used to generically store misc logging information from data management processe  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | VARCHAR(12) |  |  | string field describing the type of audit message this row represents |
| 2 | `AUDIT_DT_TM` | DATETIME | NOT NULL |  | date/time row was written |
| 3 | `AUDIT_ID` | DOUBLE | NOT NULL |  | primary key, uniquely defines the row |
| 4 | `AUDIT_LEVEL` | DOUBLE |  |  | indicates level of logging each row represents |
| 5 | `AUDIT_NAME` | VARCHAR(100) | NOT NULL |  | name field to segregate applications logging from each other |
| 6 | `TEXT` | LONGTEXT |  |  | actual logged message |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

