# TRACK_EVENT

> Reference table used to define the various tracking events each tracking group would like to be able to track.

**Description:** Tracking Event Reference Table  
**Table type:** REFERENCE  
**Primary key:** `TRACK_EVENT_ID`  
**Columns:** 47  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTO_COMPLETE_IND` | DOUBLE |  |  | An indicator whether this event should automatically go to a 'complete' status. |
| 3 | `AUTO_START_IND` | DOUBLE |  |  | An indicator whether this event should automatically go to a 'start' status. |
| 4 | `CLINIC_EVENT_CD` | DOUBLE | NOT NULL |  | Clinical event codesColumn |
| 5 | `COMPLETE_COLOR_NUM` | DOUBLE | NOT NULL |  | The color of the event in the requested state |
| 6 | `COMPLETE_ICON_ID` | DOUBLE | NOT NULL | FK→ | The icon id for the completed state of the event |
| 7 | `COMPLETE_ON_EXIT_IND` | DOUBLE |  |  | An indicator on whether this event should be 'completed' if the tracking item is moved out of the current location. |
| 8 | `CRITICAL_BLINK_IND` | DOUBLE |  |  | Critical Blink IndicatorColumn |
| 9 | `CRITICAL_COLOR` | VARCHAR(20) |  |  | Critical ColorColumn |
| 10 | `CRITICAL_ICON` | DOUBLE |  |  | Critical IconColumn |
| 11 | `CRITICAL_INTERVAL` | DOUBLE |  |  | Critical IntervalColumn |
| 12 | `DEF_BEGIN_LOC_CD` | DOUBLE | NOT NULL | FK→ | Location where to automatically move the patient once this event has started. This is the default location an can be reset if desired or will not be set if the tracking item is already in a bed. |
| 13 | `DEF_NEXT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The next event to set as the default event once this event status is set to 'complete'. |
| 14 | `DEF_PREVIOUS_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The set of events to complete once this event status is set to 'request'. |
| 15 | `DEF_REQUEST_LOC_CD` | DOUBLE | NOT NULL | FK→ | Location where to automatically move the patient once this event has been requested. This is the default location an can be reset if desired or will not be set if the tracking item is already in a bed. |
| 16 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of the Tracking Reference Item. |
| 17 | `DISPLAY` | VARCHAR(20) |  |  | Display description |
| 18 | `DISPLAY_KEY` | VARCHAR(50) |  |  | Display Key generated from the Display field (All Uppercase, No Spaces or Special Characters). |
| 19 | `EVENT_PRIORITY_RANK` | DOUBLE |  |  | Priority rank to set as the default rank once this event is selected. This rank should also be used to set the location specific priority rank. |
| 20 | `EVENT_USE_MEAN_CD` | DOUBLE | NOT NULL | FK→ | Tracking event meaning. |
| 21 | `EXEC_NEXT_EVENT_IND` | DOUBLE | NOT NULL |  | Contains next event preference. An indicator that the next event is available. |
| 22 | `FINAL_TRANSACTION_IND` | DOUBLE |  |  | An indicator on whether this event should close the tracking of this item. |
| 23 | `FLEX_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location code to allow the users to build different events for different locations. This field identifies what location this event is for. |
| 24 | `HIDE_EVENT_IND` | DOUBLE |  |  | means a auto trigger eventColumn |
| 25 | `NORMAL_COLOR` | VARCHAR(20) |  |  | Normal Event Color |
| 26 | `NORMAL_ICON` | DOUBLE |  |  | Normal Event Icon |
| 27 | `OVERDUE_BLINK_IND` | DOUBLE |  |  | Overdue Blink IndicatorColumn |
| 28 | `OVERDUE_COLOR` | VARCHAR(20) |  |  | Overdue ColorColumn |
| 29 | `OVERDUE_ICON` | DOUBLE |  |  | Overdue IconColumn |
| 30 | `OVERDUE_INTERVAL` | DOUBLE |  |  | Overdue IntervalColumn |
| 31 | `REQUEST_COLOR_NUM` | DOUBLE | NOT NULL |  | The color of the event in the requested state |
| 32 | `REQUEST_ICON_ID` | DOUBLE | NOT NULL | FK→ | The icon id for the requested state of the event |
| 33 | `SEQUENCE_NUM` | DOUBLE | NOT NULL |  | Display order sequence of the events when the events are set at the same time. |
| 34 | `SHOW_ON_MONITOR_IND` | DOUBLE |  |  | An indicator on whether this event should be shown on the monitor. |
| 35 | `SINGLE_STATE_IND` | DOUBLE | NOT NULL |  | Whether the event is set with single or multiple states |
| 36 | `SINGLE_USE_IND` | DOUBLE | NOT NULL |  | Indicates if the event can be set multiple times or just once. |
| 37 | `STAGE_CD` | DOUBLE | NOT NULL |  | The code of the staging area the track event is mapped to. |
| 38 | `START_COLOR_NUM` | DOUBLE | NOT NULL |  | The color of the event in the started state |
| 39 | `START_ICON_ID` | DOUBLE | NOT NULL | FK→ | The icon id for the started state of the event |
| 40 | `TRACKING_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Value to define what type of event this is. |
| 41 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL | FK→ | Tracking Group Code used to identify which tracking group this reference is currently associated with. |
| 42 | `TRACK_EVENT_ID` | DOUBLE | NOT NULL | PK | Tracking Event Identifier |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPLETE_ICON_ID` | [SA_REF_ICON](SA_REF_ICON.md) | `SA_REF_ICON_ID` |
| `DEF_BEGIN_LOC_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DEF_NEXT_EVENT_ID` | [TRACK_COLLECTION](TRACK_COLLECTION.md) | `TRACK_COLLECTION_ID` |
| `DEF_PREVIOUS_EVENT_ID` | [TRACK_COLLECTION](TRACK_COLLECTION.md) | `TRACK_COLLECTION_ID` |
| `DEF_REQUEST_LOC_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `EVENT_USE_MEAN_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FLEX_LOCATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `REQUEST_ICON_ID` | [SA_REF_ICON](SA_REF_ICON.md) | `SA_REF_ICON_ID` |
| `START_ICON_ID` | [SA_REF_ICON](SA_REF_ICON.md) | `SA_REF_ICON_ID` |
| `TRACKING_GROUP_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SN_TRACK_EVENT_RELTN](SN_TRACK_EVENT_RELTN.md) | `TRACK_EVENT_ID` |
| [TRACKING_EVENT](TRACKING_EVENT.md) | `TRACK_EVENT_ID` |

