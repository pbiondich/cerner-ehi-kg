# HF_D_PRESENT_ON_ADMIT

> This is the HealthFacts dimension table that contains standard values for Present on Admission

**Description:** HF_D_Present_On_Admit  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PRESENT_ON_ADMIT_CODE` | VARCHAR(5) |  |  | The CMS standard value that defines a specific Present on Admission |
| 2 | `PRESENT_ON_ADMIT_DESC` | VARCHAR(60) |  |  | The CMS standard textual description of a Present on Admission |
| 3 | `PRESENT_ON_ADMIT_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a Present on Admission |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

