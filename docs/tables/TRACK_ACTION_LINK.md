# TRACK_ACTION_LINK

> This table stores the Track Action Link Records.

**Description:** Track Action Link  
**Table type:** REFERENCE  
**Primary key:** `TRACK_ACTION_LINK_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `FOLLOWUP_ACTION_STATUS` | DOUBLE | NOT NULL |  | Similar to primary action status |
| 6 | `FOLLOWUP_TRACK_COLLECTION_ID` | DOUBLE | NOT NULL | FK→ | Track_Collection_id from track_collection table |
| 7 | `LINK_TYPE_CD` | DOUBLE | NOT NULL |  | From code set 20321Ex: EVT_EVT_TRIG Defines the link type. |
| 8 | `PRIMARY_ACTION_STATUS` | DOUBLE | NOT NULL |  | Based on action_value if its an event it will have a status otherwise this field will be empty. |
| 9 | `PRIMARY_TRACK_COLLECTION_ID` | DOUBLE | NOT NULL | FK→ | Track_collection_id from Track_collection table. |
| 10 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group Code from code set 16370. |
| 11 | `TRACK_ACTION_LINK_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 12 | `TRIGGER_ALWAYS_IND` | DOUBLE | NOT NULL |  | If Indicator is set then triggering happens all the time other wise only once. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FOLLOWUP_TRACK_COLLECTION_ID` | [TRACK_COLLECTION](TRACK_COLLECTION.md) | `TRACK_COLLECTION_ID` |
| `PRIMARY_TRACK_COLLECTION_ID` | [TRACK_COLLECTION](TRACK_COLLECTION.md) | `TRACK_COLLECTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACK_ACTION_LINK_ACTIVITY](TRACK_ACTION_LINK_ACTIVITY.md) | `TRACK_ACTION_LINK_ID` |

