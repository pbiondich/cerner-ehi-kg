# RC_CONT_PROCESS

> Current position for an instance of a continuity of flow model.

**Description:** Revenue Cycle Continuity Process  
**Table type:** ACTIVITY  
**Primary key:** `RC_CONT_PROCESS_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DELAYED_PROCESS_DT_TM` | DATETIME |  |  | The timestamp set in the workflow task process (WORKFLOW_TASK_QUEUE table) for delayed processing. |
| 2 | `DELAYED_REQUEST_LONG_TEXT_ID` | DOUBLE |  |  | Long Text Id that stores a request which needs to be enqueued in the workflow task processing (WORKFLOW_TASK_QUEUE table) when the flow is resumed. |
| 3 | `DELAYED_TASK_IDENT` | VARCHAR(250) | NOT NULL |  | Identifies a script that needs to be executed in workflow task processing (WORKFLOW_TASK_QUEUE table). |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the entity to which this process is associated. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the entity to which this process is associated. |
| 6 | `RC_CONT_CURRENT_NODE_ID` | DOUBLE | NOT NULL | FK→ | The current node, marking the process' progress through the model. |
| 7 | `RC_CONT_PROCESS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The Id representing a group of processes on a specific model instance. |
| 8 | `RC_CONT_PROCESS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RC_CONT_PROCESS table. |
| 9 | `STATUS_CD` | DOUBLE | NOT NULL |  | The code representing the status of the current process. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_CONT_CURRENT_NODE_ID` | [RC_CONT_NODE](RC_CONT_NODE.md) | `RC_CONT_NODE_ID` |
| `RC_CONT_PROCESS_GROUP_ID` | [RC_CONT_PROCESS_GROUP](RC_CONT_PROCESS_GROUP.md) | `RC_CONT_PROCESS_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CONS_BO_SCHED](CONS_BO_SCHED.md) | `RC_CONT_PROCESS_ID` |

