# UKRWH_CDE_AE_ATTENDANCE

> Contains additional attendance level details relating to an A&E CDS Event.

**Description:** UK Reporting Warehouse Cons Data Extract Accident and Emergency Attendance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 63

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCIDENT_DT_TM` | DATETIME |  |  | The date and time the accident occurred. |
| 2 | `ACCIDENT_REF` | VARCHAR(40) |  |  | Identifies the general type of accident (I.e., auto, work related, etc.) |
| 3 | `ADMIT_SOURCE_REF` | VARCHAR(40) |  |  | Admit source identifies the place from which the patient came before being admitted. (i.e., transfer from another hospital) |
| 4 | `AE_OBS_PATIENT_IND` | DOUBLE |  |  | An indication as to whether the patient is under observation in A&E |
| 5 | `AMBULANCE_NBR_TXT` | VARCHAR(20) |  |  | The service number related to the ambulance visit |
| 6 | `ARRIVAL_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the patient will arrive at the facility. This field may be null. |
| 7 | `ARRIVAL_MODE_REF` | VARCHAR(40) |  |  | Information regarding the arrival of the ambulance |
| 8 | `ATTENDANCE_CATEGORY_REF` | VARCHAR(40) |  |  | Description of the encounter readmit. |
| 9 | `ATTENDANCE_DISPOSAL_REF` | VARCHAR(40) |  |  | The location to which the patient was discharged such as another hospital or nursing home. |
| 10 | `ATTEND_DOC_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the physician attending the patient in A&E |
| 11 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 12 | `CHECKIN_DT_TM` | DATETIME |  |  | Date and time the tracking item was checked into the tracking group. |
| 13 | `CHECKOUT_DT_TM` | DATETIME |  |  | Date and time the tracking item was checked out of the tracking group. |
| 14 | `CONCLUSION_DT_TM` | DATETIME |  |  | The data time of the A&E attendance conclusion. |
| 15 | `DECISION_TO_ADMIT_DT_TM` | DATETIME |  |  | Date and Time that the Decision To Admit Tracking Event was requested. |
| 16 | `DEPARTURE_DT_TM` | DATETIME |  |  | A+E DEPARTURE TIME is the time that a PATIENT leaves the Accident And Emergency Department after an Accident And Emergency Attendance has concluded and the department is no longer responsible for the care of the PATIENT. |
| 17 | `DEPART_DT_TM` | DATETIME |  |  | A+E DEPARTURE TIME is the time that a PATIENT leaves the Accident And Emergency Department after an Accident And Emergency Attendance has concluded and the department is no longer responsible for the care of the PATIENT. |
| 18 | `DISCHARGE_DISPOSITION_REF` | VARCHAR(40) |  |  | The conditions under which the patient left the facility at the time of discharge. |
| 19 | `DISCHARGE_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the personnel that discharges the patient |
| 20 | `DISCH_DT_TM` | DATETIME |  |  | The actual date/time that the patient was discharged from the facility. For most outpatients, this column may be null unless the user process requires capturing this data, for example, day surgery. Auto discharge will populate this column. This also may or may not be a system assigned date and time depending on the discharge process used. |
| 21 | `ENCNTR_ACTIVE_IND` | DOUBLE |  |  | The Millennium encounter table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 22 | `ENCNTR_CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the encounter table. |
| 23 | `ENCNTR_CREATE_PRSNL` | VARCHAR(40) |  |  | This is the person responsible for creating a row in the encounter table. |
| 24 | `ENCNTR_LAST_UPDT_DT_TM` | DATETIME |  |  | Date Time on which the assoicited Millennium Encounter was last Updated |
| 25 | `ENCNTR_UPDT_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the encounter table. |
| 26 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 27 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 28 | `FIRST_ASSESSMENT_DT_TM` | DATETIME |  |  | Date and time the Assessment Tracking Event was completed. |
| 29 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 30 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 31 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 32 | `INCIDENT_LOCATION_REF` | VARCHAR(40) |  |  | Place of the accident (ex. Client s or Patient s Home Health Center Hospice Group Home etc.) |
| 33 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 34 | `LOC_ARRIVAL_DT_TM` | DATETIME |  |  | The date and time related to the ambulance visit. |
| 35 | `LOC_BED_REF` | VARCHAR(40) |  |  | This field is the current patient location with a location type of bed. |
| 36 | `LOC_BUILDING_REF` | VARCHAR(40) |  |  | This field is the current patient location with a location type of building. |
| 37 | `LOC_CONCLUSION_DT_TM` | DATETIME |  |  | The data time of the a&e attendance conclusion. |
| 38 | `LOC_DECISION_TO_ADMIT_DT_TM` | DATETIME |  |  | The date and time that the decision to admit tracking event was requested. |
| 39 | `LOC_DEPARTURE_DT_TM` | DATETIME |  |  | The a+e departure time is the time that a patient leaves the accident and emergency department after an accident and emergency attendance has concluded and the department is no longer responsible for the care of the patient. |
| 40 | `LOC_FACILITY_REF` | VARCHAR(40) |  |  | This field is the current patient location with a location type of facility. |
| 41 | `LOC_NURSE_UNIT_REF` | VARCHAR(40) |  |  | This field is the current patient location with a location type of building. |
| 42 | `LOC_ROOM_REF` | VARCHAR(40) |  |  | This field is the current patient location with a location type of room. |
| 43 | `MIGRATED_IND` | DOUBLE |  |  | Derived formt her encountercontributor_system_cd. Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 44 | `ORGANIZATION_SK` | VARCHAR(40) |  |  | It is the uniqueIdentifier of an entity whose activities encompass the funding or provision of health care and support services. |
| 45 | `PERSON_SK` | VARCHAR(40) | NOT NULL |  | This is the value of the unique primary identifier of the Millennium person table. It is an internal system assigned number. |
| 46 | `REASON_FOR_VISIT_TXT` | VARCHAR(255) |  |  | The free text description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 47 | `REGISTERING_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the personnel that performed the registration or admission. If the reg_dt_tm is valued then this field must be valued. |
| 48 | `REG_DT_TM` | DATETIME |  |  | The date/time that the registration or admission process was performed. If the pre_reg_dt_tm is valued then this field may be null but will be valued when the patient presents for their visit/appointment. |
| 49 | `SOURCE_OF_REFERRAL_REF` | VARCHAR(40) |  |  | Admit mode identifies the method by which the patient arrived. (i.e. helicopter ambulance etc.) |
| 50 | `STREAM_REF` | VARCHAR(40) |  |  | It is the code for the Stream to which the patients are allocated according to their needs. |
| 51 | `TETANUS_RESULT_VAL_TXT` | VARCHAR(255) |  |  | This field contains the results for the Tetanus |
| 52 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 53 | `TRACKING_GROUP_REF` | VARCHAR(40) |  |  | Tracking Group Code used to identify which tracking group this patient is currently checked into. |
| 54 | `TREATMENT_START_DT_TM` | DATETIME |  |  | Date and time the Treatment Start Tracking Event was completed. |
| 55 | `UKRWH_CDE_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde ae attendance table. It is an internal system assigned number. |
| 56 | `UKRWH_CDE_PERSON_PATIENT_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde person patient table. It is an internal system assigned number. |
| 57 | `UKRWH_CDS_AE_ATTENDANCE` | DOUBLE | NOT NULL |  | tbd, think this attribute must be a mistake |
| 58 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde ae attendance table. It is an internal system assigned number. |
| 59 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 60 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_PERSON_PATIENT_KEY` | [UKRWH_CDE_PERSON_PATIENT](UKRWH_CDE_PERSON_PATIENT.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |
| `UKRWH_CDS_AE_ATTENDANCE_KEY` | [UKRWH_CDS_AE_ATTENDANCE](UKRWH_CDS_AE_ATTENDANCE.md) | `UKRWH_CDS_AE_ATTENDANCE_KEY` |

