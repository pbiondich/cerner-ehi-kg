# UKRWH_CDE_OP_REFERRAL

> Contains additional Referral level details relating to an Outpatient CDS Event.

**Description:** UK Reporting Warehouse Consolidated Data Extract Outpatient Referral  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDE_OP_REFERRAL_KEY`  
**Columns:** 40  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMINISTRATIVE_CATEGORY_REF` | VARCHAR(40) |  |  | Identifies if a PATIENT is required to pay for treatment provided within a particular ACTIVITY or for transport. |
| 2 | `ADMIT_BOOKING_REF` | VARCHAR(40) |  |  | Admission booking system type. |
| 3 | `ADMIT_GUARANTEED_DT_TM` | DATETIME |  |  | The date by which a PATIENT on an ELECTIVE ADMISSION LIST is guaranteed to be admitted. |
| 4 | `ATTEND_DOC_PRSNL` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the personnel table. This is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table. |
| 5 | `ENCNTR_CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the encounter table. |
| 6 | `ENCNTR_CREATE_PRSNL` | VARCHAR(40) |  |  | This is the person responsible for creating a row in the encounter table. |
| 7 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 9 | `FIN_IDENT` | VARCHAR(200) |  |  | The alias is an identifier (I.e., financial number) for an encounter. The alias may be unique or non-unique depending on the type of alias. |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 11 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 14 | `LIST_TYPE_REF` | VARCHAR(40) |  |  | The code value for the planned Procedure for this wait list row. |
| 15 | `LOC_ORIG_REFERRAL_RCVD_DT_TM` | DATETIME |  |  | This records the first referral request received date for a specific health care service to be provided, which was received. |
| 16 | `LOC_WAITING_END_DT_TM` | DATETIME |  |  | The waiting end date time. |
| 17 | `MAIN_SPECIALTY_REF` | VARCHAR(40) |  |  | It is the specialty in which the CONSULTANT is contracted or recognised. MAIN SPECIALTY classifies clinical work divisions more precisely for a limited number of specialties |
| 18 | `ORIGINAL_REFERRAL_RCVD_DT_TM` | DATETIME |  |  | This records the first REFERRAL REQUEST RECEIVED DATE for a specific health care service to be provided, which was received. |
| 19 | `ORIG_OP_REF_IND` | DOUBLE | NOT NULL |  | Original Outpatient Referral Indicator |
| 20 | `OVERSEAS_STATUS_REF` | VARCHAR(40) |  |  | The status of an overseas visitor for a particular ACTIVITY, where an overseas visitor is a PERSON not ordinarily resident in the UK, with respect to charging rates. |
| 21 | `PERSON_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 22 | `REASON_FOR_REMOVAL_REF` | VARCHAR(40) |  |  | Code value for a text description of the reason a removal was made. |
| 23 | `REASON_FOR_VISIT_TXT` | VARCHAR(255) |  |  | The free text description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 24 | `REFERRAL_TYPE_REF` | VARCHAR(40) |  |  | Referral type. |
| 25 | `REFERRAL_WRITTEN_DT_TM` | DATETIME |  |  | This records the date time when REFERRAL REQUEST for a specific health care service was written into Millennium. |
| 26 | `REFERRER_DOC_PRSNL` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the personnel table. This is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table. |
| 27 | `SERVICE_TYPE_REQUESTED_REF` | VARCHAR(40) |  |  | Service type requested. |
| 28 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 29 | `TREATMENT_FUNCTION_REF` | VARCHAR(40) |  |  | This is the TREATMENT FUNCTION under which the PATIENT is treated. |
| 30 | `UBRN_IDENT` | VARCHAR(12) |  |  | This field contains the unique identifier for UBRN |
| 31 | `UKRWH_CDE_OP_REFERRAL_KEY` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ukrwh cde op referral table. It is an internal system assigned number. |
| 32 | `UKRWH_CDE_PERSON_PATIENT_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde person patient table. It is an internal system assigned number. |
| 33 | `UK_RESIDENT_IND_CD` | DOUBLE |  |  | The status of Patient with regards to whetherthey have been resident in the UK for the past 12 months. |
| 34 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `URGENCY_REF` | VARCHAR(40) |  |  | Code Value for the urgency of patient event on wait list. Example: within 7 days. |
| 40 | `WAITING_END_DT_TM` | DATETIME |  |  | Waiting End Date Time. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_PERSON_PATIENT_KEY` | [UKRWH_CDE_PERSON_PATIENT](UKRWH_CDE_PERSON_PATIENT.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_OP_ATTENDANCE](UKRWH_CDE_OP_ATTENDANCE.md) | `UKRWH_CDE_OP_REFERRAL_KEY` |

