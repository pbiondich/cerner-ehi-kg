# SA_REF_GROUP

> Contains all the top level groups that can be associated to an anesthesia action. Size - Based on the number of actions that are built. Estimate 1:1 with SA_REF_ACTION_GROUP_R.

**Description:** SA Reference Group  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_GROUP_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BILL_IND` | DOUBLE | NOT NULL |  | Indicates whether action detail for group should be displayed on the billing summary |
| 6 | `GROUP_PROMPT` | VARCHAR(30) |  |  | Group Prompt |
| 7 | `MULTI_SELECT_IND` | DOUBLE | NOT NULL |  | Indicates whether multiple action items contained within this group can be selected (1=multiple items can be selected, 0=only one item can be selected) |
| 8 | `PRINT_IND` | DOUBLE | NOT NULL |  | Indicates whether action detail for group should be printed on the finalized record |
| 9 | `SA_REF_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the group |
| 10 | `SELECTION_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether there must be an action item selected within the group (1=An action item must be selected, 0=No action item has to be selected) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SA_REF_ACTION_GROUP_R](SA_REF_ACTION_GROUP_R.md) | `SA_REF_GROUP_ID` |
| [SA_REF_ACTION_ITEM_CHILD_GROUP](SA_REF_ACTION_ITEM_CHILD_GROUP.md) | `CHILD_REF_GROUP_ID` |
| [SA_REF_ACTION_ITEM_CHILD_GROUP](SA_REF_ACTION_ITEM_CHILD_GROUP.md) | `CONTAINER_REF_GROUP_ID` |
| [SA_REF_GROUP_ACTION_ITEM_R](SA_REF_GROUP_ACTION_ITEM_R.md) | `SA_REF_GROUP_ID` |

