# OPS2_SCHED_STEP

> The operations schedule job step table stores information about a step that has been initialized for a particular operations date.

**Description:** Operations Scheduled Step  
**Table type:** ACTIVITY  
**Primary key:** `OPS2_SCHED_STEP_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTUAL_END_DT_TM` | DATETIME |  |  | The date and time for when the step finished executing. |
| 3 | `ACTUAL_START_DT_TM` | DATETIME |  |  | The date and time for when the step started executing. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `OPS2_SCHED_JOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_SCHED_JOB. Indicates to which scheduled job this scheduled step belongs. |
| 7 | `OPS2_SCHED_STEP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the OPS2_SCHED_STEP table. |
| 8 | `OPS2_STEP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_STEP. Indicates to which step this scheduled step represents. |
| 9 | `OPS_EVENT_TXT` | VARCHAR(255) |  |  | Stores additional information regarding events related to the state of the scheduled step. |
| 10 | `ORIG_OPS2_SCHED_STEP_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the scheduled steps. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 11 | `STATUS_CD` | DOUBLE | NOT NULL |  | State of the scheduled step |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS2_SCHED_JOB_ID` | [OPS2_SCHED_JOB](OPS2_SCHED_JOB.md) | `OPS2_SCHED_JOB_ID` |
| `OPS2_STEP_ID` | [OPS2_STEP](OPS2_STEP.md) | `OPS2_STEP_ID` |
| `ORIG_OPS2_SCHED_STEP_ID` | [OPS2_SCHED_STEP](OPS2_SCHED_STEP.md) | `OPS2_SCHED_STEP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OPS2_SCHED_STEP](OPS2_SCHED_STEP.md) | `ORIG_OPS2_SCHED_STEP_ID` |

