# TRACKING_ITEM

> Tracking table used to define a tracking identifier for an item (such as a person, encounter, personnel, or inventory item) that is to be tracked. This table contains a tracking item for each time an item is to start and stop tracking.

**Description:** Tracking Item Table  
**Table type:** ACTIVITY  
**Primary key:** `TRACKING_ID`  
**Columns:** 25  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL | FK→ | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BASE_LOC_CD` | DOUBLE | NOT NULL | FK→ | The location where the patient is being treated. Used to indicate the location where the patient should be put after returning from an ancillary department or temporary location such as X-Ray. |
| 6 | `BASE_LOC_DT_TM` | DATETIME |  |  | The date and time when the patient was first placed in their base location. Used to calculate Treament Time. |
| 7 | `CUR_TRACKING_LOCATOR_ID` | DOUBLE | NOT NULL |  | Pointer to the current tracking locator record. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `END_TRACKING_DT_TM` | DATETIME |  |  | Date and time that tracking ended for this tracking item. |
| 10 | `END_TRACKING_ID` | DOUBLE | NOT NULL |  | The person who caused the tracking item to end. |
| 11 | `INVENTORY_ID` | DOUBLE | NOT NULL | FK→ | Inventory item to be tracked. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Table identifier from the Parent Entity Name table. |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Table Name identifier for the Parent Entity ID |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person Identifier of the provider to be tracked. |
| 16 | `START_TRACKING_DT_TM` | DATETIME |  |  | Date and time that tracking was started for this tracking item. |
| 17 | `START_TRACKING_ID` | DOUBLE | NOT NULL |  | The person who caused the tracking item to be started. |
| 18 | `TRACKING_ID` | DOUBLE | NOT NULL | PK | Tracking IdentifierColumn |
| 19 | `TRACKING_STATUS_FLAG` | DOUBLE |  |  | The status of tracking on this item. |
| 20 | `TRACKING_TYPE_FLAG` | DOUBLE |  |  | A value that identifies what type of tracking is being used for this tracking item. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `BASE_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `INVENTORY_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [FN_OMF_ENCNTR](FN_OMF_ENCNTR.md) | `TRACKING_ID` |
| [TRACKING_CHECKIN](TRACKING_CHECKIN.md) | `TRACKING_ID` |
| [TRACKING_COMMENT](TRACKING_COMMENT.md) | `TRACKING_ID` |
| [TRACKING_COMPLAINT](TRACKING_COMPLAINT.md) | `TRACKING_ID` |
| [TRACKING_ENCNTR_PRSNL_RELTN](TRACKING_ENCNTR_PRSNL_RELTN.md) | `ENCNTR_TRACKING_ID` |
| [TRACKING_ENCNTR_PRSNL_RELTN](TRACKING_ENCNTR_PRSNL_RELTN.md) | `PRSNL_TRACKING_ID` |
| [TRACKING_EVENT](TRACKING_EVENT.md) | `TRACKING_ID` |
| [TRACKING_HOLD](TRACKING_HOLD.md) | `TRACKING_ID` |
| [TRACKING_LOCATOR](TRACKING_LOCATOR.md) | `TRACKING_ID` |
| [TRACKING_TAG](TRACKING_TAG.md) | `LAST_TRACKING_ID` |
| [TRACKING_TAG](TRACKING_TAG.md) | `TRACKING_ID` |
| [TRACK_ACTION_LINK_ACTIVITY](TRACK_ACTION_LINK_ACTIVITY.md) | `TRACKING_ID` |
| [TRACK_TRIGGER_ACTIVITY](TRACK_TRIGGER_ACTIVITY.md) | `TRACKING_ID` |

