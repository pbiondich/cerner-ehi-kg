# WORKFLOW_TASK_PAUSED

> Stores information for paused workflow tasks.

**Description:** Workflow Task Paused  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the entity associated to the original task queue row, as was stored in the workflow_task_queue table |
| 3 | `ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the entity associated to the original task queue row, as was stored in the workflow_task_queue table |
| 4 | `ORIGINAL_TASK_QUEUE_ID` | DOUBLE | NOT NULL |  | Id of the original workflor task |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the entity to which this paused task is related |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the entity to which this paused task is related |
| 7 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | priority sequence of the task |
| 8 | `PROCESS_DT_TM` | DATETIME |  |  | Time when the task would be processed |
| 9 | `QUEUE_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the task - from code set 4002853 |
| 10 | `REPLY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Id of the long text row where the task reply is stored |
| 11 | `REQUEST_CLOB` | LONGTEXT |  |  | Used to store the text related to the request for paused task. |
| 12 | `REQUEST_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Id of the long text row where the task request is stored |
| 13 | `RETRY_CNT` | DOUBLE | NOT NULL |  | Number of times task should be retried |
| 14 | `SCRIPT_NAME` | VARCHAR(250) | NOT NULL |  | The script used to handle the the task |
| 15 | `TASK_DATA_TXT` | VARCHAR(100) | NOT NULL |  | task data |
| 16 | `TASK_TYPE_FLAG` | DOUBLE | NOT NULL |  | The flag indicating which type of task is being saved. 1 = reminder; 2 - delay |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `WORKFLOW_TASK_PAUSED_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPLY_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REQUEST_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

