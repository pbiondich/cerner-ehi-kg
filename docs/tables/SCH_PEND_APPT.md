# SCH_PEND_APPT

> Stores information to the pending appointment scheduled from patient portal.

**Description:** Schedule Pending Appointment  
**Table type:** ACTIVITY  
**Primary key:** `SCH_PEND_APPT_ID`  
**Columns:** 29  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLY_SLOT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the applied slot. |
| 2 | `APPT_SYNONYM_CD` | DOUBLE | NOT NULL |  | The identifier for an appointment type synonym. |
| 3 | `APPT_TYPE_CD` | DOUBLE | NOT NULL |  | The identifier for an appointment type. |
| 4 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date and Time value |
| 5 | `BOOKING_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a resource availability lock. |
| 6 | `CLEANUP_DURATION` | DOUBLE |  |  | The duration for patient recovery or resource (such as room) clean up. |
| 7 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Create Date and Time value. |
| 8 | `DURATION` | DOUBLE | NOT NULL |  | The duration in minutes. |
| 9 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date and Time value. |
| 10 | `EXPIRE_DT_TM` | DATETIME | NOT NULL |  | The date and time that the booking_id will expire. |
| 11 | `LIST_ROLE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the list role. |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The field identifies the current permanent location of the patient. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that the appointment is for. |
| 14 | `PRIMARY_ROLE_IND` | DOUBLE | NOT NULL |  | Designated the resource's appointment role as the primary role for the appointment. |
| 15 | `RESOURCE_CD` | DOUBLE | NOT NULL |  | The identifier for the resource. A resource is an item of limited availability. |
| 16 | `RESOURCE_MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 17 | `ROLE_DESCRIPTION` | VARCHAR(200) |  |  | The description of the role on the resource list. |
| 18 | `ROLE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling role. |
| 19 | `ROLE_SEQ` | DOUBLE | NOT NULL |  | The order of the role on the resource list. |
| 20 | `SCH_PEND_APPT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SCH_PEND_APPT table. |
| 21 | `SCH_PEND_EVENT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the requested/scheduled appointment. |
| 22 | `SCH_ROLE_CD` | DOUBLE | NOT NULL |  | The coded identifier for the scheduling role. |
| 23 | `SETUP_DURATION` | DOUBLE |  |  | The duration for patient arrival or resource (such as room) set up. |
| 24 | `SLOT_MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BOOKING_ID` | [SCH_BOOKING](SCH_BOOKING.md) | `BOOKING_ID` |
| `LIST_ROLE_ID` | [SCH_LIST_ROLE](SCH_LIST_ROLE.md) | `LIST_ROLE_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_PEND_WARNING](SCH_PEND_WARNING.md) | `SCH_PEND_APPT_ID` |

