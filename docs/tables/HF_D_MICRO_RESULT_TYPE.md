# HF_D_MICRO_RESULT_TYPE

> This is the HealthFacts dimension table that contains standard values for micro result types

**Description:** HF_D_Micro_Result_Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MICRO_RESULT_TYPE_CODE` | DOUBLE |  |  | An internal Health Facts identifier for the micro result type (the same as Task_Type_Flg in HNAM) |
| 2 | `MICRO_RESULT_TYPE_DESC` | VARCHAR(60) |  |  | The textual description of the micro result type (preliminary, final, amended, etc.) |
| 3 | `MICRO_RESULT_TYPE_ID` | DOUBLE |  |  | A unique non-intelligent identifier for the table |
| 4 | `TEST_TYPE` | VARCHAR(20) |  |  | Identifies the result as a microbiology or a susceptibility result |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

