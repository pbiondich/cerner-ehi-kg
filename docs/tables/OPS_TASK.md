# OPS_TASK

> The operations task table stores the information for jobs and job groups and their schedules.

**Description:** Operations Task  
**Table type:** REFERENCE  
**Primary key:** `OPS_TASK_ID`  
**Columns:** 29  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTOSTART_IND` | DOUBLE |  |  | Indicates if the operations server will automatically start the schedule task at its designated start time or wait for a manual start from an operator via the OpsView Monitor. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DAY_INTERVAL` | DOUBLE |  |  | Indicates how many days or weeks to skip before the task is scheduled to run again. |
| 8 | `ENABLE_IND` | DOUBLE |  |  | Indicates if this task is available for initialization by the OpsExec Server or not. |
| 9 | `END_DATE_IND` | DOUBLE |  |  | Indicates if this task has an ending effective date or if it will run forever. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FREQUENCY_TYPE` | DOUBLE |  |  | Indicates which scheduling model this task uses. |
| 12 | `JOB_GRP_NAME` | VARCHAR(40) |  |  | Name of the job group. |
| 13 | `JOB_NUMBER` | DOUBLE |  |  | Number to order the sequence of jobs within a job group. Valid for jobs within a job group only. |
| 14 | `OPS_CONTROL_GRP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_CONTROL_GROUP. Indicates to which control group this task belongs. |
| 15 | `OPS_JOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_JOB. Indicates which job this task one to one with. This field is not valid for job groups. |
| 16 | `OPS_TASK_ID` | DOUBLE | NOT NULL | PK | Unique identifier of a task record. |
| 17 | `OVERDUE_IND` | DOUBLE |  |  | Indicates if a recursive task can be skipped if the operations server is running in "catch up" mode when it is first started after a period of being down. Redundant tasks will only run once instead of several times all at once. |
| 18 | `PARENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_TASK. Indicates to which job group this job within a job group belongs. Valid for jobs within a job group only. |
| 19 | `TASK_TYPE` | DOUBLE |  |  | Indicates if this task is a job group, job, or job within a job group. |
| 20 | `THRESH_IND` | DOUBLE |  |  | Indicates if the elapsed time for this task should be monitored. |
| 21 | `THRESH_PERCENT` | DOUBLE |  |  | The percentage over average elapsed time that the threshold time is set. |
| 22 | `TIME_IND` | DOUBLE |  |  | Indicates if the task is scheduled to run once or many times during one day. |
| 23 | `TIME_INTERVAL` | DOUBLE |  |  | Indicates how many hours or minutes to skip before the task is scheduled to run again. |
| 24 | `TIME_INTERVAL_IND` | DOUBLE |  |  | Indicates the Time Interval units of measure. Minutes or hours. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS_CONTROL_GRP_ID` | [OPS_CONTROL_GROUP](OPS_CONTROL_GROUP.md) | `OPS_CONTROL_GRP_ID` |
| `OPS_JOB_ID` | [OPS_JOB](OPS_JOB.md) | `OPS_JOB_ID` |
| `PARENT_ID` | [OPS_TASK](OPS_TASK.md) | `OPS_TASK_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [OPS_DAY_OF_MONTH](OPS_DAY_OF_MONTH.md) | `OPS_TASK_ID` |
| [OPS_DAY_OF_WEEK](OPS_DAY_OF_WEEK.md) | `OPS_TASK_ID` |
| [OPS_JOB_VERIFY](OPS_JOB_VERIFY.md) | `D_TASK_ID` |
| [OPS_JOB_VERIFY](OPS_JOB_VERIFY.md) | `T_TASK_ID` |
| [OPS_MONTH_OF_YEAR](OPS_MONTH_OF_YEAR.md) | `OPS_TASK_ID` |
| [OPS_SCHEDULE_PARAM](OPS_SCHEDULE_PARAM.md) | `OPS_TASK_ID` |
| [OPS_SCHEDULE_TASK](OPS_SCHEDULE_TASK.md) | `OPS_TASK_ID` |
| [OPS_TASK](OPS_TASK.md) | `PARENT_ID` |
| [OPS_WEEK_OF_MONTH](OPS_WEEK_OF_MONTH.md) | `OPS_TASK_ID` |

