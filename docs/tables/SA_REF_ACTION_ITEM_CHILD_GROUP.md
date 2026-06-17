# SA_REF_ACTION_ITEM_CHILD_GROUP

> Relates what groups an action item contains. Size - Based on the number of actions that are built. Estimate 1:1 with SA_REF_GROUP_ACTION_ITEM_R.

**Description:** SA Reference Action Item - Child Group  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHILD_REF_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Child Reference group ID. FK from SA_REF_GROUP |
| 6 | `CONTAINER_REF_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The group that is contained within the action item identified by sa_ref_action_item_id FK from SA-REF_GROUP |
| 7 | `SA_REF_ACTION_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The action item that has the group contained within it FK from SA_REF_ACTION_ITEM |
| 8 | `SA_REF_ACTN_ITEM_CHILD_GRP_ID` | DOUBLE | NOT NULL |  | Unique value that identifies the action item-group relationship |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence that the group falls within all of the groups within the action item |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_REF_GROUP_ID` | [SA_REF_GROUP](SA_REF_GROUP.md) | `SA_REF_GROUP_ID` |
| `CONTAINER_REF_GROUP_ID` | [SA_REF_GROUP](SA_REF_GROUP.md) | `SA_REF_GROUP_ID` |
| `SA_REF_ACTION_ITEM_ID` | [SA_REF_ACTION_ITEM](SA_REF_ACTION_ITEM.md) | `SA_REF_ACTION_ITEM_ID` |

