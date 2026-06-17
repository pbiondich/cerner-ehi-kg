# SCH_EVENT

> Contains the requested/scheduled appointments.

**Description:** Scheduled Appointment  
**Table type:** ACTIVITY  
**Primary key:** `SCH_EVENT_ID`  
**Columns:** 65  
**Referenced by:** 33 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_REASON_FREE` | VARCHAR(255) |  |  | The free text reason the appointment was requested. |
| 6 | `APPT_SYNONYM_CD` | DOUBLE | NOT NULL |  | The identifier for an appointment type synonym. |
| 7 | `APPT_SYNONYM_FREE` | VARCHAR(255) |  |  | The free textmnemonic corresponding to appointment type synonym used to request the appointment. |
| 8 | `APPT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for an appointment type. An example would be cardiac cath, echo stress, etc. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 11 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `ESO_SEND_IND` | DOUBLE |  |  | Determines if the scheduled event has been sent through the interface. |
| 14 | `EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | The class code for the scheduling event. An example would be onward referral, etc. |
| 15 | `EVENT_RECUR_ID` | DOUBLE | NOT NULL |  | The unique identifier for the event's recurring pattern. |
| 16 | `FIRST_BKD_ASI_DT_TM` | DATETIME |  |  | The first time the appointment was booked. |
| 17 | `GRACE_PERIOD_CD` | DOUBLE | NOT NULL |  | The unit of measure for grace period value from code set 54. |
| 18 | `GRACE_PERIOD_MEANING` | VARCHAR(12) |  |  | The meaning of the grace period cd like 'DAYS', 'WEEKS', 'MONTHS', etc. |
| 19 | `GRACE_PERIOD_VALUE` | DOUBLE |  |  | The numeric value of a period of time before and after the requested date during which an event may be scheduled. |
| 20 | `GRP_BEG_DT_TM` | DATETIME |  |  | Indicates the beginning of the first session |
| 21 | `GRP_CAPACITY` | DOUBLE |  |  | Used to know the maximum number of patients that can be scheduled for this event. |
| 22 | `GRP_CLOSED_IND` | DOUBLE | NOT NULL |  | Indicates whether session can be used once current date/time is past the first session's start date/time |
| 23 | `GRP_DESC` | VARCHAR(255) |  |  | Name of the Group Session - will be displayed on the appointment book view. |
| 24 | `GRP_END_DT_TM` | DATETIME |  |  | Indicates the end of the last session. |
| 25 | `GRP_FLAG` | DOUBLE |  |  | Indicator to distinguish between Group Sessions, Structured Group Sessions and non Group Sessions. 0 - Traditional event not part of a group session, 1 - Group session event, 2 - Structured group session event, 3 - All events scheduled in the book into the group sessions. |
| 26 | `GRP_NBR_SCHED` | DOUBLE |  |  | Used to track the number of patients that have been scheduled into this event. |
| 27 | `GRP_SHARED_IND` | DOUBLE | NOT NULL |  | Indicates whether the session can be used together with other sessions. |
| 28 | `NULL_DT_TM` | DATETIME | NOT NULL |  | Contains 31-DEC-2100 00:00:00.00 |
| 29 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | The identifier of the accept format. |
| 30 | `OFFSET_BEG_UNITS` | DOUBLE |  |  | Scheduling Offset Beg Units |
| 31 | `OFFSET_BEG_UNITS_CD` | DOUBLE | NOT NULL |  | The unit of measure for the field Offset_Beg_Units. An example would be days, dollars, etc. |
| 32 | `OFFSET_BEG_UNITS_MEANING` | VARCHAR(12) |  |  | Scheduling Offset Beg Units Meaning |
| 33 | `OFFSET_END_UNITS` | DOUBLE |  |  | Scheduling Offset End Units |
| 34 | `OFFSET_END_UNITS_CD` | DOUBLE | NOT NULL |  | The unit of measure for the field Offset_End_Units. An example would be days, dollars, etc. |
| 35 | `OFFSET_END_UNITS_MEANING` | VARCHAR(12) |  |  | Scheduling Offset End Units Meaning |
| 36 | `OFFSET_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the event the current event is offset from. |
| 37 | `OFFSET_FROM_CD` | DOUBLE | NOT NULL |  | Indicates what the offset is associated with. An example would be person or primary resource. |
| 38 | `OFFSET_FROM_MEANING` | VARCHAR(12) |  |  | Scheduling Offset From Type Meaning |
| 39 | `OFFSET_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates what type of scheduling offset it is. An example would be begining or ending. |
| 40 | `OFFSET_TYPE_MEANING` | VARCHAR(12) |  |  | Scheduling Offset Type Meaning |
| 41 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order sentence. |
| 42 | `ORIG_REQ_END_DT_TM` | DATETIME |  |  | The original requested end date time specified by the provider at the time the event was initially requested. Useful when rescheduling or for reporting purpose. |
| 43 | `ORIG_REQ_START_DT_TM` | DATETIME |  |  | The original requested start date time specified by the provider at the time the event was initially requested. Useful when rescheduling or for reporting purpose. |
| 44 | `PROTOCOL_PARENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the protocol parent event. |
| 45 | `PROTOCOL_SEQ_NBR` | DOUBLE |  |  | The sequence of the protocol component within the protocol. |
| 46 | `PROTOCOL_TYPE_FLAG` | DOUBLE |  |  | A field used to determine if the event is part of a protocol (parent, child). 0 - none, 1 - parent only, 2 - parent & child, 3 - child only. |
| 47 | `RECUR_PARENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the recurring series parent scheduled event. |
| 48 | `RECUR_SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a recursive event. |
| 49 | `RECUR_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the scheduled event that should be used to create future recurring events. |
| 50 | `RECUR_TYPE_FLAG` | DOUBLE | NOT NULL |  | The flag determines if the event is a member of a recurring series (parent, sibling?). 0 - Not a recursive event, 1 - Recursive event |
| 51 | `REFER_DT_TM` | DATETIME |  |  | The date and time of the referral information. |
| 52 | `REFER_PRINTED_IND` | DOUBLE | NOT NULL |  | Indicates whether the referral's information has been printed. |
| 53 | `REQUEST_RANGE_RETAIN_IND` | DOUBLE |  |  | When this value is set to 1, all requests for this event will retain the requested date time range from the original request for booking. When this is set to 0, the dates associated with requests are not limited to the initial date time ranges. |
| 54 | `REQ_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) that requested the appointment. |
| 55 | `SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | Used to document the rescheduling of appointments. |
| 56 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the requested/scheduled appointment. |
| 57 | `SCH_EVENT_SEQ` | DOUBLE | NOT NULL |  | Used to sequence scheduling events. |
| 58 | `SCH_MEANING` | VARCHAR(12) | NOT NULL |  | The 12-character string corresponding to the current state of the appointment. |
| 59 | `SCH_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier corresponding to the current state of the appointment. An example would be complete, confirmed, deleted. etc. |
| 60 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CONTRIBUTOR_SYSTEM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OFFSET_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `PROTOCOL_PARENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `RECUR_PARENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `RECUR_TEMPLATE_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `REQ_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (33)

| From table | Column |
|------------|--------|
| [AUTH_SCH_EVENT_RELTN](AUTH_SCH_EVENT_RELTN.md) | `SCH_EVENT_ID` |
| [AUTH_SCH_EVENT_RELTN_HIST](AUTH_SCH_EVENT_RELTN_HIST.md) | `SCH_EVENT_ID` |
| [CDI_WORK_ITEM](CDI_WORK_ITEM.md) | `SCH_EVENT_ID` |
| [ESI_LOG](ESI_LOG.md) | `SCH_EVENT_ID` |
| [MP_AMB_ORG_SAT](MP_AMB_ORG_SAT.md) | `SCH_EVENT_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `SCH_EVENT_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `SCH_EVENT_ID` |
| [PM_WAIT_LIST](PM_WAIT_LIST.md) | `SCH_EVENT_ID` |
| [RC_SLA_ACTIVITY](RC_SLA_ACTIVITY.md) | `SCH_EVENT_ID` |
| [SCH_APPT](SCH_APPT.md) | `GRPSESSION_ID` |
| [SCH_APPT](SCH_APPT.md) | `SCH_EVENT_ID` |
| [SCH_DISPLACED_APPT](SCH_DISPLACED_APPT.md) | `SCH_EVENT_ID` |
| [SCH_ENTRY](SCH_ENTRY.md) | `SCH_EVENT_ID` |
| [SCH_EVENT](SCH_EVENT.md) | `OFFSET_EVENT_ID` |
| [SCH_EVENT](SCH_EVENT.md) | `PROTOCOL_PARENT_ID` |
| [SCH_EVENT](SCH_EVENT.md) | `RECUR_PARENT_ID` |
| [SCH_EVENT](SCH_EVENT.md) | `RECUR_TEMPLATE_ID` |
| [SCH_EVENT_ACTION](SCH_EVENT_ACTION.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_ALIAS](SCH_EVENT_ALIAS.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_ATTACH](SCH_EVENT_ATTACH.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_COMM](SCH_EVENT_COMM.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_DETAIL](SCH_EVENT_DETAIL.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_DISP](SCH_EVENT_DISP.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_LINK](SCH_EVENT_LINK.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_PATIENT](SCH_EVENT_PATIENT.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_RECUR](SCH_EVENT_RECUR.md) | `RECUR_TEMPLATE_ID` |
| [SCH_EVENT_RECUR](SCH_EVENT_RECUR.md) | `SCH_EVENT_ID` |
| [SCH_EVENT_ROLE](SCH_EVENT_ROLE.md) | `SCH_EVENT_ID` |
| [SCH_MESSAGING](SCH_MESSAGING.md) | `SCH_EVENT_ID` |
| [SCH_SCHEDULE](SCH_SCHEDULE.md) | `GRPSESSION_ID` |
| [SCH_SCHEDULE](SCH_SCHEDULE.md) | `SCH_EVENT_ID` |
| [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `SCH_EVENT_ID` |
| [SURGICAL_CASE](SURGICAL_CASE.md) | `SCH_EVENT_ID` |

