# UKRWH_CDE_OP_ATTENDANCE

> Contains additional attendance level details relating to an Outpatient CDS Event.

**Description:** UK Reporting Warehouse Consolidated Data Extract Outpatient Attendance  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDE_OP_ATTENDANCE_KEY`  
**Columns:** 39  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMINISTRATIVE_CATEGORY_REF` | VARCHAR(40) |  |  | Identifies if a PATIENT is required to pay for treatment provided within a particular ACTIVITY or for transport. |
| 2 | `APPT_LOCATION_REF` | VARCHAR(40) |  |  | A coded identifier corresponding to the scheduled appointment location |
| 3 | `APPT_TYPE_REF` | VARCHAR(40) |  |  | The identifier for an appointment type. |
| 4 | `ATTENDANCE_DT_TM` | DATETIME |  |  | Begin Date and Time value |
| 5 | `ATTEND_DOC_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the physician attending the patient in outpatients |
| 6 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) |  |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 7 | `ENCNTR_ACTIVE_IND` | DOUBLE |  |  | The Millennium encounter table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 8 | `ENCNTR_CREATE_PRSNL` | VARCHAR(40) |  |  | This is the person responsible for creating a row in the encounter table. |
| 9 | `ENCNTR_UPDT_DT_TM` | DATETIME |  |  | The date and time the row on the encounter table was last inserted or updated. |
| 10 | `ENCNTR_UPDT_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the encounter table. |
| 11 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `ENCTR_CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the encounter table. |
| 13 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 14 | `FIN_IDENT` | VARCHAR(200) |  |  | The alias is an identifier (I.e., financial number) for an encounter. The alias may be unique or non-unique depending on the type of alias. |
| 15 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 16 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 17 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 18 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 19 | `LOC_ATTENDANCE_DT_TM` | DATETIME |  |  | The begin date and time value. |
| 20 | `LOC_FACILITY_REF` | VARCHAR(40) |  |  | This field is the current patient location with a location type of facility. |
| 21 | `MAIN_SPECIALTY_REF` | VARCHAR(40) |  |  | It is the specialty in which the CONSULTANT is contracted or recognised. MAIN SPECIALTY classifies clinical work divisions more precisely for a limited number of specialties |
| 22 | `MIGRATED_IND` | DOUBLE |  |  | Derived formt her encountercontributor_system_cd. Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 23 | `OVERSEAS_STATUS_REF` | VARCHAR(40) |  |  | The status of an overseas visitor for a particular ACTIVITY, where an overseas visitor is a PERSON not ordinarily resident in the UK, with respect to charging rates. |
| 24 | `REASON_FOR_VISIT_TXT` | VARCHAR(255) |  |  | The free text description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 25 | `RESOURCE_REF` | VARCHAR(40) |  |  | The identifier for the resource. A resource is an item of limited availability. |
| 26 | `SCHEDULE_SK` | VARCHAR(40) |  |  | The unique identifier for the millennium event schedule. The schedules are used to track rescheduling of an event. |
| 27 | `SCH_EVENT_SK` | VARCHAR(40) |  |  | The unique identifier for a resource's/patient's appointment |
| 28 | `SCH_STATE_REF` | VARCHAR(40) |  |  | The coded identifier corresponding to the current state of the appointment |
| 29 | `SLOT_MNEMONIC_TXT` | VARCHAR(100) |  |  | A 100-character string used for identification and selection |
| 30 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 31 | `TREATMENT_FUNCTION_REF` | VARCHAR(40) |  |  | This is the TREATMENT FUNCTION under which the PATIENT is treated. |
| 32 | `UKRWH_CDE_OP_ATTENDANCE_KEY` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ukrwh cde op attendance table. It is an internal system assigned number. |
| 33 | `UKRWH_CDE_OP_REFERRAL_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde op referral table. It is an internal system assigned number. |
| 34 | `UKRWH_CDS_OP_ATTENDANCE_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds op attendance table. It is an internal system assigned number. |
| 35 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_OP_REFERRAL_KEY` | [UKRWH_CDE_OP_REFERRAL](UKRWH_CDE_OP_REFERRAL.md) | `UKRWH_CDE_OP_REFERRAL_KEY` |
| `UKRWH_CDS_OP_ATTENDANCE_KEY` | [UKRWH_CDS_OP_ATTENDANCE](UKRWH_CDS_OP_ATTENDANCE.md) | `UKRWH_CDS_OP_ATTENDANCE_KEY` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_SCH_EVENT_ACTION](UKRWH_CDE_SCH_EVENT_ACTION.md) | `UKRWH_CDE_OP_ATTENDANCE_KEY` |

