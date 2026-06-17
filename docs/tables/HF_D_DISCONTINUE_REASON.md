# HF_D_DISCONTINUE_REASON

> This is the HealthFacts dimension table that contains standard values for discontinue reason

**Description:** HF_D_DISCONTINUE_REASON  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCONTINUE_REASON_CODE` | VARCHAR(20) |  |  | A short description of the discontinue reason |
| 2 | `DISCONTINUE_REASON_DESC` | VARCHAR(60) |  |  | The description for the discontinue reason |
| 3 | `DISCONTINUE_REASON_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a discontinue reason |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

