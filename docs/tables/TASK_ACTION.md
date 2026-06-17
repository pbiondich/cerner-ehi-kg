# TASK_ACTION

> Values of the field in the task_activity table that had action performed on it.

**Description:** TASK ACTION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RESCHEDULE_REASON_CD` | DOUBLE |  |  | Identifies that reason the task was rescheduled |
| 2 | `SCHEDULED_DT_TM` | DATETIME |  |  | The date and time that the task was scheduled to occur at the time the action was taken on the task. For unscheduled tasks, this field will be NULL |
| 3 | `TASK_ACTION_SEQ` | DOUBLE | NOT NULL |  | A unique, generated number that is used to identify and order the task action record. |
| 4 | `TASK_DT_TM` | DATETIME |  |  | The date and time an action was performed against this task. |
| 5 | `TASK_ID` | DOUBLE | NOT NULL |  | The task_id from the task_activity table. |
| 6 | `TASK_STATUS_CD` | DOUBLE |  |  | A codeset value that identifies the status of the task. |
| 7 | `TASK_STATUS_REASON_CD` | DOUBLE |  |  | The reason a task was put into the associated status. |
| 8 | `TASK_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

