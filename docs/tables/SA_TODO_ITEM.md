# SA_TODO_ITEM

> Surginet Anesthesia To Do Item

**Description:** SA To Do Item  
**Table type:** ACTIVITY  
**Primary key:** `SA_TODO_ITEM_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMPLETE_DT_TM` | DATETIME |  |  | The date/time the todo item was completed |
| 6 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates whether the todo item has been completed |
| 7 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item id for the item being documented |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the Long Text Identifier |
| 9 | `PREV_TODO_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The previous version of the todo item item |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The Provider who added the item to the todo list. |
| 11 | `RETURNED_QTY` | DOUBLE |  |  | The number of this item that were returned |
| 12 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The instance of a macro that added the item to the todo list. |
| 13 | `SA_TODO_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for this record |
| 14 | `SA_TODO_LIST_ID` | DOUBLE | NOT NULL | FK→ | The ToDo list record this item belongs to |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `USED_QTY` | DOUBLE |  |  | The number of this item that were used |
| 21 | `WASTED_QTY` | DOUBLE |  |  | The number of this item that were wasted |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PREV_TODO_ITEM_ID` | [SA_TODO_ITEM](SA_TODO_ITEM.md) | `SA_TODO_ITEM_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_TODO_LIST_ID` | [SA_TODO_LIST](SA_TODO_LIST.md) | `SA_TODO_LIST_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_TODO_ITEM](SA_TODO_ITEM.md) | `PREV_TODO_ITEM_ID` |

