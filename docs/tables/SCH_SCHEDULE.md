# SCH_SCHEDULE

> Contains the schedules for the appointments. An appointment can have multiple schedules.

**Description:** Event Schedules  
**Table type:** ACTIVITY  
**Primary key:** `SCHEDULE_ID`  
**Columns:** 25  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADDITIONAL_MINUTE_NBR` | DOUBLE | NOT NULL |  | Additional minutes to be added to current schedule. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `GRPSESSION_ID` | DOUBLE | NOT NULL | FK→ | This will be used to find the schedules associated to a given group session. This will be used when actions such as reschedule occur, to easily get to the schedules that will be affected. |
| 10 | `INDIRECT_BOOK_IND` | DOUBLE |  |  | indirect booking indicator |
| 11 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 12 | `OVERRIDE_DURATION_MINUTE_NBR` | DOUBLE | NOT NULL |  | The duration (in minutes) of the patient override. |
| 13 | `RES_LIST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the scheduling resource list. |
| 14 | `SCHEDULE_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the event schedule. The schedules are used to track rescheduling of an event. |
| 15 | `SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | Used to document the rescheduling of appointments. |
| 16 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 17 | `SCH_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the current state of the appointment. |
| 18 | `STATE_MEANING` | VARCHAR(12) |  |  | A 12-character string corresponding to the current state of the appointment. |
| 19 | `UNCONFIRM_COUNT` | DOUBLE | NOT NULL |  | Determines the number of resource that have not been confirmed for the current schedule. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GRPSESSION_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `RES_LIST_ID` | [SCH_RESOURCE_LIST](SCH_RESOURCE_LIST.md) | `RES_LIST_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SCH_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [EPISODE_ACTIVITY](EPISODE_ACTIVITY.md) | `CREATED_BY_SCHEDULE_ID` |
| [PM_OFFER](PM_OFFER.md) | `SCHEDULE_ID` |
| [PM_POST_DOC](PM_POST_DOC.md) | `SCHEDULE_ID` |
| [SCH_APPT](SCH_APPT.md) | `SCHEDULE_ID` |
| [SCH_ENTRY](SCH_ENTRY.md) | `SCHEDULE_ID` |
| [SCH_EVENT_ACTION](SCH_EVENT_ACTION.md) | `SCHEDULE_ID` |
| [SCH_EVENT_DISP](SCH_EVENT_DISP.md) | `SCHEDULE_ID` |
| [SCH_EVENT_ROLE](SCH_EVENT_ROLE.md) | `SCHEDULE_ID` |
| [SCH_LOCATION](SCH_LOCATION.md) | `SCHEDULE_ID` |
| [SCH_MESSAGING](SCH_MESSAGING.md) | `SCHEDULE_ID` |
| [SCH_SCHEDULE_MOVE](SCH_SCHEDULE_MOVE.md) | `SCHEDULE_ID` |

