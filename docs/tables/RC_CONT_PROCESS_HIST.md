# RC_CONT_PROCESS_HIST

> Contains historical data for an instance of a continuity flow model.

**Description:** Revenue Cycle Continuity Process History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the ID of the entity to which this process is associated. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the entity to which this process is associated. |
| 5 | `RC_CONT_NODE_ID` | DOUBLE | NOT NULL | FK→ | The node, marking the process' progress through the model. |
| 6 | `RC_CONT_PROCESS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related process group. |
| 7 | `RC_CONT_PROCESS_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely generated number that identifies a single row on the rc_cont_process_hist table. |
| 8 | `RC_CONT_PROCESS_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related continuity process. |
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
| `RC_CONT_NODE_ID` | [RC_CONT_NODE](RC_CONT_NODE.md) | `RC_CONT_NODE_ID` |
| `RC_CONT_PROCESS_GROUP_ID` | [RC_CONT_PROCESS_GROUP](RC_CONT_PROCESS_GROUP.md) | `RC_CONT_PROCESS_GROUP_ID` |

