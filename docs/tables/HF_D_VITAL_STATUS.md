# HF_D_VITAL_STATUS

> The dimension table of possible vital status.

**Description:** HF_D_VITAL_STATUS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 2 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 3 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |
| 4 | `VITAL_STATUS_DESC` | VARCHAR(60) |  |  | The description of the vital status. |
| 5 | `VITAL_STATUS_ID` | DOUBLE |  |  | PRIMARY KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

