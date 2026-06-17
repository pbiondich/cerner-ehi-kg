# DM_REFCHG_TASK_QUEUE

> Stores a queue of tasks to be completed for a variety of RDDS processes

**Description:** Database Architecture Refchg Task Queue  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME |  |  | Shows the time the task was started |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | Shows the time the task was added to the table |
| 3 | `DM_REFCHG_TASK_QUEUE_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 4 | `END_DT_TM` | DATETIME |  |  | Shows the time the task was completed |
| 5 | `ERROR_TEXT` | VARCHAR(250) |  |  | Shows any error message that might've occurred. |
| 6 | `LOG_FILE` | VARCHAR(80) |  |  | Holds the log file name of the session that's running the task. |
| 7 | `PROCESS_NAME` | VARCHAR(30) | NOT NULL |  | Holds a description about what process the task belongs to |
| 8 | `RDBHANDLE_VALUE` | DOUBLE |  |  | Shows the process identifier to the session that is running a given task |
| 9 | `TASK_DESC` | VARCHAR(50) | NOT NULL |  | Holds the script name that should be executed as part of this task |
| 10 | `TASK_LEVEL` | DOUBLE | NOT NULL |  | Holds the priority level of when the task should be processed |
| 11 | `TASK_NAME` | VARCHAR(2000) | NOT NULL |  | Holds a description of the task |
| 12 | `TASK_REPLY` | VARCHAR(2000) | NOT NULL |  | Holds information used to verify task was a success |
| 13 | `TASK_REQUEST` | VARCHAR(2000) | NOT NULL |  | Holds information used to call the task |
| 14 | `TASK_RETRY_CNT` | DOUBLE | NOT NULL |  | Task retry count |
| 15 | `TASK_STATUS` | VARCHAR(30) | NOT NULL |  | Holds the status of each task (READY, RUNNING, SUCCESS, ERROR, etc.) |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

