# AOAV_HOSP_OUTCOMES

> This table stores normalized and summarized AOAV outcomes for hospital scores and predictions by AOAV day.

**Description:** AOAV HOSPITAL OUTCOMES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AOAV_HOSP_OUTCOMES_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `DAY_BEG_DT_TM` | DATETIME |  |  | Day begin date time |
| 7 | `DAY_END_DT_TM` | DATETIME |  |  | Day end date time |
| 8 | `DAY_NUM` | DOUBLE | NOT NULL |  | The day number for the outcome values |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter identifier on ENCOUNTER |
| 10 | `HOSP_LOS_PRED_VALUE` | DOUBLE |  |  | Hospital length of stay predictioin |
| 11 | `HOSP_MORTALITY_PRED_VALUE` | DOUBLE |  |  | Hospital mortality prediction |
| 12 | `NORMALIZED_CI_SCORE_VALUE` | DOUBLE |  |  | Normalized comorbidity index score |
| 13 | `NORMALIZED_PI_SCORE_VALUE` | DOUBLE |  |  | Normalized physiology index score |
| 14 | `NORMALIZED_SI_SCORE_VALUE` | DOUBLE |  |  | Normalized support index score |
| 15 | `PERSON_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This field is no longer used - DBARCHDTL-23349 |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

