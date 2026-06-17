# UKRWH_CDS_AE_ATTENDANCE

> Contains CDS A&E attendance fields specific to the A&E CDS.

**Description:** UK Reporting Warehouse Commissioning Data Set Accident & Emergency Attendance  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_AE_ATTENDANCE_KEY`  
**Columns:** 62  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AE_STAFF_MEMBER_IDENT` | VARCHAR(3) |  |  | A locally determined code used to identify the person principally responsible for the care of a PATIENT during an Accident And Emergency Attendance. In the majority of cases this will be the person who took responsibility for the discharge of the PATIENT. |
| 2 | `AMBULANCE_CARE_CONTACT_IDENT` | VARCHAR(20) |  |  | An identifier allocated to each Ambulance Incident for each PATIENT. |
| 3 | `AMBULANCE_INCIDENT_IDENT` | VARCHAR(20) |  |  | An Identifierfor each PATIENT TRANSPORT JOURNEY |
| 4 | `ARRIVAL_DT_TM` | DATETIME |  |  | Date and time of patient arrival in A/E |
| 5 | `ARRIVAL_MODE_NHS` | VARCHAR(1) |  |  | Patient arrival mode in A/E |
| 6 | `ATTENDANCE_CATEGORY_NHS` | VARCHAR(1) |  |  | An indication of whether a PATIENT is making first or follow-up attendance at a particular Accident And Emergency Department. |
| 7 | `ATTENDANCE_CONCLUSION_DT_TM` | DATETIME |  |  | The time, recorded using a 24 hour clock, that a PATIENT's Accident And Emergency Attendance concludes or when treatment in Accident and Emergency is completed (whichever is the later). |
| 8 | `ATTENDANCE_CONCLUSION_TM_TXT` | VARCHAR(8) |  |  | The result of a attendance conclusion expressed in text form |
| 9 | `ATTENDANCE_DISPOSAL_NHS` | VARCHAR(2) |  |  | A coding of the ways in which an Accident And Emergency Attendance might end |
| 10 | `ATTENDANCE_NBR_IDENT` | VARCHAR(12) |  |  | A number allocated by an Accident And Emergency Department to provide a unique identifier for each Accident And Emergency Attendance. |
| 11 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) |  |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 12 | `CONVEY_AMB_TRUST_NACS` | VARCHAR(12) |  |  | ORGANISATION CODE (CONVEYING AMBULANCE TRUST) is the code of an Ambulance Service which conveys a PATIENT on a PATIENT TRANSPORT JOURNEY. |
| 13 | `DEPARTMENT_TYPE_NHS` | VARCHAR(2) |  |  | This is used to record the type of Isotope Procedure Department, based on the MAIN SPECIALTY CODE of the head of the DEPARTMENT, or the type of Physiological Measurement Department. |
| 14 | `DEPARTURE_DT_TM` | DATETIME |  |  | Date and time of patient departure from A/E |
| 15 | `DEPARTURE_TM_TXT` | VARCHAR(8) |  |  | A+E DEPARTURE TIME is the time that a PATIENT leaves the Accident And Emergency Department after an Accident And Emergency Attendance has concluded and the department is no longer responsible for the care of the PATIENT. |
| 16 | `EC_ACUITY_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to indicate the acuity of the patient's condition on the emergency care initial assessment date and emergency care initial assessment time. |
| 17 | `EC_ALLOC_TREATMENT_DT_TM` | DATETIME |  |  | The date and time that an Emergency Care Expected Date and Time of Treatment was allocated to the PATIENT. |
| 18 | `EC_ARRIVAL_MODE_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the transport mode by which the patient arrived at the emergency care department. |
| 19 | `EC_ATTENDANCE_CATEGORY_NHS` | VARCHAR(1) |  |  | The category of emergency care attendance. |
| 20 | `EC_ATTENDANCE_SOURCE_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to indicate the source of an emergency care attendance. |
| 21 | `EC_ATTENDANCE_SOURCE_SITE_NACS` | VARCHAR(12) |  |  | Organisation identifier of the organisation site from which a patient arrived at an emergency care department. |
| 22 | `EC_CHIEF_COMPLAINT_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to indicate the nature of the patient¿s chief complaint as assessed by the care professional first assessing the patient. |
| 23 | `EC_CLINCIAL_TRAIL_IDENT` | VARCHAR(20) |  |  | The clinical trial identifier must be recognised and registered with an organisation which is a primary registry in the world health organisation international clinical trials registry platform. |
| 24 | `EC_CLIN_RDY_TO_PRCED_DT_TM` | DATETIME |  |  | The first date and time that the CARE PROFESSIONAL, authorised to discharge the PATIENT from the Emergency Care Department, makes a clinical decision that the PATIENT no longer requires ongoing care in the Emergency Care Department. |
| 25 | `EC_DECIDED_TO_ADMIT_DT_TM` | DATETIME |  |  | Local date time of decided to admit date time. |
| 26 | `EC_DEPARTMENT_TYPE_NHS` | VARCHAR(2) |  |  | The type of emergency care department. |
| 27 | `EC_DISCHARGE_DESTINATION_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the intended destination of the patient following discharge from the emergency care department. |
| 28 | `EC_DISCHARGE_FOLLOW_UP_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the service to which a patient was referred for continuing care following an emergency care attendance. |
| 29 | `EC_DISCHARGE_INFO_GIVEN_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify whether a copy of a letter to their general practitioner has been printed and given to the patient on discharge from an emergency care department. |
| 30 | `EC_DISCHARGE_STATUS_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used indicate the status of the patient on discharge from an emergency care department. |
| 31 | `EC_DISEASE_OUTBREAK_NOTI` | VARCHAR(20) |  |  | Disease outbreak notification is to support collection of nationally-notifiable data relating to outbreaks of disease which are identified in emergency care departments. Where a SNOMED CT code is available, the disease outbreak notification field should contain this. If a SNOMED CT code is not available, then it is permissible to submit free-text detail of the disease. |
| 32 | `EC_DISEASE_OUTBREAK_NOTI_DESC` | VARCHAR(100) |  |  | The SNOMED CT concept ID describing nationally-notifiable outbreaks of disease. |
| 33 | `EC_DISEASE_OUTBREAK_NOTI_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID describing nationally-notifiable outbreaks of disease. |
| 34 | `EC_DTA_ACT_TREAT_FUN_CD_NHS` | VARCHAR(3) |  |  | The treatment function code of the service to which a patient is to be admitted. |
| 35 | `EC_EXP_TREATMENT_DT_TM` | DATETIME |  |  | Expected date and time of Emergency Care treatment. |
| 36 | `EC_SITE_CODE_OF_DISCHARGE_NACS` | VARCHAR(12) |  |  | The organisation identifier of the organisation site to which a patient is discharged following an emergency care attendance. |
| 37 | `ETHNIC_CATEGORY_2021_NHS` | VARCHAR(3) |  |  | The ethnicity of a PERSON, as specified by the PERSON using classification code used for the 2021 census. |
| 38 | `ETHNIC_CATEGORY_NHS` | VARCHAR(2) |  |  | The ethnicity of a PERSON, as specified by the PERSON |
| 39 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 40 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 41 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 42 | `INCIDENT_LOCATION_TYPE_NHS` | VARCHAR(2) |  |  | The type of physical LOCATION where PATIENTS are seen or where SERVICES are provided or from which requests for services are sent. |
| 43 | `INITIAL_ASSESSMENT_DT_TM` | DATETIME |  |  | Date and time of Initial assessment |
| 44 | `INITIAL_ASSESSMENT_TM_TXT` | VARCHAR(8) |  |  | The time when the patient had their initial assessment in A&E |
| 45 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 46 | `LOC_EC_ALLOC_TREATMENT_DT_TM` | DATETIME |  |  | The local date and time that an Emergency Care Expected Date and Time of Treatment was allocated to the PATIENT. |
| 47 | `LOC_EC_CLIN_RDY_TO_PRCED_DT_TM` | DATETIME |  |  | The first local date and time that the CARE PROFESSIONAL, authorised to discharge the PATIENT from the Emergency Care Department, makes a clinical decision that the PATIENT no longer requires ongoing care in the Emergency Care Department. |
| 48 | `LOC_EC_DECIDED_TO_ADMIT_DT_TM` | DATETIME |  |  | Local date time of decided to admit date time. |
| 49 | `LOC_EC_EXP_TREATMENT_DT_TM` | DATETIME |  |  | Expected local date and time of Emergency Care treatment. |
| 50 | `PATIENT_GRP_NHS` | VARCHAR(2) |  |  | The patient's group as perceived by the clinician and recorded as part of the Dataset. |
| 51 | `SEEN_FOR_TREATMENT_DT_TM` | DATETIME |  |  | Date and time when the patient was seen for treatment |
| 52 | `SEEN_FOR_TREATMENT_TM_TXT` | VARCHAR(8) |  |  | The time when the patient was seen for treatment in A&E |
| 53 | `SITE_CODE_OF_TREAT_NACS` | VARCHAR(12) |  |  | SITE CODE (OF TREATMENT) is the ORGANISATION SITE CODE of the ORGANISATION where the PATIENT was treated |
| 54 | `SOURCE_OF_REFERRAL_NHS` | VARCHAR(2) |  |  | A CLASSIFICATION which identifies the source of referral of each Accident And Emergency Episode. |
| 55 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 56 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL | PK | The event action identifier on the SCH_EVENT_ACTION table of the A/E attendance |
| 57 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 58 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 59 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_AE_ATTENDANCE](UKRWH_CDE_AE_ATTENDANCE.md) | `UKRWH_CDS_AE_ATTENDANCE_KEY` |
| [UKRWH_CDS_AE_INVESTIGATION](UKRWH_CDS_AE_INVESTIGATION.md) | `UKRWH_CDS_AE_ATTENDANCE_KEY` |
| [UKRWH_CDS_AE_TREATMENT](UKRWH_CDS_AE_TREATMENT.md) | `UKRWH_CDS_AE_ATTENDANCE_KEY` |

