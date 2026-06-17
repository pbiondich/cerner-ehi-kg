# SA_REF_ACTION_ITEM

> Contains all the lower-level action items that can be used to document an anesthesia action. Size - Based on the number of actions that are built. Estimate 2:1 with SA_REF_ACTION.

**Description:** SA Reference Action Item  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_ACTION_ITEM_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_ITEM_DESCRIPTION` | VARCHAR(250) |  |  | A description of what the action item documents |
| 2 | `ACTION_ITEM_NAME` | VARCHAR(50) |  |  | The display name of the action item |
| 3 | `ACTION_ITEM_NAME_KEY` | VARCHAR(50) |  |  | The display name of the action item _key format |
| 4 | `ACTION_ITEM_NAME_KEY_A_NLS` | VARCHAR(200) |  |  | ACTION_ITEM_NAME_KEY_A_NLS column |
| 5 | `ACTION_ITEM_NAME_KEY_NLS` | VARCHAR(102) |  |  | The display name of the action item _key format NLS form |
| 6 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 9 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 10 | `CHILD_SELECTION_REQ_IND` | DOUBLE | NOT NULL |  | Indicates that a lower level action item must be selected if this action item is selected |
| 11 | `DEFAULT_VALUE` | VARCHAR(250) |  |  | Default Value |
| 12 | `SA_REF_ACTION_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the action item |
| 13 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The task assay code associated to the response item. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VALUE_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates that a value must be associated to the action item if this item is selected |
| 20 | `VALUE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of value that is associated to the action item (string, number, item, etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SA_ACTION_ITEM](SA_ACTION_ITEM.md) | `SA_REF_ACTION_ITEM_ID` |
| [SA_REF_ACTION_ITEM_CHILD_GROUP](SA_REF_ACTION_ITEM_CHILD_GROUP.md) | `SA_REF_ACTION_ITEM_ID` |
| [SA_REF_GROUP_ACTION_ITEM_R](SA_REF_GROUP_ACTION_ITEM_R.md) | `SA_REF_ACTION_ITEM_ID` |
| [SA_REF_MACRO_ACTION_ITEM](SA_REF_MACRO_ACTION_ITEM.md) | `SA_REF_ACTION_ITEM_ID` |
| [SA_TODO_ACTION_ITEM](SA_TODO_ACTION_ITEM.md) | `SA_REF_ACTION_ITEM_ID` |

