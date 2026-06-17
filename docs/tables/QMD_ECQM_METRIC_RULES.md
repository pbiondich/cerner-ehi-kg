# QMD_ECQM_METRIC_RULES

> Contains the eCQM Metric rules that are needed for electronic submission.

**Description:** QMD_ECQM_METRIC_RULES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATED_DT_TM` | DATETIME |  |  | The date and time that the record was created. |
| 3 | `DENOM_IND` | VARCHAR(1000) |  |  | Indicates that the record qualifies as part of the denominator. |
| 4 | `METRIC_CONDITION` | VARCHAR(50) | NOT NULL |  | The condition that the metric belongs to |
| 5 | `METRIC_DISPLAY` | VARCHAR(50) | NOT NULL |  | The display name of the measure |
| 6 | `MINIMUM_CRITERIA` | VARCHAR(500) |  |  | The logic used for calculating the minimum value required for the measure. |
| 7 | `POP_IND` | VARCHAR(1000) |  |  | Indicates that the record qualifies as part of the population. |
| 8 | `SUBMETRIC_CONDITION` | VARCHAR(50) |  |  | The logic used for calculating the sub measure value. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | VARCHAR(100) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `YEAR` | DOUBLE |  |  | The year for which the measure was calculated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

