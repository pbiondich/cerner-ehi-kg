# OPS2_SCHED_JOB_GROUP

> The operations scheduled job group table stores information about a job group that has been initialized for a particular operations date.

**Description:** Operations Scheduled Job Group  
**Table type:** ACTIVITY  
**Primary key:** `OPS2_SCHED_JOB_GROUP_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTUAL_END_DT_TM` | DATETIME |  |  | The date and time for when the job group finished executing. |
| 3 | `ACTUAL_START_DT_TM` | DATETIME |  |  | The date and time for when the job group started executing. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTERNAL_USERNAME` | VARCHAR(100) |  |  | The name of the non-Millennium (e.g. Olympus) user that modified the record. |
| 7 | `INITIALIZE_DT_TM` | DATETIME | NOT NULL |  | The date and time this scheduled job group was initialized. |
| 8 | `OPS2_JOB_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_JOB_GROUP. Indicates to which job group this scheduled job group represents. |
| 9 | `OPS2_SCHED_CTRL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_SCHED_CTRL_GROUP. Indicates to which scheduled control group this scheduled job group belongs. |
| 10 | `OPS2_SCHED_JOB_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the OPS2_SCHED_JOB_GROUP table. |
| 11 | `ORIG_OPS2_SCHED_JOB_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the scheduled job groups. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 12 | `SCHEDULE_DATE_DT_TM` | DATETIME | NOT NULL |  | The date and time this scheduled job group is scheduled to execute. |
| 13 | `STATUS_CD` | DOUBLE | NOT NULL |  | State of the scheduled job group. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS2_JOB_GROUP_ID` | [OPS2_JOB_GROUP](OPS2_JOB_GROUP.md) | `OPS2_JOB_GROUP_ID` |
| `OPS2_SCHED_CTRL_GROUP_ID` | [OPS2_SCHED_CTRL_GROUP](OPS2_SCHED_CTRL_GROUP.md) | `OPS2_SCHED_CTRL_GROUP_ID` |
| `ORIG_OPS2_SCHED_JOB_GROUP_ID` | [OPS2_SCHED_JOB_GROUP](OPS2_SCHED_JOB_GROUP.md) | `OPS2_SCHED_JOB_GROUP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OPS2_SCHED_JOB](OPS2_SCHED_JOB.md) | `OPS2_SCHED_JOB_GROUP_ID` |
| [OPS2_SCHED_JOB_GROUP](OPS2_SCHED_JOB_GROUP.md) | `ORIG_OPS2_SCHED_JOB_GROUP_ID` |

