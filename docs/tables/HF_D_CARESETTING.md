# HF_D_CARESETTING

> This is the HealthFacts dimension table that contains the standard value for caresetting

**Description:** HF_D_CARESETTING  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CARESETTING_DESC` | VARCHAR(60) |  |  | The description of the caresetting |
| 2 | `CARESETTING_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a caresetting |
| 3 | `PHIN_CARESETTING_DESC` | VARCHAR(100) |  |  | PHINVADs is expecting a specific description for valid nursing units. Only records that match the PHINVads table will be populated. |
| 4 | `PHIN_CODE` | VARCHAR(10) |  |  | The standard PHIN concept code for the medical service. |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

