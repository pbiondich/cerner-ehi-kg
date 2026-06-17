# SA_REF_MACRO_ACTION

> Contains detail records about actions for a macro, when a line is executed an action instance will be added to the anesthesia record. Based on the number of macros and the number of actions that are built. Estimate 1:1 with SA_REF_MACRO. 100

**Description:** SA Reference Macro Action  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_MACRO_ACTION_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_VALUE` | VARCHAR(250) |  |  | The value that will be used for the action when it is executed |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `EXECUTE_IND` | DOUBLE |  |  | Indicates whether this record is executed by default. 1=by default, execute this detail record when the macro is executed, the user will have to uncheck the record if they do not want this detail record executed. 0=by default, do not execute this detail record when the macro is executed. This detail record still shows up under the macro, but the user will have to mark this record if they want this record executed. |
| 7 | `SA_REF_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The action that will added when the macro is executed |
| 8 | `SA_REF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that will be used as the item value for the action when it is executed |
| 9 | `SA_REF_MACRO_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies each macro action detail record |
| 10 | `SA_REF_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The macro id that this item detail belongs to |
| 11 | `TODO_IND` | DOUBLE | NOT NULL |  | Indicates whether the item defaults to be put on the ToDo list when the macro is executed |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_REF_ACTION_ID` | [SA_REF_ACTION](SA_REF_ACTION.md) | `SA_REF_ACTION_ID` |
| `SA_REF_ITEM_ID` | [SA_REF_ITEM](SA_REF_ITEM.md) | `SA_REF_ITEM_ID` |
| `SA_REF_MACRO_ID` | [SA_REF_MACRO](SA_REF_MACRO.md) | `SA_REF_MACRO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_REF_MACRO_ACTION_ITEM](SA_REF_MACRO_ACTION_ITEM.md) | `SA_REF_MACRO_ACTION_ID` |

