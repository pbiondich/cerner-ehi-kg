# WORKFLOW_TASK_QUEUE_HIST

> Stores historical information from the WORKFLOW_TASK_QUEUE table.

**Description:** Workflow Task Queue History  
**Table type:** ACTIVITY  
**Primary key:** `WORKFLOW_TASK_QUEUE_HIST_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `ENTITY_ID` | DOUBLE |  |  | Uniquely identifies the related Entity |
| 4 | `ENTITY_NAME` | VARCHAR(30) |  |  | Identifies the Name of the related Entity. |
| 5 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority sequence for all the rows. The numbering will be from 1 to 3 to determine the priority of the row. |
| 6 | `PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the ETL process was started. |
| 7 | `QUEUE_STATUS_CD` | DOUBLE | NOT NULL |  | Dsiplays the status of the task queue item. |
| 8 | `REPLY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the long text row in which the processing reply is stored. |
| 9 | `REPLY_WF_TASK_QUEUE_LT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the workflow task queue long text row in which the reply to be processed is stored. |
| 10 | `REQUEST_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the long text row in which the request to be processed is stored. |
| 11 | `REQ_WF_TASK_QUEUE_LT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the workflow task queue long text row in which the requst to be processed is stored. |
| 12 | `RETRY_CNT` | DOUBLE | NOT NULL |  | Counter that increments every time an attempt to process fails. |
| 13 | `TASK_DATA_TXT` | VARCHAR(100) |  |  | Data further describing the task. |
| 14 | `TASK_IDENT` | VARCHAR(250) | NOT NULL |  | Identifies which task is queued for processing. |
| 15 | `TIMER_DELTA_VALUE` | DOUBLE |  |  | Contains the execution time taken by each status of task. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `WORKFLOW_TASK_QUEUE_HIST_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the WORKFLOW_TASK_QUEUE_HIST table. |
| 22 | `WORKFLOW_TASK_QUEUE_ID` | DOUBLE | NOT NULL |  | Uniquley identifies the related WORKFLOW_TASK_QUEUE record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPLY_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REPLY_WF_TASK_QUEUE_LT_ID` | [WORKFLOW_TASK_QUEUE_LT](WORKFLOW_TASK_QUEUE_LT.md) | `WORKFLOW_TASK_QUEUE_LT_ID` |
| `REQUEST_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REQ_WF_TASK_QUEUE_LT_ID` | [WORKFLOW_TASK_QUEUE_LT](WORKFLOW_TASK_QUEUE_LT.md) | `WORKFLOW_TASK_QUEUE_LT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WORKFLOW_TASK_QUEUE_LT](WORKFLOW_TASK_QUEUE_LT.md) | `WORKFLOW_TASK_QUEUE_HIST_ID` |

