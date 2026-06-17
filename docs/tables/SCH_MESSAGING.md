# SCH_MESSAGING

> Table used to capture what appointments reminder messages were sent out for.

**Description:** Scheduling Messaging  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTACT_METHOD_CD` | DOUBLE | NOT NULL |  | This is the contact cd value of the type of contact (text, email, phone call, ect..) |
| 2 | `GROUP_IDENT` | VARCHAR(100) | NOT NULL |  | The identifier for the transaction that was called to get the response to the message. ID comes from Transaction Services which is external to Millennium. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location where the appointment is expected to take place. |
| 4 | `MESSAGE_SENT_FLAG` | DOUBLE | NOT NULL |  | This is the numerical value that represents the message we sent to the patient or correct responsible party for that patient. 0 - Value Not Entered, 1 = Standard Message, 3 - New Patient Message, 8 - No Show Message |
| 5 | `PATIENT_FIN_RESPONSIBILITY_AMT` | DOUBLE | NOT NULL |  | The amount of money the patient is financially responsible for services and goods rendered during their appointment. |
| 6 | `PATIENT_RESPONSE_CD` | DOUBLE | NOT NULL |  | This is the response about the appointment provided by the patient or responsible party for said patient. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person that the appointment is about. |
| 8 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the event schedule. The schedules are used to track rescheduling of an event. |
| 9 | `SCH_APPT_DT_TM` | DATETIME | NOT NULL |  | When the appointment is scheduled to take place. |
| 10 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The key that matches the message sent to the event it is about. |
| 11 | `SCH_MESSAGING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_MESSAGING table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 18 | `WRITTEN_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row is written out to the table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SCHEDULE_ID` | [SCH_SCHEDULE](SCH_SCHEDULE.md) | `SCHEDULE_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

