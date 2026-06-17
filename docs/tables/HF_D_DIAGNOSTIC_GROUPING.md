# HF_D_DIAGNOSTIC_GROUPING

> This is the HealthFacts dimension table that contains standard values for diagnostic grouping

**Description:** HF_D_DIAGNOSTIC_GROUPING  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSTIC_GROUPING_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a diagnostic grouping |
| 2 | `DRG_CODE` | VARCHAR(12) |  |  | The standard code for drg code |
| 3 | `DRG_CODE_DESC` | VARCHAR(255) |  |  | A description of the drg code |
| 4 | `DRG_ID` | DOUBLE | NOT NULL |  | Foreign key pointing to HF_D_DRG table |
| 5 | `DRG_TYPE` | VARCHAR(10) |  |  | The type of DRG system |
| 6 | `MDC_CODE` | VARCHAR(12) |  |  | The standard code for mdc code |
| 7 | `MDC_CODE_DESC` | VARCHAR(255) |  |  | A description of the mdc code. |
| 8 | `MDC_ID` | DOUBLE | NOT NULL |  | Foreign key pointing to HF_D_MDC table |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

