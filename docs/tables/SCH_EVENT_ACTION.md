# SCH_EVENT_ACTION

> Record the actions performed on an appointment

**Description:** Event Actions  
**Table type:** ACTIVITY  
**Primary key:** `SCH_ACTION_ID`  
**Columns:** 55  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_CONV_ID` | DOUBLE | NOT NULL |  | Conversation Identifier of last Medical Necessity Check |
| 2 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | The date/time of the scheduling action. |
| 3 | `ACTION_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-char description corresponding to the Scheduling ActionCode. |
| 4 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | There will be situations where the person will be a patient and not be a PRSNL. In this case the source of the _id will be PERSON. |
| 5 | `ACTION_SOURCE_CD` | DOUBLE |  |  | The code value of the source of the action being taken. (User, Appointment Reminder, Auto Dialer, etc.). |
| 6 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 9 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 10 | `APPT_SYNONYM_CD` | DOUBLE |  |  | The identifier for an appointment type synonym. |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BREACH_OFFSET_DAYS` | DOUBLE |  |  | The number of days in breach for adding a referral letter from the freeze or lead time. |
| 13 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 14 | `CONTACT_FOLLOW_UP_DT_TM` | DATETIME |  |  | The date/time of the follow-up action for scheduling items. |
| 15 | `CONTACT_OUTCOME_CD` | DOUBLE |  |  | An outcome code value associated with contacting a referrer to add a referral letter. |
| 16 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | Scheduling Conversation Identifier. This identifier is used to track all the scheduling actions to perform at a list of appointments at the same transaction. This field makes debugging much easier. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `ESO_ACTION_CD` | DOUBLE | NOT NULL | FK→ | A coded Identifier for the Scheduling ESO Action Code. An example would be 'cancel appointment', 'appointment', etc. |
| 19 | `ESO_ACTION_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling ESO Action Code. |
| 20 | `GUIDANCE_EXISTS_IND` | DOUBLE |  |  | Indicates whether a Service Specific Booking Guidance was defined for the specialty associated to the action. |
| 21 | `HIPAA_ACTION_CD` | DOUBLE | NOT NULL |  | Used to track if a record has already been processed by HIPAA logging. |
| 22 | `NULL_DT_TM` | DATETIME | NOT NULL |  | Contains 31-DEC-2100 00:00:00.00 |
| 23 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization context of the user at time of action. |
| 24 | `ORIG_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The event action identifier on the SCH_EVENT_ACTION table of the original request. |
| 25 | `PATIENT_DECEASED_IND` | DOUBLE |  |  | Indicates whether the patient is deceased at the time the action is performed. |
| 26 | `PERFORM_DT_TM` | DATETIME | NOT NULL |  | The performed date and time specified by the user that the action was performed. It is used for retroactive checkin. |
| 27 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position of the personnel when the action was performed. For example, 'RN', 'Case Manager', etc. |
| 28 | `PRACTICE_ORG_ID` | DOUBLE | NOT NULL | FK→ | The identifier of a Practice organization which applies to the action. |
| 29 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The scheduling product code. Some examples are 'Choose and Book', 'IQ Health', etc. |
| 30 | `PROXY_ID` | DOUBLE | NOT NULL | FK→ | Identifier representing the person on behalf of which the action was performed. |
| 31 | `PROXY_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization context of proxied user at time of action. |
| 32 | `PROXY_POSITION_CD` | DOUBLE | NOT NULL |  | The position of the proxy personnel when the action was performed. For example, 'RN', 'Case Manager', etc. |
| 33 | `PROXY_ROLE_PROFILE` | VARCHAR(255) |  |  | Identifies the role profile of the proxy personnel who performed this action. |
| 34 | `REASON_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling reason. |
| 35 | `REFERRING_RESOURCE_CD` | DOUBLE | NOT NULL |  | The resource_cd of the resource that onward referred the appointment. |
| 36 | `REQ_ACTION_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the requested action. An example would be 'appointment', 'cancel', etc. |
| 37 | `REQ_ACTION_ID` | DOUBLE | NOT NULL |  | The unique identifier corresponding to the requested action. This field is used to store details and comments about the requested action. |
| 38 | `REQ_ACTION_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the requested action. |
| 39 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the resource associated to this action. |
| 40 | `ROLE_PROFILE` | VARCHAR(255) |  |  | Identifies the role profile of personnel who performed this action. |
| 41 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the event schedule. |
| 42 | `SCH_ACTION_CD` | DOUBLE | NOT NULL |  | A unique identifier for the Scheduling Action Code. An example would be 'defer', 'cancel', etc. |
| 43 | `SCH_ACTION_ID` | DOUBLE | NOT NULL | PK | The identifier to uniquely identify the action being performed. The unique primary key of this table. |
| 44 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. References the SCH_EVENT table. |
| 45 | `SCH_REASON_CD` | DOUBLE | NOT NULL |  | The coded identifier of the scheduling reason. An example would be 'patient deceased', 'no show', etc., |
| 46 | `SCH_USER_SESSION_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE COLUMN (Parent table is obsolete) ** This will be the ID of the user's session that performed the action. The primary key of the SCH_USER_SESSION table. |
| 47 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 53 | `VER_INTERCHANGE_ID` | DOUBLE | NOT NULL |  | ABN (Advance Beneficiary Notices) transaction id. |
| 54 | `VER_STATUS_CD` | DOUBLE | NOT NULL | FK→ | ABN (Advance Beneficiary Notices) Verification status code. Examples are 'error', 'returned' and 'denial'. |
| 55 | `VER_STATUS_MEANING` | VARCHAR(12) |  |  | ABN (Advance Beneficiary Notices) Verification status meaning. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ESO_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIG_ACTION_ID` | [SCH_EVENT_ACTION](SCH_EVENT_ACTION.md) | `SCH_ACTION_ID` |
| `PRACTICE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PROXY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PROXY_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `REQ_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCHEDULE_ID` | [SCH_SCHEDULE](SCH_SCHEDULE.md) | `SCHEDULE_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `VER_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [PM_POST_DOC](PM_POST_DOC.md) | `SCH_ACTION_ID` |
| [SCH_ACTION_DATE](SCH_ACTION_DATE.md) | `SCH_ACTION_ID` |
| [SCH_ACTION_LOC](SCH_ACTION_LOC.md) | `SCH_ACTION_ID` |
| [SCH_ACTION_ROLE](SCH_ACTION_ROLE.md) | `SCH_ACTION_ID` |
| [SCH_ENTRY](SCH_ENTRY.md) | `SCH_ACTION_ID` |
| [SCH_EVENT_ACTION](SCH_EVENT_ACTION.md) | `ORIG_ACTION_ID` |
| [SCH_EVENT_ATTACH](SCH_EVENT_ATTACH.md) | `CANCEL_ACTION_ID` |
| [SCH_EVENT_COMM](SCH_EVENT_COMM.md) | `SCH_ACTION_ID` |
| [SCH_EVENT_DETAIL](SCH_EVENT_DETAIL.md) | `SCH_ACTION_ID` |

