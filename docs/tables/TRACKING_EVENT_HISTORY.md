# TRACKING_EVENT_HISTORY

> THE Tracking Event History

**Description:** Tracking Event History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODIFY_REASON` | VARCHAR(100) |  |  | This field stores comment or reason why an instance of event is modified. |
| 2 | `NEW_DT_TM` | DATETIME | NOT NULL |  | corrected date and time of an event instance. |
| 3 | `NEW_EVENT_STATUS_CD` | DOUBLE | NOT NULL |  | corrected event status if modified. Otherwise will match the old_event_status_cd. |
| 4 | `NEW_USER_ID` | DOUBLE | NOT NULL | FK→ | The user id if the person who set the event if modified otherwise will match old_user_id |
| 5 | `OLD_DT_TM` | DATETIME |  |  | Original date and time of an event instance |
| 6 | `OLD_EVENT_STATUS_CD` | DOUBLE | NOT NULL |  | Original status of the event instance. |
| 7 | `OLD_USER_ID` | DOUBLE | NOT NULL | FK→ | The user_id of person who originally set the instance of the event. |
| 8 | `TRACKING_EVENT_HISTORY_ID` | DOUBLE | NOT NULL |  | Primary key of the table. |
| 9 | `TRACKING_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Key from tracking_event table |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NEW_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `OLD_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRACKING_EVENT_ID` | [TRACKING_EVENT](TRACKING_EVENT.md) | `TRACKING_EVENT_ID` |

