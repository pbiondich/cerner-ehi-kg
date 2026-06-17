# SCH_JOB

> The activity table for pending scheduling ops jobs.

**Description:** Scheduling Job  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTEMPT_CNT` | DOUBLE | NOT NULL |  | The number of times the system has attempted to complete a job. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `COMPLETE_DT_TM` | DATETIME |  |  | The date and time the job was completed. |
| 8 | `DISPLAY` | VARCHAR(255) |  |  | The string that gets displayed in the report title. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `JOB_CLASS` | VARCHAR(255) |  |  | The class of the requested job. A job class is just a string (EBS, PCT, etc.) that groups jobs of a similar nature. When you run the ops jobs, you'd run all jobs of a certain class. |
| 11 | `JOB_KEY` | VARCHAR(255) |  |  | A unique identifier for each job. It's a string that is constructed from various bits of the job fields (parent_entity_id + date + key_entity_name) |
| 12 | `JOB_STATE_CD` | DOUBLE | NOT NULL |  | The current state of the job request. For example, Completed, Requested, etc. |
| 13 | `JOB_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the job request. For example, Archive Perform, etc. |
| 14 | `JOB_TYPE_CD` | DOUBLE | NOT NULL |  | The type of job being requested. For example, Print job, Slot Stat job, etc. |
| 15 | `KEY_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier of the row in the table defined by Key Entity Name. |
| 16 | `KEY_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table that contributes to the job_key field. |
| 17 | `LAST_DT_TM` | DATETIME |  |  | The date and time of the last attempted execution. |
| 18 | `LOCK_DT_TM` | DATETIME |  |  | The date and time a lock was established on the job request. A lock prevents two processes from trying to execute the job at the same time. |
| 19 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier of the row in the table defined by Parent Entity Name. |
| 20 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Identifies a table where additional information about this row could be found |
| 21 | `REQUEST_DT_TM` | DATETIME | NOT NULL |  | The date and time the job was requested. |
| 22 | `SCH_CONVERSATION_ID` | DOUBLE | NOT NULL |  | The unique identifier of the conversation that produced the job request. |
| 23 | `SCH_JOB_ID` | DOUBLE | NOT NULL |  | The primary unique identifier of this table. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

