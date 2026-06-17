# RCM_ACTION

> Records user actions for the Care Management workflows.

**Description:** Care Management - Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date and time of when the user did the action. |
| 2 | `ACTION_MEANING` | VARCHAR(12) |  |  | The meaning of the type of action that the user performed. |
| 3 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | The identifier of the person who performed the action. |
| 4 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of action that the user performed. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier for the parent row. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the parent table for the parent row. |
| 7 | `RCM_ACTION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a recorded user action from the Care Management workflow. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

