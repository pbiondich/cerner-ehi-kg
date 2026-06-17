# QMD_EPOP_CNT

> Stores the electronic population count for submission.

**Description:** QMD_EPOP_CNT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DISCHARGE_DT_TM` | VARCHAR(20) |  |  | The date and time that the discharge process began. |
| 2 | `BR_HCO_ID` | DOUBLE |  |  | Healthcare organization Number (HCO) |
| 3 | `DENOM_CNT` | DOUBLE |  |  | The count of the number of records in the denominator. |
| 4 | `END_DISCHARGE_DT_TM` | VARCHAR(20) |  |  | The date and time that the discharge process was finished. |
| 5 | `ERROR_IND` | DOUBLE |  |  | Indicates if there was an error in generating the record. |
| 6 | `FIVE_OR_FEWER` | VARCHAR(20) |  |  | The logic for the five or fewer submission qualification. |
| 7 | `HCO_NBR` | DOUBLE |  |  | The Healthcare Organizatoin Number |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | The system generated id for the health system source. |
| 9 | `METRIC_CONDITION` | VARCHAR(50) |  |  | The condition that the measure belongs to. |
| 10 | `METRIC_DISPLAY` | VARCHAR(50) |  |  | The display value of the measure. |
| 11 | `PERIOD` | DOUBLE |  |  | The period that the record qualifies for. |
| 12 | `PERIOD_DISPLAY` | VARCHAR(50) |  |  | The period that the record qualifies for. |
| 13 | `POP_CNT` | DOUBLE |  |  | The count of the number of records in the population. |
| 14 | `SUBMETRIC_CONDITION` | VARCHAR(50) |  |  | The condition that the sub measure belongs to. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `YEAR` | DOUBLE |  |  | The year of submission that the record qualifies for. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

