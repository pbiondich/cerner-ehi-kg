# SA_REF_MACRO_ACTION_ITEM

> Contains the action items that will documented when the parent macro action is executed Based on the number of macros and the number of actions that are built. Estimate 2:1 with SA_REF_MACRO_ACTION. 200

**Description:** SA Reference Macro Action Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_VALUE` | VARCHAR(250) |  |  | The value that will be used for the action item when the parent macro action is executed |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `SA_REF_ACTION_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The action item that will be documented if the parent macro action is executed |
| 7 | `SA_REF_ITEM_ID` | DOUBLE | NOT NULL |  | The item that will be used as the item value for the action item when the parent macro action is executed |
| 8 | `SA_REF_MACRO_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The parent action item that this action item falls under |
| 9 | `SA_REF_MACRO_ACTION_ITEM_ID` | DOUBLE | NOT NULL |  | Unique value that identifies the macro action item record |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_REF_ACTION_ITEM_ID` | [SA_REF_ACTION_ITEM](SA_REF_ACTION_ITEM.md) | `SA_REF_ACTION_ITEM_ID` |
| `SA_REF_MACRO_ACTION_ID` | [SA_REF_MACRO_ACTION](SA_REF_MACRO_ACTION.md) | `SA_REF_MACRO_ACTION_ID` |

