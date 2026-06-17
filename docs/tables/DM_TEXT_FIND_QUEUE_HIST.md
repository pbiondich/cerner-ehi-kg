# DM_TEXT_FIND_QUEUE_HIST

> This table serves as an archival history of the queue for hosting jobs to be consumed by server 520

**Description:** DM_TEXT_FIND_QUEUE_HISTORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_TEXT_FIND_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the DM_TEXT_FIND_DETAIL table |
| 2 | `DM_TEXT_FIND_LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the DM_TEXT_FIND_LOG row for this executing report. |
| 3 | `DM_TEXT_FIND_QUEUE_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `ENQUEUED_ON_DT_TM` | DATETIME | NOT NULL |  | The date this item was added to the queue. |
| 5 | `EXECUTE_END_DT_TM` | DATETIME | NOT NULL |  | The date this job stopped running |
| 6 | `EXECUTE_ON_DT_TM` | DATETIME | NOT NULL |  | The Date after which this job can be executed by the assigned server |
| 7 | `EXECUTE_ON_NODE_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Node this job is meant to execute on, or ANY if the call can be run by any server |
| 8 | `EXECUTE_START_DT_TM` | DATETIME | NOT NULL |  | The date this job began running |
| 9 | `LOCKED_BY_NODE_NAME` | VARCHAR(30) | NOT NULL |  | Node which has locked the job |
| 10 | `LOCKED_BY_SERVER_IDENT` | DOUBLE | NOT NULL |  | The Internal Server 520 ID that has claimed this job. This value will be NULL until a server claims this task. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_DETAIL_ID` | [DM_TEXT_FIND_DETAIL](DM_TEXT_FIND_DETAIL.md) | `DM_TEXT_FIND_DETAIL_ID` |
| `DM_TEXT_FIND_LOG_ID` | [DM_TEXT_FIND_LOG](DM_TEXT_FIND_LOG.md) | `DM_TEXT_FIND_LOG_ID` |

