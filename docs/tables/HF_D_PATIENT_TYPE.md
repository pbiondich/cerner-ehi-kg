# HF_D_PATIENT_TYPE

> This is the HealthFacts dimension table that contains standard values for patient types

**Description:** HF_D_PATIENT_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PATIENT_TYPE_DESC` | VARCHAR(60) |  |  | A description of the patient type. Defines the type of visit made |
| 2 | `PATIENT_TYPE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a patient type |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

