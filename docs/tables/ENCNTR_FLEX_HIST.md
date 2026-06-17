# ENCNTR_FLEX_HIST

> Used for tracking, modifying and inactivating the history elements of encounter information.

**Description:** Encounter Flex History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 168

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
| 11 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | This column holds the current date and time of the system that the row was inserted |
| 12 | `ADMINISTRATIVE_PROBLEM_CD` | DOUBLE |  |  | Indicates the chronic condition that is being treated for this encounter from an administrative perspective. |
| 13 | `ADMIT_DECISION_DT_TM` | DATETIME |  |  | The date and time that the decision to admit the patient to the facility is made. |
| 14 | `ADMIT_EARLY_IND` | DOUBLE | NOT NULL |  | Indicates if the patient's admission qualified under the early admission rules of the facility. |
| 15 | `ADMIT_MODE_CD` | DOUBLE | NOT NULL |  | Admit mode identifies the method by which the patient arrived. (i.e., helicopter, ambulance, etc.) |
| 16 | `ADMIT_SRC_CD` | DOUBLE | NOT NULL |  | Admit source identifies the place from which the patient came before being admitted. (i.e., transfer from another hospital) |
| 17 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Admit type indicates the circumstance under which the patient was admitted or will be admitted. (i.e., accident, emergent, routine, elective, labor/delivery, etc.) |
| 18 | `ADMIT_WITH_MEDICATION_CD` | DOUBLE | NOT NULL |  | Admit with medication describes that the patient brought their own medication with them when admitted. |
| 19 | `ALC_DECOMP_DT_TM` | DATETIME |  |  | Date and time the alternate level of care decompensation |
| 20 | `ALC_REASON_CD` | DOUBLE | NOT NULL |  | Reason the alternate level of care is being assigned or changed |
| 21 | `ALT_LVL_CARE_CD` | DOUBLE | NOT NULL |  | Level of care for the encounter that signals a difference, or alternative, to the care signified by the encntr_type, med service, location, or combination therein. Used primarily as a billing function to trigger a change in charging rates. |
| 22 | `ALT_LVL_CARE_DECOMP_DT_TM` | DATETIME |  |  | Alternate level of care decomposition date/time. |
| 23 | `ALT_LVL_CARE_DT_TM` | DATETIME |  |  | The date and time the alternate level of care was assigned |
| 24 | `ALT_RESULT_DEST_CD` | DOUBLE | NOT NULL |  | NOT USED. |
| 25 | `AMBULATORY_COND_CD` | DOUBLE | NOT NULL |  | Ambulatory condition describes the general physical condition, impairment, or limitation of the patient upon arrival. |
| 26 | `ARCHIVE_DT_TM_ACT` | DATETIME | NOT NULL |  | The actual date/time when the encounter was archived. |
| 27 | `ARCHIVE_DT_TM_EST` | DATETIME | NOT NULL |  | The estimated date when the encounter will be archived. This date is calculated based on client-defined archive criteria. |
| 28 | `ARRIVE_DT_TM` | DATETIME |  |  | The actual date/time that the patient arrived at the facility. At the time of registration, if this field is null then it should be valued with the reg_dt_tm. Otherwise, the actual arrival date/time is captured. |
| 29 | `ARRIVE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the arrive_dt_tm. |
| 30 | `ASSIGN_TO_LOC_DT_TM` | DATETIME |  |  | Date and time that the encounter was assigned to a location. |
| 31 | `BBD_PROCEDURE_CD` | DOUBLE | NOT NULL |  | Encounter (patient) was a blood blank donor and this lists the type of procedure performed on them. |
| 32 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 33 | `BIRTH_DT_CD` | DOUBLE | NOT NULL |  | Birth date code indicates the kind of birth date and time value that is contained in the birth_dt_tm field. This field will be null where the field encntr_class_cd indicates that this encounter row references a row in the person table. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 34 | `BIRTH_DT_TM` | DATETIME |  |  | The date and time of birth for the person or thing for which the encounter is being created. This field will be null where the field encntr_class_cd indicates that this encounter row references a row in the person table. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 35 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 36 | `CHART_ACCESS_ORGANIZATION_ID` | DOUBLE |  | FK→ | The identifying information of the organization (real or virtual) that indicates which groups of users should have medical chart access to the encounter. |
| 37 | `CHART_COMPLETE_DT_TM` | DATETIME |  |  | Date/time when the chart is complete for the encounter. |
| 38 | `CLERGY_VISIT_CD` | DOUBLE | NOT NULL |  | Indicates if the patient has requested a clergy visit. |
| 39 | `CLIENT_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the organization financially responsible for the encounter (e.g. an employer paying for an employee's drug test). |
| 40 | `CLIENT_REFERENCE_NBR_TXT` | VARCHAR(50) |  |  | Indicates the number assigned to the encounter for tracking purposes by an external organization that is financially responsible for the encounter. |
| 41 | `COMPLETE_REG_DT_TM` | DATETIME |  |  | The date/time that all required financial and clinical data collection necessary for registration has been completed. |
| 42 | `COMPLETE_REG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The internal person id of the personnel that completed the collection of all required financial and clinical data necessary for registration. if the complete_reg_dt_tm is valued, then this field should be valued. |
| 43 | `CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | Confidential level identifies a level of security that may restrict access or release of information. |
| 44 | `CONTRACT_STATUS_CD` | DOUBLE | NOT NULL |  | Codified field indicating status of a care contract. |
| 45 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 46 | `COURTESY_CD` | DOUBLE | NOT NULL |  | This field indicates whether the patient will be extended certain special courtesies such as express discharge, bypassing a stop at the cashiers window upon leaving when financial arrangements are agreed upon in advance. |
| 47 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the encounter table. |
| 48 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person responsible for creating a row in the encounter table. |
| 49 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 50 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 51 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 52 | `DEPART_DT_TM` | DATETIME |  |  | The actual date/time that the patient left from the facility. In many cases, this field may be null unless the user process requires capturing this data. |
| 53 | `DEPART_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the depart_dt_tm. |
| 54 | `DIET_TYPE_CD` | DOUBLE | NOT NULL |  | Diet type is used to indicate that the patient is on a special diet. |
| 55 | `DISCH_DISPOSITION_CD` | DOUBLE | NOT NULL |  | The conditions under which the patient left the facility at the time of discharge. |
| 56 | `DISCH_DT_TM` | DATETIME |  |  | Date the person was discharged from the facility |
| 57 | `DISCH_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The internal person identifier of the personnel that performed the discharge process. If the disch_dt_tm is valued, then this field must be valued. |
| 58 | `DISCH_TO_LOCTN_CD` | DOUBLE | NOT NULL |  | The location to which the patient was discharged such as another hospital or nursing home. |
| 59 | `DOC_RCVD_DT_TM` | DATETIME |  |  | Date and Time documents were received for the encounter |
| 60 | `ED_REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | Indicates the source of referral for the visit to the emergency department. |
| 61 | `ENCNTR_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter class defines how this encounter row is being used in relation to the person table. |
| 62 | `ENCNTR_COMPLETE_DT_TM` | DATETIME | NOT NULL |  | Date/time when the encounter is considered to be in a completed status. |
| 63 | `ENCNTR_FINANCIAL_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter financial table. It is an internal system assigned number. |
| 64 | `ENCNTR_FLEX_HIST_ID` | DOUBLE | NOT NULL |  | Unique identifier for the encntr_flex_hist table. |
| 65 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 66 | `ENCNTR_STATUS_CD` | DOUBLE | NOT NULL |  | Encounter status identifies the state of a particular encounter type from the time it is initiated until it is complete. (i.e., temporary, preliminary, active, discharged (complete), cancelled). |
| 67 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 68 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this code set all have Cerner defined meanings. |
| 69 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 70 | `EST_ARRIVE_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the patient will arrive at the facility. This field may be null. |
| 71 | `EST_DEPART_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the patient will depart (outpatient) or will be discharged (inpatient) from the facility. This field may be null. |
| 72 | `EST_FINANCIAL_RESP_AMT` | DOUBLE |  |  | The estimated financial responsibility of the patient (or gaurantor) for this visit. |
| 73 | `EST_LENGTH_OF_STAY` | DOUBLE |  |  | Estimated length of the patient/encounter stay, in days |
| 74 | `EXPECTED_DELIVERY_DT_TM` | DATETIME |  |  | The date and time the delivery is expected. |
| 75 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for a given encounter. Examples may include Worker's Comp, Self Pay, etc. |
| 76 | `GUARANTOR_TYPE_CD` | DOUBLE | NOT NULL |  | The guarantor type indicates that the guarantor for the encounter is either a person or an organization. This code is used to determine which set of tables to query to find the guarantor. |
| 77 | `INCIDENT_CD` | DOUBLE | NOT NULL |  | Indicates the incident or disaster that led to the patient's visit. |
| 78 | `INFO_GIVEN_BY` | CHAR(100) |  |  | Free-text attribute specifying who gave the information for this encounter. Might be a guardian, parent, patient, etc. |
| 79 | `INITIAL_CONTACT_DT_TM` | DATETIME |  |  | The initial contact of the patient and the provider submitting the claim. |
| 80 | `INPATIENT_ADMIT_DT_TM` | DATETIME |  |  | Stores the inpatient admit date and time |
| 81 | `ISOLATION_CD` | DOUBLE | NOT NULL |  | The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 82 | `KIOSK_QUEUE_NBR_DT_TM` | DATETIME |  |  | The date and time when the system generated ticket number representing their position within the queue was assigned to the patient when they are checking in for the visit. |
| 83 | `KIOSK_QUEUE_NBR_TXT` | VARCHAR(50) |  |  | The system generated ticket number assigned to the patient to represent their position within the queue when they are checking in for the visit. |
| 84 | `LAST_MENSTRUAL_PERIOD_DT_TM` | DATETIME |  |  | The date and time of the last menstrual period. |
| 85 | `LEVEL_OF_SERVICE_CD` | DOUBLE | NOT NULL |  | The level of service provided. Examples are emergency, elective, urgent and routine. |
| 86 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 87 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | This field is the current patient location with a location type of bed. |
| 88 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | This field is the current patient location with a location type of building. |
| 89 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | This field is the current patient location with a location type of facility. |
| 90 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field is the current patient location with a location type of nurse unit. |
| 91 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | This field is the current patient location with a location type of room. |
| 92 | `LOC_TEMP_CD` | DOUBLE | NOT NULL |  | This field identifies the temporary location of the patient. the temporary location may be valued at the same time the location_cd is valued. |
| 93 | `LODGER_CD` | DOUBLE | NOT NULL |  | Indicates if an additional person is staying with the patient in the same room. |
| 94 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 95 | `MENTAL_CATEGORY_CD` | DOUBLE | NOT NULL |  | Mental category code (ex. Mental illness, Mental impairment, severe mental impairment) |
| 96 | `MENTAL_HEALTH_CD` | DOUBLE | NOT NULL |  | The field is the mental health status of a patient which indicates if a patient was involuntarily or voluntarily admitted. This field is not used by all clients. |
| 97 | `MENTAL_HEALTH_DT_TM` | DATETIME |  |  | The date and time of the last time the mental health info was updated. |
| 98 | `MILITARY_SERVICE_RELATED_CD` | DOUBLE | NOT NULL |  | Indicates if the patient's visit is related to their military service. |
| 99 | `NAME_FIRST` | VARCHAR(200) |  |  | OBSOLETE - This is the person's first given name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 100 | `NAME_FIRST_KEY` | VARCHAR(200) |  |  | OBSOLETE - This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 101 | `NAME_FIRST_SYNONYM_ID` | DOUBLE | NOT NULL |  | OBSOLETE - This is the value of the unique primary identifier of the first name synonym table. It is an internal system assigned number. It is used to when searching for a person where other first names would be considered as a match. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 102 | `NAME_FULL_FORMATTED` | VARCHAR(200) |  |  | OBSOLETE - This is the complete person name including punctuation and formatting. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 103 | `NAME_LAST` | VARCHAR(200) |  |  | OBSOLETE - This is the person's family name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 104 | `NAME_LAST_KEY` | VARCHAR(200) |  |  | OBSOLETE - This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 105 | `NAME_PHONETIC` | VARCHAR(200) |  |  | OBSOLETE - This is the Soundex coded representation of the person's name. This field is used for indexing and searching for a patient by name when the exact spelling is not known. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 106 | `ONSET_DT_TM` | DATETIME |  |  | The date and time of the onset of current symptoms. |
| 107 | `ORDER_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the order (i.e. electronic, scanned, faxed by physician, faxed by patient, etc.) |
| 108 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. This column is either valued with the facility or the client organization for the encounter. |
| 109 | `OVRD_AUTOMTC_CVRG_PRTZTN_IND` | DOUBLE |  |  | Indicates if the automatic coverage prioritization processing was overridden by the user to maintain the manually entered coverage priority sequencing. |
| 110 | `PARENT_RET_CRITERIA_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This column is no longer used. This column indicates which set of retention criteria was last applied to the encounter to calculate the value in the archive_dt_tm_est column. **OBSOLETE ** |
| 111 | `PATIENT_CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | Patient classification code (ex. Ordinary admission, day case admission, regular day, regular night) |
| 112 | `PAYMENT_COLLECTION_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the payment collection (i.e. 1st attempt - left message, payment in full received, unable to pay - proceed with service, etc.) |
| 113 | `PA_CURRENT_STATUS_CD` | DOUBLE | NOT NULL |  | This column shows the last action that was performed on the encounter in relation to the purge/archive process. |
| 114 | `PA_CURRENT_STATUS_DT_TM` | DATETIME |  |  | Date/time of last purge/archive action taken on the encounter. |
| 115 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 116 | `PERSON_PLAN_PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of health insurance profile to be used for the encounter (i.e., professional, institutional, workmen's comp). |
| 117 | `PLACEMENT_AUTH_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the personnel who authorized the override of a patient placement into a location that had a "stop" attribute associated to it. |
| 118 | `PLACE_OF_SVC_ADMIT_DT_TM` | DATETIME |  |  | The date and time of admission to the place of service organization. |
| 119 | `PLACE_OF_SVC_ORG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the place of service organization for the encounter. |
| 120 | `PLACE_OF_SVC_TYPE_CD` | DOUBLE | NOT NULL |  | Code to identify the type of service performed at the place of service organization for the encounter. |
| 121 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 122 | `PREADMIT_NBR` | VARCHAR(100) |  |  | The number assigned to a pre-admit encounter. A pre-admit encounter is not required to have a pre-admit number |
| 123 | `PREADMIT_TESTING_CD` | DOUBLE | NOT NULL |  | Indicates that the patient must have pre-admission testing done in order to be admitted. |
| 124 | `PREGNANCY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the pregnancy. |
| 125 | `PRE_REG_DT_TM` | DATETIME |  |  | The date/time that the pre-registration or pre-admission process was performed. If the reg_dt_tm is valued, or no pre-registration occurred, then this field may be null. |
| 126 | `PRE_REG_PRSNL_ID` | DOUBLE | NOT NULL |  | The internal person ID of the personnel that performed the pre-registration or pre-admission. If the pre_reg_dt_tm is valued, then this field must be valued. |
| 127 | `PROGRAM_SERVICE_CD` | DOUBLE | NOT NULL |  | Represents the program service associated with the patient's location |
| 128 | `PSYCHIATRIC_STATUS_CD` | DOUBLE | NOT NULL |  | Psychiatric status code (ex. One or more previous, not known, not applicable) |
| 129 | `PURGE_DT_TM_ACT` | DATETIME |  |  | The actual date/time when data for the encounter was purged from the database. |
| 130 | `PURGE_DT_TM_EST` | DATETIME |  |  | The estimated date/time when data for the encounter will be purged from the database. |
| 131 | `READMIT_CD` | DOUBLE | NOT NULL |  | Description of the encounter readmit. |
| 132 | `REASON_FOR_VISIT` | VARCHAR(255) |  |  | The free text description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 133 | `REFERRAL_RCVD_DT_TM` | DATETIME |  |  | The date and time the referral was received |
| 134 | `REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | The information indicating the source of referral like provider, friend, web-site, etc. |
| 135 | `REFERRING_COMMENT` | VARCHAR(100) |  |  | A text field containing the comments from the referring physician or service. |
| 136 | `REFER_FACILITY_CD` | DOUBLE | NOT NULL |  | The location of the referring facility. This code set is used at sites that do not have full referral management integration. |
| 137 | `REFER_TO_UNIT_STAFF_CD` | DOUBLE | NOT NULL |  | Indicates if any inquiries regarding the patient need to be redirected to a unit staff member. |
| 138 | `REGION_CD` | DOUBLE | NOT NULL |  | A codified field which indicates the area or region which the encounter was referred. |
| 139 | `REG_DT_TM` | DATETIME |  |  | The date/time that the registration or admission process was performed. In some circumstances this may only involve a minimal amount of data collection to simply get the encounter added to the system for clinical purposes.if the pre_reg_dt_tm is valued, then this field may be null, but will be valued when the patient presents for their visit/appointment. |
| 140 | `REG_PRSNL_ID` | DOUBLE | NOT NULL |  | The internal person ID of the personnel that performed the registration or admission. If the reg_dt_tm is valued, then this field must be valued. |
| 141 | `RESULT_ACCUMULATION_DT_TM` | DATETIME |  |  | Reference date for an encounter that determines the starting point when printing a patient's chart |
| 142 | `RESULT_DEST_CD` | DOUBLE | NOT NULL |  | NOT USED. |
| 143 | `SAFEKEEPING_CD` | DOUBLE | NOT NULL |  | Where or how valuables are being stored. |
| 144 | `SECURITY_ACCESS_CD` | DOUBLE | NOT NULL |  | The security access code is a codified field which identifies the current level of security access the encounter requires. |
| 145 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving for this encounter. |
| 146 | `SERVICE_DT_TM` | DATETIME |  |  | The start or if in the future the anticipated start date of service for the encounter. The service date time is determined per the following date availability: Arrival date/time, Registration date/time, Estimated arrival date/time, and Pre-Registration date/time. |
| 147 | `SERVICE_PROVIDER_ORG_ID` | DOUBLE |  | FK→ | The identifier of the organization (real or virtual) that is primarily responsible for the encounter (owner of the information). |
| 148 | `SEX_CD` | DOUBLE | NOT NULL |  | The gender of the patient (i.e., male, female, unknown). This field will be null where the field encntr_class_cd indicates that this encounter row references a row in the person table. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 149 | `SITTER_REQUIRED_CD` | DOUBLE | NOT NULL |  | A codified field that indicates whether a Personnel is required to sit with the encounter |
| 150 | `SPECIALTY_UNIT_CD` | DOUBLE | NOT NULL |  | The specialty unit associated with the program service |
| 151 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A fundamental category of taxonomic classification, ranking after a genus and consisting of organisms capable of interbreeding. OBSOLETE: SHOULD USE INFORMATION ON THE PERSON TABLE. |
| 152 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 153 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time the transaction, which triggered the history row, occurred. This field can be system assigned or manually manipulated by users. |
| 154 | `TRANSFER_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason the person was transferred or moved from one location to another. |
| 155 | `TRAUMA_CD` | DOUBLE | NOT NULL |  | Type of trauma related to this encounter. |
| 156 | `TRAUMA_DT_TM` | DATETIME |  |  | Date and time the trauma related incident occurred. |
| 157 | `TREATMENT_PHASE_CD` | DOUBLE | NOT NULL |  | Treatment phase (Code Set: 4018002) identifies the current stage of a unit that the encounter is in (i.e. phase 1, phase 2, entry, intermediate). Used to describe the different levels of care as the encounter progresses. A common use would be behavioral health scenarios. |
| 158 | `TRIAGE_CD` | DOUBLE | NOT NULL |  | Describes the triage performed on, or related to, this encounter. |
| 159 | `TRIAGE_DT_TM` | DATETIME |  |  | Date and time the triage occurred. |
| 160 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 161 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 162 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 163 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 164 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 165 | `VALUABLES_CD` | DOUBLE | NOT NULL |  | Type of valuables being kept for the patient. |
| 166 | `VIP_CD` | DOUBLE | NOT NULL |  | The VIP code indicates for this encounter that the person is to be identified and possibly treated with special consideration during the active time of the encounter. (i.e., employee, board member, famous person). |
| 167 | `VISITOR_STATUS_CD` | DOUBLE | NOT NULL |  | Describes the type, or what kind of, visitors the patient wishes to see during their encounter. |
| 168 | `ZERO_BALANCE_DT_TM` | DATETIME |  |  | Date/time when the account balance becomes zero for the encounter. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_ACCESS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CLIENT_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `COMPLETE_REG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DISCH_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PLACE_OF_SVC_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `SERVICE_PROVIDER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

