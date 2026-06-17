# SCH_APPT

> Contains the appointments for a resource.

**Description:** Schedule Appointment  
**Table type:** ACTIVITY  
**Primary key:** `SCH_APPT_ID`  
**Columns:** 78  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling activity type. |
| 6 | `ACTIVITY_MEANING` | VARCHAR(12) |  |  | A 12-char description of the scheduling activity type. |
| 7 | `ALERT_BIT_MASK` | DOUBLE |  |  | Alert Bit Mask. Do not believe this column is used. It is obsolete. |
| 8 | `ALLOCATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the clinician allocated to a specific slot. |
| 9 | `APPLY_DEF_ID` | DOUBLE | NOT NULL |  | This unique identifier for a slot is used to store the slot definitions for the slot. The field is used to join to the SCH_APPT_DEF table for the slot definition. |
| 10 | `APPLY_LIST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the application of a default schedule to a resource |
| 11 | `APPLY_SLOT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the applied slot. |
| 12 | `APPT_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier corresponding to the scheduled appointment location. |
| 13 | `APPT_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | The scheduling display scheme for the appointment type and state. |
| 14 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date and Time value |
| 15 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 16 | `BIT_MASK` | DOUBLE | NOT NULL |  | A Bit String used to store internal processing flags. |
| 17 | `BOOKING_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a resource availability lock. |
| 18 | `BORDER_COLOR` | DOUBLE |  |  | The numeric equilivant of the border color. |
| 19 | `BORDER_SIZE` | DOUBLE |  |  | The numeric equilivant of the border size. |
| 20 | `BORDER_STYLE` | DOUBLE |  |  | The numeric equilivant of the border style. |
| 21 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 22 | `CLEANUP_DURATION` | DOUBLE |  |  | The duration for patient recovery or resource (such as room) clean up. |
| 23 | `CONTIGUOUS_IND` | DOUBLE | NOT NULL |  | Determines if a slot type is defined to be contiguous or discrete. |
| 24 | `DEFINING_IND` | DOUBLE | NOT NULL |  | Determines if the role is the defining role. |
| 25 | `DEF_SLOT_ID` | DOUBLE | NOT NULL |  | The identifier for the default schedule slot. |
| 26 | `DESCRIPTION` | VARCHAR(255) |  |  | A long description used for documentation. |
| 27 | `DURATION` | DOUBLE | NOT NULL |  | The duration in minutes. |
| 28 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 29 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date and Time value |
| 30 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 31 | `EXCLUDE_IND` | DOUBLE |  |  | NOT CURRENTLY USED. |
| 32 | `GROUP_SLOT_LINK_VALUE` | DOUBLE | NOT NULL |  | An identifier to link all the slots or/and appointments in the same group session together. |
| 33 | `GRPSESSION_ID` | DOUBLE | NOT NULL | FK→ | This will be used to find the appts associated to a given group session. This will be when viewing the appointments on the book. |
| 34 | `HOLIDAY_WEEKEND_FLAG` | DOUBLE |  |  | This field is used to denote if holidays and/or weekend should be excluded in the computation of scheduling release times. |
| 35 | `LIST_ROLE_ID` | DOUBLE | NOT NULL |  | The identifier for the list role. |
| 36 | `NON_SCHEDULE_IND` | DOUBLE |  |  | To indicate that the slot type is not schedulable. 1 = Not Schedulable. |
| 37 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 38 | `ORIG_BEG_DT_TM` | DATETIME |  |  | The original beg date and time for the default schedule slot. This is used to restore a modified slot to its original state. |
| 39 | `ORIG_END_DT_TM` | DATETIME |  |  | The original end date and time for the default schedule slot. This is used to restore a modified slot to its original state. |
| 40 | `PEN_SHAPE` | DOUBLE |  |  | A "0" in this column will indicate a "square" border pen. A "1" in this column will represent a "round" border pen. |
| 41 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. If the role is a patient role, the person_id is patient's person_id. If the role is not a patient role, it will be a scheduling resource. There are different type of resources. If the resource is a personnel resource, the person_id will be provider's person_id. If the resource is not a personnel resource, then the person_id will be 0. |
| 42 | `PRIMARY_ROLE_IND` | DOUBLE | NOT NULL |  | Designated the resource's appointment role as the primary role for the appointment. |
| 43 | `REFERRING_ORG_ID` | DOUBLE | NOT NULL | FK→ | The ID of the referring organization. |
| 44 | `RESERVE_RELEASE_DT_TM` | DATETIME | NOT NULL |  | The date that the slot will be released for general booking. |
| 45 | `RESOURCE_CD` | DOUBLE | NOT NULL |  | The identifier for the resource. A resource is an item of limited availability. |
| 46 | `ROLE_DESCRIPTION` | VARCHAR(200) |  |  | The description of the role on the resource list. |
| 47 | `ROLE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling role. |
| 48 | `ROLE_SEQ` | DOUBLE | NOT NULL |  | The order of the role on the resource list. |
| 49 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the event schedule. |
| 50 | `SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | Used to document the rescheduling of appointments. |
| 51 | `SCH_APPT_ID` | DOUBLE | NOT NULL | PK | The unique identifier for a resource's/patient's appointment. |
| 52 | `SCH_DATE_APPLY_ID` | DOUBLE | NOT NULL |  | Identifies the date and resource template associated to the appointment. |
| 53 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 54 | `SCH_ROLE_CD` | DOUBLE | NOT NULL |  | The coded identifier for the scheduling role. |
| 55 | `SCH_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier corresponding to the current state of the appointment. |
| 56 | `SCH_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the slot type at the time of scheduling. |
| 57 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The generic term used to denote a physical place in the Health Care Organization. |
| 58 | `SETUP_DURATION` | DOUBLE |  |  | The duration for patient arrival or resource (such as room) set up. |
| 59 | `SHAPE` | DOUBLE |  |  | The numeric equilivant of the shape. |
| 60 | `SLOT_MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 61 | `SLOT_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | The coded identifier of the disp scheme associated to the appointment.. |
| 62 | `SLOT_STATE_CD` | DOUBLE | NOT NULL | FK→ | The code_value for the current slot state. |
| 63 | `SLOT_STATE_MEANING` | VARCHAR(12) |  |  | A 12-char description of the schedule slot state. |
| 64 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the slot type that is associated to the appointment. |
| 65 | `SLOT_VIS_BEG_DT_TM` | DATETIME |  |  | The visible beginning time for the original slot. |
| 66 | `SLOT_VIS_END_DT_TM` | DATETIME |  |  | The visible end time for the original slot. |
| 67 | `STATE_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the current state of the appointment. |
| 68 | `TEMPLATE_LOCATION_CD` | DOUBLE |  | FK→ | Indicates which location can be booked into this slot, 0 means all locations. |
| 69 | `TIME_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines if the current entry is holding time. 0 - Unheld Time, 1 - Held Time. |
| 70 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 71 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 72 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 73 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 74 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 75 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 76 | `VIS_BEG_DT_TM` | DATETIME | NOT NULL |  | NOT CURRENTLY USED. |
| 77 | `VIS_END_DT_TM` | DATETIME | NOT NULL |  | NOT CURRENTLY USED. |
| 78 | `WARN_BIT_MASK` | DOUBLE | NOT NULL |  | This field is a bit mask used to store indicators about the warnings generated during the life-cycle of the appointment. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ALLOCATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `APPLY_LIST_ID` | [SCH_APPLY_LIST](SCH_APPLY_LIST.md) | `APPLY_LIST_ID` |
| `APPT_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `APPT_SCHEME_ID` | [SCH_DISP_SCHEME](SCH_DISP_SCHEME.md) | `DISP_SCHEME_ID` |
| `BOOKING_ID` | [SCH_BOOKING](SCH_BOOKING.md) | `BOOKING_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `GRPSESSION_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REFERRING_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SCHEDULE_ID` | [SCH_SCHEDULE](SCH_SCHEDULE.md) | `SCHEDULE_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SCH_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SLOT_SCHEME_ID` | [SCH_DISP_SCHEME](SCH_DISP_SCHEME.md) | `DISP_SCHEME_ID` |
| `SLOT_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |
| `TEMPLATE_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BH_GROUP_DOC](BH_GROUP_DOC.md) | `SCH_APPT_ID` |
| [SCH_DISPLACED_APPT](SCH_DISPLACED_APPT.md) | `SCH_APPT_ID` |
| [SCH_ENTRY](SCH_ENTRY.md) | `SCH_APPT_ID` |
| [SCH_EVENT_DISP](SCH_EVENT_DISP.md) | `SCH_APPT_ID` |
| [WL_ACTIVITY](WL_ACTIVITY.md) | `SCH_APPT_ID` |

