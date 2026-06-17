# WORKFLOW_TASK_QUEUE_LT

> Contains long text data for requests and replies for workflow task processing

**Description:** Workflow Task Queue Long Text  
**Table type:** ACTIVITY  
**Primary key:** `WORKFLOW_TASK_QUEUE_LT_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LONG_TEXT` | LONGTEXT |  |  | Used to store the text related to the workflow_task_queue_hist row. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `WORKFLOW_TASK_QUEUE_HIST_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifes the related row on the workfow_task_queue_hist table. |
| 14 | `WORKFLOW_TASK_QUEUE_LT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the WORKFLOW_TASK_QUEUE_LT TABLE. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKFLOW_TASK_QUEUE_HIST_ID` | [WORKFLOW_TASK_QUEUE_HIST](WORKFLOW_TASK_QUEUE_HIST.md) | `WORKFLOW_TASK_QUEUE_HIST_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [WORKFLOW_TASK_QUEUE](WORKFLOW_TASK_QUEUE.md) | `REPLY_WF_TASK_QUEUE_LT_ID` |
| [WORKFLOW_TASK_QUEUE](WORKFLOW_TASK_QUEUE.md) | `REQ_WF_TASK_QUEUE_LT_ID` |
| [WORKFLOW_TASK_QUEUE_HIST](WORKFLOW_TASK_QUEUE_HIST.md) | `REPLY_WF_TASK_QUEUE_LT_ID` |
| [WORKFLOW_TASK_QUEUE_HIST](WORKFLOW_TASK_QUEUE_HIST.md) | `REQ_WF_TASK_QUEUE_LT_ID` |

