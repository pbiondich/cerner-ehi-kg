# HF_D_LAB_PROCEDURE

> health facts lab procedure table

**Description:** HF_D_LAB_PROCEDURE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HEALTHAWARE_IND` | DOUBLE |  |  | Indicates if the record was generated via the HealthAware solution. |
| 2 | `LAB_PROCEDURE_GROUP` | VARCHAR(60) |  |  | The lab procedure group can be used to find all related tests |
| 3 | `LAB_PROCEDURE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a lab procedure |
| 4 | `LAB_PROCEDURE_MNEMONIC` | VARCHAR(100) |  |  | Abbreviated name for a lab procedure |
| 5 | `LAB_PROCEDURE_NAME` | VARCHAR(100) |  |  | Full name of a laboratory test |
| 6 | `LAB_SUPER_GROUP` | VARCHAR(25) |  |  | A high level group relating lab procedures together |
| 7 | `LOINC_CODE` | VARCHAR(10) |  |  | Contains the Loinc Code associated with a lab procedure |
| 8 | `LOINC_IND` | DOUBLE |  |  | Reserved for future functionality |
| 9 | `LOINC_LONG` | VARCHAR(255) |  |  | The LOINC code display associated with a foreign file system DTA. |
| 10 | `LOINC_SHORT` | VARCHAR(60) |  |  | The LOINC code display associated with a foreign file system DTA. |
| 11 | `ODIN_IND` | DOUBLE |  |  | Indicates if a lab procedure is potentially reportable in the HealthSentry process |
| 12 | `PSP_RULE_GROUP` | VARCHAR(25) |  |  | Which group of PSP rules this lab |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

