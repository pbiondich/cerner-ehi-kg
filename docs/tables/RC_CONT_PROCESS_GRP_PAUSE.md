# RC_CONT_PROCESS_GRP_PAUSE

> This table stores information about when the workflow was paused or resumed for a particular entity.

**Description:** Revenue Cycle Continuity Process Group Pause  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PAUSE_DT_TM` | DATETIME |  |  | Contains the time when the flow was paused. |
| 3 | `RC_CONT_PROCESS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the rc_cont_process_group table. |
| 4 | `RC_CONT_PROCESS_GRP_PAUSE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_CONT_PROCESS_GRP_PAUSE table. |
| 5 | `RESUME_DT_TM` | DATETIME |  |  | Contains the time when the flow was resumed. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_CONT_PROCESS_GROUP_ID` | [RC_CONT_PROCESS_GROUP](RC_CONT_PROCESS_GROUP.md) | `RC_CONT_PROCESS_GROUP_ID` |

