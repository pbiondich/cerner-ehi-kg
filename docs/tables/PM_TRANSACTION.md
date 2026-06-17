# PM_TRANSACTION

> Audit table for every Person Management transaction. ADMT, TRAN, DSCH...

**Description:** Person Management Transaction Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 264

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date and time the transaction happened |
| 2 | `CURRENT_USER` | CHAR(10) |  |  | Current User of the system when this transaction row was created |
| 3 | `HL7_EVENT` | VARCHAR(10) |  |  | Stores the according HL7_Event. |
| 4 | `N_ACCOM_CD` | DOUBLE | NOT NULL |  | The codeset value for the new accommodation. |
| 5 | `N_ACCOM_REQ_CD` | DOUBLE | NOT NULL |  | Code value representing the new accommodation request. |
| 6 | `N_ADMIT_DOC_ID` | DOUBLE | NOT NULL |  | ID of the new Doctor that admitted the patient. This is a key from the personnel (prsnl) table. |
| 7 | `N_ADMIT_DOC_NAME` | CHAR(30) |  |  | Name of new doctor that admitted the patient. |
| 8 | `N_ADMIT_DOC_NBR` | CHAR(16) |  |  | Doctor Number for the new admitting doctor. |
| 9 | `N_ADMIT_MODE_CD` | DOUBLE | NOT NULL |  | Code value for the new admit. |
| 10 | `N_ADMIT_SRC_CD` | DOUBLE | NOT NULL |  | Code value for the new admit source. |
| 11 | `N_ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value for the new admit type. |
| 12 | `N_ADMIT_WITH_MED_CD` | DOUBLE | NOT NULL |  | Code value for a new admit with medication. |
| 13 | `N_ALT_LVL_CARE_CD` | DOUBLE | NOT NULL |  | New alternate level of care code value. |
| 14 | `N_ALT_RESULT_DEST_CD` | DOUBLE | NOT NULL |  | *** No longer in Use *** |
| 15 | `N_AMB_COND_CD` | DOUBLE | NOT NULL |  | New Ambulatory Condition Code value. Ambulatory condition describes the general physical condition, impairment, or limitation of the patient upon arrival. |
| 16 | `N_ARRIVE_DT_TM` | DATETIME |  |  | Date/Time of new transaction arrival. |
| 17 | `N_ASSIGN_TO_LOC_DT_TM` | DATETIME |  |  | Date and time that the encounter was assigned to a location. |
| 18 | `N_ATTEND_DOC_ID` | DOUBLE | NOT NULL |  | ID of new attending doctor. This is a primary key from the personnel (prsnl) table. |
| 19 | `N_ATTEND_DOC_NAME` | CHAR(30) |  |  | Name of new attending doctor. |
| 20 | `N_ATTEND_DOC_NBR` | CHAR(16) |  |  | Doctor Nuber of new attending doctor |
| 21 | `N_AUTOPSY_CD` | DOUBLE | NOT NULL |  | New Autopsy Code Value |
| 22 | `N_BIRTH_DT_CD` | DOUBLE | NOT NULL |  | New Birth Date Code Value |
| 23 | `N_BIRTH_DT_TM` | DATETIME |  |  | Date/Time of new birth. |
| 24 | `N_CAUSE_OF_DEATH` | CHAR(40) |  |  | New Cause of Death |
| 25 | `N_CHART_ACCESS_ORGANIZATION_ID` | DOUBLE |  | FK→ | New Identifier. The identifying information of the organization (real or vitural) taht indicates which groups of users should have a medical changre access to the encounter. |
| 26 | `N_CITIZENSHIP_CD` | DOUBLE | NOT NULL |  | New Citizenship Code Value. |
| 27 | `N_CMNTY_CASE_CLOSURE_REASON_CD` | DOUBLE | NOT NULL |  | The new community case closure reason. The reason the community case was closed. |
| 28 | `N_CMNTY_CASE_ENROLLMENT_DT_TM` | DATETIME |  |  | The new community case enrollment date and time. The date and time of the patient's enrollment on the community case. |
| 29 | `N_CMNTY_CASE_STATUS_CD` | DOUBLE | NOT NULL |  | The new community case status code. The case status identifies the state of a particular community case from the time it is initiated until it is closed |
| 30 | `N_CONCEPTION_DT_TM` | DATETIME |  |  | Date and Time of a new conception. |
| 31 | `N_CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | New Confidence Level Code Value. |
| 32 | `N_CONSULT_DOC_ID` | DOUBLE | NOT NULL |  | New Consulting Doctor ID. This is a primary key the personnel (prsnl) table. |
| 33 | `N_CONSULT_DOC_NAME` | CHAR(30) |  |  | Name of new consulting doctor. |
| 34 | `N_CONSULT_DOC_NBR` | CHAR(16) |  |  | Doctor Number of new consulting doctor. |
| 35 | `N_CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed |
| 36 | `N_COURTESY_CD` | DOUBLE | NOT NULL |  | This field indicates whether the patient will be extended certain special courtesies such as express discharge, bypassing a stop at the cashiers window upon leaving when financial arrangements are agreed upon in advance. |
| 37 | `N_DECEASED_CD` | DOUBLE | NOT NULL |  | This is a codified cause of death. |
| 38 | `N_DECEASED_DT_TM` | DATETIME |  |  | Date/Time of new deceased transaction. |
| 39 | `N_DEPART_DT_TM` | DATETIME |  |  | New Date/Time of patient departure. |
| 40 | `N_DIET_TYPE_CD` | DOUBLE | NOT NULL |  | New Diet Type Code Value. Diet type is used to indicate that the patient is on a special diet. |
| 41 | `N_DISCH_DISP_CD` | DOUBLE | NOT NULL |  | The conditions under which the patient left the facility at the time of discharge. |
| 42 | `N_DISCH_DT_TM` | DATETIME |  |  | Date/Time of new discharge. |
| 43 | `N_DISCH_TO_LOCTN_CD` | DOUBLE | NOT NULL |  | New Discharge to Location Code Value. The location to which the patient was discharged such as another hospital or nursing home. |
| 44 | `N_ENCNTR_CLASS_CD` | DOUBLE | NOT NULL |  | New Encntr Class Code Value. Encounter class defines how this encounter row is being used in relation to the person table. |
| 45 | `N_ENCNTR_COMPLETE_DT_TM` | DATETIME |  |  | Encounter complete date/time after updates have occurred |
| 46 | `N_ENCNTR_FIN_ID` | DOUBLE | NOT NULL |  | New Encounter Financial Id. This is the value of the unique primary identifier of the encounter financial table. It is an internal system assigned number. |
| 47 | `N_ENCNTR_ID` | DOUBLE | NOT NULL |  | New Encounter ID. This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 48 | `N_ENCNTR_SEX_CD` | DOUBLE | NOT NULL |  | New Encntr Sex Code Value. Code that represents the sex of the patient in a transaction. |
| 49 | `N_ENCNTR_STATUS_CD` | DOUBLE | NOT NULL |  | New Encounterr Status Code. Encounter status identifies the state of a particular encounter type from the time it is initiated until it is complete. (i.e., temporary, preliminary, active, discharged (complete), cancelled). |
| 50 | `N_ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | New Ecounter Type Code. Encounter type such as Inpatient, Outpatient, ER, etc. |
| 51 | `N_ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | New Encounter Type Class Code. Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this codeset all have Cerner defined meanings. |
| 52 | `N_ENCNTR_VIP_CD` | DOUBLE | NOT NULL |  | New Enchounter VIP Code. The VIP code indicates for this encounter that the person is to be identified and possibly treated with special consideration during the active time of the encounter. (i.e., employee, board member, famous person). |
| 53 | `N_EST_ARRIVE_DT_TM` | DATETIME |  |  | New Estimated Arrive Date/Time. |
| 54 | `N_EST_DEPART_DT_TM` | DATETIME |  |  | New Estimated Depart Date/Time |
| 55 | `N_ETHNIC_GRP_CD` | DOUBLE | NOT NULL |  | New Ethnic Group Code Value |
| 56 | `N_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification. Examples may include Worker's Comp, Self Pay, etc. |
| 57 | `N_FIN_NBR` | CHAR(20) |  |  | New Financial Number. |
| 58 | `N_GUAR_TYPE_CD` | DOUBLE | NOT NULL |  | New Guaranotor Type Code. The guarantor type indicates that the guarantor for the encounter is either a person or an organization. This code is used to determine which set of tables to query to find the guarantor. |
| 59 | `N_ISOLATION_CD` | DOUBLE | NOT NULL |  | New Isolation Code. The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 60 | `N_LANGUAGE_CD` | DOUBLE | NOT NULL |  | New Language Code. The code_value identifying the language of the patient. |
| 61 | `N_LANG_DIALECT_CD` | DOUBLE | NOT NULL |  | New Language Dialect Code. The dialect of the primary language spoken by the person. |
| 62 | `N_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | New Location Code. The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 63 | `N_LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | New Location Bed Code. This field is the current patient location with a location type of bed. |
| 64 | `N_LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | New Location Building Code. This field is the current patient location with a location type of building. |
| 65 | `N_LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | New Location Facility Code. This field is the current patient location with a location type of facility. |
| 66 | `N_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | New Location Nurse Unit Code. This field is the current patient location with a location type of Nurse Unit. |
| 67 | `N_LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | New Location Room Code. This field is the current patient location with a location type of room. |
| 68 | `N_LOC_TEMP_CD` | DOUBLE | NOT NULL |  | New Location Temporary Code. This field identifies the temporary location of the patient. The temporary location may be valued at the same time the location_cd is valued. |
| 69 | `N_MARITAL_TYPE_CD` | DOUBLE | NOT NULL |  | New Marital Type Code. This field identifies the status of the person with regard to being married. |
| 70 | `N_MED_SERVICE_CD` | DOUBLE | NOT NULL |  | New Medical Serice Code. The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 71 | `N_MRN` | CHAR(20) |  |  | New Medical Record Number def |
| 72 | `N_MTHR_MAID_NAME` | CHAR(20) |  |  | New Mother's Maiden Name |
| 73 | `N_NAME_FIRST` | CHAR(20) |  |  | New First Name |
| 74 | `N_NAME_FORMATTED` | CHAR(30) |  |  | New Formatted Name |
| 75 | `N_NAME_LAST` | CHAR(20) |  |  | New Last Name |
| 76 | `N_NAME_MIDDLE` | CHAR(20) |  |  | New Middle Name |
| 77 | `N_NATIONALITY_CD` | DOUBLE | NOT NULL |  | New Nationality Code Value. |
| 78 | `N_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID on encounter after updates have occurred |
| 79 | `N_PERSON_BIRTH_SEX_CD` | DOUBLE | NOT NULL |  | The new person birth sex code. The sex, typically determined by biological characteristics such as reproductive anatomy or genetic makeup, assigned at birth for the purposes of birth registration. |
| 80 | `N_PERSON_ID` | DOUBLE | NOT NULL |  | New Person ID. This is a key from the Person table. |
| 81 | `N_PERSON_SEX_CD` | DOUBLE | NOT NULL |  | The new person sex code. The sex/gender that the patient is considered to have for administration and record keeping purposes. this is typically asserted by the patient when they present to administrative users. this may not match the biological sex as determined by anatomy or genetics, or the individual's preferred identification (gender identity). |
| 82 | `N_PERSON_TYPE_CD` | DOUBLE | NOT NULL |  | New Person Type Code. The person type field identifies the general type of data being stored in a given person row. As a general guideline, most rows in the person table will be identifiedwith a person type of PERSON. This field can be used to filter out NON-PERSON rows. |
| 83 | `N_PERSON_VIP_CD` | DOUBLE | NOT NULL |  | New Person VIP Code. The VIP code indicates for this encounter that the person is to be identified and possibly treated with special consideration during the active time of the encounter. (i.e., employee, board member, famous person). |
| 84 | `N_PER_BUS_ADDRESS_ID` | DOUBLE | NOT NULL |  | New Person Business Address ID. This is a primary key in the Address table. |
| 85 | `N_PER_BUS_ADDR_CITY` | CHAR(40) |  |  | New Person Business Address City. |
| 86 | `N_PER_BUS_ADDR_COUNTRY` | CHAR(20) |  |  | New Person Business Address Country |
| 87 | `N_PER_BUS_ADDR_COUNTY` | CHAR(20) |  |  | New Person Business Address County |
| 88 | `N_PER_BUS_ADDR_STATE` | CHAR(20) |  |  | New Person Business Address State |
| 89 | `N_PER_BUS_ADDR_STREET` | CHAR(100) |  |  | New Person Business Address Street |
| 90 | `N_PER_BUS_ADDR_STREET2` | CHAR(100) |  |  | New Person Business Address Street 2 |
| 91 | `N_PER_BUS_ADDR_ZIPCODE` | CHAR(20) |  |  | New Person Business Address Zipcode |
| 92 | `N_PER_BUS_EXT` | CHAR(10) |  |  | New Person Business Extension |
| 93 | `N_PER_BUS_PHONE_ID` | DOUBLE | NOT NULL |  | New Person Business Phone ID used to identify a phone number. |
| 94 | `N_PER_BUS_PH_FORMAT_CD` | DOUBLE | NOT NULL |  | New Person Business Phone Format Code |
| 95 | `N_PER_BUS_PH_NUMBER` | CHAR(20) |  |  | New Person Business Phone Number |
| 96 | `N_PER_HOME_ADDRESS_ID` | DOUBLE | NOT NULL |  | New Person Home Address ID |
| 97 | `N_PER_HOME_ADDR_CITY` | CHAR(40) |  |  | New Person Home Address City |
| 98 | `N_PER_HOME_ADDR_COUNTRY` | CHAR(20) |  |  | New Person Home Address Country |
| 99 | `N_PER_HOME_ADDR_COUNTY` | CHAR(20) |  |  | New Person Home Address County |
| 100 | `N_PER_HOME_ADDR_STATE` | CHAR(20) |  |  | New Person Home Address State |
| 101 | `N_PER_HOME_ADDR_STREET` | CHAR(100) |  |  | New Person Home Address Street |
| 102 | `N_PER_HOME_ADDR_STREET2` | CHAR(100) |  |  | New Person Home Address Street 2 |
| 103 | `N_PER_HOME_ADDR_ZIPCODE` | CHAR(20) |  |  | New Person Home Address Zipcode |
| 104 | `N_PER_HOME_EXT` | CHAR(10) |  |  | New Person Home Extension |
| 105 | `N_PER_HOME_PHONE_ID` | DOUBLE | NOT NULL |  | New Person Home Phone Id |
| 106 | `N_PER_HOME_PH_FORMAT_CD` | DOUBLE | NOT NULL |  | New Person Home Phone Format Code |
| 107 | `N_PER_HOME_PH_NUMBER` | CHAR(20) |  |  | New Person Home Phone Number |
| 108 | `N_PREADMIT_NBR` | CHAR(20) |  |  | New Preadmit Number |
| 109 | `N_PREADMIT_TEST_CD` | DOUBLE | NOT NULL |  | New Preadmit Test Code |
| 110 | `N_PRE_REG_DT_TM` | DATETIME |  |  | New Pre-Registration Date/Time. The date/time that the pre-registration or pre-admission process was performed. If the reg_dt_tm is valued, or no pre-registration occurred, then this field may be null. |
| 111 | `N_PRE_REG_PRSNL_ID` | DOUBLE | NOT NULL |  | New Pre-Registration PersonnelID. The internal person ID of the personnel that performed the pre-registration or pre-admission. If the pre_reg_dt_tm is valued, then this field must be valued. |
| 112 | `N_PROGRAM_SERVICE_CD` | DOUBLE | NOT NULL |  | Code value identifying the new program service associated with the patient registration |
| 113 | `N_RACE_CD` | DOUBLE | NOT NULL |  | New Race Code. The code_value identifying the race of the patient |
| 114 | `N_READMIT_CD` | DOUBLE | NOT NULL |  | New Readmit Code. Value contains a description of the encounter readmit. |
| 115 | `N_REASON_FOR_VISIT` | CHAR(40) |  |  | New Reason For Visit. The free text description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 116 | `N_REFER_COMMENT` | CHAR(40) |  |  | A text field containing the comments from the referring physician or service. |
| 117 | `N_REFER_DOC_ID` | DOUBLE | NOT NULL |  | ID of the new referring doctor. This is a key value from the personnel (prsnl) table. |
| 118 | `N_REFER_DOC_NAME` | CHAR(30) |  |  | Name of the new referring doctor. |
| 119 | `N_REFER_DOC_NBR` | CHAR(16) |  |  | Nubmer of the new referring doctor. |
| 120 | `N_REG_DT_TM` | DATETIME |  |  | New Registration Date/Time. The date/time that the registration or admission process was performed. If the pre_reg_dt_tm is valued, then this field may be null, but will be valued when the patient presents for their visit/appointment. |
| 121 | `N_REG_PRSNL_ID` | DOUBLE | NOT NULL |  | New Registration PersonnelID. The internal person ID of the personnel that performed the registration or admission. If the reg_dt_tm is valued, then this field must be valued. |
| 122 | `N_RELIGION_CD` | DOUBLE | NOT NULL |  | New Religion Code. The code_value identifying the religion of the patient. |
| 123 | `N_RESULT_DEST_CD` | DOUBLE | NOT NULL |  | *** No longer in Use *** |
| 124 | `N_SEX_AGE_CHG_IND` | DOUBLE |  |  | New Sex Age Change Indicator. This field indicates that the sex of the person has changed as the result of a correction of the data or actual physical change to the person. |
| 125 | `N_SPECIES_CD` | DOUBLE | NOT NULL |  | New Species Code. A fundamental category of taxonomic classification, ranking after a genus and consisting of organisms capable of interbreeding. |
| 126 | `N_SSN` | CHAR(15) |  |  | New Social Security Number |
| 127 | `N_VET_MIL_STAT_CD` | DOUBLE | NOT NULL |  | New Veterans Military Status Code. |
| 128 | `O_ACCOM_CD` | DOUBLE | NOT NULL |  | The codeset value for the old accommodation. |
| 129 | `O_ACCOM_REQ_CD` | DOUBLE | NOT NULL |  | Code value representing the old accommodation request. |
| 130 | `O_ADMIT_DOC_ID` | DOUBLE | NOT NULL |  | ID of the old Doctor that admitted the patient. This is a key from the personnel (prsnl) table. |
| 131 | `O_ADMIT_DOC_NAME` | CHAR(30) |  |  | Name of old doctor that admitted the patient. |
| 132 | `O_ADMIT_DOC_NBR` | CHAR(16) |  |  | Doctor Number for the old admitting doctor. |
| 133 | `O_ADMIT_MODE_CD` | DOUBLE | NOT NULL |  | Code value for the old admit. |
| 134 | `O_ADMIT_SRC_CD` | DOUBLE | NOT NULL |  | Code value for the old admit source. |
| 135 | `O_ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value for the old admit type. |
| 136 | `O_ADMIT_WITH_MED_CD` | DOUBLE | NOT NULL |  | Code value for an old admit with medication. |
| 137 | `O_ALT_LVL_CARE_CD` | DOUBLE | NOT NULL |  | Old alternate level of care code value. |
| 138 | `O_ALT_RESULT_DEST_CD` | DOUBLE | NOT NULL |  | *** No longer in Use *** |
| 139 | `O_AMB_COND_CD` | DOUBLE | NOT NULL |  | Old Ambulatory Condition Code Value. Ambulatory condition describes the general physical condition, impairment, or limitation of the patient upon arrival. |
| 140 | `O_ARRIVE_DT_TM` | DATETIME |  |  | Date/Time of old transaction arrival. |
| 141 | `O_ASSIGN_TO_LOC_DT_TM` | DATETIME |  |  | Date and time that the encounter was assigned to a location. |
| 142 | `O_ATTEND_DOC_ID` | DOUBLE | NOT NULL |  | ID of old attending doctor. This is a primary key from the personnel (prsnl) table. |
| 143 | `O_ATTEND_DOC_NAME` | CHAR(30) |  |  | Name of old attending doctor. |
| 144 | `O_ATTEND_DOC_NBR` | CHAR(16) |  |  | Doctor number of new attending doctor. |
| 145 | `O_AUTOPSY_CD` | DOUBLE | NOT NULL |  | Old Autopsy Code Value. |
| 146 | `O_BIRTH_DT_CD` | DOUBLE | NOT NULL |  | New Birth Date Code Value. |
| 147 | `O_BIRTH_DT_TM` | DATETIME |  |  | Date/Time of new birth. |
| 148 | `O_CAUSE_OF_DEATH` | CHAR(40) |  |  | Old Cause of Death |
| 149 | `O_CHART_ACCESS_ORGANIZATION_ID` | DOUBLE |  | FK→ | Old Identifier. The identifying information of the orgainzation (real or virtual) that indicates which groups of users should have medical chart access to the encounter. |
| 150 | `O_CITIZENSHIP_CD` | DOUBLE | NOT NULL |  | Old Citizenship Code value. |
| 151 | `O_CMNTY_CASE_CLOSURE_REASON_CD` | DOUBLE | NOT NULL |  | The old community case closure reason. The reason the community case was closed. |
| 152 | `O_CMNTY_CASE_ENROLLMENT_DT_TM` | DATETIME |  |  | The old community case enrollment date and time. The date and time of the patient's enrollment on the community case. |
| 153 | `O_CMNTY_CASE_STATUS_CD` | DOUBLE | NOT NULL |  | The old community case status code. The case status identifies the state of a particular community case from the time it is initiated until it is closed |
| 154 | `O_CONCEPTION_DT_TM` | DATETIME |  |  | Date and time of old conception. |
| 155 | `O_CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | Old Confidence Level Code Value. |
| 156 | `O_CONSULT_DOC_ID` | DOUBLE | NOT NULL |  | Old Consulting Doctor ID. This is a primary key the perosnel (prsnl) table. |
| 157 | `O_CONSULT_DOC_NAME` | CHAR(30) |  |  | Name of old consulting doctor. |
| 158 | `O_CONSULT_DOC_NBR` | CHAR(16) |  |  | Doctor number of old consulting doctor. |
| 159 | `O_CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | OId contributor system code. Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed |
| 160 | `O_COURTESY_CD` | DOUBLE | NOT NULL |  | Old Courtesy Code value. This field indicates whether the patient will be extended certain special courtesies such as express discharge, bypassing a stop at the cashiers window upon leaving when financial arrangements are agreed upon in advance. |
| 161 | `O_DECEASED_CD` | DOUBLE | NOT NULL |  | This is the old codified cause of death. |
| 162 | `O_DECEASED_DT_TM` | DATETIME |  |  | Date/Time of old deceased transaction. |
| 163 | `O_DEPART_DT_TM` | DATETIME |  |  | Old date/time of patient departure. |
| 164 | `O_DIET_TYPE_CD` | DOUBLE | NOT NULL |  | Old Diet Type Code Value. Diet type is used to indicate that the patient is on a special diet. |
| 165 | `O_DISCH_DISP_CD` | DOUBLE | NOT NULL |  | The conditions under which the patient left the facility at the time of discharge. |
| 166 | `O_DISCH_DT_TM` | DATETIME |  |  | Date/Time of new discharge. |
| 167 | `O_DISCH_TO_LOCTN_CD` | DOUBLE | NOT NULL |  | Old Discharge to Location Code Value. The location to which the patient was discharged such as another hospital or nursing home. |
| 168 | `O_ENCNTR_CLASS_CD` | DOUBLE | NOT NULL |  | Old Encntr Class Code Value. Encounter class defines how this encounter row is being used in relation to the person table. |
| 169 | `O_ENCNTR_COMPLETE_DT_TM` | DATETIME |  |  | Encounter Complete Date/Time Prior to update |
| 170 | `O_ENCNTR_FIN_ID` | DOUBLE | NOT NULL | FK→ | Old Encounter Financial Id. This is the value of the unique primary identifier of the encounter financial table. It is an internal system assigned number. |
| 171 | `O_ENCNTR_ID` | DOUBLE | NOT NULL |  | Old Encounter ID. This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 172 | `O_ENCNTR_SEX_CD` | DOUBLE | NOT NULL |  | Old Encntr Sex Code Value. Code that represents the sex of the patient in a transaction. |
| 173 | `O_ENCNTR_STATUS_CD` | DOUBLE | NOT NULL |  | Old Encounterr Status Code. Encounter status identifies the state of a particular encounter type from the time it is initiated until it is complete. (i.e., temporary, preliminary, active, discharged (complete), cancelled). |
| 174 | `O_ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Old Ecounter Type Code. Encounter type such as Inpatient, Outpatient, ER, etc. |
| 175 | `O_ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Old Encounter Type Class Code. Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this codeset all have Cerner defined meanings. |
| 176 | `O_ENCNTR_VIP_CD` | DOUBLE | NOT NULL |  | Old Encounter VIP Code. The VIP code indicates for this encounter that the person is to be identified and possibly treated with special consideration during the active time of the encounter. (i.e., employee, board member, famous person). |
| 177 | `O_EST_ARRIVE_DT_TM` | DATETIME |  |  | Old Estimated Arrive Date/Time |
| 178 | `O_EST_DEPART_DT_TM` | DATETIME |  |  | Old Estimated Depart Date/Time |
| 179 | `O_ETHNIC_GRP_CD` | DOUBLE | NOT NULL |  | Old Ethnic Group Code Value |
| 180 | `O_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification. Examples may include Worker's Comp, Self Pay, etc.. |
| 181 | `O_FIN_NBR` | CHAR(20) |  |  | Old Financial Number |
| 182 | `O_GUAR_TYPE_CD` | DOUBLE | NOT NULL |  | Old Guaranotor Type Code. The guarantor type indicates that the guarantor for the encounter is either a person or an organization. This code is used to determine which set of tables to query to find the guarantor. |
| 183 | `O_ISOLATION_CD` | DOUBLE | NOT NULL |  | Old Isolation Code. The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 184 | `O_LANGUAGE_CD` | DOUBLE | NOT NULL |  | Old Language Code. The code_value identifying the language of the patient |
| 185 | `O_LANG_DIALECT_CD` | DOUBLE | NOT NULL |  | Old Language Dialect Code. The dialect of the primary language spoken by the person. |
| 186 | `O_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Old Location Code. The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 187 | `O_LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | Old Location Bed Code. This field is the current patient location with a location type of bed. |
| 188 | `O_LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | Old Location Building Code. This field is the current patient location with a location type of building. |
| 189 | `O_LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Old Location Facility Code. This field is the current patient location with a location type of facility. |
| 190 | `O_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Old Location Nurse Unit Code. This field is the current patient location with a location type of Nurse Unit. |
| 191 | `O_LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | Old Location Room Code. This field is the current patient location with a location type of room. |
| 192 | `O_LOC_TEMP_CD` | DOUBLE | NOT NULL |  | Old Location Temporary Code. This field identifies the temporary location of the patient. The temporary location may be valued at the same time the location_cd is valued. |
| 193 | `O_MARITAL_TYPE_CD` | DOUBLE | NOT NULL |  | Old Marital Type Code. This field identifies the status of the person with regard to being married. |
| 194 | `O_MED_SERVICE_CD` | DOUBLE | NOT NULL |  | Old Medical Serice Code. The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 195 | `O_MRN` | CHAR(20) |  |  | Old Medical Record Number |
| 196 | `O_MTHR_MAID_NAME` | CHAR(20) |  |  | Old Mother's Maiden Name |
| 197 | `O_NAME_FIRST` | CHAR(20) |  |  | Old First Name |
| 198 | `O_NAME_FORMATTED` | CHAR(30) |  |  | Old Name Formatted |
| 199 | `O_NAME_LAST` | CHAR(20) |  |  | Old Name Last |
| 200 | `O_NAME_MIDDLE` | CHAR(20) |  |  | Old Name Middle |
| 201 | `O_NATIONALITY_CD` | DOUBLE | NOT NULL |  | Old Nationality Code Value |
| 202 | `O_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID on encounter before updates |
| 203 | `O_PERSON_BIRTH_SEX_CD` | DOUBLE | NOT NULL |  | The old person birth sex code. The sex, typically determined by biological characteristics such as reproductive anatomy or genetic makeup, assigned at birth for the purposes of birth registration. |
| 204 | `O_PERSON_ID` | DOUBLE | NOT NULL |  | Old Person Id. This is a key from the Person table. |
| 205 | `O_PERSON_SEX_CD` | DOUBLE | NOT NULL |  | The old person sex code. The sex/gender that the patient is considered to have for administration and record keeping purposes. this is typically asserted by the patient when they present to administrative users. this may not match the biological sex as determined by anatomy or genetics, or the individual's preferred identification (gender identity). |
| 206 | `O_PERSON_TYPE_CD` | DOUBLE | NOT NULL |  | Old Person Type Code. The person type field identifies the general type of data being stored in a given person row. As a general guideline, most rows in the person table will be identifiedwith a person type of PERSON. This field can be used to filter out NON-PERSON rows. |
| 207 | `O_PERSON_VIP_CD` | DOUBLE | NOT NULL |  | Old Person VIP Code. The VIP code indicates for this encounter that the person is to be identified and possibly treated with special consideration during the active time of the encounter. (i.e., employee, board member, famous person). |
| 208 | `O_PER_BUS_ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | Old Person Business Address ID. This is a primary key in the Address table. |
| 209 | `O_PER_BUS_ADDR_CITY` | CHAR(40) |  |  | Old Person Business Address City |
| 210 | `O_PER_BUS_ADDR_COUNTRY` | CHAR(20) |  |  | Old Person Business Address Country |
| 211 | `O_PER_BUS_ADDR_COUNTY` | CHAR(20) |  |  | Old Person Business Address County |
| 212 | `O_PER_BUS_ADDR_STATE` | CHAR(20) |  |  | Old Person Business Address State |
| 213 | `O_PER_BUS_ADDR_STREET` | CHAR(100) |  |  | Old Person Business Address Street |
| 214 | `O_PER_BUS_ADDR_STREET2` | CHAR(100) |  |  | Old Person Business Address Street 2 |
| 215 | `O_PER_BUS_ADDR_ZIPCODE` | CHAR(20) |  |  | Old Person Business Address Zipcode |
| 216 | `O_PER_BUS_EXT` | CHAR(10) |  |  | Old Person Business Phone Extension |
| 217 | `O_PER_BUS_PHONE_ID` | DOUBLE | NOT NULL | FK→ | Old Person Business Phone ID used to identify a phone number. |
| 218 | `O_PER_BUS_PH_FORMAT_CD` | DOUBLE | NOT NULL |  | Old Person Business Phone Format Code. |
| 219 | `O_PER_BUS_PH_NUMBER` | CHAR(20) |  |  | Old Person Business Phone Number. |
| 220 | `O_PER_HOME_ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | Old Person Home Address ID |
| 221 | `O_PER_HOME_ADDR_CITY` | CHAR(40) |  |  | Old Person Home Address City |
| 222 | `O_PER_HOME_ADDR_COUNTRY` | CHAR(20) |  |  | Old Person Home Address Country |
| 223 | `O_PER_HOME_ADDR_COUNTY` | CHAR(20) |  |  | Old Person Home Address County |
| 224 | `O_PER_HOME_ADDR_STATE` | CHAR(20) |  |  | Old Person Home Address State |
| 225 | `O_PER_HOME_ADDR_STREET` | CHAR(100) |  |  | Old Person Home Address Street |
| 226 | `O_PER_HOME_ADDR_STREET2` | CHAR(100) |  |  | Old Person Home Address Street 2 |
| 227 | `O_PER_HOME_ADDR_ZIPCODE` | CHAR(20) |  |  | Old Person Home Address Zipcode |
| 228 | `O_PER_HOME_EXT` | CHAR(10) |  |  | Old Person Home Extension |
| 229 | `O_PER_HOME_PHONE_ID` | DOUBLE | NOT NULL | FK→ | Old Person Home Phone Id |
| 230 | `O_PER_HOME_PH_FORMAT_CD` | DOUBLE | NOT NULL |  | Old Person Home Phone Format Code. |
| 231 | `O_PER_HOME_PH_NUMBER` | CHAR(20) |  |  | Old Person Home Phone Number |
| 232 | `O_PREADMIT_NBR` | CHAR(20) |  |  | Old Preadmit Number. |
| 233 | `O_PREADMIT_TEST_CD` | DOUBLE | NOT NULL |  | Old Preadmit Test Code. |
| 234 | `O_PRE_REG_DT_TM` | DATETIME |  |  | Old Pre-Registration Date/Time. The date/time that the pre-registration or pre-admission process was performed. If the reg_dt_tm is valued, or no pre-registration occurred, then this field may be null. |
| 235 | `O_PRE_REG_PRSNL_ID` | DOUBLE | NOT NULL |  | Old Pre-Registration PersonnelID. The internal person ID of the personnel that performed the pre-registration or pre-admission. If the pre_reg_dt_tm is valued, then this field must be valued. |
| 236 | `O_PROGRAM_SERVICE_CD` | DOUBLE | NOT NULL |  | Code value identifying the old program service associated with the patient registration |
| 237 | `O_RACE_CD` | DOUBLE | NOT NULL |  | Old Race Code. The code_value identifying the race of the patient. |
| 238 | `O_READMIT_CD` | DOUBLE | NOT NULL |  | Old Readmit Code. Value contains a description of the encounter readmit. |
| 239 | `O_REASON_FOR_VISIT` | CHAR(40) |  |  | Old Reason For Visit. The free text description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 240 | `O_REFER_COMMENT` | CHAR(40) |  |  | A text field containing the comments from the referring physician or service. |
| 241 | `O_REFER_DOC_ID` | DOUBLE | NOT NULL |  | ID of the old referring doctor. This is a key value from the personnel (prsnl) table. |
| 242 | `O_REFER_DOC_NAME` | CHAR(30) |  |  | Name of the old referring doctor. |
| 243 | `O_REFER_DOC_NBR` | CHAR(16) |  |  | Number of the old referring doctor. |
| 244 | `O_REG_DT_TM` | DATETIME |  |  | Old Registration Date/Time. The date/time that the registration or admission process was performed. If the pre_reg_dt_tm is valued, then this field may be null, but will be valued when the patient presents for their visit/appointment. |
| 245 | `O_REG_PRSNL_ID` | DOUBLE | NOT NULL |  | Old Registration PersonnelID. The internal person ID of the personnel that performed the registration or admission. If the reg_dt_tm is valued, then this field must be valued. |
| 246 | `O_RELIGION_CD` | DOUBLE | NOT NULL |  | Old Religion Code. The code_value identifying the religion of the patient. |
| 247 | `O_RESULT_DEST_CD` | DOUBLE | NOT NULL |  | *** No longer in Use *** |
| 248 | `O_SEX_AGE_CHG_IND` | DOUBLE |  |  | Old Sex Age Change Indicator. This field indicates that the sex of the person has changed as the result of a correction of the data or actual physical change to the person. |
| 249 | `O_SPECIES_CD` | DOUBLE | NOT NULL |  | Old Species Code. A fundamental category of taxonomic classification, ranking after a genus and consisting of organisms capable of interbreeding. |
| 250 | `O_SSN` | CHAR(15) |  |  | Old Social Security Number. |
| 251 | `O_VET_MIL_STAT_CD` | DOUBLE | NOT NULL |  | Old Veteran Military Status Code Value |
| 252 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Contains the foreign key to the history tracking table identifying the associated history row. |
| 253 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the PM_RPT_REPORT table identifying the report that was ran |
| 254 | `REPORT_NAME` | CHAR(20) |  |  | Free-text Name of the report that was ran |
| 255 | `TASK_NUMBER` | DOUBLE |  |  | The task_number of the application that created the transaction row. |
| 256 | `TRANSACTION` | CHAR(4) | NOT NULL |  | Type of transaction that occurred. Example: UPDT, ATDS, etc. |
| 257 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Unique identifier of the transaction. |
| 258 | `TRANSACTION_REASON` | VARCHAR(100) |  |  | Text that describes the reason for the transaction. |
| 259 | `TRANSACTION_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason for the transaction. |
| 260 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 261 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 262 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 263 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 264 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `N_CHART_ACCESS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `N_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `N_LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `N_LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `N_LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `N_LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `N_LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `N_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `O_CHART_ACCESS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `O_ENCNTR_FIN_ID` | [ENCNTR_FINANCIAL](ENCNTR_FINANCIAL.md) | `ENCNTR_FINANCIAL_ID` |
| `O_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `O_LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `O_LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `O_LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `O_LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `O_LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `O_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `O_PER_BUS_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `O_PER_BUS_PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `O_PER_HOME_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `O_PER_HOME_PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `REPORT_ID` | [PM_RPT_REPORT](PM_RPT_REPORT.md) | `REPORT_ID` |

