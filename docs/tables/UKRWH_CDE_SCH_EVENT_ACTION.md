# UKRWH_CDE_SCH_EVENT_ACTION

> Contains denormalised schedule event action details relating to Outpatiient and Elective Admission List CDS Events.

**Description:** UK Reporting Warehouse Consolidated Data Extract Schedule Event Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BOOKING_ACTION_DT_TM` | DATETIME |  |  | Booking Action Date and Time |
| 2 | `BOOKING_ACTION_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the personnel making the booking |
| 3 | `CANCEL_DNA_ACTION_DT_TM` | DATETIME |  |  | DNA Cancel Date and Time |
| 4 | `CANCEL_DNA_ACTION_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that cancelled the DNA |
| 5 | `CANCEL_DNA_PERFOM_DT_TM` | DATETIME |  |  | Date and Time when the DNA was actually perfomed |
| 6 | `CANCEL_REASON_MEANING_TXT` | VARCHAR(12) |  |  | A 12-character description corresponding to the cancelling reason |
| 7 | `CANCEL_REASON_REF` | VARCHAR(40) |  |  | The coded identifier of the cancelling reason |
| 8 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 9 | `CHECKIN_ACTION_DT_TM` | DATETIME |  |  | Date and Time of Checkin |
| 10 | `CHECKIN_ACTION_PRSNL` | VARCHAR(40) |  |  | The Millennium person_id of the person from the personnel table (prsnl) that checked in the patient |
| 11 | `CHECKIN_PERFOM_DT_TM` | DATETIME |  |  | Date and Time when the Checkin was actually performed |
| 12 | `CHECKOUT_ACTION_DT_TM` | DATETIME |  |  | Date and Time of Checkout |
| 13 | `CHECKOUT_ACTION_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that checked out the patient |
| 14 | `CHECKOUT_PERFORM_DT_TM` | DATETIME |  |  | Date and Time when the Checkout was actually performed |
| 15 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 16 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 17 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 18 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 19 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 20 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 21 | `LOC_BOOKING_ACTION_DT_TM` | DATETIME |  |  | The booking action date and time. |
| 22 | `LOC_CANCEL_DNA_ACTION_DT_TM` | DATETIME |  |  | The DNA cancel date and time. |
| 23 | `RESCHEDULE_ACTION_DT_TM` | DATETIME |  |  | Scheduling Action Data and Time |
| 24 | `RESCHEDULE_ACTION_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that rescheduled the appointment |
| 25 | `RESCHEDULE_PERFORM_DT_TM` | DATETIME |  |  | The performed date and time specified by the user that the Rescheduling action was performed. It is used for retroactive checkin. |
| 26 | `RESCHEDULE_REASON_MEANING_TXT` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling reason |
| 27 | `RESCHEDULE_REASON_REF` | VARCHAR(40) |  |  | The coded identifier of the scheduling reason |
| 28 | `SCHEDULE_SK` | VARCHAR(40) |  |  | The unique identifier for the event schedule. |
| 29 | `SCH_ACTION_SK` | VARCHAR(40) |  |  | The Millennium identifier to uniquely identify the action being performed |
| 30 | `SCH_EVENT_SK` | VARCHAR(40) |  |  | The identifier to uniquely identify the event being performed |
| 31 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 32 | `UKRWH_CDE_OP_ATTENDANCE_KEY` | DOUBLE | NOT NULL | FK→ | The event action identifier on the SCH_EVENT_ACTION table of the O/P attendance |
| 33 | `UKRWH_CDE_SCH_EVENT_ACTION_KEY` | DOUBLE | NOT NULL |  | The event action identifier of the event action |
| 34 | `UKRWH_CDS_EAL_OFFER_KEY` | DOUBLE | NOT NULL | FK→ | The event action identifier on the SCH_EVENT_ACTION table of the EAL offer |
| 35 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 36 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_OP_ATTENDANCE_KEY` | [UKRWH_CDE_OP_ATTENDANCE](UKRWH_CDE_OP_ATTENDANCE.md) | `UKRWH_CDE_OP_ATTENDANCE_KEY` |
| `UKRWH_CDS_EAL_OFFER_KEY` | [UKRWH_CDS_EAL_OFFER](UKRWH_CDS_EAL_OFFER.md) | `UKRWH_CDS_EAL_OFFER_KEY` |
| `UKRWH_CDS_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

