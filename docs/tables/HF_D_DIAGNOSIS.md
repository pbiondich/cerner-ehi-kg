# HF_D_DIAGNOSIS

> This is the HealthFacts dimension table that contains standard values for ICD diagnosis

**Description:** HF_D_DIAGNOSIS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CONDITION_CATEGORY` | VARCHAR(150) |  |  | A standard diagnosis category to summarize related diagnoses. |
| 3 | `DIAGNOSIS_CODE` | VARCHAR(12) |  |  | The ICD diagnosis code |
| 4 | `DIAGNOSIS_DESCRIPTION` | VARCHAR(255) |  |  | The ICD diagnosis description |
| 5 | `DIAGNOSIS_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines an ICD diagnosis |
| 6 | `DIAGNOSIS_TYPE` | VARCHAR(50) |  |  | The type of ICD classification. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `HEALTHAWARE_IND` | DOUBLE |  |  | Indicator signifying if this is used for HealthAware: 0 No and 1 Yes |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

