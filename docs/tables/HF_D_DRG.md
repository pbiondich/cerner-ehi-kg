# HF_D_DRG

> This is that HealthFacts dimension table that contains standard values for CMS DRG's

**Description:** HF_D_DRG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CLINICAL_SERVICE_CODE` | DOUBLE |  |  | A CMS code for the clinical service |
| 3 | `DRG` | VARCHAR(3) |  |  | The CMS standard numeric value assigned for a particular DRG |
| 4 | `DRG_DEFINITION` | VARCHAR(255) |  |  | The full definition of the DRG |
| 5 | `DRG_DESCRIPTION` | VARCHAR(45) |  |  | A longer description of the DRG |
| 6 | `DRG_DISPLAY` | VARCHAR(15) |  |  | A short description of the DRG |
| 7 | `DRG_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely defines a DRG |
| 8 | `DRG_TYPE` | VARCHAR(10) |  |  | The type of DRG system |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

