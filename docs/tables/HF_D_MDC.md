# HF_D_MDC

> This is that HealthFacts dimension table that contains standard values for CMS MDC's

**Description:** HF_D_MDC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Date that the MDC value came into use |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | Date that the MDC value stopped being used |
| 3 | `MDC` | VARCHAR(2) |  |  | The CMS standard numeric value assigned for a particular MDC |
| 4 | `MDC_DEFINITION` | VARCHAR(255) |  |  | The full definition of the MDC |
| 5 | `MDC_DESCRIPTION` | VARCHAR(45) |  |  | A longer description of the MDC |
| 6 | `MDC_DISPLAY` | VARCHAR(15) |  |  | A short description of the MDC |
| 7 | `MDC_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely defines an MDC |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 9 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 10 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

