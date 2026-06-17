# SCH_BOOKING

> This table is used to record time availability used or released by scheduling appointments.

**Description:** Scheduling Booking  
**Table type:** ACTIVITY  
**Primary key:** `BOOKING_ID`  
**Columns:** 37  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLY_SLOT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the applied slot. |
| 6 | `APPT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for an appointment type. |
| 7 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date and Time value |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BOOKING_ID` | DOUBLE | NOT NULL | PK | The unique identifier for a resource availability lock. |
| 10 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date and Time value |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FORCE_IND` | DOUBLE |  |  | Determines if the user force the locking of the resource's availability. |
| 15 | `GRANTED_DT_TM` | DATETIME |  |  | Date and Time the availability lock as granted. |
| 16 | `GRANTED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) to whom the availability lock was granted. There will be situations where the person will be a patient and not be a PRSNL. In this case the source of the _id will be PERSON. |
| 17 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The field identifies the current permanent location of the patient. |
| 18 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 19 | `ORIG_BEG_DT_TM` | DATETIME |  |  | Begin Date and Time prior to extending the slot. |
| 20 | `ORIG_END_DT_TM` | DATETIME |  |  | End Date and Time prior to extending the slot. |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. If the role is a patient role, the person_id is patient's person_id. If the role is not a patient role, it will be a scheduling resource. There are different type of resources. If the resource is a personnel resource, the person_id will be provider's person_id. If the resource is not a personnel resource, then the person_id will be 0. |
| 22 | `RELEASE_DT_TM` | DATETIME |  |  | The date and time the row should automatically release. |
| 23 | `RELEASE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) that released the availability lock. There will be situations where the person will be a patient and not be a PRSNL. In this case the source of the _id will be PERSON. |
| 24 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the resource. A resource is an item of limited availability. |
| 25 | `ROLE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling role. |
| 26 | `SCH_ROLE_CD` | DOUBLE | NOT NULL |  | The coded identifier for the scheduling role. |
| 27 | `SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence number of the resource list role for the booking appointment. |
| 28 | `STATUS_FLAG` | DOUBLE |  |  | A coded field used to denote the current status. |
| 29 | `STATUS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the STATUS_FLAG. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the record was verified. |
| 36 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 37 | `WRITTEN_DT_TM` | DATETIME |  |  | The date and time the corresponding record was written. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `GRANTED_PRSNL_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RELEASE_PRSNL_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SCH_APPT](SCH_APPT.md) | `BOOKING_ID` |
| [SCH_BOOKING_ORD](SCH_BOOKING_ORD.md) | `BOOKING_ID` |
| [SCH_PEND_APPT](SCH_PEND_APPT.md) | `BOOKING_ID` |

