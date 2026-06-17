# QMD_EPOP_QUERY_LOG

> Stores the process log information for calculating the electronic population record.

**Description:** QMD_EPOP_QUERY_LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_HCO_ID` | DOUBLE |  |  | Healthcare organization Number (HCO) |
| 2 | `HCO_NBR` | DOUBLE |  |  | The Healthcare Organizatoin Number |
| 3 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | The system generated id for the health system source |
| 4 | `METRIC_CONDITION` | VARCHAR(50) |  |  | The condition that the measure belongs to |
| 5 | `PERIOD_NBR` | DOUBLE |  |  | The period that the record qualifies for. |
| 6 | `QUERY_LOG` | VARCHAR(4000) |  |  | The logged information during the creating of the electronic population record. |
| 7 | `QUERY_MESSAGE` | VARCHAR(500) |  |  | The result of the query |
| 8 | `SUB_METRIC_CONDITION` | VARCHAR(50) |  |  | The sub condition that the measure belongs to |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | VARCHAR(100) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `YEAR` | DOUBLE |  |  | The year of submission that the record qualifies for. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

