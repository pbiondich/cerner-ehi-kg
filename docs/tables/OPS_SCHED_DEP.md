# OPS_SCHED_DEP

> The operations schedule dependency table stores the information about a dependency that has been initialized for a particular operations date.

**Description:** operations scheduled dependency  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL | FK→ | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `D_SCHED_STEP_ID` | DOUBLE | NOT NULL | FK→ | The ops_schedule_job_step_id of the dependent step. |
| 7 | `D_SCHED_TASK_ID` | DOUBLE | NOT NULL | FK→ | The ops_schedule_task_id of the dependent task. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `OPS_JOB_VERIFY_ID` | DOUBLE | NOT NULL |  | The foreign key to the ops_job_verify table that tells which dependency this record belongs to. |
| 10 | `OPS_SCHED_DEP_ID` | DOUBLE | NOT NULL |  | Unique identifier for a scheduled dependency record. |
| 11 | `T_SCHED_STEP_ID` | DOUBLE | NOT NULL | FK→ | The ops_schedule_job_step_id of the triggering step. |
| 12 | `T_SCHED_TASK_ID` | DOUBLE | NOT NULL | FK→ | The ops_schedule_task_id of the triggering task. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `D_SCHED_STEP_ID` | [OPS_SCHEDULE_JOB_STEP](OPS_SCHEDULE_JOB_STEP.md) | `OPS_SCHEDULE_JOB_STEP_ID` |
| `D_SCHED_TASK_ID` | [OPS_SCHEDULE_TASK](OPS_SCHEDULE_TASK.md) | `OPS_SCHEDULE_TASK_ID` |
| `T_SCHED_STEP_ID` | [OPS_SCHEDULE_JOB_STEP](OPS_SCHEDULE_JOB_STEP.md) | `OPS_SCHEDULE_JOB_STEP_ID` |
| `T_SCHED_TASK_ID` | [OPS_SCHEDULE_TASK](OPS_SCHEDULE_TASK.md) | `OPS_SCHEDULE_TASK_ID` |

