# HF_D_FORMULARY_TYPE

> This is the HealthFacts dimension table that contains standard values for formulary type

**Description:** HF_D_FORMULARY_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORMULARY_TYPE_CODE` | VARCHAR(20) |  |  | A short description of the formulary type |
| 2 | `FORMULARY_TYPE_DESC` | VARCHAR(60) |  |  | The description for the formulary type |
| 3 | `FORMULARY_TYPE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a formulary type |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

