# UKRWH_CDS_OP_ATTENDANCE

> Contains CDS Outpatient details relating to an Outpatient CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Outpatient Attendance  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_OP_ATTENDANCE_KEY`  
**Columns:** 35  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_LOC_TYPE_NHS` | VARCHAR(3) |  |  | The type of LOCATION for an ACTIVITY |
| 2 | `ATTENDANCE_DT_TM` | DATETIME |  |  | The date of an attendance, for example at a Consultant Clinic, Nurse Clinic, Accident And Emergency Department or by a Ward Attender. |
| 3 | `ATTENDANCE_IDENT` | VARCHAR(12) |  |  | The ACTIVITY IDENTIFIER for the attendance. A sequential number or time of day used to enable an attendance to be uniquely identified. |
| 4 | `ATTENDED_NHS` | VARCHAR(1) |  |  | This indicates whether or not an APPOINTMENT for a CARE CONTACT took place. If the APPOINTMENT did not take place it also indicates whether or not advanced warning was given. |
| 5 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 6 | `CLINIC_NHS` | VARCHAR(12) |  |  | An identifier for a CLINIC OR FACILITY |
| 7 | `CONSULTATION_MEDIUM_USED_NHS` | VARCHAR(2) |  |  | "CONSULTATION MEDIUM USED identifies the communication mechanism used to relay information between the CARE PROFESSIONAL and the PERSON who is the subject of the consultation, during a CARE ACTIVITY." |
| 8 | `EARLIEST_CLIN_APPROP_DT_TM` | DATETIME |  |  | The earliest DATE that it was clinically appropriate for an ACTIVITY to take place. |
| 9 | `EARLIEST_RSNBL_OFFER_DT_TM` | DATETIME |  |  | It is the date of the earliest of the Reasonable Offers made to a PATIENT for an APPOINTMENT or Elective Admission. It should only be included on the Commissioning Data Sets where the PATIENT has declined at least two Reasonable Offers. |
| 10 | `EXPECTED_DUR_OF_APPT` | DOUBLE |  |  | The expected duration in minutes of an APPOINTMENT when booked, prior to the attendance of the PATIENT. |
| 11 | `FIRST_ATTENDANCE_NHS` | VARCHAR(1) |  |  | This indicates whether a PATIENT is making a first attendance or contact; or a follow-up attendance or contact. |
| 12 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 13 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 14 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 15 | `LAST_DNA_CANCELLED_DT_TM` | DATETIME |  |  | The DATE recorded when PATIENTS who have been offered a date for admission have missed this admission date with or without advance notice. |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 17 | `LOCATION_CLASS_NHS` | VARCHAR(2) |  |  | A classification for use within CDS messages of the physical location within which the recorded patient event occurs. |
| 18 | `MEDICAL_STAFF_TYPE_NHS` | VARCHAR(2) |  |  | A classification of the type of care professional staff dealing with the PATIENT during an Out-Patient Attendance Consultant or Nurse or Midwife Contact. |
| 19 | `MULTI_PROFESS_OR_MCIC_NHS` | VARCHAR(1) |  |  | An indication of whether a PATIENT was seen by a single or multiple CARE PROFESSIONALS during an Clinic Attendance Consultant or Clinic Attendance Non-Consultant, recorded for the purposes of Payment by Results. |
| 20 | `OPERATION_STATUS_NHS` | VARCHAR(1) |  |  | OPERATION STATUS should be used once for each record to record states of knowledge regarding the operative procedure. |
| 21 | `OUTCOME_OF_ATTENDANCE_NHS` | VARCHAR(1) |  |  | This records the outcome of an Out-Patient Attendance Consultant. |
| 22 | `PRIORITY_TYPE_NHS` | VARCHAR(1) |  |  | This is the priority of a request for services; in the case of services to be provided by a CONSULTANT, it is as assessed by or on behalf of the CONSULTANT. |
| 23 | `REFERRAL_REQUEST_RCVD_DT_TM` | DATETIME |  |  | This records the date the REFERRAL REQUEST was received by the Health Care Provider. |
| 24 | `REFERRAL_SOURCE_NHS` | VARCHAR(2) |  |  | A CLASSIFICATION which is used to identify the source of referral of each Consultant Out-Patient Episode. |
| 25 | `REHAB_ASSESS_TEAM_TYPE_NHS` | VARCHAR(1) |  |  | An indication of whether the CARE PROFESSIONAL TEAM undertaking a Rehabilitation Assessment, is specialised or non-specialised. This information is recorded for the purposes of Payment by Results. |
| 26 | `SERVICE_REQUESTED_TYPE_NHS` | VARCHAR(1) |  |  | A request for the provision of care services to a PATIENT. |
| 27 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 28 | `TREATMENT_SITE_NACS` | VARCHAR(12) |  |  | SITE CODE (OF TREATMENT) is the ORGANISATION SITE CODE for the ORGANISATION SITE where the PATIENT was treated. |
| 29 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 30 | `UKRWH_CDS_OP_ATTENDANCE_KEY` | DOUBLE | NOT NULL | PK | The ACTIVITY IDENTIFIER for the OP attendance. |
| 31 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_OP_ATTENDANCE](UKRWH_CDE_OP_ATTENDANCE.md) | `UKRWH_CDS_OP_ATTENDANCE_KEY` |

