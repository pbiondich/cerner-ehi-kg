# QC_STAT_PERIOD

> Stores the statistics accumulated for a given period time, assay, and control.

**Description:** Quality Control Statistics Period  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_CNT` | DOUBLE |  |  | Defines the number of alpha responses that were abnormal for the given statistical range. |
| 2 | `ARL_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the service resource, discrete task assay, and control lot associated with the QC statistics period. Creates a relationship to the assay resource lot table. |
| 3 | `BEG_DT_TM` | DATETIME |  |  | Defines the beginning date and time for the range of statistical information. |
| 4 | `CONTROL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific control material associated with the QC statistical period. Creates a relationship to the control material table. |
| 5 | `CO_VAR` | DOUBLE |  |  | Stores the statistic for coefficient of variation. |
| 6 | `END_DT_TM` | DATETIME |  |  | Defines the ending date and time for the range of statistical information. |
| 7 | `FREQUENCY_FLAG` | DOUBLE |  |  | Defines the frequency of the statistics that have been accumulated. |
| 8 | `F_VAL` | DOUBLE |  |  | Stores the statistic for the f-value. |
| 9 | `LOT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific quality control lot associated with the statistical period. Creates a relationship to the control lot table. |
| 10 | `MEAN` | DOUBLE |  |  | Stores the mean for the given statistical range. |
| 11 | `NORMAL_CNT` | DOUBLE |  |  | Defines the number of alpha responses that were normal for the given statistical range. |
| 12 | `OPS_IND` | DOUBLE |  |  | Indicates whether the statistical period was requested by an operations process. A value of 0 indicates the statistical period was requested manually or ad hoc. A value of 1 indicates the statistical period was requested by operations. |
| 13 | `PDM_PARAM_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific patient data monitoring parameters used to create the QC result. Creates a relationship to the patient data monitoring parameters table. |
| 14 | `PDM_RANGE_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific patient data monitoring range parameters (such as species, gender, and age) used to create the QC result. Creates a relationship to the patient data monitoring ranges table. |
| 15 | `QC_RESULT_TYPE_FLAG` | DOUBLE |  |  | Defines the type of quality control result. |
| 16 | `QC_STAT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific statistical period. |
| 17 | `QC_STAT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific type of statistics being accumulated. (Currently not implemented) |
| 18 | `RESULTS_INC_FLAG` | DOUBLE |  |  | Defines what result values were included in the statistical range. |
| 19 | `RESULT_CNT` | DOUBLE |  |  | Defines the number of results included for the given statistical range. |
| 20 | `REVIEW_CNT` | DOUBLE |  |  | Defines the number of alpha responses that were flagged for review for the given statistical range. |
| 21 | `SERIES_INTERVAL_NBR` | DOUBLE | NOT NULL |  | This is the interval value used when the user chose to use the analytical series to calculate statistics. |
| 22 | `SERIES_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | This is the sequence value used when the user chose to use the analytical series to calculate statistics. |
| 23 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific service resource used for the given statistical period. |
| 24 | `SERVICE_RESOURCE_GROUP_IND` | DOUBLE |  |  | Indicates whether QC results were accumulated for a group of service resources. A value of 0 indicates the results were accumulated for a specific service resource. A value of 1 indicates the results were accumulated for a service resource group. |
| 25 | `STD_DEV` | DOUBLE |  |  | Stores the standard deviation statistic for the given statistical period. |
| 26 | `SUM_OF_RESULTS` | DOUBLE |  |  | Stores the sum of the results for the given statistical period. |
| 27 | `SUM_OF_SQUARES` | DOUBLE |  |  | Stores the sum of the results individually squared for the given statistical period. |
| 28 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific discrete task assay for which statistics were accumulated during the statistical period. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 34 | `Z_STAT` | DOUBLE |  |  | Stores the z-stat statistic for the given statistical period. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTROL_ID` | [CONTROL_MATERIAL](CONTROL_MATERIAL.md) | `CONTROL_ID` |
| `LOT_ID` | [CONTROL_LOT](CONTROL_LOT.md) | `LOT_ID` |
| `PDM_PARAM_ID` | [PDM_PARAMS](PDM_PARAMS.md) | `PDM_PARAM_ID` |
| `PDM_RANGE_ID` | [PDM_RANGES](PDM_RANGES.md) | `PDM_RANGE_ID` |

