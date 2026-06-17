# TRACK_ACTION

> Holds individual actions that can be launched from toolbars, menus, columns, the depart process, or user actions.

**Description:** Track Action  
**Table type:** REFERENCE  
**Primary key:** `TRACK_ACTION_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_ENUM` | DOUBLE | NOT NULL |  | Identifies what the action will do. |
| 2 | `ACTION_NAME` | VARCHAR(128) | NOT NULL |  | Configured Display Name for the action |
| 3 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | If this action is part of an action group, this specifies where in the group the action belongs. |
| 4 | `BEHAVIOR_BIT_MAP` | DOUBLE | NOT NULL |  | A bitmask that configures the way this action behaves. |
| 5 | `ICON_ENUM` | DOUBLE | NOT NULL |  | An idex to a FirstNet icon to display on this action. There could be hundreds of possible values. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary Key from the parent table identified in PARENT_ENTITY_NAME |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Specifies whether this action is part of a track_action_group or a direct child of a track_field_spec |
| 8 | `TRACK_ACTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACK_ACTION_REFINEMENT](TRACK_ACTION_REFINEMENT.md) | `TRACK_ACTION_ID` |

