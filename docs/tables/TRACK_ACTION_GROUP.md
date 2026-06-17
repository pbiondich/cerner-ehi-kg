# TRACK_ACTION_GROUP

> Holds configurations for toolbars, menus, and other groups of actions that can be launched.

**Description:** Track Action Group  
**Table type:** REFERENCE  
**Primary key:** `TRACK_ACTION_GROUP_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_NAME` | VARCHAR(128) | NOT NULL |  | The configured name for this group of actions |
| 2 | `GROUP_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether this group represents a toolbar, menu, etc. |
| 3 | `LIST_TYPE_FLAG` | DOUBLE | NOT NULL |  | Group List, Bed List, Pick List, etc.GROUP=1, BED=2, LOCATION=4, PROVIDER=8, CASE TRACKING = 16 |
| 4 | `TRACK_ACTION_GROUP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACK_ACTION_GROUP_RELTN](TRACK_ACTION_GROUP_RELTN.md) | `TRACK_ACTION_GROUP_ID` |

