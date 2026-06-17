# TRACKING_EVENT

> Tracking table used to store the events that are Requested, Started, or Completed for a tracking item.

**Description:** Tracking Event Table  
**Table type:** ACTIVITY  
**Primary key:** `TRACKING_EVENT_ID`  
**Columns:** 25  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLINICAL_EVENT_CD` | DOUBLE | NOT NULL |  | Contains the associated clinical event |
| 3 | `COLLECTED_DT_TM` | DATETIME |  |  | Date n time at which the event when to this statusColumn |
| 4 | `COLLECTED_ID` | DOUBLE | NOT NULL |  | ID of the person who collectedthe tracking event. |
| 5 | `COMNOTREW_DT_TM` | DATETIME |  |  | Date n time at which the event when to this statusColumn |
| 6 | `COMNOTREW_ID` | DOUBLE | NOT NULL |  | ID of the person who collectedthe tracking event.Column |
| 7 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time the tracking event was completed. |
| 8 | `COMPLETE_ID` | DOUBLE | NOT NULL |  | ID of the person who completed the tracking event. |
| 9 | `COMPLETE_ON_EXIT_IND` | DOUBLE |  |  | Indicator used to identify that this event should be auto completed once the patient leaves. |
| 10 | `EVENT_STATUS_CD` | DOUBLE | NOT NULL | FK→ | Code value used to identify if the event status is to be set to Request, Onset, Complete, or Hold. |
| 11 | `INLAB_DT_TM` | DATETIME |  |  | Date n time at which the event when to this statusColumn |
| 12 | `INLAB_ID` | DOUBLE | NOT NULL |  | ID of the person who inlab the tracking event.Column |
| 13 | `ONSET_DT_TM` | DATETIME |  |  | Date and time the tracking event was started. |
| 14 | `ONSET_ID` | DOUBLE | NOT NULL |  | ID of the person who started the tracking event. |
| 15 | `REQUESTED_DT_TM` | DATETIME |  |  | Date and time the tracking event was requested. |
| 16 | `REQUESTED_ID` | DOUBLE | NOT NULL |  | ID of the person who requested the tracking event. |
| 17 | `TRACKING_EVENT_ID` | DOUBLE | NOT NULL | PK | Tracking Event Identifier used to associated a Tracking Event to a Tracking Item |
| 18 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL | FK→ | Tracking Group Code used to identify which tracking group this patient is currently checked into. |
| 19 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking ItemColumn |
| 20 | `TRACK_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Tracking Event Assigned |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_GROUP_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |
| `TRACK_EVENT_ID` | [TRACK_EVENT](TRACK_EVENT.md) | `TRACK_EVENT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RAD_TRACK_EVENT_DETAIL](RAD_TRACK_EVENT_DETAIL.md) | `TRACKING_EVENT_ID` |
| [TRACKING_EVENT_HISTORY](TRACKING_EVENT_HISTORY.md) | `TRACKING_EVENT_ID` |
| [TRACKING_EVENT_ORD](TRACKING_EVENT_ORD.md) | `TRACKING_EVENT_ID` |
| [TRACKING_EVT_CMT](TRACKING_EVT_CMT.md) | `TRACKING_EVENT_ID` |

