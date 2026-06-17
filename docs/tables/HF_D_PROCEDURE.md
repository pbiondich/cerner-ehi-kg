# HF_D_PROCEDURE

> This is the HealthFacts dimension table that contains standard values for ICD procedure

**Description:** HF_D_PROCEDURE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `PROCEDURE_CODE` | VARCHAR(12) |  |  | The ICD procedure code |
| 4 | `PROCEDURE_DESCRIPTION` | VARCHAR(255) |  |  | The ICD procedure description |
| 5 | `PROCEDURE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines an ICD procedure |
| 6 | `PROCEDURE_TYPE` | VARCHAR(50) |  |  | The type of ICD classification. "ICD-9_CM' |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

