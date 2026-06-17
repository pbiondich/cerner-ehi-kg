# OPS_SCHEDULE_JOB_STEP

> The operations schedule job step table stores information about a step that has been initialized for a particular operations date.

**Description:** Operations Schedule Job Step  
**Table type:** ACTIVITY  
**Primary key:** `OPS_SCHEDULE_JOB_STEP_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AVG_DT_TM` | DATETIME |  |  | The average time is the offset between the scheduled task schedule_dt_tm and avg_dt_tm (thresh_dt_tm - avg_dt_tm) |
| 6 | `AVG_FLAG` | DOUBLE |  |  | 0 = no average has been calculated. 1 = Runtimes < 5. 2 = average is calculated, but threshold is not applicable. 3 = average is calculated, threshold is calculated. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `OPS_EVENT` | VARCHAR(100) |  |  | Stores run-time errors or information for the scheduled step. |
| 10 | `OPS_JOB_STEP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_JOB_STEP. Indicates which step this scheduled step relates. |
| 11 | `OPS_SCHEDULE_JOB_STEP_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a scheduled step record. |
| 12 | `OPS_SCHEDULE_TASK_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_SCHEDULE_TASK. Indicates to which scheduled task this scheduled step belongs. |
| 13 | `STATUS_CD` | DOUBLE | NOT NULL |  | Foreign key to CODE_VALUE. State of the scheduled step. |
| 14 | `THRESH_DT_TM` | DATETIME |  |  | The threshold time is the offset between the scheduled task schedule_dt_tm and thresh_dt_tm (schedule_dt_tm - thresh_dt_tm). |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS_JOB_STEP_ID` | [OPS_JOB_STEP](OPS_JOB_STEP.md) | `OPS_JOB_STEP_ID` |
| `OPS_SCHEDULE_TASK_ID` | [OPS_SCHEDULE_TASK](OPS_SCHEDULE_TASK.md) | `OPS_SCHEDULE_TASK_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OPS_SCHED_DEP](OPS_SCHED_DEP.md) | `D_SCHED_STEP_ID` |
| [OPS_SCHED_DEP](OPS_SCHED_DEP.md) | `T_SCHED_STEP_ID` |

