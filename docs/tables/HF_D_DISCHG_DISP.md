# HF_D_DISCHG_DISP

> This is the HealthFacts dimension table that contains standard values for discharge dispositions

**Description:** HF_D_DISCHG_DISP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `DISCHG_DISP_CODE` | DOUBLE |  |  | The UB92 standard value that defines a specific discharge disposition |
| 3 | `DISCHG_DISP_CODE_DESC` | VARCHAR(190) |  |  | The UB92 standard textual description of a discharge disposition |
| 4 | `DISCHG_DISP_ID` | DOUBLE |  |  | A primary key to the table. Uniquely identifies a discharge disposition |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

