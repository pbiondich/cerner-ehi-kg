# ENCNTR_ACP_HIST

> TRACKS THE HISTORY OF AUGMENTED CARE PERIODS WITHIN AN ENCOUNTER.

**Description:** ENCNTR ACP HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUGM_CARE_PERIOD_DISPOSAL_CD` | DOUBLE | NOT NULL |  | The historical encounter's disposition of the respective augmented care period. |
| 6 | `AUGM_CARE_PERIOD_PLAN_CD` | DOUBLE | NOT NULL |  | An indication of whether any of an augmented care period was initiated as a planned event. |
| 7 | `AUGM_CARE_PERIOD_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the augmented care period. |
| 8 | `AUGM_MEDICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their augmented care period. The category may be of treatment type, surgery, general resources, or other. |
| 9 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 10 | `ENCNTR_ACP_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key for the ENCNTR_ACP_HIST table. |
| 11 | `ENCNTR_AUGM_CARE_PERIOD_ID` | DOUBLE | NOT NULL | FK→ | FK from the encntr_augm_care_period table. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This column no longer used |
| 13 | `HIGH_DEPEND_CARE_LVL_DAYS` | DOUBLE |  |  | The number of days the patient received high dependency care within an augmented care period. |
| 14 | `INTENSIVE_CARE_LVL_DAYS` | DOUBLE |  |  | The number of days the patient received intensive care within an augmented care period. |
| 15 | `NUM_ORGAN_SYS_SUPPORT_NBR` | DOUBLE |  |  | The maximum number of organ systems supported during an augmented care period at any one time. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL |  | This column no longer used |
| 17 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 18 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 19 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and time the transaction, which triggered the history row, occurred. This field can be system assigned or manually manipulated by users. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_AUGM_CARE_PERIOD_ID` | [ENCNTR_AUGM_CARE_PERIOD](ENCNTR_AUGM_CARE_PERIOD.md) | `ENCNTR_AUGM_CARE_PERIOD_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

