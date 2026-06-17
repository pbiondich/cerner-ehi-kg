# ENCOUNTER

> The encounter table contains patient information for a specific period of time that a person comes in contact with a healthcare provider (i.e., inpatient hospital stay, outpatient clinic visit, office visit, phone call to the doctor, etc.).

**Description:** Encounter  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_ID`  
**Columns:** 159  
**Referenced by:** 425 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_STATUS_CD` | DOUBLE | NOT NULL |  | Tracks the current ABN status for the encounter. |
| 2 | `ACCIDENT_RELATED_IND` | DOUBLE |  |  | The information indicating if the patient's visit is related to an accident. |
| 3 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) |
| 4 | `ACCOMMODATION_REASON_CD` | DOUBLE | NOT NULL |  | Describes why the accommodation the patient received was given. (e.g. Doctor requested, patient requested) |
| 5 | `ACCOMMODATION_REQUEST_CD` | DOUBLE | NOT NULL |  | Describes the accommodation that was requested, either by the patient or a staff member. This value may differ from the actual accommodation that the patient/encounter was given. For example, the patient may request a private room, but only receive a semi-private room because no private beds were available. |
| 6 | `ACCOMP_BY_CD` | DOUBLE | NOT NULL |  | Describes who the patient was with at the time of registration. (e.g. friend, spouse, parent, etc.) |
| 7 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 9 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 10 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 11 | `ADMINISTRATIVE_PROBLEM_CD` | DOUBLE |  |  | Indicates the chronic condition that is being treated for this encounter from an administrative perspective. |
| 12 | `ADMIT_DECISION_DT_TM` | DATETIME |  |  | The date and time that the decision to admit the patient to the facility is made. |
| 13 | `ADMIT_EARLY_IND` | DOUBLE | NOT NULL |  | Indicates if the patient's admission qualified under the early admission rules of the facility. |
| 14 | `ADMIT_MODE_CD` | DOUBLE | NOT NULL |  | Admit mode identifies the method by which the patient arrived. (i.e., helicopter, ambulance, etc.) |
| 15 | `ADMIT_SRC_CD` | DOUBLE | NOT NULL |  | Admit source identifies the place from which the patient came before being admitted. (i.e., transfer from another hospital) |
| 16 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Admit type indicates the circumstance under which the patient was admitted or will be admitted. (i.e., accident, emergent, routine, elective, labor/delivery, etc.) |
| 17 | `ADMIT_WITH_MEDICATION_CD` | DOUBLE | NOT NULL |  | Admit with medication describes that the patient brought their own medication with them when admitted. |
| 18 | `ALC_DECOMP_DT_TM` | DATETIME |  |  | Date and time the alternate level of care decompensation |
| 19 | `ALC_REASON_CD` | DOUBLE | NOT NULL |  | Reason the alternate level of care is being assigned or changed |
| 20 | `ALT_LVL_CARE_CD` | DOUBLE | NOT NULL |  | Level of care for the encounter that signals a difference, or alternative, to the care signified by the encntr_type, med service, location, or combination therein. Used primarily as a billing function to trigger a change in charging rates. |
| 21 | `ALT_LVL_CARE_DT_TM` | DATETIME |  |  | The date and time the alternate level of care was assigned |
| 22 | `ALT_RESULT_DEST_CD` | DOUBLE | NOT NULL |  | NOT USED. |
| 23 | `AMBULATORY_COND_CD` | DOUBLE | NOT NULL |  | Ambulatory condition describes the general physical condition, impairment, or limitation of the patient upon arrival. |
| 24 | `ARCHIVE_DT_TM_ACT` | DATETIME | NOT NULL |  | The actual date/time when the encounter was archived. |
| 25 | `ARCHIVE_DT_TM_EST` | DATETIME | NOT NULL |  | The estimated date when the encounter will be archived. This date is calculated based on client-defined archive criteria. |
| 26 | `ARRIVE_DT_TM` | DATETIME |  |  | The actual date/time that the patient arrived at the facility. At the time of registration, if this field is null then it should be valued with the reg_dt_tm. Otherwise, the actual arrival date/time is captured. |
| 27 | `ASSIGN_TO_LOC_DT_TM` | DATETIME |  |  | Date and time that the encounter was assigned to a location. |
| 28 | `BBD_PROCEDURE_CD` | DOUBLE | NOT NULL |  | Encounter (patient) was a blood blank donor and this lists the type of procedure performed on them. |
| 29 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 30 | `BIRTH_DT_CD` | DOUBLE | NOT NULL |  | Birth date code indicates the kind of birth date and time value that is contained in the birth_dt_tm field. This field will be null where the field encntr_class_cd indicates that this encounter row references a row in the person table. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 31 | `BIRTH_DT_TM` | DATETIME |  |  | The date and time of birth for the person or thing for which the encounter is being created. This field will be null where the field encntr_class_cd indicates that this encounter row references a row in the person table. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 32 | `CHART_ACCESS_ORGANIZATION_ID` | DOUBLE |  | FK→ | The identifying information of the organization (real or virtual) that indicates which groups of users should have medical chart access to the encounter. |
| 33 | `CHART_COMPLETE_DT_TM` | DATETIME |  |  | Date/time when the chart is complete for the encounter. |
| 34 | `CLERGY_VISIT_CD` | DOUBLE | NOT NULL |  | Indicates if the patient has requested a clergy visit. |
| 35 | `CLIENT_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the organization financially responsible for the encounter (e.g. an employer paying for an employee's drug test). |
| 36 | `CLIENT_REFERENCE_NBR_TXT` | VARCHAR(50) |  |  | Indicates the number assigned to the encounter for tracking purposes by an external organization that is financially responsible for the encounter. |
| 37 | `COMPLETE_REG_DT_TM` | DATETIME |  |  | The date/time that all required financial and clinical data collection necessary for registration has been completed. |
| 38 | `COMPLETE_REG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The internal person id of the personnel that completed the collection of all required financial and clinical data necessary for registration. if the complete_reg_dt_tm is valued, then this field should be valued. |
| 39 | `CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | Confidential level identifies a level of security that may restrict access or release of information. |
| 40 | `CONTRACT_STATUS_CD` | DOUBLE | NOT NULL |  | Codified field indicating status of a care contract. |
| 41 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 42 | `COURTESY_CD` | DOUBLE | NOT NULL |  | This field indicates whether the patient will be extended certain special courtesies such as express discharge, bypassing a stop at the cashiers window upon leaving when financial arrangements are agreed upon in advance. |
| 43 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the encounter table. |
| 44 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person responsible for creating a row in the encounter table. |
| 45 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 46 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 47 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 48 | `DEPART_DT_TM` | DATETIME |  |  | The actual date/time that the patient left from the facility. In many cases, this field may be null unless the user process requires capturing this data. |
| 49 | `DIET_TYPE_CD` | DOUBLE | NOT NULL |  | Diet type is used to indicate that the patient is on a special diet. |
| 50 | `DISCH_DISPOSITION_CD` | DOUBLE | NOT NULL |  | The conditions under which the patient left the facility at the time of discharge. |
| 51 | `DISCH_DT_TM` | DATETIME |  |  | The actual date/time that the patient was discharged from the facility. For most outpatients, this column may be null unless the user process requires capturing this data, for example, day surgery. Auto discharge will populate this column. This also may or may not be a system assigned date and time depending on the discharge process used. |
| 52 | `DISCH_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The internal person identifier of the personnel that performed the discharge process. If the disch_dt_tm is valued, then this field must be valued. |
| 53 | `DISCH_TO_LOCTN_CD` | DOUBLE | NOT NULL |  | The location to which the patient was discharged such as another hospital or nursing home. |
| 54 | `DOC_RCVD_DT_TM` | DATETIME |  |  | Date and Time documents were received for the encounter |
| 55 | `ED_REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | Indicates the source of referral for the visit to the emergency department. |
| 56 | `ENCNTR_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter class defines how this encounter row is being used in relation to the person table. |
| 57 | `ENCNTR_COMPLETE_DT_TM` | DATETIME | NOT NULL |  | Date/time when the encounter is considered to be in a completed status. |
| 58 | `ENCNTR_FINANCIAL_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter financial table. It is an internal system assigned number. |
| 59 | `ENCNTR_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the Encounter table. |
| 60 | `ENCNTR_STATUS_CD` | DOUBLE | NOT NULL |  | Encounter status identifies the state of a particular encounter type from the time it is initiated until it is complete. (i.e., temporary, preliminary, active, discharged (complete), cancelled). |
| 61 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 62 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this codeset all have Cerner defined meanings. |
| 63 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 64 | `EST_ARRIVE_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the patient will arrive at the facility. This field may be null. |
| 65 | `EST_DEPART_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the patient will depart (outpatient) or will be discharged (inpatient) from the facility. This field may be null. |
| 66 | `EST_FINANCIAL_RESP_AMT` | DOUBLE |  |  | Contains the estimated amount for which the patient is responsible for this encounter. |
| 67 | `EST_LENGTH_OF_STAY` | DOUBLE |  |  | Estimated length of the patient/encounter stay, in days |
| 68 | `EXPECTED_DELIVERY_DT_TM` | DATETIME |  |  | The date and time the delivery is expected. |
| 69 | `EXTERNAL_IND` | DOUBLE | NOT NULL |  | Set to true (1), if the encounter is external to the hospital network. Otherwise, set to false (0). |
| 70 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for a given encounter. Examples may include Worker's Comp, Self Pay, etc. |
| 71 | `GUARANTOR_TYPE_CD` | DOUBLE | NOT NULL |  | The guarantor type indicates that the guarantor for the encounter is either a person or an organization. This code is used to determine which set of tables to query to find the guarantor. |
| 72 | `INCIDENT_CD` | DOUBLE | NOT NULL |  | Indicates the incident or disaster that led to the patient's visit. |
| 73 | `INFO_GIVEN_BY` | CHAR(100) |  |  | Free-text attribute specifying who gave the information for this encounter. Might be a guardian, parent, patient, etc. |
| 74 | `INITIAL_CONTACT_DT_TM` | DATETIME |  |  | The initial contact of the patient and the provider submitting the claim. |
| 75 | `INPATIENT_ADMIT_DT_TM` | DATETIME |  |  | Stores the inpatient admit date and time |
| 76 | `ISOLATION_CD` | DOUBLE | NOT NULL |  | The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 77 | `KIOSK_QUEUE_NBR_DT_TM` | DATETIME |  |  | The date and time when the system generated ticket number representing their position within the queue was assigned to the patient when they are checking in for the visit. |
| 78 | `KIOSK_QUEUE_NBR_TXT` | VARCHAR(50) |  |  | The system generated ticket number assigned to the patient to represent their position within the queue when they are checking in for the visit. |
| 79 | `LAST_MENSTRUAL_PERIOD_DT_TM` | DATETIME |  |  | The date and time of the last menstrual period. |
| 80 | `LEVEL_OF_SERVICE_CD` | DOUBLE | NOT NULL |  | The level of service provided. Examples are emergency, elective, urgent and routine. |
| 81 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 82 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of bed. |
| 83 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of building. |
| 84 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of facility. |
| 85 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of nurse unit. |
| 86 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of room. |
| 87 | `LOC_TEMP_CD` | DOUBLE | NOT NULL |  | This field identifies the temporary location of the patient. The temporary location may be valued at the same time the location_cd is valued. |
| 88 | `LODGER_CD` | DOUBLE | NOT NULL |  | Indicates if an additional person is staying with the patient in the same room. |
| 89 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 90 | `MENTAL_CATEGORY_CD` | DOUBLE | NOT NULL |  | Mental category code (ex. Mental illness, Mental impairment, severe mental impairment) |
| 91 | `MENTAL_HEALTH_CD` | DOUBLE | NOT NULL |  | The field is the mental health status of a patient which indicates if a patient was involuntarily or voluntarily admitted. This field is not used by all clients. |
| 92 | `MENTAL_HEALTH_DT_TM` | DATETIME |  |  | The date and time of the last time the mental health info was updated. |
| 93 | `MILITARY_SERVICE_RELATED_CD` | DOUBLE | NOT NULL |  | Indicates if the patient's visit is related to their military service. |
| 94 | `NAME_FIRST` | VARCHAR(200) |  |  | OBSOLETE - This is the person's first given name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 95 | `NAME_FIRST_KEY` | VARCHAR(200) |  |  | OBSOLETE - This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 96 | `NAME_FIRST_SYNONYM_ID` | DOUBLE | NOT NULL |  | OBSOLETE - This is the value of the unique primary identifier of the first name synonym table. It is an internal system assigned number. It is used to when searching for a person where other first names would be considered as a match. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 97 | `NAME_FULL_FORMATTED` | VARCHAR(200) |  |  | OBSOLETE - This is the complete person name including punctuation and formatting. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 98 | `NAME_LAST` | VARCHAR(200) |  |  | OBSOLETE - This is the person's family name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 99 | `NAME_LAST_KEY` | VARCHAR(200) |  |  | OBSOLETE - This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 100 | `NAME_PHONETIC` | VARCHAR(200) |  |  | OBSOLETE - This is the Soundex coded representation of the person's name. This field is used for indexing and searching for a patient by name when the exact spelling is not known. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 101 | `ONSET_DT_TM` | DATETIME |  |  | The date and time of the onset of current symptoms. |
| 102 | `ORDER_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the order (i.e. electronic, scanned, faxed by physician, faxed by patient, etc.) |
| 103 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. This column is either valued with the facility or the client organization for the encounter. |
| 104 | `OVRD_AUTOMTC_CVRG_PRTZTN_IND` | DOUBLE |  |  | Indicates if the automatic coverage prioritization processing was overridden by the user to maintain the manually entered coverage priority sequencing. |
| 105 | `PARENT_RET_CRITERIA_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This column is no longer used. This column indicates which set of retention criteria was last applied to the encounter to calculate the value in the archive_dt_tm_est column. ** Obsolete ** |
| 106 | `PATIENT_CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | Patient classification code (ex. Ordinary admission, day case admission, regular day, regular night) |
| 107 | `PAYMENT_COLLECTION_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the payment collection (i.e. 1st attempt - left message, payment in full received, unable to pay - proceed with service, etc.) |
| 108 | `PA_CURRENT_STATUS_CD` | DOUBLE | NOT NULL |  | This column shows the last action that was performed on the encounter in relation to the purge/archive process. |
| 109 | `PA_CURRENT_STATUS_DT_TM` | DATETIME |  |  | Date/time of last purge/archive action taken on the encounter. |
| 110 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person whom this encounter is for. |
| 111 | `PERSON_PLAN_PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of health insurance profile to be used for the encounter (i.e., professional, institutional, workmen's comp). |
| 112 | `PLACEMENT_AUTH_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the personnel who authorized the override of a patient placement into a location that had a "stop" attribute associated to it. |
| 113 | `PLACE_OF_SVC_ADMIT_DT_TM` | DATETIME |  |  | The date and time of admission to the place of service organization. |
| 114 | `PLACE_OF_SVC_ORG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the place of service organization for the encounter. |
| 115 | `PLACE_OF_SVC_TYPE_CD` | DOUBLE | NOT NULL |  | Code to identify the type of service performed at the place of service organization for the encounter. |
| 116 | `PREADMIT_NBR` | VARCHAR(100) |  |  | The number assigned to a pre-admit encounter. A pre-admit encounter is not required to have a pre-admit number |
| 117 | `PREADMIT_TESTING_CD` | DOUBLE | NOT NULL |  | Indicates that the patient must have pre-admission testing done in order to be admitted. |
| 118 | `PREGNANCY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the pregnancy. |
| 119 | `PRE_REG_DT_TM` | DATETIME |  |  | The date/time that the pre-registration or pre-admission process was performed. If the reg_dt_tm is valued, or no pre-registration occurred, then this field may be null. |
| 120 | `PRE_REG_PRSNL_ID` | DOUBLE | NOT NULL |  | The internal person ID of the personnel that performed the pre-registration or pre-admission. If the pre_reg_dt_tm is valued, then this field must be valued. |
| 121 | `PROGRAM_SERVICE_CD` | DOUBLE | NOT NULL |  | Represents the program service associated with the patient's location |
| 122 | `PSYCHIATRIC_STATUS_CD` | DOUBLE | NOT NULL |  | Psychiatric status code (ex. One or more previous, not known, not applicable) |
| 123 | `PURGE_DT_TM_ACT` | DATETIME |  |  | The actual date/time when data for the encounter was purged from the database. |
| 124 | `PURGE_DT_TM_EST` | DATETIME |  |  | The estimated date/time when data for the encounter will be purged from the database. |
| 125 | `READMIT_CD` | DOUBLE | NOT NULL |  | Description of the encounter readmit. |
| 126 | `REASON_FOR_VISIT` | VARCHAR(255) |  |  | The free text description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 127 | `REFERRAL_RCVD_DT_TM` | DATETIME |  |  | The date and time the referral was received |
| 128 | `REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | The information indicating the source of referral like provider, friend, web-site, etc. |
| 129 | `REFERRING_COMMENT` | VARCHAR(100) |  |  | A text field containing the comments from the referring physician or service. |
| 130 | `REFER_FACILITY_CD` | DOUBLE | NOT NULL |  | The location of the referring facility. This code set is used at sites that do not have full referral management integration. |
| 131 | `REFER_TO_UNIT_STAFF_CD` | DOUBLE | NOT NULL |  | Indicates if any inquiries regarding the patient need to be redirected to a unit staff member. |
| 132 | `REGION_CD` | DOUBLE | NOT NULL |  | A codified field which indicates the area or region which the encounter was referred. |
| 133 | `REG_DT_TM` | DATETIME |  |  | The date/time that the registration or admission process was performed. In some circumstances this may only involve a minimal amount of data collection to simply get the encounter added to the system for clinical purposes.if the pre_reg_dt_tm is valued, then this field may be null, but will be valued when the patient presents for their visit/appointment. |
| 134 | `REG_PRSNL_ID` | DOUBLE | NOT NULL |  | The internal person ID of the personnel that performed the registration or admission. If the reg_dt_tm is valued, then this field must be valued. |
| 135 | `RESULT_ACCUMULATION_DT_TM` | DATETIME |  |  | Reference date for an encounter that determines the starting point when printing a patient's chart |
| 136 | `RESULT_DEST_CD` | DOUBLE | NOT NULL |  | NOT USED. |
| 137 | `SAFEKEEPING_CD` | DOUBLE | NOT NULL |  | Where or how valuables are being stored. |
| 138 | `SECURITY_ACCESS_CD` | DOUBLE | NOT NULL |  | Security Access Code value. |
| 139 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving for this encounter. |
| 140 | `SERVICE_DT_TM` | DATETIME |  |  | The start or if in the future the anticipated start date of service for the encounter. The service date time is determined per the following date availability: Arrival date/time, Registration date/time, Estimated arrival date/time, and Pre-Registration date/time. |
| 141 | `SERVICE_PROVIDER_ORG_ID` | DOUBLE |  | FK→ | The identifier of the organization (real or virtual) that is primarily responsible for the encounter (owner of the information). |
| 142 | `SEX_CD` | DOUBLE | NOT NULL |  | The gender of the patient (i.e., male, female, unknown). This field will be null where the field encntr_class_cd indicates that this encounter row references a row in the person table. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 143 | `SITTER_REQUIRED_CD` | DOUBLE | NOT NULL |  | A codified field that indicates whether a Personnel is required to sit with the encounter |
| 144 | `SPECIALTY_UNIT_CD` | DOUBLE | NOT NULL |  | The specialty unit associated with the program service |
| 145 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A fundamental category of taxonomic classification, ranking after a genus and consisting of organisms capable of interbreeding. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 146 | `TRAUMA_CD` | DOUBLE | NOT NULL |  | Type of trauma related to this encounter. |
| 147 | `TRAUMA_DT_TM` | DATETIME |  |  | Date and time the trauma related incident occurred. |
| 148 | `TREATMENT_PHASE_CD` | DOUBLE | NOT NULL |  | Treatment phase (Code Set: 4018002) identifies the current stage of a unit that the encounter is in (i.e. phase 1, phase 2, entry, intermediate). Used to describe the different levels of care as the encounter progresses. A common use would be behavioral health scenarios. |
| 149 | `TRIAGE_CD` | DOUBLE | NOT NULL |  | Describes the triage performed on, or related to, this encounter. |
| 150 | `TRIAGE_DT_TM` | DATETIME |  |  | Date and time the triage occurred. |
| 151 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 152 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 153 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 154 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 155 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 156 | `VALUABLES_CD` | DOUBLE | NOT NULL |  | Type of valuables being kept for the patient. |
| 157 | `VIP_CD` | DOUBLE | NOT NULL |  | The VIP code indicates for this encounter that the person is to be identified and possibly treated with special consideration during the active time of the encounter. (i.e., employee, board member, famous person). |
| 158 | `VISITOR_STATUS_CD` | DOUBLE | NOT NULL |  | Describes the type, or what kind of, visitors the patient wishes to see during their encounter. |
| 159 | `ZERO_BALANCE_DT_TM` | DATETIME |  |  | Date/time when the account balance becomes zero for the encounter. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_ACCESS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CLIENT_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `COMPLETE_REG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DISCH_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_FINANCIAL_ID` | [ENCNTR_FINANCIAL](ENCNTR_FINANCIAL.md) | `ENCNTR_FINANCIAL_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PLACE_OF_SVC_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SERVICE_PROVIDER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (425)

| From table | Column |
|------------|--------|
| [ABSTRACTING](ABSTRACTING.md) | `ENCNTR_ID` |
| [ABSTRACT_DATA](ABSTRACT_DATA.md) | `ENCNTR_ID` |
| [ABST_CODING_RELTN](ABST_CODING_RELTN.md) | `ENCNTR_ID` |
| [ACT_PW_COMP](ACT_PW_COMP.md) | `ENCNTR_ID` |
| [ACT_PW_COMP](ACT_PW_COMP.md) | `ORIGINATING_ENCNTR_ID` |
| [ALERT_AUDIT_ALLERGY_DOM](ALERT_AUDIT_ALLERGY_DOM.md) | `ENCNTR_ID` |
| [ALERT_AUDIT_DRUG_DOM](ALERT_AUDIT_DRUG_DOM.md) | `ENCNTR_ID` |
| [ALERT_AUDIT_DUP_DOM](ALERT_AUDIT_DUP_DOM.md) | `ENCNTR_ID` |
| [ALERT_AUDIT_FOOD_DOM](ALERT_AUDIT_FOOD_DOM.md) | `ENCNTR_ID` |
| [ALLERGY](ALLERGY.md) | `ENCNTR_ID` |
| [ALLERGY_EXT_DATA](ALLERGY_EXT_DATA.md) | `ENCNTR_ID` |
| [AOAV_CONDITION](AOAV_CONDITION.md) | `ENCNTR_ID` |
| [AOAV_DIAGNOSES](AOAV_DIAGNOSES.md) | `ENCNTR_ID` |
| [AOAV_ENCNTR_LOC_HIST](AOAV_ENCNTR_LOC_HIST.md) | `ENCNTR_ID` |
| [AOAV_ENCNTR_RISK_HIST](AOAV_ENCNTR_RISK_HIST.md) | `ENCNTR_ID` |
| [AOAV_EVENT](AOAV_EVENT.md) | `ENCNTR_ID` |
| [AOAV_HOSP_OUTCOMES](AOAV_HOSP_OUTCOMES.md) | `ENCNTR_ID` |
| [AOAV_ICU_STAY](AOAV_ICU_STAY.md) | `ENCNTR_ID` |
| [AOAV_MED_RESULT](AOAV_MED_RESULT.md) | `ENCNTR_ID` |
| [AOAV_OUTCOME](AOAV_OUTCOME.md) | `ENCNTR_ID` |
| [AOAV_PERSON_ENCNTR](AOAV_PERSON_ENCNTR.md) | `ENCNTR_ID` |
| [AP_EXT_DATA](AP_EXT_DATA.md) | `ENCNTR_ID` |
| [AP_LOGIN_ORDER_LIST](AP_LOGIN_ORDER_LIST.md) | `ENCNTR_ID` |
| [AUTHORIZATION](AUTHORIZATION.md) | `ENCNTR_ID` |
| [AUTO_DIRECTED](AUTO_DIRECTED.md) | `ENCNTR_ID` |
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `ENCNTR_ID` |
| [BBHIST_PRODUCT_EVENT](BBHIST_PRODUCT_EVENT.md) | `ENCNTR_ID` |
| [BB_SPEC_EXPIRE_OVRD](BB_SPEC_EXPIRE_OVRD.md) | `ENCNTR_ID` |
| [BCE_EVENT_LOG](BCE_EVENT_LOG.md) | `ENCNTR_ID` |
| [BH_GROUP_DOC_PATIENT](BH_GROUP_DOC_PATIENT.md) | `ENCNTR_ID` |
| [BMDI_ADT_PERSON_R](BMDI_ADT_PERSON_R.md) | `ENCNTR_ID` |
| [CAC_DOCUMENT](CAC_DOCUMENT.md) | `ENCNTR_ID` |
| [CDI_TRANS_LOG](CDI_TRANS_LOG.md) | `ENCNTR_ID` |
| [CE_EVENT_ACTION](CE_EVENT_ACTION.md) | `ENCNTR_ID` |
| [CE_FLAGGED_RESULT](CE_FLAGGED_RESULT.md) | `ENCNTR_ID` |
| [CE_INTAKE_OUTPUT_RESULT](CE_INTAKE_OUTPUT_RESULT.md) | `ENCNTR_ID` |
| [CE_IO_TOTAL_RESULT](CE_IO_TOTAL_RESULT.md) | `ENCNTR_ID` |
| [CE_LINKED_RESULT](CE_LINKED_RESULT.md) | `ENCNTR_ID` |
| [CHARGE](CHARGE.md) | `ENCNTR_ID` |
| [CHARGE](CHARGE.md) | `ORIGINAL_ENCNTR_ID` |
| [CHARGE_BATCH_DETAIL](CHARGE_BATCH_DETAIL.md) | `ENCNTR_ID` |
| [CHARGE_EVENT](CHARGE_EVENT.md) | `ENCNTR_ID` |
| [CHARGE_TRANS_LOG](CHARGE_TRANS_LOG.md) | `ENCNTR_ID` |
| [CHART_ENCNTR_DISCHARGE](CHART_ENCNTR_DISCHARGE.md) | `ENCNTR_ID` |
| [CHART_PROCESS](CHART_PROCESS.md) | `ENCNTR_ID` |
| [CHART_REQUEST](CHART_REQUEST.md) | `ENCNTR_ID` |
| [CHART_REQUEST_ENCNTR](CHART_REQUEST_ENCNTR.md) | `ENCNTR_ID` |
| [CHART_TEMP](CHART_TEMP.md) | `ENCNTR_ID` |
| [CLINICAL_EVENT](CLINICAL_EVENT.md) | `ENCNTR_ID` |
| [CN_DCP_SHIFT_ASSIGNMENT_ST](CN_DCP_SHIFT_ASSIGNMENT_ST.md) | `ENCNTR_ID` |
| [CODING](CODING.md) | `ENCNTR_ID` |
| [CODING_AUDIT](CODING_AUDIT.md) | `ENCNTR_ID` |
| [CODING_ENTITY](CODING_ENTITY.md) | `ENCNTR_ID` |
| [CODING_HIST](CODING_HIST.md) | `ENCNTR_ID` |
| [CODING_SPECIALTY](CODING_SPECIALTY.md) | `ENCNTR_ID` |
| [CODING_SPECIALTY](CODING_SPECIALTY.md) | `MERGED_ENCNTR_ID` |
| [COMPLETION_HOLD](COMPLETION_HOLD.md) | `ENCNTR_ID` |
| [CONDITION_PRIORITY](CONDITION_PRIORITY.md) | `ENCNTR_ID` |
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `ENCNTR_ID` |
| [CP_PATHWAY_ACTION](CP_PATHWAY_ACTION.md) | `ENCNTR_ID` |
| [CP_PATHWAY_ACTIVITY](CP_PATHWAY_ACTIVITY.md) | `ENCNTR_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `ENCNTR_ID` |
| [CR_REPORT_REQUEST_ENCNTR](CR_REPORT_REQUEST_ENCNTR.md) | `ENCNTR_ID` |
| [CR_XML_DOC_REQUEST](CR_XML_DOC_REQUEST.md) | `ENCNTR_ID` |
| [CS_CPP_ERROR_LOG](CS_CPP_ERROR_LOG.md) | `ENCNTR_ID` |
| [CS_CPP_UNDO](CS_CPP_UNDO.md) | `ENCNTR_ID` |
| [CUSTOM_PT_LIST_ENTRY](CUSTOM_PT_LIST_ENTRY.md) | `ENCNTR_ID` |
| [CV_CASE](CV_CASE.md) | `ENCNTR_ID` |
| [CV_PROC](CV_PROC.md) | `ENCNTR_ID` |
| [CV_PROC_HX](CV_PROC_HX.md) | `ENCNTR_ID` |
| [CV_STG_METADATA](CV_STG_METADATA.md) | `ENCNTR_ID` |
| [DCP_FORMS_ACTIVITY](DCP_FORMS_ACTIVITY.md) | `ENCNTR_ID` |
| [DCP_MP_PL_CUSTOM_ENTRY](DCP_MP_PL_CUSTOM_ENTRY.md) | `ENCNTR_ID` |
| [DCP_PL_CUSTOM_ENTRY](DCP_PL_CUSTOM_ENTRY.md) | `ENCNTR_ID` |
| [DCP_PL_PRIORITIZATION](DCP_PL_PRIORITIZATION.md) | `ENCNTR_ID` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `ENCNTR_ID` |
| [DD_CONTRIBUTION](DD_CONTRIBUTION.md) | `ENCNTR_ID` |
| [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `ENCNTR_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `ENCNTR_ID` |
| [DIAGNOSIS_HIST](DIAGNOSIS_HIST.md) | `ENCNTR_ID` |
| [DM_COMBINE_ERROR](DM_COMBINE_ERROR.md) | `ENCNTR_ID` |
| [DM_COMBINE_QUEUE](DM_COMBINE_QUEUE.md) | `ENCNTR_ID` |
| [DOCUMENT_QUALITY_REVIEW](DOCUMENT_QUALITY_REVIEW.md) | `ENCNTR_ID` |
| [DOC_TRANSCRIPTION_QUEUE](DOC_TRANSCRIPTION_QUEUE.md) | `ENCNTR_ID` |
| [DQR_DOCUMENT_ACTION](DQR_DOCUMENT_ACTION.md) | `ENCOUNTER_ID` |
| [DRG](DRG.md) | `ENCNTR_ID` |
| [DRG_ENCNTR_EXTENSION](DRG_ENCNTR_EXTENSION.md) | `ENCNTR_ID` |
| [DRG_SPECIALTY](DRG_SPECIALTY.md) | `ENCNTR_ID` |
| [DSI_FEEDBACK](DSI_FEEDBACK.md) | `ENCNTR_ID` |
| [DSM_ASSESSMENT](DSM_ASSESSMENT.md) | `ENCNTR_ID` |
| [DTS_TRANS_STATS](DTS_TRANS_STATS.md) | `ENCNTR_ID` |
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `ENCNTR_ID` |
| [EEM_ABN_LINK](EEM_ABN_LINK.md) | `ENCNTR_ID` |
| [EEM_AUTH_DETAIL](EEM_AUTH_DETAIL.md) | `ENCOUNTER_ID` |
| [EEM_BENEFIT_ALLOC](EEM_BENEFIT_ALLOC.md) | `ENCNTR_ID` |
| [EEM_NOTIFICATION_DETAIL](EEM_NOTIFICATION_DETAIL.md) | `ENCNTR_ID` |
| [EEM_RX_ELIG_DETAIL](EEM_RX_ELIG_DETAIL.md) | `ENCNTR_ID` |
| [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `ENCNTR_ID` |
| [EKS_ALERT_ESCALATION](EKS_ALERT_ESCALATION.md) | `ENCNTR_ID` |
| [EKS_ALERT_ESC_HIST](EKS_ALERT_ESC_HIST.md) | `ENCNTR_ID` |
| [EKS_DLG_EVENT](EKS_DLG_EVENT.md) | `ENCNTR_ID` |
| [EKS_MODULE_AUDIT_DET](EKS_MODULE_AUDIT_DET.md) | `ENCNTR_ID` |
| [ENCNTR_ACCIDENT](ENCNTR_ACCIDENT.md) | `ENCNTR_ID` |
| [ENCNTR_ALIAS_HIST](ENCNTR_ALIAS_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_AMBULANCE](ENCNTR_AMBULANCE.md) | `ENCNTR_ID` |
| [ENCNTR_APPEAL](ENCNTR_APPEAL.md) | `ENCNTR_ID` |
| [ENCNTR_AUGM_CARE_PERIOD](ENCNTR_AUGM_CARE_PERIOD.md) | `ENCNTR_ID` |
| [ENCNTR_AVOIDABLE_DAYS](ENCNTR_AVOIDABLE_DAYS.md) | `ENCNTR_ID` |
| [ENCNTR_CARE_MGMT](ENCNTR_CARE_MGMT.md) | `ENCNTR_ID` |
| [ENCNTR_CARE_MGMT_COMM](ENCNTR_CARE_MGMT_COMM.md) | `ENCNTR_ID` |
| [ENCNTR_CATCHMENT_RELTN](ENCNTR_CATCHMENT_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_CATCHMENT_R_HIST](ENCNTR_CATCHMENT_R_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_CLASSIFICATION](ENCNTR_CLASSIFICATION.md) | `ENCNTR_ID` |
| [ENCNTR_CLIN_REVIEW](ENCNTR_CLIN_REVIEW.md) | `ENCNTR_ID` |
| [ENCNTR_CMNTY_CASE](ENCNTR_CMNTY_CASE.md) | `ENCNTR_ID` |
| [ENCNTR_CODE_VALUE_R](ENCNTR_CODE_VALUE_R.md) | `ENCNTR_ID` |
| [ENCNTR_CODE_VALUE_R_HIST](ENCNTR_CODE_VALUE_R_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_COMBINE](ENCNTR_COMBINE.md) | `FROM_ENCNTR_ID` |
| [ENCNTR_COMBINE](ENCNTR_COMBINE.md) | `TO_ENCNTR_ID` |
| [ENCNTR_CONDITION_CODE](ENCNTR_CONDITION_CODE.md) | `ENCNTR_ID` |
| [ENCNTR_CRIMINAL_CHARGES_R](ENCNTR_CRIMINAL_CHARGES_R.md) | `ENCNTR_ID` |
| [ENCNTR_DATA_NOT_COLL](ENCNTR_DATA_NOT_COLL.md) | `ENCNTR_ID` |
| [ENCNTR_DENIED_DAYS](ENCNTR_DENIED_DAYS.md) | `ENCNTR_ID` |
| [ENCNTR_DOMAIN](ENCNTR_DOMAIN.md) | `ENCNTR_ID` |
| [ENCNTR_ENCNTR_RELTN](ENCNTR_ENCNTR_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_ENCNTR_RELTN](ENCNTR_ENCNTR_RELTN.md) | `RELATED_ENCNTR_ID` |
| [ENCNTR_EVENT_SET_IO](ENCNTR_EVENT_SET_IO.md) | `ENCNTR_ID` |
| [ENCNTR_FLEX_HIST](ENCNTR_FLEX_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_INFO](ENCNTR_INFO.md) | `ENCNTR_ID` |
| [ENCNTR_INFO_HIST](ENCNTR_INFO_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_INPTNT_REHAB](ENCNTR_INPTNT_REHAB.md) | `ENCNTR_ID` |
| [ENCNTR_LEAVE](ENCNTR_LEAVE.md) | `ENCNTR_ID` |
| [ENCNTR_LEGAL_AUTH_RELTN](ENCNTR_LEGAL_AUTH_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_LEGAL_AUTH_R_HIST](ENCNTR_LEGAL_AUTH_R_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_LEGAL_STATUS_R](ENCNTR_LEGAL_STATUS_R.md) | `ENCNTR_ID` |
| [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `ENCNTR_ID` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_MEDICARE_MGMT](ENCNTR_MEDICARE_MGMT.md) | `ENCNTR_ID` |
| [ENCNTR_MOTHER_CHILD_RELTN](ENCNTR_MOTHER_CHILD_RELTN.md) | `CHILD_ENCNTR_ID` |
| [ENCNTR_MOTHER_CHILD_RELTN](ENCNTR_MOTHER_CHILD_RELTN.md) | `MOTHER_ENCNTR_ID` |
| [ENCNTR_NEWBORN_CE_RELTN](ENCNTR_NEWBORN_CE_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_OCCURRENCE_CODE](ENCNTR_OCCURRENCE_CODE.md) | `ENCNTR_ID` |
| [ENCNTR_ORG_RELTN](ENCNTR_ORG_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_ORG_SERVICE_RELTN](ENCNTR_ORG_SERVICE_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_PENDING](ENCNTR_PENDING.md) | `ENCNTR_ID` |
| [ENCNTR_PENDING_HIST](ENCNTR_PENDING_HIST.md) | `ENCNTR_ID` |
| [ENCNTR_PERSON_RELTN](ENCNTR_PERSON_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_PLAN_COB](ENCNTR_PLAN_COB.md) | `ENCNTR_ID` |
| [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_POSTACUTE_ORG_RELTN](ENCNTR_POSTACUTE_ORG_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_PROCEDURE](ENCNTR_PROCEDURE.md) | `ENCNTR_ID` |
| [ENCNTR_PRSNL_GRP_RELTN](ENCNTR_PRSNL_GRP_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_PRSNL_RELTN](ENCNTR_PRSNL_RELTN.md) | `ENCNTR_ID` |
| [ENCNTR_PRSNL_RELTN_HISTORY](ENCNTR_PRSNL_RELTN_HISTORY.md) | `ENCNTR_ID` |
| [ENCNTR_READMIT_ASSESS](ENCNTR_READMIT_ASSESS.md) | `ENCNTR_ID` |
| [ENCNTR_READMIT_ASSESS](ENCNTR_READMIT_ASSESS.md) | `PREVIOUS_ENCNTR_ID` |
| [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_ID` |
| [ENCNTR_SOCIAL_HEALTHCARE](ENCNTR_SOCIAL_HEALTHCARE.md) | `ENCNTR_ID` |
| [ENCNTR_SPAN_CODE](ENCNTR_SPAN_CODE.md) | `ENCNTR_ID` |
| [ENCNTR_VALUE_CODE](ENCNTR_VALUE_CODE.md) | `ENCNTR_ID` |
| [EPA_RECORD](EPA_RECORD.md) | `ENCNTR_ID` |
| [EPISODE_ACTIVITY](EPISODE_ACTIVITY.md) | `CREATED_BY_ENCNTR_ID` |
| [EPISODE_ACTIVITY_HIST](EPISODE_ACTIVITY_HIST.md) | `CREATED_BY_ENCNTR_ID` |
| [EPISODE_ENCNTR_RELTN](EPISODE_ENCNTR_RELTN.md) | `ENCNTR_ID` |
| [ERX_EXT_MED_LIST_ACCESS](ERX_EXT_MED_LIST_ACCESS.md) | `ENCNTR_ID` |
| [ESI_LOG](ESI_LOG.md) | `ENCNTR_ID` |
| [ESO_TRANSACTION_RECORD](ESO_TRANSACTION_RECORD.md) | `ENCNTR_ID` |
| [EXAM_DATA](EXAM_DATA.md) | `ENCNTR_ID` |
| [EXPEDITE_LOG](EXPEDITE_LOG.md) | `ENCNTR_ID` |
| [EXPEDITE_MANUAL](EXPEDITE_MANUAL.md) | `ENCNTR_ID` |
| [EXT_DATA_GROUP](EXT_DATA_GROUP.md) | `SUBMITTED_ENCNTR_ID` |
| [EXT_DATA_INFO](EXT_DATA_INFO.md) | `ENCNTR_ID` |
| [EXT_REQ_STATUS](EXT_REQ_STATUS.md) | `ENCNTR_ID` |
| [FHX_ACTIVITY](FHX_ACTIVITY.md) | `ORIGINATING_ENCNTR_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `ENCNTR_ID` |
| [FN_EV_SURVEY_ACT](FN_EV_SURVEY_ACT.md) | `ENCNTR_ID` |
| [FN_OMF_ENCNTR](FN_OMF_ENCNTR.md) | `ENCNTR_ID` |
| [GEN_LAB_EXT_DATA](GEN_LAB_EXT_DATA.md) | `ENCNTR_ID` |
| [HANDHELD_DETAIL](HANDHELD_DETAIL.md) | `ENCNTR1_ID` |
| [HANDHELD_DETAIL](HANDHELD_DETAIL.md) | `ENCNTR2_ID` |
| [HCM_COMM_EVENT](HCM_COMM_EVENT.md) | `ENCNTR_ID` |
| [HCM_COMM_EVENT_H](HCM_COMM_EVENT_H.md) | `ENCNTR_ID` |
| [HEALTH_CONCERN](HEALTH_CONCERN.md) | `DOCUMENTED_ENCNTR_ID` |
| [HEALTH_CONCERN](HEALTH_CONCERN.md) | `LAST_UPDT_ENCNTR_ID` |
| [HIM_EVENT_ALLOCATION](HIM_EVENT_ALLOCATION.md) | `ENCNTR_ID` |
| [HIM_LETTERS_TEMP](HIM_LETTERS_TEMP.md) | `ENCNTR_ID` |
| [HIM_PV_CHART](HIM_PV_CHART.md) | `ENCNTR_ID` |
| [HIM_PV_DOCUMENT](HIM_PV_DOCUMENT.md) | `ENCNTR_ID` |
| [HIM_PV_PHYSICIAN](HIM_PV_PHYSICIAN.md) | `ENCNTR_ID` |
| [HIM_REQUEST_CRITERIA](HIM_REQUEST_CRITERIA.md) | `ENCNTR_ID` |
| [HIM_REQUEST_PATIENT](HIM_REQUEST_PATIENT.md) | `ENCNTR_ID` |
| [HIM_TEMP_REQUEST_LOG](HIM_TEMP_REQUEST_LOG.md) | `ENCNTR_ID` |
| [HIM_UNSIGNED_ORDERS](HIM_UNSIGNED_ORDERS.md) | `ENCNTR_ID` |
| [HISTORY_ACTION](HISTORY_ACTION.md) | `ENCNTR_ID` |
| [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `ENCNTR_ID` |
| [HOLD_QUEUE](HOLD_QUEUE.md) | `ENCNTR_ID` |
| [IB_RX_REQ_ACTION](IB_RX_REQ_ACTION.md) | `PROPOSED_ENCNTR_ID` |
| [IMMUNIZATION_EXT_DATA](IMMUNIZATION_EXT_DATA.md) | `ENCNTR_ID` |
| [IMPLANT_HISTORY](IMPLANT_HISTORY.md) | `ENCNTR_ID` |
| [IMPLANT_HISTORY](IMPLANT_HISTORY.md) | `ORIGINATING_ENCNTR_ID` |
| [IM_U_NOTIFY](IM_U_NOTIFY.md) | `ENCNTR_ID` |
| [INFUSION_BILLING_EVENT](INFUSION_BILLING_EVENT.md) | `ENCNTR_ID` |
| [INFUSION_BILL_RPT](INFUSION_BILL_RPT.md) | `ENCNTR_ID` |
| [INTERFACE_TRANSACTION](INTERFACE_TRANSACTION.md) | `ENCNTR_ID` |
| [IO_DEVICE_INTERRUPT](IO_DEVICE_INTERRUPT.md) | `ENCNTR_ID` |
| [IO_TOTAL_START_TIME](IO_TOTAL_START_TIME.md) | `ENCNTR_ID` |
| [LAB_EXT_IDENTIFIER](LAB_EXT_IDENTIFIER.md) | `ENCNTR_ID` |
| [LH_CNT_IC_ADV_EVENT_LOC](LH_CNT_IC_ADV_EVENT_LOC.md) | `ENCNTR_ID` |
| [LH_CNT_IC_ADV_LAB_DATA](LH_CNT_IC_ADV_LAB_DATA.md) | `ENCNTR_ID` |
| [LH_CNT_IC_ADV_LTD](LH_CNT_IC_ADV_LTD.md) | `ENCNTR_ID` |
| [LH_CNT_IC_ADV_MICRO](LH_CNT_IC_ADV_MICRO.md) | `ENCNTR_ID` |
| [LH_CNT_IC_ADV_SURG_DATA](LH_CNT_IC_ADV_SURG_DATA.md) | `ENCNTR_ID` |
| [LH_CNT_IC_ADV_WOUND_DATA](LH_CNT_IC_ADV_WOUND_DATA.md) | `ENCNTR_ID` |
| [LH_CNT_IC_LOC_HIST](LH_CNT_IC_LOC_HIST.md) | `ENCNTR_ID` |
| [LH_CNT_IC_MED_ADMIN_EVENT](LH_CNT_IC_MED_ADMIN_EVENT.md) | `ENCNTR_ID` |
| [LH_CNT_IC_MICRO_EVENT](LH_CNT_IC_MICRO_EVENT.md) | `ENCNTR_ID` |
| [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `ENCNTR_ID` |
| [LH_CNT_IC_PATIENT_POP_TAGS](LH_CNT_IC_PATIENT_POP_TAGS.md) | `ENCNTR_ID` |
| [LH_CNT_IC_RPT_EVENT](LH_CNT_IC_RPT_EVENT.md) | `ENCNTR_ID` |
| [LH_CNT_IC_VAE](LH_CNT_IC_VAE.md) | `ENCNTR_ID` |
| [LH_CNT_IRFPAI](LH_CNT_IRFPAI.md) | `ENCNTR_ID` |
| [LH_CNT_IRFPAI_CHANGE](LH_CNT_IRFPAI_CHANGE.md) | `ENCNTR_ID` |
| [LH_CNT_IRFPAI_ICD](LH_CNT_IRFPAI_ICD.md) | `ENCNTR_ID` |
| [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `INSERT_ENCNTR_ID` |
| [LH_CNT_PATIENT_EXTENSION](LH_CNT_PATIENT_EXTENSION.md) | `ENCNTR_ID` |
| [LH_CNT_READMIT_WORKLIST](LH_CNT_READMIT_WORKLIST.md) | `ENCNTR_ID` |
| [LH_CNT_REPORT](LH_CNT_REPORT.md) | `ENCNTR_ID` |
| [LH_CNT_WL_POP](LH_CNT_WL_POP.md) | `ENCNTR_ID` |
| [LH_CNT_WL_POP_H](LH_CNT_WL_POP_H.md) | `ENCNTR_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `ENCNTR_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `ENCNTR_ID` |
| [MEDIA_ENCNTR_RELTN](MEDIA_ENCNTR_RELTN.md) | `ENCNTR_ID` |
| [MEDIA_EXAM](MEDIA_EXAM.md) | `ENCNTR_ID` |
| [MEDIA_MASTER](MEDIA_MASTER.md) | `ENCNTR_ID` |
| [MED_ADMIN_IDENT_ERROR](MED_ADMIN_IDENT_ERROR.md) | `ENCNTR_ID` |
| [MED_ADMIN_INGREDIENT_META](MED_ADMIN_INGREDIENT_META.md) | `ENCNTR_ID` |
| [MED_ADMIN_MED_ERROR](MED_ADMIN_MED_ERROR.md) | `ENCOUNTER_ID` |
| [MED_ADMIN_RECORD](MED_ADMIN_RECORD.md) | `ENCNTR_ID` |
| [MED_HISTORY_AUDIT](MED_HISTORY_AUDIT.md) | `ENCNTR_ID` |
| [MESSAGING_AUDIT](MESSAGING_AUDIT.md) | `ENCNTR_ID` |
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `ENCNTR_ID` |
| [MIC_EXT_DATA](MIC_EXT_DATA.md) | `ENCNTR_ID` |
| [MIC_IC_ORDERS](MIC_IC_ORDERS.md) | `ENCNTR_ID` |
| [MIC_STAT_ORDER](MIC_STAT_ORDER.md) | `ENCNTR_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `ENCNTR_ID` |
| [MP_NOTIFICATION](MP_NOTIFICATION.md) | `ENCNTR_ID` |
| [MP_PRIMED_VIEW_ACT](MP_PRIMED_VIEW_ACT.md) | `ENCNTR_ID` |
| [NC_CHARTED_SECTION](NC_CHARTED_SECTION.md) | `ENCNTR_ID` |
| [NC_CHARTED_VIEW](NC_CHARTED_VIEW.md) | `ENCNTR_ID` |
| [NOMENCLATURE_ENCNTR_DESC](NOMENCLATURE_ENCNTR_DESC.md) | `ENCNTR_ID` |
| [NOMEN_ENTITY_RELTN](NOMEN_ENTITY_RELTN.md) | `ENCNTR_ID` |
| [NURSING_ENCNTR_SCRATCHPAD](NURSING_ENCNTR_SCRATCHPAD.md) | `ENCNTR_ID` |
| [OMF_ABSTRACT_DATA_ST](OMF_ABSTRACT_DATA_ST.md) | `ENCNTR_ID` |
| [OMF_ABST_CODING_RELTN_ST](OMF_ABST_CODING_RELTN_ST.md) | `ENCNTR_ID` |
| [OMF_APC_CODING_ST](OMF_APC_CODING_ST.md) | `ENCNTR_ID` |
| [OMF_CHARGE_ST](OMF_CHARGE_ST.md) | `ENCNTR_ID` |
| [OMF_CLINICAL_EVENT_ST](OMF_CLINICAL_EVENT_ST.md) | `ENCNTR_ID` |
| [OMF_CODING_ST](OMF_CODING_ST.md) | `ENCNTR_ID` |
| [OMF_ENCNTR_PRSNL_RELTN_ST](OMF_ENCNTR_PRSNL_RELTN_ST.md) | `ENCNTR_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `ENCNTR_ID` |
| [OMF_ENCNTR_ST_EXT](OMF_ENCNTR_ST_EXT.md) | `ENCNTR_ID` |
| [OMF_ENCNTR_TYPE_HIST_ST](OMF_ENCNTR_TYPE_HIST_ST.md) | `ENCNTR_ID` |
| [OMF_LOCATION_HIST_ST](OMF_LOCATION_HIST_ST.md) | `ENCNTR_ID` |
| [OMF_MED_SERVICE_HIST_ST](OMF_MED_SERVICE_HIST_ST.md) | `ENCNTR_ID` |
| [OMF_ORDER_ST](OMF_ORDER_ST.md) | `ENCNTR_ID` |
| [OMF_POSTED_CHARGE_ST](OMF_POSTED_CHARGE_ST.md) | `ENCNTR_ID` |
| [OMF_RADMGMT_ORDER_ST](OMF_RADMGMT_ORDER_ST.md) | `ENCNTR_ID` |
| [OMF_REVENUE_ST](OMF_REVENUE_ST.md) | `ENCNTR_ID` |
| [OMF_SVC_CAT_HIST_ST](OMF_SVC_CAT_HIST_ST.md) | `ENCNTR_ID` |
| [ONC_FORM_ACTIVITY](ONC_FORM_ACTIVITY.md) | `ENCNTR_ID` |
| [ONC_II_AUTO_ACTIVITY](ONC_II_AUTO_ACTIVITY.md) | `ENCNTR_ID` |
| [ONC_INFUSION_ACTIVITY](ONC_INFUSION_ACTIVITY.md) | `ENCNTR_ID` |
| [ORDERS](ORDERS.md) | `ENCNTR_ID` |
| [ORDERS](ORDERS.md) | `ORIGINATING_ENCNTR_ID` |
| [ORDER_COMPLIANCE](ORDER_COMPLIANCE.md) | `ENCNTR_ID` |
| [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `ENCNTR_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `ENCNTR_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ENCNTR_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORIGINATING_ENCNTR_ID` |
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ENCNTR_ID` |
| [ORDER_RECON](ORDER_RECON.md) | `ENCNTR_ID` |
| [ORDER_STAGING](ORDER_STAGING.md) | `ENCOUNTER_ID` |
| [ORDER_SUPPLY_REVIEW](ORDER_SUPPLY_REVIEW.md) | `ENCNTR_ID` |
| [ORDER_TRACKING_WORKLIST](ORDER_TRACKING_WORKLIST.md) | `EFFECTIVE_ENCNTR_ID` |
| [ORD_RQSTN](ORD_RQSTN.md) | `ENCNTR_ID` |
| [ORM_ERROR_LOG](ORM_ERROR_LOG.md) | `ENCNTR_ID` |
| [ORM_ORD_HIST_SNAPSHOT](ORM_ORD_HIST_SNAPSHOT.md) | `ENCNTR_ID` |
| [ORM_ORD_HIST_SNAPSHOT_COMP](ORM_ORD_HIST_SNAPSHOT_COMP.md) | `ENCNTR_ID` |
| [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `ENCNTR_ID` |
| [PASSIVE_ALERT](PASSIVE_ALERT.md) | `ENCNTR_ID` |
| [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `ENCNTR_ID` |
| [PATHWAY](PATHWAY.md) | `ENCNTR_ID` |
| [PATIENT_CASE_ENCNTR_R](PATIENT_CASE_ENCNTR_R.md) | `ENCNTR_ID` |
| [PATIENT_EVENT](PATIENT_EVENT.md) | `ENCNTR_ID` |
| [PAT_ED_DOCUMENT](PAT_ED_DOCUMENT.md) | `ENCNTR_ID` |
| [PCA_ENCNTR_MEASURE_OUTCOME](PCA_ENCNTR_MEASURE_OUTCOME.md) | `ENCNTR_ID` |
| [PCA_ENCNTR_TOPIC_RELTN](PCA_ENCNTR_TOPIC_RELTN.md) | `ENCNTR_ID` |
| [PCT_IPASS](PCT_IPASS.md) | `ENCNTR_ID` |
| [PDOC_AUTOSAVE](PDOC_AUTOSAVE.md) | `ENCNTR_ID` |
| [PDOC_TAG](PDOC_TAG.md) | `ENCNTR_ID` |

_… and 125 more (see `data/foreign_keys.jsonl`)._

