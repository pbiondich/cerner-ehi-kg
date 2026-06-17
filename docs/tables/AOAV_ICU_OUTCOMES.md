# AOAV_ICU_OUTCOMES

> This table is for AOAV reporting. This table stores the AOAV Outcomes for patients defined in the corresponding AOAV_ICU_STAY table.

**Description:** AOAV ICU OUTCOMES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AOAV_ICU_OUTCOMES_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `AOAV_ICU_STAY_ID` | DOUBLE | NOT NULL | FK→ | AOAV ICU stay identifier |
| 4 | `ICU_DAY_BEG_DT_TM` | DATETIME |  |  | ICU day begin date time |
| 5 | `ICU_DAY_END_DT_TM` | DATETIME |  |  | ICU day end date time |
| 6 | `ICU_DAY_NUM` | DOUBLE | NOT NULL |  | ICU Predictive Day Number. ICU Predictive Day 1 starts when a patient is transferred into an AOAV ICU mapped level of care. |
| 7 | `ICU_LOS_PRED_VALUE` | DOUBLE |  |  | ICU length of stay prediction - the predicted length of stay in the ICU AOAV level of care. |
| 8 | `ICU_MORTALITY_PRED_VALUE` | DOUBLE |  |  | ICU mortality prediction - the probability of dying before transfer from the ICU AOAV Level of care. |
| 9 | `ICU_VENT_DURATION_PRED_VALUE` | DOUBLE |  |  | ICU vent duration prediction |
| 10 | `NORMALIZED_ICU_CI_SCORE_VALUE` | DOUBLE |  |  | Normalized ICU comorbidity index score. This is the portion of the Severity of Illness (SOI) that is based on the patient's comorbidities. |
| 11 | `NORMALIZED_ICU_PI_SCORE_VALUE` | DOUBLE |  |  | Normalized ICU physiology index score. This is the portion of the Severity of Illness (SOI) that is based on the patient's physiology values. |
| 12 | `NORMALIZED_ICU_SI_SCORE_VALUE` | DOUBLE |  |  | Normalized ICU support index score. This is the portion of the Severity of Illness (SOI) that is based on the patient's support therapies. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AOAV_ICU_STAY_ID` | [AOAV_ICU_STAY](AOAV_ICU_STAY.md) | `AOAV_ICU_STAY_ID` |

