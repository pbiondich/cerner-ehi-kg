# HF_D_DIAGNOSIS_TYPE

> The dimension table for the types of diagnosis.

**Description:** HF_D_DIAGNOSIS_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS_TYPE_DISPLAY` | VARCHAR(60) |  |  | The display value of the diagnosis type. |
| 2 | `DIAGNOSIS_TYPE_ID` | DOUBLE |  |  | PRIMARY KEY |
| 3 | `DIAGNOSIS_TYPE_MEANING` | VARCHAR(12) |  |  | The meaning for the diagnosis type is the same as the display or an abbreviation. |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

