# QMD_LH_E_MEASURE_OUTCOMES

> A table that stores the measure outcomes for electronic hospital quality submission that is leveraged by quality clearing house

**Description:** QMD_LH_E_MEASURE_OUTCOMES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCHARGE_DT_TM` | DATETIME |  |  | A column that acts as an identifier for discharge date time from the submission tables. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | A column that acts as an identifier for encounter id from the submission tables. |
| 3 | `METRIC_ID` | DOUBLE | NOT NULL |  | A column that acts as an identifier for metric id from the submission tables. |
| 4 | `METRIC_TYPE` | VARCHAR(50) |  |  | A column that acts as an identifier for metric type from the submission tables. |
| 5 | `OUTCOME_1` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 6 | `OUTCOME_10` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 7 | `OUTCOME_11` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 8 | `OUTCOME_12` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 9 | `OUTCOME_13` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 10 | `OUTCOME_14` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 11 | `OUTCOME_15` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 12 | `OUTCOME_16` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 13 | `OUTCOME_17` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 14 | `OUTCOME_18` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 15 | `OUTCOME_19` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 16 | `OUTCOME_2` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 17 | `OUTCOME_20` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 18 | `OUTCOME_3` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 19 | `OUTCOME_4` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 20 | `OUTCOME_5` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 21 | `OUTCOME_6` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 22 | `OUTCOME_7` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 23 | `OUTCOME_8` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 24 | `OUTCOME_9` | VARCHAR(20) |  |  | A column the represents the calculated outcome for a hospital quality measure |
| 25 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `VAL_1` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 28 | `VAL_10` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 29 | `VAL_2` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 30 | `VAL_3` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 31 | `VAL_4` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 32 | `VAL_5` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 33 | `VAL_6` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 34 | `VAL_7` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 35 | `VAL_8` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |
| 36 | `VAL_9` | VARCHAR(20) |  |  | A column that represents the outcome value for a given hospital quality measure |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

