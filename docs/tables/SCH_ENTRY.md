# SCH_ENTRY

> Master table to store scheduling requests information.

**Description:** Scheduling Entry  
**Table type:** ACTIVITY  
**Primary key:** `SCH_ENTRY_ID`  
**Columns:** 34  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for an appointment type. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `EARLIEST_DT_TM` | DATETIME |  |  | The earliest request start date and time. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `ENTRY_STATE_CD` | DOUBLE | NOT NULL |  | The coded identifier for the state of the request list entry. |
| 12 | `ENTRY_STATE_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-character description corresponding to the state of the request list entry. |
| 13 | `ENTRY_TYPE_CD` | DOUBLE | NOT NULL |  | The coded identifier for the request list entry type. |
| 14 | `ENTRY_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-character description corresponding to the request list entry type. |
| 15 | `LATEST_DT_TM` | DATETIME |  |  | The latest requested start date and time. |
| 16 | `NO_CONTACT_FLAG` | DOUBLE |  |  | Indicates if the scheduling patient can be contacted. When set to 1 the patient should not be contacted. |
| 17 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 19 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling request list queue. |
| 20 | `REQUEST_MADE_DT_TM` | DATETIME | NOT NULL |  | The date and time the original request was created. |
| 21 | `REQ_ACTION_CD` | DOUBLE | NOT NULL |  | The coded identifier for the requested action. |
| 22 | `REQ_ACTION_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-character description corresponding to the requested action. |
| 23 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the event schedule. |
| 24 | `SCH_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The identifier to uniquely identify the action being performed. |
| 25 | `SCH_APPT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a resource's/patient's appointment. |
| 26 | `SCH_ENTRY_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the scheduling request list entry. |
| 27 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 28 | `STANDBY_PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority of the standby appointment reqquest. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `QUEUE_ID` | [SCH_OBJECT](SCH_OBJECT.md) | `SCH_OBJECT_ID` |
| `SCHEDULE_ID` | [SCH_SCHEDULE](SCH_SCHEDULE.md) | `SCHEDULE_ID` |
| `SCH_ACTION_ID` | [SCH_EVENT_ACTION](SCH_EVENT_ACTION.md) | `SCH_ACTION_ID` |
| `SCH_APPT_ID` | [SCH_APPT](SCH_APPT.md) | `SCH_APPT_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `SCH_ENTRY_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `SCH_ENTRY_ID` |

