# HF_D_INTERP_RESULT

> This is the HealthFacts dimension table that contains standard values for interpretative results

**Description:** HF_D_Interp_Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERP_RESULT_DESC` | VARCHAR(60) |  |  | The textual description of an interpretative result |
| 2 | `INTERP_RESULT_ID` | DOUBLE |  |  | A unique non-intelligent identifier for the table |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

