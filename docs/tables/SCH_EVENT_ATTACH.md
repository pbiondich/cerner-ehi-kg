# SCH_EVENT_ATTACH

> Scheduling Event Attachments

**Description:** Scheduling Event Attachments  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTACH_SOURCE_FLAG` | DOUBLE | NOT NULL |  | This is the source of the association of the order_to_appointment. |
| 6 | `ATTACH_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded Identifier for the scheduling attachment type. |
| 7 | `ATTACH_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-characted description corresponding to the scheduling attchment type code. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BEG_SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | The scheduling sequence on which the attachment became active. |
| 10 | `CANCEL_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Used to track the scheduling action on which an order was cancelled. This provides the ability to 're-associate' cancelled orders. |
| 11 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 12 | `CONCURRENT_IND` | DOUBLE | NOT NULL |  | Determines if the order is concurrent with the previous order in the event. |
| 13 | `DESCRIPTION` | VARCHAR(100) |  |  | A long description used for documentation. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `END_SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | The ending schedule sequence on which the attachment became inactive. |
| 16 | `EVENT_DT_TM` | DATETIME |  |  | The date and time the row was written from the scheduling appointment book. |
| 17 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 18 | `ORDER_DT_TM` | DATETIME |  |  | The date and time the order corresponding to the row was written from the order server. |
| 19 | `ORDER_ID` | DOUBLE | NOT NULL |  | The unique identifier of the order. |
| 20 | `ORDER_SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence of the order within the appointment. |
| 21 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the status of the order. |
| 22 | `ORDER_STATUS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding ORDER_STATUS_CD. |
| 23 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | Mark the attachment as the primary attachment for the schedule sequence. |
| 24 | `SCH_ATTACH_ID` | DOUBLE | NOT NULL |  | The generated numeric identifier for the scheduling event attachment. |
| 25 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 26 | `SCH_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier corresponding to the current state of association to the attachment. |
| 27 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 28 | `STATE_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the current state of association to the attachment. |
| 29 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the order catalog synonym. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTACH_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CANCEL_ACTION_ID` | [SCH_EVENT_ACTION](SCH_EVENT_ACTION.md) | `SCH_ACTION_ID` |
| `ORDER_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SCH_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

