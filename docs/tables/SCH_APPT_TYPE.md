# SCH_APPT_TYPE

> The appointment type specifies the type of service to perform in the appointment.

**Description:** Appointment Type  
**Table type:** REFERENCE  
**Primary key:** `APPT_TYPE_CD`  
**Columns:** 27  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_TYPE_CD` | DOUBLE | NOT NULL | PK FK→ | The identifier for an appointment type. |
| 6 | `APPT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines if the appointment type is a protocol or a discrete appointment type. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `GRP_PROMPT_CD` | DOUBLE | NOT NULL |  | Code value that indicates whether group session prompting is optional, required or disabled |
| 12 | `GRP_PROMPT_MEANING` | VARCHAR(12) |  |  | CDF meaning value that indicates whether group session prompting is optional, required or disabled |
| 13 | `GRP_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | this resource will be used to store the availability when a group session is created for the associated appointment. |
| 14 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 15 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 16 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the accept format. |
| 17 | `PERSON_ACCEPT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the person accept option. This is used to determine if the person/patient is required/optional/disabled for the appointment type. |
| 18 | `PERSON_ACCEPT_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the person accept option. |
| 19 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Priority sequence of the appointment type. |
| 20 | `RECUR_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the ability to recur. |
| 21 | `RECUR_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the ability to recur. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `GRP_RESOURCE_CD` | [SCH_RESOURCE](SCH_RESOURCE.md) | `RESOURCE_CD` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `OE_FORMAT_ID` | [ORDER_ENTRY_FORMAT_PARENT](ORDER_ENTRY_FORMAT_PARENT.md) | `OE_FORMAT_ID` |
| `PERSON_ACCEPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RECUR_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SCH_APPT_TYPE_SYN_R](SCH_APPT_TYPE_SYN_R.md) | `APPT_TYPE_CD` |
| [SCH_AT_ENCNTR_TYPE_R](SCH_AT_ENCNTR_TYPE_R.md) | `APPT_TYPE_CD` |
| [SCH_AT_INSUR_PROFILE_R](SCH_AT_INSUR_PROFILE_R.md) | `APPT_TYPE_CD` |
| [SCH_AT_MED_SERVICE_R](SCH_AT_MED_SERVICE_R.md) | `APPT_TYPE_CD` |
| [SCH_AT_SPECIALTY_R](SCH_AT_SPECIALTY_R.md) | `APPT_TYPE_CD` |

