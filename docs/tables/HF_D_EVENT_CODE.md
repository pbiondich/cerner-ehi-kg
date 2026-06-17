# HF_D_EVENT_CODE

> HF_D_EVENT_CODE table

**Description:** HF_D_EVENT_CODE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_CODE_CATEGORY` | VARCHAR(40) |  |  | The category of the event code. |
| 2 | `EVENT_CODE_DESC` | VARCHAR(60) |  |  | The description for the event code |
| 3 | `EVENT_CODE_DISPLAY` | VARCHAR(40) |  |  | The display value of the event code. |
| 4 | `EVENT_CODE_GROUP` | VARCHAR(40) |  |  | The group of event codes that the event code belongs to. |
| 5 | `EVENT_CODE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines an event code |
| 6 | `HEALTHAWARE_IND` | DOUBLE |  |  | Indicates if the record was generated via the HealthAware solution. |
| 7 | `HS_IND` | DOUBLE |  |  | Indicates if the record was generated via the HealthSentry solution. |
| 8 | `LOINC_CODE` | VARCHAR(10) |  |  | The LOINC code associated with a foreign file system DTA. |
| 9 | `SNOMED_CODE` | VARCHAR(15) |  |  | The Health Data assigned SNOMED code if applicable for the event. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

