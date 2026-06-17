# HF_D_MEDICAL_SERVICE

> A dimension table that stores the list of medical services.

**Description:** HF_D_MEDICAL_SERVICE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MEDICAL_SERVICE_CODE` | VARCHAR(40) |  |  | The short abbreviation that represents the medical service (hospital service). Approved values for HL7. |
| 2 | `MEDICAL_SERVICE_DESC` | VARCHAR(100) |  |  | The description of the medical service (hospital service). Used for HealthSentry and PV1.10. |
| 3 | `MEDICAL_SERVICE_ID` | DOUBLE |  |  | PRIMARY KEY |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

