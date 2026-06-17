# HF_R_HL7_ISOLATE

> This table contains all the general lab and microbiology result that being outbound

**Description:** HF_R_HL7_ISOLATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 346

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(100) |  |  | Accession number |
| 2 | `ACTION_PRSNL_FT` | VARCHAR(100) |  |  | The free text value of the personnel that performed the action. This is used to map the PERFORMED_PRSNL_* fields. |
| 3 | `ADMISSION_SOURCE_CODE` | VARCHAR(12) |  |  | The mapped admission source PHINVads concept value. |
| 4 | `ADMISSION_SOURCE_CODE_DESC` | VARCHAR(60) |  |  | The mapped admission source PHINVads concept description. |
| 5 | `ADMISSION_TYPE_CODE_DESC` | VARCHAR(60) |  |  | The mapped admission type PHINVads concept description. |
| 6 | `ADMISSION_TYPE_CONCEPT` | VARCHAR(10) |  |  | The mapped admission type PHINVads concept value. |
| 7 | `ADMITTING_DIAGNOSIS_1_DESC` | VARCHAR(255) |  |  | The description of the first admitting diagnosis |
| 8 | `ADMITTING_DIAGNOSIS_2_DESC` | VARCHAR(255) |  |  | The description of the second admitting diagnosis |
| 9 | `ADMITTING_DIAGNOSIS_3_DESC` | VARCHAR(255) |  |  | The description of the third admitting diagnosis |
| 10 | `ADMIT_DT_TM` | DATETIME |  |  | The date and time when the patient was admitted to the hospital |
| 11 | `ADMIT_PHSYICIAN_NAME` | VARCHAR(100) |  |  | The admitting Physician name |
| 12 | `ADMIT_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The admitting physician address |
| 13 | `ADMIT_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The admitting physician city |
| 14 | `ADMIT_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The admitting physician's email address. |
| 15 | `ADMIT_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The admitting physician's fax number. |
| 16 | `ADMIT_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The admitting physician's mobile phone number. |
| 17 | `ADMIT_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The NPI for the admitting physician. |
| 18 | `ADMIT_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The admitting physician's phone number |
| 19 | `ADMIT_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The admitting physician state |
| 20 | `ADMIT_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The admitting physician's zip code |
| 21 | `ADMIT_TM_ZN` | DOUBLE |  |  | The time zone in which the admission occurred. |
| 22 | `AGE_IN_DAYS` | DOUBLE |  |  | The persons age in days if 2 days thru 2 weeks old. Values 2 - 13 days. This value is blank if the age was extracted to only the whole year detail. |
| 23 | `AGE_IN_HOURS` | DOUBLE |  |  | The persons age in hours, if less than 2 days old. Values 0-47 hours. This value is blank if the age was extracted to only the whole year detail. If hours, days, weeks, months, and years are all equal 0, then these persons are less than 1 hour. |
| 24 | `AGE_IN_MONTHS` | DOUBLE |  |  | The persons age in months if 3 months thru 2 years. Values 3-23 months. This value is blank if the age was extracted to only the whole year detail. |
| 25 | `AGE_IN_WEEKS` | DOUBLE |  |  | The persons age in weeks if 2 weeks thru 3 months. Values 2-8 weeks. This value is blank if the age was extracted to only the whole year detail. |
| 26 | `AGE_IN_YEARS` | DOUBLE |  |  | The age (in years) of the patient at admission. For HIPAA compliance, ages greater than 90 are categorized as age 90. If the person is less than 2 years old, this field will be set to 0 but age_in_months, age_in_weeks, age_in_days or age_in_hours will be populated |
| 27 | `ALT_PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | The patient alternative first address. |
| 28 | `ALT_PATIENT_ADDRESS_2` | VARCHAR(100) |  |  | The patient alternative second address. |
| 29 | `ALT_PATIENT_CITY` | VARCHAR(100) |  |  | The patient alternative city. |
| 30 | `ALT_PATIENT_COUNTRY` | VARCHAR(100) |  |  | The patient alternative country. |
| 31 | `ALT_PATIENT_COUNTY` | VARCHAR(100) |  |  | The patient alternative county. |
| 32 | `ALT_PATIENT_FIRST_NAME` | VARCHAR(100) |  |  | The patient alternative first name. |
| 33 | `ALT_PATIENT_LAST_NAME` | VARCHAR(100) |  |  | The patient alternative last name. |
| 34 | `ALT_PATIENT_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's alternative initials. |
| 35 | `ALT_PATIENT_NAME_PREFIX` | VARCHAR(100) |  |  | The patient alternative name prefix. |
| 36 | `ALT_PATIENT_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient alternative name suffix. |
| 37 | `ALT_PATIENT_NAME_TITLE` | VARCHAR(100) |  |  | The patient alternative name title. |
| 38 | `ALT_PATIENT_STATE` | VARCHAR(100) |  |  | The patient alternative state. |
| 39 | `ALT_PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | The patient alternative zip code. |
| 40 | `ATTEND_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The address of the attending physician. |
| 41 | `ATTEND_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The city of the attending physician. |
| 42 | `ATTEND_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The attending physician's email address. |
| 43 | `ATTEND_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The attending physician's fax number. |
| 44 | `ATTEND_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The attending physician's mobile phone number. |
| 45 | `ATTEND_PHYSICIAN_NAME` | VARCHAR(100) |  |  | The name of the attending physician. |
| 46 | `ATTEND_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The NPI for the attending physician. |
| 47 | `ATTEND_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The primary phone number of the attending physician. |
| 48 | `ATTEND_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The State of the attending physician. |
| 49 | `ATTEND_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code of the attending physician. |
| 50 | `BIRTH_DT_TM` | DATETIME |  |  | Patient's birth date and time |
| 51 | `BUSINESS_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the business phone number. |
| 52 | `BUSINESS_PHONE` | VARCHAR(100) |  |  | The patient's business phone number. |
| 53 | `BUSINESS_PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's business phone number extension. |
| 54 | `CALL_INSTRUCTION` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the patient's number. |
| 55 | `CARESETTING_DESC` | VARCHAR(40) |  |  | The description of the caresetting |
| 56 | `CHARACTER_RESULT` | VARCHAR(60) |  |  | The character result |
| 57 | `CLIA_NBR` | VARCHAR(10) |  |  | The CLIA number associated with the facility |
| 58 | `CLIENT_DTA_CODE` | VARCHAR(40) |  |  | The client task assay number from the task assay reference for the detail lab test. |
| 59 | `CLIENT_DTA_DESC` | VARCHAR(100) |  |  | The client task assay long description from the task assay reference for the detail lab test. |
| 60 | `CLIENT_DTA_MNEM` | VARCHAR(50) |  |  | The client task assay mnemonic from the task assay reference for the detail lab test. |
| 61 | `CLIENT_LOINC_CODE` | VARCHAR(10) |  |  | The LOINC code assigned by the client for the detail test if general lab and the order if microbiology. |
| 62 | `CLIENT_LOINC_CONCEPT_NAME` | VARCHAR(255) |  |  | If the hospital assigned their own LOINC codes at the detail test level, this is the LOINC concept description. |
| 63 | `CLIENT_LOINC_DESC` | VARCHAR(255) |  |  | The LOINC description assigned by the client for the detail test if general lab and the order if microbiology. |
| 64 | `CLIENT_METHOD_CODE` | VARCHAR(40) |  |  | The client code value from code set 2058 for the collection method. |
| 65 | `CLIENT_METHOD_DESC` | VARCHAR(100) |  |  | The client code value description from code set 2058 for the collection method. |
| 66 | `CLIENT_METHOD_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 2058 for the collection method. |
| 67 | `CLIENT_METHOD_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 2058 for the collection method. |
| 68 | `CLIENT_ORDERABLE_CONCEPT_NAME` | VARCHAR(255) |  |  | If the hospital assigned their own LOINC codes for the orderable, this is the LOINC concept description. |
| 69 | `CLIENT_ORDERABLE_LOINC_CODE` | VARCHAR(10) |  |  | If the hospital assigned their own LOINC codes for the orderable, this is the LOINC Code. |
| 70 | `CLIENT_ORDERABLE_LOINC_DESC` | VARCHAR(255) |  |  | If the hospital assigned their own LOINC codes for the orderable, this is the long LOINC description. |
| 71 | `CLIENT_ORDER_CODE` | VARCHAR(40) |  |  | The client orderable number from code set 200. |
| 72 | `CLIENT_ORDER_DESC` | VARCHAR(100) |  |  | The client orderable description from code set 200. |
| 73 | `CLIENT_ORDER_DISPLAY` | VARCHAR(45) |  |  | The client orderable mnemonic from code set 200. |
| 74 | `CLIENT_ORGANISM_CODE` | VARCHAR(40) |  |  | The client code value from code set 1021/1022 for the organism or codified result. |
| 75 | `CLIENT_ORGANISM_DESC` | VARCHAR(100) |  |  | The client code value description from code set 1021/1022 for the organism or codified result. |
| 76 | `CLIENT_ORGANISM_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 1021/1022 for the organism or codified result. |
| 77 | `CLIENT_ORGANISM_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 1021/1022 for the organism or codified result. |
| 78 | `CLIENT_RESULT_IND_CODE` | VARCHAR(40) |  |  | The client code value code for the abnormal indicator. Code set 52. |
| 79 | `CLIENT_RESULT_IND_DESC` | VARCHAR(100) |  |  | The client code value description for the abnormal indicator. Code set 52. |
| 80 | `CLIENT_RESULT_IND_DISPLAY` | VARCHAR(45) |  |  | The client code value display for the abnormal indicator. Code set 52. |
| 81 | `CLIENT_RESULT_IND_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning for the abnormal indicator. Code set 52. |
| 82 | `CLIENT_SITE_CODE` | VARCHAR(40) |  |  | The client code value from code set 1028 for the body site. |
| 83 | `CLIENT_SITE_DESC` | VARCHAR(100) |  |  | The client code value description from code set 1028 for the body site. |
| 84 | `CLIENT_SITE_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 1028 for the body site. |
| 85 | `CLIENT_SITE_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 1028 for the body site. |
| 86 | `CLIENT_SPECIMEN_CODE` | VARCHAR(40) |  |  | The client code value from code set 2052 for the specimen. |
| 87 | `CLIENT_SPECIMEN_DESC` | VARCHAR(100) |  |  | The client code value description from code set 2052 for the specimen. |
| 88 | `CLIENT_SPECIMEN_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 2052 for the specimen. |
| 89 | `CLIENT_SPECIMEN_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 2052 for the specimen. |
| 90 | `CLIENT_UNIT_CODE` | VARCHAR(40) |  |  | The client code value from code set 54 for the unit of measure. |
| 91 | `CLIENT_UNIT_DESC` | VARCHAR(100) |  |  | The client code value description from code set 54 for the unit of measure. |
| 92 | `CLIENT_UNIT_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 54 for the unit of measure. |
| 93 | `CLIENT_UNIT_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 54 for the unit of measure. |
| 94 | `CLINICAL_OBSERVATION` | VARCHAR(4000) |  |  | A long text field that originates from the client long text field. |
| 95 | `COLLECTION_METHOD_CODE` | VARCHAR(6) |  |  | The code of the procedure for collecting a specimen. |
| 96 | `COLLECTION_METHOD_DESC` | VARCHAR(40) |  |  | The description of the procedure for collecting a specimen. |
| 97 | `COLLECTION_METHOD_ID` | VARCHAR(40) |  |  | The identifier for the procedure for collecting a specimen. |
| 98 | `COLLECTION_METHOD_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the collection method modifier. A modifier is the left, right, upper, lower location for the collection method. |
| 99 | `COLLECTION_METHOD_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED CT code for the collection method modifier. A modifier is the left, right, upper, lower location for the collection method. |
| 100 | `COLLECTION_METHOD_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection method. |
| 101 | `COLLECTION_SITE_CODE` | VARCHAR(6) |  |  | The SNOMED code for sites from an HL7 file |
| 102 | `COLLECTION_SITE_DESC` | VARCHAR(40) |  |  | The collection site for the microbiology specimen |
| 103 | `COLLECTION_SITE_ID` | DOUBLE | NOT NULL |  | The collection site |
| 104 | `COLLECTION_SITE_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the body site modifier. A modifier is the left, right, upper, lower location for the site. |
| 105 | `COLLECTION_SITE_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED code for the body site modifier. A modifier is the left, right, upper, lower location for the body site. |
| 106 | `COLLECTION_SITE_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection site. |
| 107 | `COLLECTION_SOURCE_CODE` | VARCHAR(6) |  |  | The SNOMED code for sources from an HL7 file |
| 108 | `COLLECTION_SOURCE_DESC` | VARCHAR(40) |  |  | The collection source for the microbiology specimen |
| 109 | `COLLECTION_SOURCE_ID` | DOUBLE | NOT NULL |  | The collection source |
| 110 | `COLLECTION_SOURCE_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection source. |
| 111 | `COLLECTION_SRC_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the collection specimen modifier. A modifier is the left, right, upper, lower location for the specimen. |
| 112 | `COLLECTION_SRC_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED CT code for the collection specimen modifier. A modifier is the left, right, upper, lower location for the specimen. |
| 113 | `COLLECTION_STATUS_DESC` | VARCHAR(60) |  |  | The textual description of a collection status (collection, ordered, scheduled, etc.) |
| 114 | `CONTAINER_TYPE` | VARCHAR(100) |  |  | The type of contain the specimen was collected in. |
| 115 | `COUNTY_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital three digit county FIPS code. |
| 116 | `DECEASED_DT_TM` | DATETIME |  |  | The date and time in which the patient expired. |
| 117 | `DIRECTOR_FIRST_NAME` | VARCHAR(100) |  |  | The hospital's director's first name. |
| 118 | `DIRECTOR_LAST_NAME` | VARCHAR(100) |  |  | The hospital's director's last name. |
| 119 | `DIRECTOR_MIDDLE_NAME` | VARCHAR(100) |  |  | The hospital's director's middle name. |
| 120 | `DIRECTOR_PREFIX` | VARCHAR(10) |  |  | The hospital's directors prefix. |
| 121 | `DIRECTOR_SUFFIX` | VARCHAR(10) |  |  | The hospital's directors suffix. |
| 122 | `DIRECTOR_TITLE` | VARCHAR(10) |  |  | The title of the hospital's director. |
| 123 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 124 | `DISCHARGE_DISP_DESC` | VARCHAR(190) |  |  | The UB92 standard textual description of a discharge disposition |
| 125 | `EMAIL_ADDRESS` | VARCHAR(100) |  |  | The patient's email address. |
| 126 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The visit identifier for the encounter |
| 127 | `ETHNICITY` | VARCHAR(40) |  |  | Identifies a religious national racial or cultural group of the person. |
| 128 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time of the contributor extraction of data. |
| 129 | `FALSE_POSITIVE_IND` | DOUBLE |  |  | When a response is marked as positive but the system has detected a negating phrase surrounding the response, this will be set to 1. For all other rows, it will be set to 0 |
| 130 | `FILE_NAME` | VARCHAR(50) |  |  | The flat file name that was contains this record. This file is prior to the HL7 transformation in Open Engine. |
| 131 | `FINANCIAL_NBR` | VARCHAR(40) |  |  | The formatted Financial number |
| 132 | `FINANCIAL_NBR_RAW` | VARCHAR(40) |  |  | The unformatted Financial number. |
| 133 | `FIRST_OBSERVED_ISOLATE_DT_TM` | DATETIME |  |  | The date/time when an isolate was first observed on this micro task |
| 134 | `GENDER` | VARCHAR(60) |  |  | Patient's gender |
| 135 | `HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | Address of the hospital |
| 136 | `HOSPITAL_ADDRESS_2` | VARCHAR(100) |  |  | The second line address of the hospital. |
| 137 | `HOSPITAL_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the hospital number. |
| 138 | `HOSPITAL_CITY` | VARCHAR(50) |  |  | City of the hospital |
| 139 | `HOSPITAL_CODE` | DOUBLE |  |  | A Millennium identifier for the hospital |
| 140 | `HOSPITAL_COUNTRY` | VARCHAR(100) |  |  | The country of the hospital. |
| 141 | `HOSPITAL_COUNTY` | VARCHAR(100) |  |  | The county of the hospital. |
| 142 | `HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display name of the hospital. |
| 143 | `HOSPITAL_EXTENSION` | VARCHAR(100) |  |  | The phone extension of the hospital's primary phone number. |
| 144 | `HOSPITAL_ID` | DOUBLE |  |  | The dim table key for the hospital that this record's encounter is attached to |
| 145 | `HOSPITAL_NAME` | VARCHAR(50) |  |  | Name of the hospital |
| 146 | `HOSPITAL_OID` | VARCHAR(100) |  |  | The OID (HL7 Object Identifier) for the facility. http://www.hl7.org/oid/index.cfm |
| 147 | `HOSPITAL_PHONE` | VARCHAR(30) |  |  | Phone number for the hospital |
| 148 | `HOSPITAL_STATE` | VARCHAR(2) |  |  | State of the hospital |
| 149 | `HOSPITAL_ZIP` | VARCHAR(25) |  |  | Zipcode of the hospital |
| 150 | `INTERP_DATA` | VARCHAR(4000) |  |  | A long text field that originates from the client interp field. |
| 151 | `ISOLATE_ID` | DOUBLE | NOT NULL |  | The isolate name |
| 152 | `ISOLATE_NAME` | VARCHAR(50) |  |  | The scientific name for the isolate |
| 153 | `ISOLATE_REPT_CATEGORY` | VARCHAR(30) |  |  | The reporting category for the isolate. Typically the genus; however sometimes this is at a finer grain than the genus |
| 154 | `ISOLATE_TYPE` | VARCHAR(25) |  |  | The type of isolate |
| 155 | `LAB_COMPLETED_DT_TM` | DATETIME |  |  | The date and time when a micro result is completed or general lab result is verified |
| 156 | `LAB_COMPLETED_MONTH_NAME` | VARCHAR(9) |  |  | The month represented as text |
| 157 | `LAB_COMPLETED_YEAR` | DOUBLE |  |  | The 4 digit year of the date |
| 158 | `LAB_DRAWN_DT_TM` | DATETIME |  |  | The date/time the specimen was drawn |
| 159 | `LAB_ORDERED_DT_TM` | DATETIME |  |  | The date/time a gen lab order was ordered |
| 160 | `LAB_PERFORMED_DT_TM` | DATETIME |  |  | The date and time in which the lab was performed. |
| 161 | `LAB_PROCEDURE_NAME` | VARCHAR(100) |  |  | Full name of a laboratory test |
| 162 | `LAB_RECEIVED_DT_TM` | DATETIME |  |  | The date/time the specimen was received |
| 163 | `LAST_REPORT_UPDATED_DT_TM` | DATETIME |  |  | The date/time when a report was last entered for this micro task |
| 164 | `LOINC_CODE` | VARCHAR(10) |  |  | The PHIN approved LOINC codes used for reporting purposes |
| 165 | `LOINC_CODE_LONG` | VARCHAR(255) |  |  | The long RELMA description for the mapped detail test LOINC. |
| 166 | `LOINC_CODE_SHORT` | VARCHAR(60) |  |  | The short RELMA description for the mapped detail test LOINC |
| 167 | `MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | The formatted patient medical record number |
| 168 | `MEDICAL_RECORD_NBR_RAW` | VARCHAR(40) |  |  | The unformatted patient medical record number |
| 169 | `MEDICAL_SERVICE_CODE` | VARCHAR(40) |  |  | The code for the Medical Services. |
| 170 | `MEDICAL_SERVICE_DESC` | VARCHAR(100) |  |  | The description of the Medical Services. |
| 171 | `MEDICAL_SERVICE_ID` | DOUBLE |  |  | Unique identifier for Medical Services |
| 172 | `MICRO_RESULT_TYPE_DESC` | VARCHAR(60) |  |  | The textual description of the micro result type (preliminary, final, amended, etc.) |
| 173 | `MICRO_RESULT_TYPE_ID` | DOUBLE | NOT NULL |  | The result type |
| 174 | `MIC_ORDER_STATUS_DESC` | VARCHAR(60) |  |  | The textual description of the micro order status (preliminary report, final report, etc.) |
| 175 | `MOBILE_NUMBER` | VARCHAR(100) |  |  | The patient's mobile phone number. |
| 176 | `MOTHER_MAIDEN_FIRST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden first name. |
| 177 | `MOTHER_MAIDEN_LAST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden last name. |
| 178 | `MOTHER_MAIDEN_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's mother's maiden name initials. |
| 179 | `MOTHER_MAIDEN_NAME_PREFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name prefix. |
| 180 | `MOTHER_MAIDEN_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name suffix. |
| 181 | `MOTHER_MAIDEN_NAME_TITLE` | VARCHAR(100) |  |  | The patient's mother's maiden name title. |
| 182 | `NAME_INITIALS` | VARCHAR(100) |  |  | The patient's initials. |
| 183 | `NAME_PREFIX` | VARCHAR(100) |  |  | The prefix of the patient name. |
| 184 | `NAME_SUFFIX` | VARCHAR(100) |  |  | The suffix of the patient name. |
| 185 | `NAME_TITLE` | VARCHAR(100) |  |  | The title of the patient. |
| 186 | `NEXT_OF_KIN_ADDRESS_1` | VARCHAR(100) |  |  | The address of the patient's closest living blood relative or relatives |
| 187 | `NEXT_OF_KIN_ADDRESS_2` | VARCHAR(100) |  |  | The address of the patient's closest living blood relative or relatives |
| 188 | `NEXT_OF_KIN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the next of kin number. |
| 189 | `NEXT_OF_KIN_CITY` | VARCHAR(100) |  |  | The city where the patient's closest living blood relative or relatives live |
| 190 | `NEXT_OF_KIN_FIRST_NAME` | VARCHAR(40) |  |  | The first name of the patient's closest living blood relative or relatives |
| 191 | `NEXT_OF_KIN_LAST_NAME` | VARCHAR(100) |  |  | The last name of the patient's closest living blood relative or relatives |
| 192 | `NEXT_OF_KIN_MIDDLE_NAME` | VARCHAR(40) |  |  | The middle name of the patient's closest living blood relative or relatives |
| 193 | `NEXT_OF_KIN_NAME` | VARCHAR(100) |  |  | The next of kin's full name |
| 194 | `NEXT_OF_KIN_PHONE` | VARCHAR(30) |  |  | The phone number of the patient's closest living blood relative or relatives live |
| 195 | `NEXT_OF_KIN_PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's next of kin's phone extension. |
| 196 | `NEXT_OF_KIN_RELATION` | VARCHAR(40) |  |  | The relationship type of the patient's closest living blood relative to the patient |
| 197 | `NEXT_OF_KIN_RELATION_CODE` | VARCHAR(40) |  |  | The mapped person relationship for the next of kin. |
| 198 | `NEXT_OF_KIN_STATE` | VARCHAR(50) |  |  | The state where the patient's closest living blood relative or relatives live |
| 199 | `NEXT_OF_KIN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code where the patient's closest living blood relative or relatives live |
| 200 | `NOK_COUNTRY` | VARCHAR(100) |  |  | The country of the patient's next of kin. |
| 201 | `NOK_COUNTY` | VARCHAR(100) |  |  | The county of the patient's next of kin. |
| 202 | `NOK_EMAIL` | VARCHAR(100) |  |  | The email of the patient's next of kin. |
| 203 | `NOK_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's next of kin initials. |
| 204 | `NOK_NAME_PREFIX` | VARCHAR(100) |  |  | The patient's next of kin's name prefix. |
| 205 | `NOK_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient's next of kin's name suffix. |
| 206 | `NOK_NAME_TITLE` | VARCHAR(100) |  |  | The patient's next of kin's title. |
| 207 | `NORMAL_ALPHA` | VARCHAR(200) |  |  | Defines the normal alpha response for a procedure with the result type of alpha. |
| 208 | `NORMAL_RANGE_HIGH` | VARCHAR(16) |  |  | Defines the normal high reference range value associated with a result. The result must be greater than the normal high to be flagged as high. |
| 209 | `NORMAL_RANGE_LOW` | VARCHAR(16) |  |  | Defines the normal low reference range value associated with a result. The result must be less than the normal low to be flagged as low. |
| 210 | `NOTE_TEXT` | VARCHAR(4000) |  |  | A long text field that originates from the client clinical event note field. |
| 211 | `NPI` | VARCHAR(10) |  |  | The NPI for the ordering hospital. |
| 212 | `NUMERIC_RESULT` | DOUBLE |  |  | The numeric result |
| 213 | `ORDERABLE_DESC` | VARCHAR(100) |  |  | The HealthSentry mapped test description for the orderable. |
| 214 | `ORDERABLE_LAB_PROCEDURE_ID` | DOUBLE |  |  | The Health Data internal ID for the orderable lab. |
| 215 | `ORDERABLE_LOINC_CODE` | VARCHAR(10) |  |  | The HealthSentry assigned LOINC code for the mapped orderable. |
| 216 | `ORDERABLE_LOINC_CODE_LONG` | VARCHAR(255) |  |  | The long RELMA description for the mapped orderable LOINC. |
| 217 | `ORDERABLE_LOINC_CODE_SHORT` | VARCHAR(60) |  |  | The short RELMA description for the mapped orderable LOINC |
| 218 | `ORDER_CARESETTING_RAW` | VARCHAR(40) |  |  | The client value representing the location where the test was ordered |
| 219 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE | NOT NULL |  | The lab procedure |
| 220 | `ORDER_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The ordering physician address |
| 221 | `ORDER_PHYSICIAN_ADDRESS_2` | VARCHAR(255) |  |  | The second line of the address for the ordering physician. |
| 222 | `ORDER_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The ordering physician city |
| 223 | `ORDER_PHYSICIAN_COUNTRY` | VARCHAR(100) |  |  | The country of the ordering physician. |
| 224 | `ORDER_PHYSICIAN_COUNTY` | VARCHAR(100) |  |  | The county of the ordering physician. |
| 225 | `ORDER_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The ordering physician's email address. |
| 226 | `ORDER_PHYSICIAN_EXTENSION` | VARCHAR(100) |  |  | The ordering physician's phone extension. |
| 227 | `ORDER_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The ordering physician's fax number. |
| 228 | `ORDER_PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | The first name of the ordering physician. |
| 229 | `ORDER_PHYSICIAN_INITIALS` | VARCHAR(100) |  |  | The initials of the ordering physician. |
| 230 | `ORDER_PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | The last name of the ordering physician. |
| 231 | `ORDER_PHYSICIAN_MIDDLE_NAME` | VARCHAR(100) |  |  | The middle name of the ordering physician. |
| 232 | `ORDER_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The ordering physician's mobile phone number. |
| 233 | `ORDER_PHYSICIAN_NAME` | VARCHAR(100) |  |  | The ordering Physician name |
| 234 | `ORDER_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The NPI for the ordering physician. |
| 235 | `ORDER_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The ordering physician's phone number |
| 236 | `ORDER_PHYSICIAN_PREFIX` | VARCHAR(100) |  |  | The prefix of the ordering physician. |
| 237 | `ORDER_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The ordering physician state |
| 238 | `ORDER_PHYSICIAN_SUFFIX` | VARCHAR(100) |  |  | The suffix of the ordering physician. |
| 239 | `ORDER_PHYSICIAN_TITLE` | VARCHAR(100) |  |  | The title of the ordering physician. |
| 240 | `ORDER_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The ordering physician's zip code |
| 241 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE |  |  | Within microbiology, the organisms have a sequence. This is the sequence number of the organism that is associated with the susceptibility results. |
| 242 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The encounter identifier from the source system |
| 243 | `OUTBOUND_HSS_ID` | DOUBLE | NOT NULL |  | The outbound health system source |
| 244 | `O_PHYSICIAN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the physician number. |
| 245 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 246 | `PATIENT_ADDRESS1` | VARCHAR(100) |  |  | Patient's hone address |
| 247 | `PATIENT_ADDRESS2` | VARCHAR(100) |  |  | Patient's hone address |
| 248 | `PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | Patient's home address |
| 249 | `PATIENT_CITY` | VARCHAR(100) |  |  | Patient's city |
| 250 | `PATIENT_COUNTRY` | VARCHAR(50) |  |  | Patient's country |
| 251 | `PATIENT_COUNTRY_CODE` | VARCHAR(10) |  |  | The patient's country standard PHINVads code. |
| 252 | `PATIENT_COUNTY` | VARCHAR(50) |  |  | Patient's county |
| 253 | `PATIENT_COUNTY_CODE` | VARCHAR(40) |  |  | The source key of the county from the source system |
| 254 | `PATIENT_ID` | DOUBLE |  |  | The patient unique identifier used within the Cerner Health Facts Data Warehouse. |
| 255 | `PATIENT_LAST_NAME` | VARCHAR(100) |  |  | Patient's last name |
| 256 | `PATIENT_MAIDEN_LAST_NAME` | VARCHAR(100) |  |  | The patient's maiden last name. |
| 257 | `PATIENT_MIDDLE_NAME` | VARCHAR(40) |  |  | Patient's middle name |
| 258 | `PATIENT_NAME` | VARCHAR(100) |  |  | The patient's full name |
| 259 | `PATIENT_PHONE` | VARCHAR(40) |  |  | Patient's phone number |
| 260 | `PATIENT_SSN` | VARCHAR(40) |  |  | Patient social security numbe |
| 261 | `PATIENT_STATE` | VARCHAR(50) |  |  | Patient state |
| 262 | `PATIENT_STATE_CODE` | VARCHAR(10) |  |  | The patient state FIP code per the zipcode. |
| 263 | `PATIENT_TYPE_DESC` | VARCHAR(60) |  |  | A description of the patient type. Defines the type of visit made |
| 264 | `PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | Patient's zip code |
| 265 | `PERFORMED_BENCH_ADDRESS` | VARCHAR(100) |  |  | The perform lab address derived from the bench location. |
| 266 | `PERFORMED_BENCH_CITY` | VARCHAR(50) |  |  | The perform lab city derived from the bench location. |
| 267 | `PERFORMED_BENCH_CLIA_NBR` | VARCHAR(10) |  |  | The perform lab CLIA derived from the bench location. |
| 268 | `PERFORMED_BENCH_CODE` | DOUBLE |  |  | The client code for the bench. |
| 269 | `PERFORMED_BENCH_COUNTRY` | VARCHAR(100) |  |  | The perform lab country derived from the bench location. |
| 270 | `PERFORMED_BENCH_COUNTY` | VARCHAR(100) |  |  | The perform lab county derived from the bench location. |
| 271 | `PERFORMED_BENCH_DISPLAY` | VARCHAR(30) |  |  | The perform lab display name derived from the bench location. Usually the display is 20 characters or less and used for the HL7 messages. |
| 272 | `PERFORMED_BENCH_ID` | DOUBLE |  |  | The unique identifier of the bench that was used. |
| 273 | `PERFORMED_BENCH_NAME` | VARCHAR(50) |  |  | The perform lab name derived from bench location. |
| 274 | `PERFORMED_BENCH_PHONE` | VARCHAR(30) |  |  | The perform lab phone derived from the bench location. |
| 275 | `PERFORMED_BENCH_STATE` | VARCHAR(2) |  |  | The perform lab state derived from the bench location. |
| 276 | `PERFORMED_BENCH_ZIP` | VARCHAR(25) |  |  | The perform lab zip derived from the bench location. |
| 277 | `PERFORMED_HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | The address of the hospital in which the action was performed. |
| 278 | `PERFORMED_HOSPITAL_CITY` | VARCHAR(50) |  |  | The city of the hospital in which the action was performed. |
| 279 | `PERFORMED_HOSPITAL_CLIA_NBR` | VARCHAR(10) |  |  | The CLIA number for the performing hospital. |
| 280 | `PERFORMED_HOSPITAL_CODE` | DOUBLE |  |  | The identifying code of the hospital in which the action was performed. |
| 281 | `PERFORMED_HOSPITAL_COUNTRY` | VARCHAR(100) |  |  | The country of the hospital in which the action was performed. |
| 282 | `PERFORMED_HOSPITAL_COUNTY` | VARCHAR(100) |  |  | The county of the hospital in which the action was performed. |
| 283 | `PERFORMED_HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display name of the hospital in which the action was performed. |
| 284 | `PERFORMED_HOSPITAL_ID` | DOUBLE |  |  | The unique identifier of the hospital in which the action was performed. |
| 285 | `PERFORMED_HOSPITAL_NAME` | VARCHAR(50) |  |  | The name of the hospital in which the action was performed. |
| 286 | `PERFORMED_HOSPITAL_PHONE` | VARCHAR(30) |  |  | The primary phone number of the hospital in which the action was performed. |
| 287 | `PERFORMED_HOSPITAL_STATE` | VARCHAR(2) |  |  | The state of the hospital in which the action was performed. |
| 288 | `PERFORMED_HOSPITAL_ZIP` | VARCHAR(25) |  |  | The zip code of the hospital in which the action was performed. |
| 289 | `PERFORMED_PRSNL_ADDRESS` | VARCHAR(100) |  |  | The mapped perform hospital address determined from action perform personnel. |
| 290 | `PERFORMED_PRSNL_CITY` | VARCHAR(50) |  |  | The mapped perform hospital city determined from action perform personnel. |
| 291 | `PERFORMED_PRSNL_CLIA_NBR` | VARCHAR(10) |  |  | The mapped perform hospital CLIA number determined from action perform personnel. |
| 292 | `PERFORMED_PRSNL_CODE` | DOUBLE |  |  | N/A. Blank. |
| 293 | `PERFORMED_PRSNL_COUNTRY` | VARCHAR(100) |  |  | The mapped perform hospital country determined from action perform personnel. |
| 294 | `PERFORMED_PRSNL_COUNTY` | VARCHAR(100) |  |  | The mapped perform hospital county determined from action perform personnel. |
| 295 | `PERFORMED_PRSNL_DISPLAY` | VARCHAR(30) |  |  | The mapped perform hospital display name determined from action perform personnel. |
| 296 | `PERFORMED_PRSNL_ID` | DOUBLE |  |  | The mapped perform hospital id determined from action perform personnel from hf_d_hospital. |
| 297 | `PERFORMED_PRSNL_NAME` | VARCHAR(50) |  |  | The mapped perform hospital name determined from action perform personnel. |
| 298 | `PERFORMED_PRSNL_PHONE` | VARCHAR(30) |  |  | The mapped perform hospital phone determined from action perform personnel. |
| 299 | `PERFORMED_PRSNL_STATE` | VARCHAR(2) |  |  | The mapped perform hospital state determined from action perform personnel. |
| 300 | `PERFORMED_PRSNL_ZIP` | VARCHAR(25) |  |  | The mapped perform hospital zip code determined from action perform personnel. |
| 301 | `PHIN_ABNORMAL_CODE` | VARCHAR(10) |  |  | PHINVADs has defined abbreviations for abnormal flags. This translates the Health Data values to a standard code for HL7. |
| 302 | `PHIN_ABNORMAL_DESC` | VARCHAR(100) |  |  | PHINVADs has defined abbreviations for abnormal flags. This translates the Health Data values to a standard description for HL7. |
| 303 | `PHIN_CARESETTING_CODE` | VARCHAR(10) |  |  | The PHINVads code for the type of care given at the admitting nursing unit. |
| 304 | `PHIN_CARESETTING_DESC` | VARCHAR(100) |  |  | The PHINVads description for the type of care given at the admitting nursing unit. |
| 305 | `PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's phone extension. |
| 306 | `POSITIVE_IND` | DOUBLE |  |  | Some reportables microbiology are negative. This differentiates the positive microbiology from the negative. |
| 307 | `PREGNANCY_STATUS` | VARCHAR(255) |  |  | The raw text from pregnancy status entered by the client. |
| 308 | `PREGNANCY_STATUS_SNOMED` | VARCHAR(20) |  |  | After pregnancy status values are mapped, a standard SNOMED code is applied. This field contains the standard SNOMED code for the response. |
| 309 | `QUALITATIVE_RESULT` | VARCHAR(100) |  |  | The mapped general lab character_result (qualitative). |
| 310 | `QUALITATIVE_RESULT_SNOMED` | VARCHAR(60) |  |  | The SNOMED CT code for mapped general lab character_result (qualitative). |
| 311 | `RACE` | VARCHAR(40) |  |  | Patient's race |
| 312 | `RAW_FACILITY_ADDRESS` | VARCHAR(100) |  |  | The first address for the raw facility. |
| 313 | `RAW_FACILITY_ADDRESS_2` | VARCHAR(100) |  |  | The second address for the raw facility. |
| 314 | `RAW_FACILITY_ADDRESS_3` | VARCHAR(100) |  |  | The third address for the raw facility. |
| 315 | `RAW_FACILITY_ADDRESS_4` | VARCHAR(100) |  |  | The fourth address for the raw facility. |
| 316 | `RAW_FACILITY_CITY` | VARCHAR(100) |  |  | The raw facility city. |
| 317 | `RAW_FACILITY_NAME` | VARCHAR(100) |  |  | The raw facility client description. |
| 318 | `RAW_FACILITY_PHONE` | VARCHAR(50) |  |  | The unformatted phone number of the facility. |
| 319 | `RAW_FACILITY_STATE` | VARCHAR(50) |  |  | The raw facility state. |
| 320 | `RAW_FACILITY_ZIP_CODE` | VARCHAR(25) |  |  | The raw facility zip code. |
| 321 | `REASON_FOR_STUDY_DESC` | VARCHAR(1000) |  |  | The reason why the study was initiated. |
| 322 | `RELEASE_NUMBER` | VARCHAR(255) |  |  | A field with the release number to pass into the HL7 message. |
| 323 | `REMARK` | VARCHAR(100) |  |  | Blank. |
| 324 | `REPORTING_PRIORITY_DESC` | VARCHAR(60) |  |  | The textual description of the reporting priority (As Soon As Possible) |
| 325 | `RESULT_INDICATOR_DESC` | VARCHAR(60) |  |  | A text description of the type of normality. If the result was not normal, this field indicates that the result was out of range, not normal, etc. |
| 326 | `RESULT_TYPE_PROCEDURE_DESC` | VARCHAR(60) |  |  | A textual description of the detail procedure/report (preliminary, final, etc.) |
| 327 | `RESULT_TYPE_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the type of procedure that was performed |
| 328 | `RESULT_UNIT_DESC` | VARCHAR(60) |  |  | A description of the unit of measure for the result |
| 329 | `RESULT_UNIT_DISPLAY` | VARCHAR(40) |  |  | The display of the unit of measure for the result |
| 330 | `RESULT_UNIT_UCUM` | VARCHAR(250) |  |  | The standard UCUM description for the result unit. |
| 331 | `SNOMEDCT_CODE` | VARCHAR(15) |  |  | A newer version of the SNOMED code. Only populated when the SNOMEDCT code is different from the SNOMED code |
| 332 | `SNOMED_CODE` | VARCHAR(15) |  |  | The SNOMED code(s) for the isolate |
| 333 | `SRC_FCT_KEY` | VARCHAR(100) |  |  | The identifying source key for the record. |
| 334 | `STATE_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital two digit state FIPS code. |
| 335 | `TOTAL_REPORT_UPDATES` | DOUBLE |  |  | The total number of times reports have been entered for this micro task |
| 336 | `UNIQUE_ORDER_ID` | VARCHAR(80) |  |  | Combination of fields that uniquely define an order |
| 337 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 338 | `VERIFIED_DT_TM` | DATETIME |  |  | The date and time in which the result was verified. |
| 339 | `VERIFIED_PRSNL_INITIALS` | VARCHAR(100) |  |  | The initials of the personnel that verified the results. |
| 340 | `VERIFIED_PRSNL_NAME` | VARCHAR(100) |  |  | The full name of the personnel that validated the results. |
| 341 | `VERIFIED_PRSNL_PREFIX` | VARCHAR(100) |  |  | The prefix of the personnel that verified the results. |
| 342 | `VERIFIED_PRSNL_SUFFIX` | VARCHAR(100) |  |  | The suffix of the personnel that verified the results. |
| 343 | `VERIFIED_PRSNL_TITLE` | VARCHAR(100) |  |  | The title of the personnel that verified the results. |
| 344 | `VITAL_STATUS` | VARCHAR(60) |  |  | A field that identifies alive, deceased status. |
| 345 | `WEIGHT` | DOUBLE |  |  | Patient's weight |
| 346 | `WEIGHT_UNIT_DISPLAY` | VARCHAR(40) |  |  | The display of the unit of measure |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

