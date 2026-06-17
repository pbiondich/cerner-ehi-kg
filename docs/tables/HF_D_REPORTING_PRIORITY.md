# HF_D_REPORTING_PRIORITY

> This is the HealthFacts dimension table that contains standard values for lab reporting priorities

**Description:** HF_D_Reporting_Priority  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `REPORTING_PRIORITY_CODE` | VARCHAR(12) |  |  | A short description of the reporting priority (ASAP) |
| 2 | `REPORTING_PRIORITY_DESC` | VARCHAR(60) |  |  | The textual description of the reporting priority (As Soon As Possible) |
| 3 | `REPORTING_PRIORITY_ID` | DOUBLE |  |  | A unique non-intelligent identifier for the table |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

