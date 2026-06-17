# HF_D_ROUTE_ADMIN

> This is the HealthFacts dimension table that contains standard values for medication administration routes

**Description:** HF_D_ROUTE_ADMIN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ROUTE_ADMIN_DESCRIPTION` | VARCHAR(60) |  |  | The full description of the administration route |
| 2 | `ROUTE_ADMIN_DISPLAY` | VARCHAR(25) |  |  | A short description for the administration route |
| 3 | `ROUTE_ADMIN_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely defines an administration route |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

