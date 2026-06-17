# ENCNTR_INPTNT_REHAB_HIST

> Used for tracking history of columns on the ENCNTR_INPATIENT_REHAB table.

**Description:** Encounter Inpatient Rehab History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIT_IMPAIR_GRP_CD` | DOUBLE |  |  | The physical, mental, or cognitive limitation category for the patient at the time of admission. Each impairment group may require different types of support, accommodations, and interventions to address the specific challenges and needs of individuals with those limitations. |
| 6 | `CHANGE_BIT` | DOUBLE |  |  | Identifies which columns have had a change. |
| 7 | `DISCH_IMPAIR_GRP_CD` | DOUBLE |  |  | The physical, mental, or cognitive limitation category for the patient at the time of discharge. Each impairment group may require different types of support, accommodations, and interventions to address the specific challenges and needs of individuals with those limitations. |
| 8 | `ENCNTR_INPTNT_REHAB_HIST_ID` | DOUBLE | NOT NULL |  | A system generated code used to uniquely identify a row on the ENCNTR_INPTNT_REHAB_HIST table. |
| 9 | `ENCNTR_INPTNT_REHAB_ID` | DOUBLE |  |  | A system generated number used to uniquely identify a row on the ENCNTR_INPTNT_REHAB table. |
| 10 | `PM_HIST_TRACKING_ID` | DOUBLE |  | FK→ | ID used to uniquely identify the related row on the PM_HIST_TRACKING table. |
| 11 | `QUALIFYING_COND_CD` | DOUBLE |  |  | The condition that qualifies the patient for Medicare coverage at an inpatient rehab facility. |
| 12 | `TRACKING_BIT` | DOUBLE |  |  | Identifies which columns are being tracked for history. |
| 13 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 14 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

