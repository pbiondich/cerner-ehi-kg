# SCH_EVENT_RECUR

> The table hold the frequencies for a recurring event.

**Description:** Scheduling Event Recur  
**Table type:** ACTIVITY  
**Primary key:** `EVENT_RECUR_ID`  
**Columns:** 29  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DAYS_OF_WEEK` | VARCHAR(7) |  |  | A 7-char string representing the days of the week. |
| 8 | `DURATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of duration. |
| 9 | `DURATION_UNITS` | DOUBLE | NOT NULL |  | Scheduling Duration Units |
| 10 | `DURATION_UNITS_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Duration Units Code |
| 11 | `DURATION_UNITS_MEANING` | VARCHAR(12) |  |  | Scheduling Duration Units Meaning |
| 12 | `END_DT_TM` | DATETIME |  |  | End Date and Time value |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_RECUR_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the event's recurring pattern. |
| 15 | `LAST_DT_TM` | DATETIME |  |  | The last date and time an action was taken on the object. |
| 16 | `LAST_SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence number corresponding last execution. |
| 17 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 18 | `ORDER_PROTOCOL_TYPE_FLAG` | DOUBLE |  |  | Determines whether the recurring series is generated from a protocol order and how the protocol is to be managed. 0 - Generated using protocol order.1 - Not generated from future recurring, 2 - Generated from future recurring. |
| 19 | `RECUR_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the current state of the recurring frequency. This column is not being used. |
| 20 | `RECUR_STATE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the current recurring frequency state. |
| 21 | `RECUR_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the scheduled event that should be used to create future recurring events. |
| 22 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 23 | `START_DT_TM` | DATETIME |  |  | The start date and time. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DURATION_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RECUR_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RECUR_TEMPLATE_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SCH_EVENT_RECUR_COMM](SCH_EVENT_RECUR_COMM.md) | `EVENT_RECUR_ID` |
| [SCH_EVENT_RECUR_DETAIL](SCH_EVENT_RECUR_DETAIL.md) | `EVENT_RECUR_ID` |
| [SCH_EVENT_RECUR_LIST](SCH_EVENT_RECUR_LIST.md) | `EVENT_RECUR_ID` |
| [SCH_EVENT_RECUR_ORDER](SCH_EVENT_RECUR_ORDER.md) | `EVENT_RECUR_ID` |

