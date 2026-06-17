# OPS2_JOB

> The operations job table stores information about a job and its default parameter values.

**Description:** Operations Job  
**Table type:** REFERENCE  
**Primary key:** `OPS2_JOB_ID`  
**Columns:** 20  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTOSTART_IND` | DOUBLE | NOT NULL |  | Indicates if the OpsExec server will automatically start processing this job at its scheduled time or wait until a user manually starts the job via the Operations front-end tools. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `ENABLED_IND` | DOUBLE | NOT NULL |  | Indicates if this job is eligible to run. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTERNAL_USERNAME` | VARCHAR(100) |  |  | The name of the non-Millennium (e.g. Olympus) user that modified the record. |
| 7 | `JOB_NAME` | VARCHAR(50) | NOT NULL |  | The name of the job. |
| 8 | `JOB_SEQ` | DOUBLE | NOT NULL |  | For jobs within a job group, a number that orders the sequence of jobs within the job group. |
| 9 | `OPS2_CTRL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_CTRL_GROUP. Indicates to which control group this job or job within a job group belongs. |
| 10 | `OPS2_JOB_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_JOB_GROUP. Indicates to which job group this job belongs. |
| 11 | `OPS2_JOB_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the OPS2_JOB table. |
| 12 | `OPS2_JOB_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_JOB_TEMPLATE. Indicates to which job template this job or job within a job group was originally created from. |
| 13 | `ORIG_OPS2_JOB_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the jobs. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 14 | `THRESHOLD_IND` | DOUBLE | NOT NULL |  | Indicates if the elapsed time for this job should be monitored. |
| 15 | `THRESHOLD_PCT` | DOUBLE | NOT NULL |  | The percentage over the job's average elapsed time at which a threshold alert should be reported. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS2_CTRL_GROUP_ID` | [OPS2_CTRL_GROUP](OPS2_CTRL_GROUP.md) | `OPS2_CTRL_GROUP_ID` |
| `OPS2_JOB_GROUP_ID` | [OPS2_JOB_GROUP](OPS2_JOB_GROUP.md) | `OPS2_JOB_GROUP_ID` |
| `OPS2_JOB_TEMPLATE_ID` | [OPS2_JOB_TEMPLATE](OPS2_JOB_TEMPLATE.md) | `OPS2_JOB_TEMPLATE_ID` |
| `ORIG_OPS2_JOB_ID` | [OPS2_JOB](OPS2_JOB.md) | `OPS2_JOB_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [OPS2_JOB](OPS2_JOB.md) | `ORIG_OPS2_JOB_ID` |
| [OPS2_JOB_SCHED](OPS2_JOB_SCHED.md) | `OPS2_JOB_ID` |
| [OPS2_SCHED_JOB](OPS2_SCHED_JOB.md) | `OPS2_JOB_ID` |
| [OPS2_STEP](OPS2_STEP.md) | `OPS2_JOB_ID` |

