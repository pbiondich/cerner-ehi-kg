# HF_D_ADMISSION_TYPE

> This is the HealthFacts dimension table that contains standard values for admission types

**Description:** HF_D_ADMISSION_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMISSION_TYPE_CODE` | VARCHAR(2) |  |  | The standard code for admission type |
| 2 | `ADMISSION_TYPE_CODE_DESC` | VARCHAR(60) |  |  | A description of the admission type code. |
| 3 | `ADMISSION_TYPE_CONCEPT` | VARCHAR(10) |  |  | A one character field containing the PHINVads concept identifier for admission type used for HealthSentry HL7. |
| 4 | `ADMISSION_TYPE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a admission type |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

