# PFT_WF_STATE_ACTION_RELTN

> This table stores the relationship between different states that the work item can be in, and the respective action code that is applied on that specific state to transition it to another state.

**Description:** ProFit Workflow State Action Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CD` | DOUBLE | NOT NULL |  | The action code that will transition the work item from its current state. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `PFT_ENTITY_STATUS_CD` | DOUBLE | NOT NULL |  | Represents the state that the work items of this process model can be in. |
| 4 | `PFT_WF_PROCESS_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related ProFit workflow process model. |
| 5 | `PFT_WF_STATE_ACTION_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between the pft_wf_process_model and a pft_entity_status. |
| 6 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Represents the priority sequence for the action code. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_WF_PROCESS_MODEL_ID` | [PFT_WF_PROCESS_MODEL](PFT_WF_PROCESS_MODEL.md) | `PFT_WF_PROCESS_MODEL_ID` |

