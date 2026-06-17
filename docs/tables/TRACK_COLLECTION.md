# TRACK_COLLECTION

> This table stores the FirstNet's Track Collection Reference Data.

**Description:** Track_Collection  
**Table type:** REFERENCE  
**Primary key:** `TRACK_COLLECTION_ID`  
**Columns:** 16  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COLLECTION_TYPE_CD` | DOUBLE | NOT NULL |  | Code value from code set 20320 |
| 6 | `COLOR_NUM` | DOUBLE | NOT NULL |  | Color of the Track Collection |
| 7 | `DESCRIPTION` | VARCHAR(250) | NOT NULL |  | Description or Name of the collectionColumn |
| 8 | `DISPLAY` | VARCHAR(50) | NOT NULL |  | Short Display for the collectionColumn |
| 9 | `SEQUENCE_NUM` | DOUBLE | NOT NULL |  | Sequence number of the track event group for display |
| 10 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group Code from code set 16370. |
| 11 | `TRACK_COLLECTION_ID` | DOUBLE | NOT NULL | PK | Key of the table |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [TRACK_ACTION_LINK](TRACK_ACTION_LINK.md) | `FOLLOWUP_TRACK_COLLECTION_ID` |
| [TRACK_ACTION_LINK](TRACK_ACTION_LINK.md) | `PRIMARY_TRACK_COLLECTION_ID` |
| [TRACK_COLLECTION_ELEMENT](TRACK_COLLECTION_ELEMENT.md) | `TRACK_COLLECTION_ID` |
| [TRACK_EVENT](TRACK_EVENT.md) | `DEF_NEXT_EVENT_ID` |
| [TRACK_EVENT](TRACK_EVENT.md) | `DEF_PREVIOUS_EVENT_ID` |

