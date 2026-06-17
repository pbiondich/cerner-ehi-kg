# UKRWH_CDE_EAL_ENTRY

> Contains additional Elective Admnission List Entry (EAL) level details relating to an EAL CDS Event.

**Description:** UK Reporting Warehouse Consolidated Data Extract Elective Admission List Entry  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 50

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_BOOKING_REF` | VARCHAR(40) |  |  | Admission booking system type. |
| 2 | `ADMIT_CATEGORY_REF` | VARCHAR(40) |  |  | Admission or administrative category |
| 3 | `ADMIT_DECISION_DT_TM` | DATETIME |  |  | Date and time the decision to admit was made |
| 4 | `ADMIT_GUARANTEED_DT_TM` | DATETIME |  |  | Guaranteed admission date and time |
| 5 | `ADMIT_TYPE_REF` | VARCHAR(40) |  |  | Type of waiting list admission. (ex. Day case, inpatient) |
| 6 | `ATTEND_DOC_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the physician attending the patient in elective admissions (wait list) |
| 7 | `BOTH_DATES_REFUSED_REF` | VARCHAR(40) |  |  | This field indicates whether the patient has refused both the wait list offers |
| 8 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 9 | `EAL_ENTRY_SK` | VARCHAR(40) |  |  | A number to provide a unique identifier for each ELECTIVE ADMISSION LIST ENTRY within an ELECTIVE ADMISSION LIST. |
| 10 | `ENCNTR_ACTIVE_IND` | DOUBLE |  |  | The Millennium encounter table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 11 | `ENCNTR_CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the encounter table. |
| 12 | `ENCNTR_CREATE_PRSNL` | VARCHAR(40) |  |  | This is the person responsible for creating a row in the encounter table. |
| 13 | `ENCNTR_UPDT_DT_TM` | DATETIME |  |  | The date and time the row on the encounter table was last inserted or updated. |
| 14 | `ENCNTR_UPDT_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the encounter table. |
| 15 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 16 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 17 | `FIN_IDENT` | VARCHAR(200) |  |  | The alias is an identifier (I.e., financial number) for an encounter. The alias may be unique or non-unique depending on the type of alias. |
| 18 | `FIRST_OFFERED_DT_TM` | DATETIME |  |  | It is the date/time for which the patient was offered the first elective admission (wait list) |
| 19 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 20 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 21 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 22 | `INTENDED_MANAGEMENT_REF` | VARCHAR(40) |  |  | Intended management. |
| 23 | `LAST_DNA_DT_TM` | DATETIME |  |  | Last date and time a DNA was recorded for a waiting list entry |
| 24 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 25 | `LAST_STATUS_REVIEW_DT_TM` | DATETIME |  |  | The date/time that a wait list status was reviewed. |
| 26 | `MAIN_SPECIALTY_REF` | VARCHAR(40) |  |  | It is the specialty in which the CONSULTANT is contracted or recognised. MAIN SPECIALTY classifies clinical work divisions more precisely for a limited number of specialties |
| 27 | `MIGRATED_IND` | DOUBLE |  |  | Derived formt her encountercontributor_system_cd. Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 28 | `OFFERS_MADE_DT_TM` | DATETIME |  |  | It is the date/time at which the elective admission (wait list) offer/s were made. |
| 29 | `ORIGINAL_ADMIT_DECISION_DT_TM` | DATETIME |  |  | The date/time at which the original decision was made to admit the patient |
| 30 | `OVERSEAS_STATUS_REF` | VARCHAR(40) |  |  | The status of an overseas visitor for a particular ACTIVITY, where an overseas visitor is a PERSON not ordinarily resident in the UK, with respect to charging rates. |
| 31 | `PERSON_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 32 | `PRE_ADMIT_WARD_REF` | VARCHAR(40) |  |  | This field is the code value for the current patient location with a location type of Nurse Unit. |
| 33 | `REASON_FOR_CHANGE_REF` | VARCHAR(40) |  |  | Code value for a text description of the reason a change was made. |
| 34 | `REASON_FOR_REMOVAL_REF` | VARCHAR(40) |  |  | Code value for a text description of the reason a removal was made. |
| 35 | `REFERRER_DOC_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the physician referring the patient in elective admissions (wait list) |
| 36 | `SECOND_OFFERED_DT_TM` | DATETIME |  |  | It is the date/time for which the patient was offered the second elective admission (wait list) |
| 37 | `STAND_BY_REF` | VARCHAR(40) |  |  | Code Value that contains a text description of a wait list stand by. |
| 38 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 39 | `TREATMENT_FUNCTION_REF` | VARCHAR(40) |  |  | This is the TREATMENT FUNCTION under which the PATIENT is treated. |
| 40 | `UKRWH_CDE_EAL_ENTRY_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde eal entry table. It is an internal system assigned number. |
| 41 | `UKRWH_CDE_PERSON_PATIENT_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde person patient table. It is an internal system assigned number. |
| 42 | `UKRWH_CDS_EAL_ENTRY_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde eal entry table. It is an internal system assigned number. |
| 43 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row |
| 48 | `URGENCY_REF` | VARCHAR(40) |  |  | Code Value for the urgency of patient event on wait list. Example: within 7 days. |
| 49 | `WAITING_END_DT_TM` | DATETIME |  |  | Waiting End Date Time. |
| 50 | `WAITLIST_STATUS_REF` | VARCHAR(40) |  |  | Code value that refers to the status of a wait list row. Examples: Normal Deferred. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_PERSON_PATIENT_KEY` | [UKRWH_CDE_PERSON_PATIENT](UKRWH_CDE_PERSON_PATIENT.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |
| `UKRWH_CDS_EAL_ENTRY_KEY` | [UKRWH_CDS_EAL_ENTRY](UKRWH_CDS_EAL_ENTRY.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |

