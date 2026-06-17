# OPS_SCHEDULE_PARAM

> The operations schedule parameter table stores the scheduled parameter values for each step. These are the parameter values that will be used at execution time.

**Description:** Operations Schedule Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_SELECTION` | VARCHAR(2000) |  |  | The scheduled parameter value for batch selection. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `MESSAGE` | VARCHAR(100) |  |  | The scheduled parameter value for message. |
| 9 | `OPS_JOB_STEP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_JOB_STEP. Indicates which step this parameter belongs to. |
| 10 | `OPS_SCHEDULE_PARAM_ID` | DOUBLE | NOT NULL |  | Unique identifier for a scheduled parameter record. |
| 11 | `OPS_TASK_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_TASK. Indicates which task this parameter belongs to. |
| 12 | `OUTPUT_DIST` | VARCHAR(100) |  |  | The scheduled parameter value for output distribution. |
| 13 | `THRESH_IND` | DOUBLE |  |  | Indicates if the threshold for the scheduled step should be monitored or not. |
| 14 | `THRESH_PERCENT` | DOUBLE |  |  | The percentage over average elapsed time that the threshold time is set. |
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
| `OPS_TASK_ID` | [OPS_TASK](OPS_TASK.md) | `OPS_TASK_ID` |

