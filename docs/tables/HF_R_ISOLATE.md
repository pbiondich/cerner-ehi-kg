# HF_R_ISOLATE

> This table is used to facilitate in the creation of the Health Sentry isolate BO report

**Description:** HF_R_Isolate  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 349

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The primary accession number identifies an order or a group of orders. |
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
| 56 | `CHARACTER_RESULT` | VARCHAR(2000) |  |  | The textual value of the gen lab result |
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
| 97 | `COLLECTION_METHOD_ID` | VARCHAR(40) |  |  | The Health Data ID fro HF_D_COLLECTION_SRC_SITE for the mapped collection method. |
| 98 | `COLLECTION_METHOD_ID_TXT` | VARCHAR(40) |  |  | The identifier for the procedure for collecting a specimen. |
| 99 | `COLLECTION_METHOD_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the collection method modifier. A modifier is the left, right, upper, lower location for the collection method. |
| 100 | `COLLECTION_METHOD_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED CT code for the collection method modifier. A modifier is the left, right, upper, lower location for the collection method. |
| 101 | `COLLECTION_METHOD_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection method. |
| 102 | `COLLECTION_SITE_CODE` | VARCHAR(6) |  |  | The SNOMED code for sites from an HL7 file |
| 103 | `COLLECTION_SITE_DESC` | VARCHAR(40) |  |  | The collection site for the microbiology specimen |
| 104 | `COLLECTION_SITE_ID` | DOUBLE | NOT NULL |  | The dim table key for the collection site of the isolate |
| 105 | `COLLECTION_SITE_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the body site modifier. A modifier is the left, right, upper, lower location for the site. |
| 106 | `COLLECTION_SITE_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED code for the body site modifier. A modifier is the left, right, upper, lower location for the body site. |
| 107 | `COLLECTION_SITE_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection site. |
| 108 | `COLLECTION_SOURCE_CODE` | VARCHAR(6) |  |  | The SNOMED code for sources from an HL7 file |
| 109 | `COLLECTION_SOURCE_DESC` | VARCHAR(40) |  |  | The collection source for the microbiology specimen |
| 110 | `COLLECTION_SOURCE_ID` | DOUBLE | NOT NULL |  | The dim table key for the collection source of the isolate |
| 111 | `COLLECTION_SOURCE_SNOMED` | VARCHAR(100) |  |  | The HealthSentry assigned SNOMED CT for the collection source. |
| 112 | `COLLECTION_SRC_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the collection specimen modifier. A modifier is the left, right, upper, lower location for the specimen. |
| 113 | `COLLECTION_SRC_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED CT code for the collection specimen modifier. A modifier is the left, right, upper, lower location for the specimen. |
| 114 | `COLLECTION_STATUS_DESC` | VARCHAR(60) |  |  | The textual description of a collection status (collection, ordered, scheduled, etc.) |
| 115 | `COL_IDENT` | VARCHAR(50) |  |  | N/A Should be No such field on this table. |
| 116 | `CONTAINER_TYPE` | VARCHAR(100) |  |  | The type of contain the specimen was collected in. |
| 117 | `COUNTY_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital three digit county FIPS code. |
| 118 | `DECEASED_DT_TM` | DATETIME |  |  | The date and time in which the patient expired. |
| 119 | `DIRECTOR_FIRST_NAME` | VARCHAR(100) |  |  | The hospital's director's first name. |
| 120 | `DIRECTOR_LAST_NAME` | VARCHAR(100) |  |  | The hospital's director's last name. |
| 121 | `DIRECTOR_MIDDLE_NAME` | VARCHAR(100) |  |  | The hospital's director's middle name. |
| 122 | `DIRECTOR_PREFIX` | VARCHAR(10) |  |  | The hospital's directors prefix. |
| 123 | `DIRECTOR_SUFFIX` | VARCHAR(10) |  |  | The hospital's directors suffix. |
| 124 | `DIRECTOR_TITLE` | VARCHAR(10) |  |  | The title of the hospital's director. |
| 125 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 126 | `DISCHARGE_DISP_DESC` | VARCHAR(190) |  |  | The UB92 standard textual description of a discharge disposition |
| 127 | `EMAIL_ADDRESS` | VARCHAR(100) |  |  | The patient's email address. |
| 128 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The visit identifier for the encounter |
| 129 | `ETHNICITY` | VARCHAR(40) |  |  | Identifies a religious national racial or cultural group of the person. |
| 130 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time of the contributor extraction of data. |
| 131 | `FALSE_POSITIVE_IND` | DOUBLE |  |  | When a response is marked as positive but the system has detected a negating phrase surrounding the response, this will be set to 1. For all other rows, it will be set to 0 |
| 132 | `FINANCIAL_NBR` | VARCHAR(40) |  |  | The formatted Financial number |
| 133 | `FINANCIAL_NBR_RAW` | VARCHAR(40) |  |  | The unformatted Financial number. |
| 134 | `FIRST_OBSERVED_ISOLATE_DT_TM` | DATETIME |  |  | The date/time when an isolate was first observed on this micro task |
| 135 | `GENDER` | VARCHAR(60) |  |  | Patient's gender |
| 136 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The health system that the hospital belongs to |
| 137 | `HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | Address of the hospital |
| 138 | `HOSPITAL_ADDRESS_2` | VARCHAR(100) |  |  | The second line address of the hospital. |
| 139 | `HOSPITAL_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the hospital number. |
| 140 | `HOSPITAL_CITY` | VARCHAR(50) |  |  | City of the hospital |
| 141 | `HOSPITAL_CODE` | DOUBLE |  |  | A Millennium identifier for the hospital |
| 142 | `HOSPITAL_COUNTRY` | VARCHAR(100) |  |  | The country of the hospital. |
| 143 | `HOSPITAL_COUNTY` | VARCHAR(100) |  |  | The county of the hospital. |
| 144 | `HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display name of the hospital. |
| 145 | `HOSPITAL_EXTENSION` | VARCHAR(100) |  |  | The phone extension of the hospital's primary phone number. |
| 146 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | The dim table key for the hospital that this record's encounter is attached to |
| 147 | `HOSPITAL_NAME` | VARCHAR(50) |  |  | Name of the hospital |
| 148 | `HOSPITAL_OID` | VARCHAR(100) |  |  | The OID (HL7 Object Identifier) for the facility. http://www.hl7.org/oid/index.cfm |
| 149 | `HOSPITAL_PHONE` | VARCHAR(30) |  |  | Phone number for the hospital |
| 150 | `HOSPITAL_STATE` | VARCHAR(2) |  |  | State of the hospital |
| 151 | `HOSPITAL_ZIP` | VARCHAR(25) |  |  | Zipcode of the hospital |
| 152 | `INTERP_DATA` | VARCHAR(4000) |  |  | A long text field that originates from the client interp field. |
| 153 | `ISOLATE_ID` | DOUBLE | NOT NULL |  | The dim table key for the isolate |
| 154 | `ISOLATE_NAME` | VARCHAR(50) |  |  | The scientific name for the isolate |
| 155 | `ISOLATE_REPT_CATEGORY` | VARCHAR(30) |  |  | The reporting category for the isolate. Typically the genus; however sometimes this is at a finer grain than the genus |
| 156 | `ISOLATE_TYPE` | VARCHAR(25) |  |  | The type of isolate |
| 157 | `LAB_COMPLETED_DT_TM` | DATETIME |  |  | The date/time the micro order was completed |
| 158 | `LAB_COMPLETED_MONTH_NAME` | VARCHAR(9) |  |  | The month represented as text |
| 159 | `LAB_COMPLETED_YEAR` | DOUBLE |  |  | The 4 digit year of the date |
| 160 | `LAB_DRAWN_DT_TM` | DATETIME |  |  | The date/time the specimen was drawn |
| 161 | `LAB_ORDERED_DT_TM` | DATETIME |  |  | The date/time a gen lab order was ordered |
| 162 | `LAB_PERFORMED_DT_TM` | DATETIME |  |  | The date and time in which the lab was performed. |
| 163 | `LAB_PROCEDURE_NAME` | VARCHAR(100) |  |  | Full name of a laboratory test |
| 164 | `LAB_RECEIVED_DT_TM` | DATETIME |  |  | The date/time the specimen was received |
| 165 | `LAST_REPORT_UPDATED_DT_TM` | DATETIME |  |  | The date/time when a report was last entered for this micro task |
| 166 | `LOINC_CODE` | VARCHAR(10) |  |  | The PHIN approved LOINC codes used for reporting purposes |
| 167 | `LOINC_CODE_LONG` | VARCHAR(255) |  |  | The long RELMA description for the mapped detail test LOINC. |
| 168 | `LOINC_CODE_SHORT` | VARCHAR(60) |  |  | The short RELMA description for the mapped detail test LOINC |
| 169 | `MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | The formatted patient medical record number |
| 170 | `MEDICAL_RECORD_NBR_RAW` | VARCHAR(40) |  |  | The unformatted patient medical record number |
| 171 | `MEDICAL_SERVICE_CODE` | VARCHAR(40) |  |  | The code for the Medical Services. |
| 172 | `MEDICAL_SERVICE_DESC` | VARCHAR(100) |  |  | The description of the Medical Services. |
| 173 | `MEDICAL_SERVICE_ID` | DOUBLE |  |  | Unique identifier for Medical Services |
| 174 | `MICRO_RESULT_TYPE_DESC` | VARCHAR(60) |  |  | The textual description of the micro result type (preliminary, final, amended, etc.) |
| 175 | `MICRO_RESULT_TYPE_ID` | DOUBLE | NOT NULL |  | The dim table key for the type of micro result (preliminary, final, etc.) |
| 176 | `MIC_ORDER_STATUS_DESC` | VARCHAR(60) |  |  | The textual description of the micro order status (preliminary report, final report, etc.) |
| 177 | `MOBILE_NUMBER` | VARCHAR(100) |  |  | The patient's mobile phone number. |
| 178 | `MOTHER_MAIDEN_FIRST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden first name. |
| 179 | `MOTHER_MAIDEN_LAST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden last name. |
| 180 | `MOTHER_MAIDEN_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's mother's maiden name initials. |
| 181 | `MOTHER_MAIDEN_NAME_PREFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name prefix. |
| 182 | `MOTHER_MAIDEN_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name suffix. |
| 183 | `MOTHER_MAIDEN_NAME_TITLE` | VARCHAR(100) |  |  | The patient's mother's maiden name title. |
| 184 | `NAME_INITIALS` | VARCHAR(100) |  |  | The patient's initials. |
| 185 | `NAME_PREFIX` | VARCHAR(100) |  |  | The prefix of the patient name. |
| 186 | `NAME_SUFFIX` | VARCHAR(100) |  |  | The suffix of the patient name. |
| 187 | `NAME_TITLE` | VARCHAR(100) |  |  | The title of the patient. |
| 188 | `NEXT_OF_KIN_ADDRESS_1` | VARCHAR(100) |  |  | The address of the patient's closest living blood relative or relatives |
| 189 | `NEXT_OF_KIN_ADDRESS_2` | VARCHAR(100) |  |  | The address of the patient's closest living blood relative or relatives |
| 190 | `NEXT_OF_KIN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the next of kin number. |
| 191 | `NEXT_OF_KIN_CITY` | VARCHAR(100) |  |  | The city where the patient's closest living blood relative or relatives live |
| 192 | `NEXT_OF_KIN_FIRST_NAME` | VARCHAR(40) |  |  | The first name of the patient's closest living blood relative or relatives |
| 193 | `NEXT_OF_KIN_LAST_NAME` | VARCHAR(100) |  |  | The last name of the patient's closest living blood relative or relatives |
| 194 | `NEXT_OF_KIN_MIDDLE_NAME` | VARCHAR(40) |  |  | The middle name of the patient's closest living blood relative or relatives |
| 195 | `NEXT_OF_KIN_NAME` | VARCHAR(100) |  |  | The person name of the patient's closest living blood relative or relatives |
| 196 | `NEXT_OF_KIN_PHONE` | VARCHAR(30) |  |  | The phone number of the patient's closest living blood relative or relatives live |
| 197 | `NEXT_OF_KIN_PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's next of kin's phone extension. |
| 198 | `NEXT_OF_KIN_RELATION` | VARCHAR(40) |  |  | The relationship type of the patient's closest living blood relative to the patient |
| 199 | `NEXT_OF_KIN_RELATION_CODE` | VARCHAR(40) |  |  | The mapped person relationship for the next of kin. |
| 200 | `NEXT_OF_KIN_STATE` | VARCHAR(50) |  |  | The state where the patient's closest living blood relative or relatives live |
| 201 | `NEXT_OF_KIN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code where the patient's closest living blood relative or relatives live |
| 202 | `NOK_COUNTRY` | VARCHAR(100) |  |  | The country of the patient's next of kin. |
| 203 | `NOK_COUNTY` | VARCHAR(100) |  |  | The county of the patient's next of kin. |
| 204 | `NOK_EMAIL` | VARCHAR(100) |  |  | The email of the patient's next of kin. |
| 205 | `NOK_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's next of kin initials. |
| 206 | `NOK_NAME_PREFIX` | VARCHAR(100) |  |  | The patient's next of kin's name prefix. |
| 207 | `NOK_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient's next of kin's name suffix. |
| 208 | `NOK_NAME_TITLE` | VARCHAR(100) |  |  | The patient's next of kin's title. |
| 209 | `NORMAL_ALPHA` | VARCHAR(200) |  |  | Defines the normal alpha response for a procedure with the result type of alpha. |
| 210 | `NORMAL_RANGE_HIGH` | VARCHAR(16) |  |  | Defines the normal high reference range value associated with a result. The result must be greater than the normal high to be flagged as high. |
| 211 | `NORMAL_RANGE_LOW` | VARCHAR(16) |  |  | Defines the normal low reference range value associated with a result. The result must be less than the normal low to be flagged as low. |
| 212 | `NOTE_TEXT` | VARCHAR(4000) |  |  | A long text field that originates from the client clinical event note field. |
| 213 | `NPI` | VARCHAR(10) |  |  | The NPI for the ordering hospital. |
| 214 | `NUMERIC_RESULT` | DOUBLE |  |  | The numeric value of the gen lab result |
| 215 | `ORDERABLE_DESC` | VARCHAR(100) |  |  | The HealthSentry mapped test description for the orderable. |
| 216 | `ORDERABLE_LAB_PROCEDURE_ID` | DOUBLE |  |  | The Health Data internal ID for the orderable lab. |
| 217 | `ORDERABLE_LOINC_CODE` | VARCHAR(10) |  |  | The HealthSentry assigned LOINC code for the mapped orderable. |
| 218 | `ORDERABLE_LOINC_CODE_LONG` | VARCHAR(255) |  |  | The long RELMA description for the mapped orderable LOINC. |
| 219 | `ORDERABLE_LOINC_CODE_SHORT` | VARCHAR(60) |  |  | The short RELMA description for the mapped orderable LOINC |
| 220 | `ORDER_CARESETTING_RAW` | VARCHAR(40) |  |  | The client value representing the location where the test was ordered |
| 221 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE | NOT NULL |  | The dim table key for the ordered lab procedure |
| 222 | `ORDER_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The ordering physician address |
| 223 | `ORDER_PHYSICIAN_ADDRESS_2` | VARCHAR(255) |  |  | The second line of the address for the ordering physician. |
| 224 | `ORDER_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The ordering physician city |
| 225 | `ORDER_PHYSICIAN_COUNTRY` | VARCHAR(100) |  |  | The country of the ordering physician. |
| 226 | `ORDER_PHYSICIAN_COUNTY` | VARCHAR(100) |  |  | The county of the ordering physician. |
| 227 | `ORDER_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The ordering physician's email address. |
| 228 | `ORDER_PHYSICIAN_EXTENSION` | VARCHAR(100) |  |  | The ordering physician's phone extension. |
| 229 | `ORDER_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The ordering physician's fax number. |
| 230 | `ORDER_PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | The first name of the ordering physician. |
| 231 | `ORDER_PHYSICIAN_INITIALS` | VARCHAR(100) |  |  | The initials of the ordering physician. |
| 232 | `ORDER_PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | The last name of the ordering physician. |
| 233 | `ORDER_PHYSICIAN_MIDDLE_NAME` | VARCHAR(100) |  |  | The middle name of the ordering physician. |
| 234 | `ORDER_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The ordering physician's mobile phone number. |
| 235 | `ORDER_PHYSICIAN_NAME` | VARCHAR(100) |  |  | The ordering Physician name |
| 236 | `ORDER_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The NPI for the ordering physician. |
| 237 | `ORDER_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The ordering physician's phone number |
| 238 | `ORDER_PHYSICIAN_PREFIX` | VARCHAR(100) |  |  | The prefix of the ordering physician. |
| 239 | `ORDER_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The ordering physician state |
| 240 | `ORDER_PHYSICIAN_SUFFIX` | VARCHAR(100) |  |  | The suffix of the ordering physician. |
| 241 | `ORDER_PHYSICIAN_TITLE` | VARCHAR(100) |  |  | The title of the ordering physician. |
| 242 | `ORDER_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The ordering physician's zip code |
| 243 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE |  |  | Within microbiology, the organisms have a sequence. This is the sequence number of the organism that is associated with the susceptibility results. |
| 244 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The encounter identifier from the source system |
| 245 | `OUTBOUND_HSS_ID` | DOUBLE | NOT NULL |  | The unique identifier of the organization that this result will be reported to |
| 246 | `O_PHYSICIAN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the physician number. |
| 247 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 248 | `PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | Patient's home address |
| 249 | `PATIENT_ADDRESS_2` | VARCHAR(100) |  |  | Patient's home address |
| 250 | `PATIENT_CITY` | VARCHAR(100) |  |  | City of the patient's home |
| 251 | `PATIENT_COUNTRY` | VARCHAR(50) |  |  | Country of the patient's home |
| 252 | `PATIENT_COUNTRY_CODE` | VARCHAR(10) |  |  | The patient's country standard PHINVads code. |
| 253 | `PATIENT_COUNTY` | VARCHAR(50) |  |  | County of the patient's home |
| 254 | `PATIENT_COUNTY_CODE` | VARCHAR(40) |  |  | The source key of the county from the source system |
| 255 | `PATIENT_FIRST_NAME` | VARCHAR(40) |  |  | Patient's first name |
| 256 | `PATIENT_ID` | DOUBLE | NOT NULL |  | The patient unique identifier used within the Cerner Health Facts Data Warehouse. |
| 257 | `PATIENT_LAST_NAME` | VARCHAR(100) |  |  | Patient's last name |
| 258 | `PATIENT_MAIDEN_LAST_NAME` | VARCHAR(100) |  |  | The patient's maiden last name. |
| 259 | `PATIENT_MIDDLE_NAME` | VARCHAR(40) |  |  | Patient's middle name |
| 260 | `PATIENT_NAME` | VARCHAR(100) |  |  | Patient's name |
| 261 | `PATIENT_PHONE` | VARCHAR(40) |  |  | Patient's phone number |
| 262 | `PATIENT_SSN` | VARCHAR(40) |  |  | Patient's social security number |
| 263 | `PATIENT_STATE` | VARCHAR(50) |  |  | State of the patient's home |
| 264 | `PATIENT_STATE_CODE` | VARCHAR(10) |  |  | The patient state FIP code per the zipcode. |
| 265 | `PATIENT_TYPE_DESC` | VARCHAR(60) |  |  | A description of the patient type. Defines the type of visit made |
| 266 | `PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | Zipcode of the patient's home |
| 267 | `PERFORMED_BENCH_ADDRESS` | VARCHAR(100) |  |  | The perform lab address derived from the bench location. |
| 268 | `PERFORMED_BENCH_CITY` | VARCHAR(50) |  |  | The perform lab city derived from the bench location. |
| 269 | `PERFORMED_BENCH_CLIA_NBR` | VARCHAR(10) |  |  | The perform lab CLIA derived from the bench location. |
| 270 | `PERFORMED_BENCH_CODE` | DOUBLE |  |  | The client code for the bench. |
| 271 | `PERFORMED_BENCH_COUNTRY` | VARCHAR(100) |  |  | The perform lab country derived from the bench location. |
| 272 | `PERFORMED_BENCH_COUNTY` | VARCHAR(100) |  |  | The perform lab county derived from the bench location. |
| 273 | `PERFORMED_BENCH_DISPLAY` | VARCHAR(30) |  |  | The perform lab display name derived from the bench location. Usually the display is 20 characters or less and used for the HL7 messages. |
| 274 | `PERFORMED_BENCH_ID` | DOUBLE |  |  | The unique identifier of the bench that was used. |
| 275 | `PERFORMED_BENCH_NAME` | VARCHAR(50) |  |  | The perform lab name derived from bench location. |
| 276 | `PERFORMED_BENCH_PHONE` | VARCHAR(30) |  |  | The perform lab phone derived from the bench location. |
| 277 | `PERFORMED_BENCH_STATE` | VARCHAR(2) |  |  | The perform lab state derived from the bench location. |
| 278 | `PERFORMED_BENCH_ZIP` | VARCHAR(25) |  |  | The perform lab zip derived from the bench location. |
| 279 | `PERFORMED_HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | The address of the hospital in which the action was performed. |
| 280 | `PERFORMED_HOSPITAL_CITY` | VARCHAR(50) |  |  | The city of the hospital in which the action was performed. |
| 281 | `PERFORMED_HOSPITAL_CLIA_NBR` | VARCHAR(10) |  |  | The CLIA number for the performing hospital. |
| 282 | `PERFORMED_HOSPITAL_CODE` | DOUBLE |  |  | The identifying code of the hospital in which the action was performed. |
| 283 | `PERFORMED_HOSPITAL_COUNTRY` | VARCHAR(100) |  |  | The country of the hospital in which the action was performed. |
| 284 | `PERFORMED_HOSPITAL_COUNTY` | VARCHAR(100) |  |  | The county of the hospital in which the action was performed. |
| 285 | `PERFORMED_HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display name of the hospital in which the action was performed. |
| 286 | `PERFORMED_HOSPITAL_ID` | DOUBLE | NOT NULL |  | The unique identifier of the hospital in which the action was performed. |
| 287 | `PERFORMED_HOSPITAL_NAME` | VARCHAR(50) |  |  | The name of the hospital in which the action was performed. |
| 288 | `PERFORMED_HOSPITAL_PHONE` | VARCHAR(30) |  |  | The primary phone number of the hospital in which the action was performed. |
| 289 | `PERFORMED_HOSPITAL_STATE` | VARCHAR(2) |  |  | The state of the hospital in which the action was performed. |
| 290 | `PERFORMED_HOSPITAL_ZIP` | VARCHAR(25) |  |  | The zip code of the hospital in which the action was performed. |
| 291 | `PERFORMED_PRSNL_ADDRESS` | VARCHAR(100) |  |  | The mapped perform hospital address determined from action perform personnel. |
| 292 | `PERFORMED_PRSNL_CITY` | VARCHAR(50) |  |  | The mapped perform hospital city determined from action perform personnel. |
| 293 | `PERFORMED_PRSNL_CLIA_NBR` | VARCHAR(10) |  |  | The mapped perform hospital CLIA number determined from action perform personnel. |
| 294 | `PERFORMED_PRSNL_CODE` | DOUBLE |  |  | N/A. Blank. |
| 295 | `PERFORMED_PRSNL_COUNTRY` | VARCHAR(100) |  |  | The mapped perform hospital country determined from action perform personnel. |
| 296 | `PERFORMED_PRSNL_COUNTY` | VARCHAR(100) |  |  | The mapped perform hospital county determined from action perform personnel. |
| 297 | `PERFORMED_PRSNL_DISPLAY` | VARCHAR(30) |  |  | The mapped perform hospital display name determined from action perform personnel. |
| 298 | `PERFORMED_PRSNL_ID` | DOUBLE |  |  | The mapped perform hospital id determined from action perform personnel from hf_d_hospital. |
| 299 | `PERFORMED_PRSNL_NAME` | VARCHAR(50) |  |  | The mapped perform hospital name determined from action perform personnel. |
| 300 | `PERFORMED_PRSNL_PHONE` | VARCHAR(30) |  |  | The mapped perform hospital phone determined from action perform personnel. |
| 301 | `PERFORMED_PRSNL_STATE` | VARCHAR(2) |  |  | The mapped perform hospital state determined from action perform personnel. |
| 302 | `PERFORMED_PRSNL_ZIP` | VARCHAR(25) |  |  | The mapped perform hospital zip code determined from action perform personnel. |
| 303 | `PHIN_ABNORMAL_CODE` | VARCHAR(10) |  |  | PHINVADs has defined abbreviations for abnormal flags. This translates the Health Data values to a standard code for HL7. |
| 304 | `PHIN_ABNORMAL_DESC` | VARCHAR(100) |  |  | PHINVADs has defined abbreviations for abnormal flags. This translates the Health Data values to a standard description for HL7. |
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
| 325 | `RESULT_INDICATOR_CODE` | VARCHAR(40) |  |  | The dim table key used to indicate special information in regards to the gen lab result (Abnormal, Low, High, Critical, etc.) |
| 326 | `RESULT_INDICATOR_DESC` | VARCHAR(60) |  |  | A text description of the type of normality. If the result was not normal, this field indicates that the result was out of range, not normal, etc. |
| 327 | `RESULT_INDICATOR_DISPLAY` | VARCHAR(45) |  |  | The display value to indicate special information in regards to the gen lab result (Abnormal, Low, High, Critical, etc.) |
| 328 | `RESULT_INDICATOR_MEANING` | VARCHAR(45) |  |  | The Health Data standard mapped value for abnormal flag. |
| 329 | `RESULT_TYPE_PROCEDURE_DESC` | VARCHAR(60) |  |  | A textual description of the detail procedure/report (preliminary, final, etc.) |
| 330 | `RESULT_TYPE_PROCEDURE_ID` | DOUBLE | NOT NULL |  | The dim table key for the type of procedure that was performed |
| 331 | `RESULT_UNIT_DESC` | VARCHAR(60) |  |  | A description of the unit of measure for the result |
| 332 | `RESULT_UNIT_DISPLAY` | VARCHAR(2) |  |  | The display of the unit of measure for the result |
| 333 | `RESULT_UNIT_UCUM` | VARCHAR(250) |  |  | The standard UCUM description for the result unit. |
| 334 | `SNOMEDCT_CODE` | VARCHAR(15) |  |  | A newer version of the SNOMED code. Only populated when the SNOMEDCT code is different from the SNOMED code |
| 335 | `SNOMED_CODE` | VARCHAR(15) |  |  | The SNOMED code(s) for the isolate |
| 336 | `SRC_FCT_KEY` | DOUBLE |  |  | The identifying source key for the record. |
| 337 | `STATE_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital two digit state FIPS code. |
| 338 | `TOTAL_REPORT_UPDATES` | DOUBLE |  |  | The total number of times reports have been entered for this micro task |
| 339 | `UNIQUE_ORDER_ID` | VARCHAR(80) | NOT NULL |  | Combination of fields that uniquely define an order |
| 340 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 341 | `VERIFIED_DT_TM` | DATETIME |  |  | The date and time in which the result was verified. |
| 342 | `VERIFIED_PRSNL_INITIALS` | VARCHAR(100) |  |  | The initials of the personnel that verified the results. |
| 343 | `VERIFIED_PRSNL_NAME` | VARCHAR(100) |  |  | The full name of the personnel that validated the results. |
| 344 | `VERIFIED_PRSNL_PREFIX` | VARCHAR(100) |  |  | The prefix of the personnel that verified the results. |
| 345 | `VERIFIED_PRSNL_SUFFIX` | VARCHAR(100) |  |  | The suffix of the personnel that verified the results. |
| 346 | `VERIFIED_PRSNL_TITLE` | VARCHAR(100) |  |  | The title of the personnel that verified the results. |
| 347 | `VITAL_STATUS` | VARCHAR(60) |  |  | A field that identifies alive, deceased status. |
| 348 | `WEIGHT` | DOUBLE |  |  | Patient's weight |
| 349 | `WEIGHT_UNIT_DISPLAY` | VARCHAR(40) |  |  | The display of the unit of measure |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

