# TRACKING_LOCATOR

> Tracking table used to store all locations and their related information for each tracking item.

**Description:** Tracking Locator Table  
**Table type:** ACTIVITY  
**Primary key:** `TRACKING_LOCATOR_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_EVENTS_IND` | DOUBLE |  |  | Active Events Indicator (Not Used)Column |
| 2 | `ARRIVE_DT_TM` | DATETIME |  |  | Date and time the tracking item arrived in this location. |
| 3 | `ARRIVE_ID` | DOUBLE | NOT NULL | FK→ | The person who defined when the tracking item arrived in the location. |
| 4 | `AVAILABILITY_IND` | DOUBLE |  |  | An indicator defining the availability of the tracking item. |
| 5 | `DEPART_DT_TM` | DATETIME |  |  | Date and time the tracking item departed from this location. |
| 6 | `DEPART_ID` | DOUBLE | NOT NULL | FK→ | Date and time the tracking item departed from this location. |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location Code of the physical location the tracking item is being tracked to. |
| 8 | `LOCATOR_CREATE_DATE` | DOUBLE | NOT NULL |  | This columns used to identify location history sequence. The column is populated with a numeric value of the create date/time (when inserted) adjusted for time zone. It should never be modified. |
| 9 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | Location Bed Code of the physical location the tracking item is being tracked to. |
| 10 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Location Nurse Unit Code of the physical location the tracking item is being tracked to. |
| 11 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | Location Room Code of the physical location the tracking item is being tracked to. |
| 12 | `RANK_SEQUENCE` | DOUBLE |  |  | The rank sequence of the item while it was in this location. |
| 13 | `SCHEDULED_DT_TM` | DATETIME |  |  | Date and time the tracking item is scheduled to arrived in this location. |
| 14 | `TRACKING_ACUITY_LEVEL_ID` | DOUBLE | NOT NULL | FK→ | The acuity level of the tracking item while it was in this location. |
| 15 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking Identifier of the tracking item being tracked to this location. |
| 16 | `TRACKING_LOCATOR_ID` | DOUBLE | NOT NULL | PK | Tracking Locator Identifier |
| 17 | `TRACKING_REASON_CD` | DOUBLE | NOT NULL | FK→ | Value that identifies why the tracking item is in this tracking location. |
| 18 | `TRACKING_REASON_COMMENT` | VARCHAR(200) |  |  | Tracking Reason CommentColumn |
| 19 | `UNAVAIL_TRACKING_EVENT_ID` | DOUBLE | NOT NULL |  | Pointer to the tracking items tracking event that is not available to complete while the tracking item is in this tracking location. (Not Used) |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ARRIVE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DEPART_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOCATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOC_BED_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOC_NURSE_UNIT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOC_ROOM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_ACUITY_LEVEL_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |
| `TRACKING_REASON_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACKING_ENCNTR_PRSNL_RELTN](TRACKING_ENCNTR_PRSNL_RELTN.md) | `TRACKING_LOCATOR_ID` |

