# HF_R_SYNDROMIC

> BLANK

**Description:** HF_R_SYNDROMIC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 203

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMISSION_REASON` | VARCHAR(255) |  |  | If the person was admitted as Inpatient particularly from the emergency room, this is the physician textual reason for admission. |
| 2 | `ADMISSION_SOURCE_CODE` | VARCHAR(12) |  |  | The mapped admission source PHINVads concept value. |
| 3 | `ADMISSION_SOURCE_CODE_DESC` | VARCHAR(60) |  |  | The mapped admission source PHINVads concept description. |
| 4 | `ADMISSION_TYPE_CODE_DESC` | VARCHAR(60) |  |  | The mapped admission type PHINVads concept description. |
| 5 | `ADMISSION_TYPE_CONCEPT` | VARCHAR(10) |  |  | The mapped admission type PHINVads concept value. |
| 6 | `ADMITTED_TO_ER_IND` | DOUBLE |  |  | Not valid any longer. This is a flag that says if the visit came through the Emergency room: 1 is yes, 0 is no, and blank is unknown. |
| 7 | `ADMITTING_DIAGNOSIS_1_DESC` | VARCHAR(255) |  |  | Free text admitting diagnosis 1 from the encounter. |
| 8 | `ADMITTING_DIAGNOSIS_2_DESC` | VARCHAR(255) |  |  | Free text admitting diagnosis 2 from the encounter. |
| 9 | `ADMITTING_DIAGNOSIS_3_DESC` | VARCHAR(255) |  |  | Free text admitting diagnosis 3 from the encounter. |
| 10 | `ADMIT_DIAGNOSIS_DESC` | VARCHAR(2000) |  |  | A list of codified admitting diagnoses from the diagnosis table. This text field contains the codes and descriptions separated by a delimiter if there are more than one. |
| 11 | `ADMIT_DIAGNOSIS_DT_TM_TXT` | VARCHAR(2000) |  |  | The dates for the admitting diagnoses from the diagnosis table. |
| 12 | `ADMIT_DIAG_DTTM_ICD10` | VARCHAR(2000) |  |  | Admitting diagnosis date times for the ICD-10 codes. |
| 13 | `ADMIT_DIAG_ICD10` | VARCHAR(2000) |  |  | ICD-10 diagnosis codes and descriptions for admitting diagnoses separated by delimiters. |
| 14 | `ADMIT_DT_TM` | DATETIME |  |  | The date in which the patient was registered. |
| 15 | `ADMIT_PHSYICIAN_NAME` | VARCHAR(100) |  |  | The admitting physician's name. |
| 16 | `ADMIT_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The admitting physician's address. |
| 17 | `ADMIT_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The admitting physician's city. |
| 18 | `ADMIT_PHYSICIAN_COUNTRY` | VARCHAR(100) |  |  | The admitting physician's country. |
| 19 | `ADMIT_PHYSICIAN_COUNTY` | VARCHAR(100) |  |  | The admitting physician's county. |
| 20 | `ADMIT_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The email of the admitting physician. |
| 21 | `ADMIT_PHYSICIAN_EXTENSION` | VARCHAR(100) |  |  | The admitting physician's phone extension. |
| 22 | `ADMIT_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The fax number of the admitting physician. |
| 23 | `ADMIT_PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | The admitting physician first name. |
| 24 | `ADMIT_PHYSICIAN_INITIALS` | VARCHAR(100) |  |  | The admitting physician name initials. |
| 25 | `ADMIT_PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | The admitting physician first name. |
| 26 | `ADMIT_PHYSICIAN_MIDDLE_NAME` | VARCHAR(100) |  |  | The admitting physician middle name. |
| 27 | `ADMIT_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The mobile phone number of the admitting physician. |
| 28 | `ADMIT_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The admitting physician NPI. |
| 29 | `ADMIT_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The admitting physician's primary phone number. |
| 30 | `ADMIT_PHYSICIAN_PREFIX` | VARCHAR(100) |  |  | The admitting physician name prefix. |
| 31 | `ADMIT_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The admitting physician's state. |
| 32 | `ADMIT_PHYSICIAN_SUFFIX` | VARCHAR(100) |  |  | The admitting physician name suffix. |
| 33 | `ADMIT_PHYSICIAN_TITLE` | VARCHAR(100) |  |  | The admitting physician name title. |
| 34 | `ADMIT_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code of the admitting physician. |
| 35 | `ADMIT_TM_ZN` | DOUBLE |  |  | The time zone in which the admission occurred. |
| 36 | `AD_PHYSICIAN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the admitting physician's number. |
| 37 | `AGE_IN_MONTHS` | DOUBLE |  |  | The age represent in months if the person if less than 2 years old. |
| 38 | `AGE_IN_YEARS` | DOUBLE |  |  | The age in years of the patient at time of registration. |
| 39 | `ARRIVAL_MODE_CODE` | VARCHAR(10) |  |  | Admit mode code which identifies the method by which the patient arrived. (i.e., helicopter, ambulance, etc.) |
| 40 | `ARRIVAL_MODE_DESC` | VARCHAR(100) |  |  | Admit mode description which identifies the method by which the patient arrived. (i.e., helicopter, ambulance, etc.) |
| 41 | `ATTEND_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The address of the attending physician. |
| 42 | `ATTEND_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The city of the attending physician. |
| 43 | `ATTEND_PHYSICIAN_COUNTRY` | VARCHAR(100) |  |  | The attending physician's country. |
| 44 | `ATTEND_PHYSICIAN_COUNTY` | VARCHAR(100) |  |  | The attending physician's county. |
| 45 | `ATTEND_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The email of the attending physician. |
| 46 | `ATTEND_PHYSICIAN_EXTENSION` | VARCHAR(100) |  |  | The attending physician's phone extension. |
| 47 | `ATTEND_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The fax number of the attending physician. |
| 48 | `ATTEND_PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | The attending physician first name. |
| 49 | `ATTEND_PHYSICIAN_INITIALS` | VARCHAR(100) |  |  | The attending physician name initials. |
| 50 | `ATTEND_PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | The attending physician last name. |
| 51 | `ATTEND_PHYSICIAN_MIDDLE_NAME` | VARCHAR(100) |  |  | The attending physician middle name. |
| 52 | `ATTEND_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The mobile phone number of the attending physician. |
| 53 | `ATTEND_PHYSICIAN_NAME` | VARCHAR(100) |  |  | The name of the attending physician. |
| 54 | `ATTEND_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The attending physician NPI. |
| 55 | `ATTEND_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The primary phone number of the attending physician. |
| 56 | `ATTEND_PHYSICIAN_PREFIX` | VARCHAR(100) |  |  | The attending physician name prefix. |
| 57 | `ATTEND_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The State of the attending physician. |
| 58 | `ATTEND_PHYSICIAN_SUFFIX` | VARCHAR(100) |  |  | The attending physician name suffix. |
| 59 | `ATTEND_PHYSICIAN_TITLE` | VARCHAR(100) |  |  | The attending physician name title. |
| 60 | `ATTEND_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code of the attending physician. |
| 61 | `AT_PHYSICIAN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the attending physician's number. |
| 62 | `BIRTH_DT_TM` | DATETIME |  |  | The patient's birth date. |
| 63 | `CARESETTING_DESC` | VARCHAR(40) |  |  | The mapped caresetting for the admitting location. |
| 64 | `CHIEF_COMPLAINT_CODE_TXT` | VARCHAR(2000) |  |  | Some chief complaints have code field. |
| 65 | `CHIEF_COMPLAINT_TXT` | VARCHAR(255) |  |  | A free text field that should contain the persons point of view of why they presented for this visit. |
| 66 | `CHIEF_COMPLAINT_VERF_DT_TM` | DATETIME |  |  | The clinical event verified date for chief complaint being entered. |
| 67 | `CLIA_NBR` | VARCHAR(10) |  |  | The admitting hospital CLIA number. |
| 68 | `CLINICAL_IMPRESSION_TXT` | VARCHAR(255) |  |  | A free text field containing the clinical impression which are the physicians additional impressions not captured per other diagnostic fields. |
| 69 | `COUNTY_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital three digit county FIPS code. |
| 70 | `CPT_PROCEDURE_CODE` | VARCHAR(2000) |  |  | If there are CPT procedures, this field contains the procedure codes separated by a delimiter. |
| 71 | `CPT_PROCEDURE_DESC` | VARCHAR(2000) |  |  | If there are CPT procedures, this field contains the procedure descriptions separated by a delimiter. |
| 72 | `CPT_PROCEDURE_DT_TM_TXT` | VARCHAR(2000) |  |  | If there are CPT procedures, this field contains the procedure date times separated by a delimiter. |
| 73 | `DECEASED_DT_TM` | DATETIME |  |  | The person's date of death. |
| 74 | `DISCHARGED_DT_TM` | DATETIME |  |  | The patient's medical record number. |
| 75 | `DISCHARGE_DIAGNOSIS_DESC` | VARCHAR(2000) |  |  | The codes and descriptions for the discharge ICD-9 diagnoses separated by delimiters. |
| 76 | `DISCHARGE_DIAGNOSIS_DT_TM_TXT` | VARCHAR(2000) |  |  | The date and time for the discharge ICD-9 diagnoses separated by delimiters. |
| 77 | `DISCHARGE_DIAG_DTTM_ICD10` | VARCHAR(2000) |  |  | Discharge diagnosis date times for the ICD-10 codes. |
| 78 | `DISCHARGE_DIAG_ICD10` | VARCHAR(2000) |  |  | ICD-10 diagnosis codes and descriptions for discharge diagnoses separated by delimiters. |
| 79 | `DISCHARGE_DISP_DESC` | VARCHAR(190) |  |  | The mapped description for discharge disposition. |
| 80 | `DISCHG_DISP_CODE` | DOUBLE |  |  | The standard code for the discharge disposition. |
| 81 | `ENCOUNTER_ID` | DOUBLE |  |  | The encounter unique identifier used within the Cerner Health Facts Data Warehouse. This is the visit identifier for the patient that this record is associated. This number is unique to the patient. |
| 82 | `ETHNICITY` | VARCHAR(40) |  |  | The mapped ethnicity for the person. Identifies a religious national racial or cultural group of the person. |
| 83 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time of the contributor extraction of data. |
| 84 | `FINAL_DIAGNOSIS_DESC` | VARCHAR(2000) |  |  | The ICD-9 final diagnosis codes and descriptions separated by delimiters. |
| 85 | `FINAL_DIAGNOSIS_DT_TM_TXT` | VARCHAR(2000) |  |  | The ICD-9 final diagnosis date/times separated by delimiters. |
| 86 | `FINAL_DIAG_DTTM_ICD10` | VARCHAR(2000) |  |  | Final diagnosis date times for the ICD-10 codes. |
| 87 | `FINAL_DIAG_ICD10` | VARCHAR(2000) |  |  | ICD-10 diagnosis codes and descriptions for final diagnoses separated by delimiters. |
| 88 | `FINANCIAL_NBR` | VARCHAR(40) |  |  | This number identifies the encounter or visit typically for financial and medical record identification. This financial number should be unique per encounter and crosses clinical and billing systems. |
| 89 | `FINANCIAL_NBR_RAW` | VARCHAR(40) |  |  | This unformatted number identifies the encounter or visit typically for financial and medical record identification. This financial number should be unique per encounter and crosses clinical and billing systems. |
| 90 | `GENDER` | VARCHAR(60) |  |  | The gender of the patient. |
| 91 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | The health system that the hospital belongs to. |
| 92 | `HEIGHT` | DOUBLE |  |  | Height value from clinical events. |
| 93 | `HEIGHT_TYPE` | VARCHAR(60) |  |  | The mapped type of height such as Height, Height Estimated, Height Measured. |
| 94 | `HEIGHT_UNIT_DESC` | VARCHAR(60) |  |  | The mapped long description for the height unit of measurement. |
| 95 | `HEIGHT_UNIT_DISPLAY` | VARCHAR(60) |  |  | The abbreviation or short display of the mapped unit. UCUM abbreviation. |
| 96 | `HEIGHT_UNIT_UCUM` | VARCHAR(250) |  |  | The standard UCUM description for the person's initial height unit of measure. |
| 97 | `HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | The address of the hospital as defined by HealthSentry. |
| 98 | `HOSPITAL_CITY` | VARCHAR(50) |  |  | The city of the hospital as defined by HealthSentry. |
| 99 | `HOSPITAL_CODE` | DOUBLE |  |  | The hospital code. |
| 100 | `HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display value of the hospital name. |
| 101 | `HOSPITAL_ID` | DOUBLE |  |  | The unique identifier of the hospital from the hf_d_hospital. Assigned per the organization roll up for the ordering facility. |
| 102 | `HOSPITAL_NAME` | VARCHAR(50) |  |  | The name of the admitting hospital as defined by HealthSentry. |
| 103 | `HOSPITAL_OID` | VARCHAR(100) |  |  | The OID (HL7 Object Identifier) for the facility. http://www.hl7.org/oid/index.cfm |
| 104 | `HOSPITAL_PHONE` | VARCHAR(30) |  |  | The primary phone number of the hospital as defined by HealthSentry. |
| 105 | `HOSPITAL_STATE` | VARCHAR(2) |  |  | The state of the hospital as defined by HealthSentry. |
| 106 | `HOSPITAL_UNIT_ID` | VARCHAR(40) |  |  | The Health Data internal ID from hf_d_caresetting for the admitting nursing unit location. |
| 107 | `HOSPITAL_ZIP` | VARCHAR(25) |  |  | The zip code of the hospital as defined by HealthSentry. |
| 108 | `INITIAL_DIASTOLIC_BP_VALUE` | DOUBLE |  |  | The initial diastolic blood pressure value. |
| 109 | `INITIAL_ED_ACUITY_TXT` | VARCHAR(255) |  |  | A free text field from clinical events describing the ED Acuity. |
| 110 | `INITIAL_PULSE_OXIMETRY_VALUE` | DOUBLE |  |  | The initial pulse oximetry value. |
| 111 | `INITIAL_PULSE_OX_UNIT_DESC` | VARCHAR(60) |  |  | The unit of measure long description for the initial pulse oximetry. |
| 112 | `INITIAL_PULSE_OX_UNIT_DISPLAY` | VARCHAR(60) |  |  | The unit of measure display abbreviation for the initial pulse oximetry or SPO2. |
| 113 | `INITIAL_PULSE_OX_UNIT_UCUM` | VARCHAR(250) |  |  | The standard UCUM description for the initial pulse oximetry unit of measure. |
| 114 | `INITIAL_SYSTOLIC_BP_VALUE` | DOUBLE |  |  | The initial systolic blood pressure value. |
| 115 | `INITIAL_TEMPERATURE_UNIT_DESC` | VARCHAR(60) |  |  | The unit of measure long description for the initial temperature. |
| 116 | `INITIAL_TEMPERATURE_VALUE` | DOUBLE |  |  | The initial temperature value. |
| 117 | `INITIAL_TEMP_UNIT_DISPLAY` | VARCHAR(60) |  |  | The unit of measure display abbreviation for the initial temperature. |
| 118 | `INITIAL_TEMP_UNIT_UCUM` | VARCHAR(250) |  |  | The standard UCUM description for the person's initial temperature unit of measure. |
| 119 | `MAPPED_PAYER_CODE_DESC` | VARCHAR(100) |  |  | The insurance payer two digit character code per PHINVads. |
| 120 | `MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | The patient's medical record number. |
| 121 | `MEDICAL_RECORD_NBR_RAW` | VARCHAR(40) |  |  | The unformatted patient medical record number. |
| 122 | `MEDICAL_SERVICE_CODE` | VARCHAR(40) |  |  | A PHINVads standard abbreviation for the type of medical service for the visit. |
| 123 | `MEDICAL_SERVICE_DESC` | VARCHAR(100) |  |  | A PHINVads standard description for the type of medical service for the visit. |
| 124 | `MEDICAL_SERVICE_ID` | DOUBLE |  |  | The unique identifier for the type or category of medical service that was received. |
| 125 | `MOBILE_NUMBER` | VARCHAR(100) |  |  | The mobile phone number of the patient. |
| 126 | `MSG_FLG` | DOUBLE |  |  | Each synodromic message is an A01, A03, A04 or A08. This field has a 1, 3, 4 or 8 denoting the trigger reason for the message. |
| 127 | `NEXT_OF_KIN_ADDRESS_1` | VARCHAR(100) |  |  | The patient's next of kin's address. |
| 128 | `NEXT_OF_KIN_ADDRESS_2` | VARCHAR(100) |  |  | The patient's next of kin's address. |
| 129 | `NEXT_OF_KIN_CITY` | VARCHAR(100) |  |  | The patient's next of kin's city. |
| 130 | `NEXT_OF_KIN_FIRST_NAME` | VARCHAR(40) |  |  | The patient's next of kin's first name. |
| 131 | `NEXT_OF_KIN_LAST_NAME` | VARCHAR(100) |  |  | The patient's next of kin's last name. |
| 132 | `NEXT_OF_KIN_MIDDLE_NAME` | VARCHAR(40) |  |  | The patient's next of kin's middle name. |
| 133 | `NEXT_OF_KIN_NAME` | VARCHAR(100) |  |  | The patient's next of kin's name. |
| 134 | `NEXT_OF_KIN_PHONE` | VARCHAR(30) |  |  | The patient's next of kin's primary phone number. |
| 135 | `NEXT_OF_KIN_RELATION` | VARCHAR(40) |  |  | The relation of the next of kin to the patient. |
| 136 | `NEXT_OF_KIN_RELATION_CODE` | VARCHAR(40) |  |  | The mapped person relationship for the next of kin. |
| 137 | `NEXT_OF_KIN_STATE` | VARCHAR(50) |  |  | The patient's next of kin's state. |
| 138 | `NEXT_OF_KIN_ZIP_CODE` | VARCHAR(25) |  |  | The patient's next of kin's zip code. |
| 139 | `NPI` | VARCHAR(10) |  |  | The NPI for the admit hospital. |
| 140 | `ONSET_DT_TM` | DATETIME |  |  | The chief complaint on set date. |
| 141 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The encounter identifier from the source system. |
| 142 | `OUTBOUND_HSS_ID` | DOUBLE |  |  | The unique identifier of the organization that this result will be reported to. |
| 143 | `PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | The first line of the patient's address. |
| 144 | `PATIENT_ADDRESS_2` | VARCHAR(100) |  |  | The second line of the patient's address. |
| 145 | `PATIENT_CITY` | VARCHAR(100) |  |  | The city that the patient lives in. |
| 146 | `PATIENT_COUNTRY` | VARCHAR(50) |  |  | The country that the patient lives in. |
| 147 | `PATIENT_COUNTRY_CODE` | VARCHAR(10) |  |  | The patient's country standard PHINVads code. |
| 148 | `PATIENT_COUNTY` | VARCHAR(50) |  |  | The county that the patient lives in. |
| 149 | `PATIENT_COUNTY_CODE` | VARCHAR(40) |  |  | The county code that the patient lives in. |
| 150 | `PATIENT_FIRST_NAME` | VARCHAR(40) |  |  | The first name of the patient. |
| 151 | `PATIENT_ID` | DOUBLE |  |  | The unformatted patient medical record number. |
| 152 | `PATIENT_LAST_NAME` | VARCHAR(100) |  |  | The last name of the patient. |
| 153 | `PATIENT_MIDDLE_NAME` | VARCHAR(40) |  |  | The middle name of the patient. |
| 154 | `PATIENT_NAME` | VARCHAR(100) |  |  | The full name of the patient. |
| 155 | `PATIENT_PHONE` | VARCHAR(40) |  |  | The primary phone number of the patient. |
| 156 | `PATIENT_SSN` | VARCHAR(40) |  |  | The social security number of the patient. |
| 157 | `PATIENT_STATE` | VARCHAR(50) |  |  | The state that the patient lives in. |
| 158 | `PATIENT_STATE_CODE` | VARCHAR(10) |  |  | If the person State is populate, this is a State FIPS code. |
| 159 | `PATIENT_TYPE_DESC` | VARCHAR(60) |  |  | The mapped visit type for the encounter. |
| 160 | `PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | The zip code that the patient lives in. |
| 161 | `PAYER_SOURCE_DESC` | VARCHAR(100) |  |  | The mapped payer (insurance) description. |
| 162 | `PHIN_CARESETTING_CODE` | VARCHAR(10) |  |  | The PHINVads code for the type of care given at the admitting nursing unit. |
| 163 | `PHIN_CARESETTING_DESC` | VARCHAR(100) |  |  | The PHINVads description for the type of care given at the admitting nursing unit. |
| 164 | `PREGNANCY_STATUS` | VARCHAR(255) |  |  | Pregnancy status from clinical event. |
| 165 | `PREGNANCY_STATUS_SNOMED` | VARCHAR(20) |  |  | The SNOMED code for the patient's pregnancy status. |
| 166 | `PROBLEM_CODE_LIST` | VARCHAR(2000) |  |  | The SNOMED, ICD9 or ICD10 codes related to the problem list diagnoses. |
| 167 | `PROBLEM_LIST` | VARCHAR(2000) |  |  | The problem list are diagnoses that are at the person level and unresolved such as chronic conditions. These are not visit related. Problems are often SNOMED but can be ICD9 or 10 as well. |
| 168 | `PROCEDURE_CODE` | VARCHAR(2000) |  |  | If there are ICD-9 procedures, this field contains the procedure codes separated by a delimiter. |
| 169 | `PROCEDURE_CODE_ICD10` | VARCHAR(2000) |  |  | ICD-10 procedure codes separated by delimiters. |
| 170 | `PROCEDURE_DESC` | VARCHAR(2000) |  |  | If there are ICD-9 procedures, this field contains the procedure descriptions separated by a delimiter. |
| 171 | `PROCEDURE_DESC_ICD10` | VARCHAR(2000) |  |  | ICD-10 procedure descriptions separated by delimiters. |
| 172 | `PROCEDURE_DT_TM_ICD10` | VARCHAR(2000) |  |  | Procedure date times for the ICD-10 codes. |
| 173 | `PROCEDURE_DT_TM_TXT` | VARCHAR(2000) |  |  | If there are ICD-9 procedures, this field contains the procedure date times separated by a delimiter. |
| 174 | `RACE` | VARCHAR(40) |  |  | The mapped race for the person. |
| 175 | `RAW_FACILITY_ADDRESS` | VARCHAR(100) |  |  | The first address for the raw ordering facility. |
| 176 | `RAW_FACILITY_ADDRESS_2` | VARCHAR(100) |  |  | The second address for the raw facility. |
| 177 | `RAW_FACILITY_ADDRESS_3` | VARCHAR(100) |  |  | The third address for the raw facility. |
| 178 | `RAW_FACILITY_ADDRESS_4` | VARCHAR(100) |  |  | The fourth address for the raw facility. |
| 179 | `RAW_FACILITY_CITY` | VARCHAR(100) |  |  | The raw ordering facility city. |
| 180 | `RAW_FACILITY_NAME` | VARCHAR(100) |  |  | The raw ordering facility client description. |
| 181 | `RAW_FACILITY_STATE` | VARCHAR(50) |  |  | The raw ordering facility state. |
| 182 | `RAW_FACILITY_ZIP_CODE` | VARCHAR(25) |  |  | The raw ordering facility zip code. |
| 183 | `REASON_FOR_VISIT_CODE_DESC` | VARCHAR(500) |  |  | The ICD-9 diagnosis code descriptions if reason for visit came from the diagnosis table. |
| 184 | `REASON_FOR_VISIT_DT_TM` | DATETIME |  |  | The ICD-9 reason for visit diagnosis date/times separated by delimiters. |
| 185 | `REASON_FOR_VISIT_TXT` | VARCHAR(255) |  |  | A free text field from the encounter table for the reason for visit. |
| 186 | `RELEASE_NUMBER` | VARCHAR(255) |  |  | The Health Data release number based on the date of this records update date. |
| 187 | `SMOKING_STATUS` | VARCHAR(255) |  |  | The mapped smoking status from clinical event. |
| 188 | `STATE_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital two digit state FIPS code. |
| 189 | `SYN_REPORT_DT_TM` | DATETIME |  |  | The date and time associated to the event trigger. |
| 190 | `TEMPERATURE_ROUTE` | VARCHAR(255) |  |  | If there is an initial temperature, this field specifies if it came from a Temperature (Route Not Specified), Temperature Oral, Temperature Skin or other route. |
| 191 | `TRANSPORT_MODE_TXT` | VARCHAR(255) |  |  | A free text field from clinical events describing the mode of transportation to the facility. |
| 192 | `TRIAGE_NOTES_TXT` | VARCHAR(255) |  |  | A free text field containing triage notes which are usually additional nursing notes and documentation. |
| 193 | `TRIAGE_NOTES_VERF_DT_TM` | DATETIME |  |  | The clinical event verified date for triage notes being entered. |
| 194 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 195 | `WEIGHT` | DOUBLE |  |  | The weight from clinical events. |
| 196 | `WEIGHT_TYPE` | VARCHAR(60) |  |  | HealthSentry weight name such as Weight, Weight Admit, Weight Pounds. |
| 197 | `WEIGHT_UNIT_DESC` | VARCHAR(60) |  |  | The mapped long description for the weight unit of measurement. |
| 198 | `WEIGHT_UNIT_DISPLAY` | VARCHAR(40) |  |  | The unit for weight from clinical events. |
| 199 | `WEIGHT_UNIT_UCUM` | VARCHAR(250) |  |  | The standard UCUM description for the person's initial weight unit of measure. |
| 200 | `WORKING_DIAGNOSIS_DESC` | VARCHAR(2000) |  |  | The ICD-9 working diagnosis codes and descriptions separated by delimiters. |
| 201 | `WORKING_DIAGNOSIS_DT_TM_TXT` | VARCHAR(2000) |  |  | The ICD-9 working diagnosis date/times separated by delimiters. |
| 202 | `WORKING_DIAG_DTTM_ICD10` | VARCHAR(2000) |  |  | Working diagnosis date times for the ICD-10 codes. |
| 203 | `WORKING_DIAG_ICD10` | VARCHAR(2000) |  |  | ICD-10 diagnosis codes and descriptions for working diagnoses separated by delimiters. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

