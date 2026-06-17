# OPS_JOB_VERIFY

> The operations job verify table stores job dependencies. JobA is dependent upon Job1 if Job1 must finish executing with a specific status before JobA can start.

**Description:** Operations Job Verify  
**Table type:** REFERENCE  
**Primary key:** `OPS_JOB_VERIFY_ID`  
**Columns:** 32  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLMATCH_IND` | DOUBLE |  |  | Indicates if the dependency is enforced for all scheduled instances of the dependent or just a few. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DAY_INTERVAL` | DOUBLE |  |  | If a dependency is enforced for just a few scheduled instances of the dependent and the dependent's schedule is either daily or weekly, this value determines the daily interval for the enforcement schedule. |
| 8 | `DEP_DT_TM` | DATETIME |  |  | not used |
| 9 | `DEP_JOB_STEP_ID` | DOUBLE |  |  | Not used |
| 10 | `DEP_TASK_ID` | DOUBLE |  |  | not used |
| 11 | `D_JJG_DT_TM` | DATETIME |  |  | The start time of the dependent job within a job group. |
| 12 | `D_STEP_ID` | DOUBLE |  | FK→ | ops_job_step_id of the dependent step |
| 13 | `D_TASK_DT_TM` | DATETIME |  |  | The scheduled time of the dependent task |
| 14 | `D_TASK_ID` | DOUBLE | NOT NULL | FK→ | ops_task_id of the dependent task |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `FAIL_IND` | DOUBLE |  |  | Determines whether the dependent will run if a trigger completes (fail_ind = 0) or errors (fail_ind = 1). |
| 17 | `LEVEL_TYPE` | DOUBLE |  |  | not used |
| 18 | `OPS_JOB_VERIFY_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a dependency record. |
| 19 | `SAMEDAY_IND` | DOUBLE |  |  | Determines if the trigger runs the same day as the dependent (sameday_ind = 1) or if the trigger runs the day before the dependent (sameday_ind = 0) |
| 20 | `SKIP_IND` | DOUBLE |  |  | Indicates whether the dependent is skipped (skip_ind = 1) or not (skip_ind = 0) if the trigger status is not satisfied. |
| 21 | `TRIG_DT_TM` | DATETIME |  |  | not used |
| 22 | `TRIG_JOB_STEP_ID` | DOUBLE |  |  | not used |
| 23 | `TRIG_TASK_ID` | DOUBLE |  |  | not used |
| 24 | `T_JJG_DT_TM` | DATETIME |  |  | Start time of the trigger job within a job group. |
| 25 | `T_STEP_ID` | DOUBLE |  | FK→ | ops_job_step_id of the trigger step |
| 26 | `T_TASK_DT_TM` | DATETIME |  |  | The scheduled time of the triggering task |
| 27 | `T_TASK_ID` | DOUBLE | NOT NULL | FK→ | The ops_task_id of the triggering task. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_STEP_ID` | [OPS_JOB_STEP](OPS_JOB_STEP.md) | `OPS_JOB_STEP_ID` |
| `D_TASK_ID` | [OPS_TASK](OPS_TASK.md) | `OPS_TASK_ID` |
| `T_STEP_ID` | [OPS_JOB_STEP](OPS_JOB_STEP.md) | `OPS_JOB_STEP_ID` |
| `T_TASK_ID` | [OPS_TASK](OPS_TASK.md) | `OPS_TASK_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [OPS_DAY_OF_MONTH](OPS_DAY_OF_MONTH.md) | `OPS_JOB_VERIFY_ID` |
| [OPS_DAY_OF_WEEK](OPS_DAY_OF_WEEK.md) | `OPS_JOB_VERIFY_ID` |
| [OPS_MONTH_OF_YEAR](OPS_MONTH_OF_YEAR.md) | `OPS_JOB_VERIFY_ID` |
| [OPS_WEEK_OF_MONTH](OPS_WEEK_OF_MONTH.md) | `OPS_JOB_VERIFY_ID` |

