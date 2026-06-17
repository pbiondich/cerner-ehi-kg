# SA_TODO_ACTION

> Surginet Anesthesia To Do Action

**Description:** SA To Do Action  
**Table type:** ACTIVITY  
**Primary key:** `SA_TODO_ACTION_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_VALUE` | VARCHAR(250) |  |  | The value associated to this action |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `COMPLETE_DT_TM` | DATETIME |  |  | The date/time the todo item was completed |
| 7 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates whether the todo item has been completed |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the Long Text identifier |
| 9 | `PREV_TODO_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The previous version of the todo action item |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The provider who added the item to the todo list |
| 11 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The instance of a macro that added the item to the todo list. |
| 12 | `SA_REF_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The Anesthesia action to be performed |
| 13 | `SA_REF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item associated as the value to this action |
| 14 | `SA_TODO_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for this record |
| 15 | `SA_TODO_LIST_ID` | DOUBLE | NOT NULL | FK→ | The ToDo list record this item belongs to |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PREV_TODO_ACTION_ID` | [SA_TODO_ACTION](SA_TODO_ACTION.md) | `SA_TODO_ACTION_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_REF_ACTION_ID` | [SA_REF_ACTION](SA_REF_ACTION.md) | `SA_REF_ACTION_ID` |
| `SA_REF_ITEM_ID` | [SA_REF_ITEM](SA_REF_ITEM.md) | `SA_REF_ITEM_ID` |
| `SA_TODO_LIST_ID` | [SA_TODO_LIST](SA_TODO_LIST.md) | `SA_TODO_LIST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_TODO_ACTION](SA_TODO_ACTION.md) | `PREV_TODO_ACTION_ID` |
| [SA_TODO_ACTION_ITEM](SA_TODO_ACTION_ITEM.md) | `SA_TODO_ACTION_ID` |

