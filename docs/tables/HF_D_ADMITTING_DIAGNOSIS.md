# HF_D_ADMITTING_DIAGNOSIS

> Contains the distinct list of possible diagnosis for selection during admission diagnosis.

**Description:** HF_D_ADMITTING_DIAGNOSIS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMITTING_DIAGNOSIS_DESC` | VARCHAR(255) |  |  | The raw text admitting diagnosis description provided by the clinical system. Not codified at this time. |
| 2 | `ADMITTING_DIAGNOSIS_ID` | DOUBLE |  |  | A unique identifier used to link the admitting_diagnosis dimension table to the hf_f_encounter table. |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

