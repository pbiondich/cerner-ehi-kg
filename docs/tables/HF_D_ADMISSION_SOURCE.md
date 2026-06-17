# HF_D_ADMISSION_SOURCE

> This is the HealthFacts dimension table that contains standard values for admission sources

**Description:** HF_D_ADMISSION_SOURCE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMISSION_SOURCE_CODE` | VARCHAR(12) |  |  | The standard code for admission source |
| 2 | `ADMISSION_SOURCE_CODE_DESC` | VARCHAR(60) |  |  | A description of the admission source code. |
| 3 | `ADMISSION_SOURCE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a admission source |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, MANUAL should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

