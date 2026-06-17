# TRACK_ACTION_GROUP_RELTN

> Associates a group of actions to a tracking list or depart configuration.

**Description:** Track Action Group Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether this group represents a toolbar, menu, etc.0=TOOLBAR, 1=MENU, 2=DEPART PROCESS, 3=USER ACTIONS |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The track_list_id, position_cd, prsnl_id, or tracking_ref_id that this action group is being assigned to. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent Entity Name for the group function |
| 4 | `TRACK_ACTION_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The action group that is associated |
| 5 | `TRACK_ACTION_GROUP_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMAR KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_ACTION_GROUP_ID` | [TRACK_ACTION_GROUP](TRACK_ACTION_GROUP.md) | `TRACK_ACTION_GROUP_ID` |

