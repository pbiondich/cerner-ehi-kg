# HF_R_MICRO_SUSCEPTIBILITY

> BLANK

**Description:** HF_R_MICRO_SUSCEPTIBILITY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 319

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The primary accession number identifies an order or a group of orders. |
| 2 | `ADMISSION_SOURCE_CODE` | VARCHAR(12) |  |  | The mapped admission source PHINVads concept value. |
| 3 | `ADMISSION_SOURCE_CODE_DESC` | VARCHAR(60) |  |  | The mapped admission source PHINVads concept description. |
| 4 | `ADMISSION_TYPE_CODE_DESC` | VARCHAR(60) |  |  | The mapped admission type PHINVads concept description. |
| 5 | `ADMISSION_TYPE_CONCEPT` | VARCHAR(10) |  |  | The mapped admission type PHINVads concept value. |
| 6 | `ADMITTING_DIAGNOSIS_1_DESC` | VARCHAR(255) |  |  | Free text admitting diagnosis 1 from the encounter. |
| 7 | `ADMITTING_DIAGNOSIS_2_DESC` | VARCHAR(255) |  |  | Free text admitting diagnosis 2 from the encounter. |
| 8 | `ADMITTING_DIAGNOSIS_3_DESC` | VARCHAR(255) |  |  | Free text admitting diagnosis 3 from the encounter. |
| 9 | `ADMIT_DT_TM` | DATETIME |  |  | The date in which the patient was registered. |
| 10 | `ADMIT_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The admitting physician's address. |
| 11 | `ADMIT_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The admitting physician's city. |
| 12 | `ADMIT_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The admitting physician's email address. |
| 13 | `ADMIT_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The admitting physician's fax number. |
| 14 | `ADMIT_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The admitting physician's mobile phone number. |
| 15 | `ADMIT_PHYSICIAN_NAME` | VARCHAR(100) |  |  | The admitting physician's name. |
| 16 | `ADMIT_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The NPI for the admitting physician. |
| 17 | `ADMIT_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The admitting physician's primary phone number. |
| 18 | `ADMIT_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The admitting physician's state. |
| 19 | `ADMIT_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code of the admitting physician. |
| 20 | `ADMIT_TM_ZN` | DOUBLE |  |  | The time zone of the admit date/time. |
| 21 | `AGE_IN_YEARS` | DOUBLE |  |  | The age in years of the patient at time of registration. |
| 22 | `ALT_PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | The first address for the person's alternative information. |
| 23 | `ALT_PATIENT_ADDRESS_2` | VARCHAR(100) |  |  | The second address for the person's alternative information. |
| 24 | `ALT_PATIENT_CITY` | VARCHAR(100) |  |  | The city for the person's alternative information. |
| 25 | `ALT_PATIENT_COUNTRY` | VARCHAR(100) |  |  | The country for the person's alternative information. |
| 26 | `ALT_PATIENT_COUNTY` | VARCHAR(100) |  |  | The county for the person's alternative information. |
| 27 | `ALT_PATIENT_FIRST_NAME` | VARCHAR(100) |  |  | The first name for the person's alternative name. |
| 28 | `ALT_PATIENT_LAST_NAME` | VARCHAR(100) |  |  | The last name for the person's alternative name. |
| 29 | `ALT_PATIENT_NAME_INITIALS` | VARCHAR(100) |  |  | The initials for the person's alternative name. |
| 30 | `ALT_PATIENT_NAME_PREFIX` | VARCHAR(100) |  |  | The prefix for the person's alternative name. |
| 31 | `ALT_PATIENT_NAME_SUFFIX` | VARCHAR(100) |  |  | The suffix for the person's alternative name. |
| 32 | `ALT_PATIENT_NAME_TITLE` | VARCHAR(100) |  |  | The title for the person's alternative name. |
| 33 | `ALT_PATIENT_STATE` | VARCHAR(100) |  |  | The state for the person's alternative information. |
| 34 | `ALT_PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | The zip code for the person's alternative information. |
| 35 | `ANTIMICROBIAL_DESC` | VARCHAR(50) |  |  | The textual description of an antimicrobial |
| 36 | `ANTIMICROBIAL_ID` | DOUBLE | NOT NULL |  | The dim table key for the antimicrobial being used in the susceptibility test |
| 37 | `ANTIMICROBIAL_LOINC` | VARCHAR(10) |  |  | The LOINC for the antimicrobial |
| 38 | `ANTIMICROBIAL_LOINC_LONG` | VARCHAR(255) |  |  | The long RELMA description for the mapped antimicrobial. |
| 39 | `ANTIMICROBIAL_LOINC_SHORT` | VARCHAR(60) |  |  | The short RELMA description for the mapped antimicrobial. |
| 40 | `ANTIMICROBIAL_MNEMONIC` | VARCHAR(10) |  |  | A standard (NCLS) abbreviation for an antimicrobial |
| 41 | `ATTEND_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The address of the attending physician. |
| 42 | `ATTEND_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The city of the attending physician. |
| 43 | `ATTEND_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The attending physician's email address. |
| 44 | `ATTEND_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The attending physician's fax number. |
| 45 | `ATTEND_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The attending physician's mobile phone number. |
| 46 | `ATTEND_PHYSICIAN_NAME` | VARCHAR(100) |  |  | The name of the attending physician. |
| 47 | `ATTEND_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The NPI for the attending physician. |
| 48 | `ATTEND_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The primary phone number of the attending physician. |
| 49 | `ATTEND_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The State of the attending physician. |
| 50 | `ATTEND_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code of the attending physician. |
| 51 | `BIRTH_DT_TM` | DATETIME |  |  | The patient's birth date. |
| 52 | `BUSINESS_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the business phone number. |
| 53 | `BUSINESS_PHONE` | VARCHAR(100) |  |  | The patient's business phone |
| 54 | `BUSINESS_PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's business phone number extension. |
| 55 | `CALL_INSTRUCTION` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the patient's number. |
| 56 | `CARESETTING_DESC` | VARCHAR(40) |  |  | The mapped caresetting for the ordering location. |
| 57 | `CLIA_NBR` | VARCHAR(10) |  |  | The ordering hospital CLIA number. |
| 58 | `CLIENT_ABX_CODE` | VARCHAR(40) |  |  | The client code value from code set 1011 for the antimicrobial. |
| 59 | `CLIENT_ABX_DESC` | VARCHAR(100) |  |  | The client code value description from code set 1011 for the antimicrobial. |
| 60 | `CLIENT_ABX_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 1011 for the antimicrobial. |
| 61 | `CLIENT_ABX_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 1011 for the antimicrobial. |
| 62 | `CLIENT_METHOD_CODE` | VARCHAR(40) |  |  | The client code value from code set 2058 for the collection method. |
| 63 | `CLIENT_METHOD_DESC` | VARCHAR(100) |  |  | The client code value description from code set 2058 for the collection method. |
| 64 | `CLIENT_METHOD_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 2058 for the collection method. |
| 65 | `CLIENT_METHOD_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 2058 for the collection method. |
| 66 | `CLIENT_ORDERABLE_CONCEPT_NAME` | VARCHAR(255) |  |  | The client LOINC code concept description for the orderable. |
| 67 | `CLIENT_ORDERABLE_LOINC_CODE` | VARCHAR(10) |  |  | The client assigned LOINC code for orderable. |
| 68 | `CLIENT_ORDERABLE_LOINC_DESC` | VARCHAR(255) |  |  | The client LOINC code description for the orderable. |
| 69 | `CLIENT_ORDER_CODE` | VARCHAR(40) |  |  | The client orderable number from code set 200. |
| 70 | `CLIENT_ORDER_DESC` | VARCHAR(100) |  |  | The client orderable description from code set 200. |
| 71 | `CLIENT_ORDER_DISPLAY` | VARCHAR(45) |  |  | The client orderable mnemonic from code set 200. |
| 72 | `CLIENT_ORGANISM_CODE` | VARCHAR(40) |  |  | The client code value from code set 1021/1022 for the organism or codified result. |
| 73 | `CLIENT_ORGANISM_DESC` | VARCHAR(100) |  |  | The client code value description from code set 1021/1022 for the organism or codified result. |
| 74 | `CLIENT_ORGANISM_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 1021/1022 for the organism or codified result. |
| 75 | `CLIENT_ORGANISM_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 1021/1022 for the organism or codified result. |
| 76 | `CLIENT_RESULT_IND_CODE` | VARCHAR(40) |  |  | The client code value code for the abnormal indicator. Code set 52. |
| 77 | `CLIENT_RESULT_IND_DESC` | VARCHAR(100) |  |  | The client code value description for the abnormal indicator. Code set 52. |
| 78 | `CLIENT_RESULT_IND_DISPLAY` | VARCHAR(45) |  |  | The client code value display for the abnormal indicator. Code set 52. |
| 79 | `CLIENT_SITE_CODE` | VARCHAR(40) |  |  | The client code value from code set 1028 for the body site. |
| 80 | `CLIENT_SITE_DESC` | VARCHAR(100) |  |  | The client code value description from code set 1028 for the body site. |
| 81 | `CLIENT_SITE_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 1028 for the body site. |
| 82 | `CLIENT_SITE_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 1028 for the body site. |
| 83 | `CLIENT_SPECIMEN_CODE` | VARCHAR(40) |  |  | The client code value from code set 2052 for the specimen. |
| 84 | `CLIENT_SPECIMEN_DESC` | VARCHAR(100) |  |  | The client code value description from code set 2052 for the specimen. |
| 85 | `CLIENT_SPECIMEN_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 2052 for the specimen. |
| 86 | `CLIENT_SPECIMEN_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 2052 for the specimen. |
| 87 | `CLIENT_UNIT_CODE` | VARCHAR(40) |  |  | The client code value from code set 54 for the unit of measure. |
| 88 | `CLIENT_UNIT_DESC` | VARCHAR(100) |  |  | The client code value description from code set 54 for the unit of measure. |
| 89 | `CLIENT_UNIT_DISPLAY` | VARCHAR(45) |  |  | The client code value display from code set 54 for the unit of measure. |
| 90 | `CLIENT_UNIT_MEANING` | VARCHAR(45) |  |  | The client code value CDF meaning from code set 54 for the unit of measure. |
| 91 | `COLLECTION_METHOD_CODE` | VARCHAR(6) |  |  | The code of the procedure for collecting a specimen. |
| 92 | `COLLECTION_METHOD_DESC` | VARCHAR(40) |  |  | The description of the procedure for collecting a specimen. |
| 93 | `COLLECTION_METHOD_ID` | VARCHAR(40) |  |  | The identifier for the procedure for collecting a specimen. |
| 94 | `COLLECTION_METHOD_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the collection method modifier. A modifier is the left, right, upper, lower location for the collection method. |
| 95 | `COLLECTION_METHOD_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED CT code for the collection method modifier. A modifier is the left, right, upper, lower location for the collection method. |
| 96 | `COLLECTION_METHOD_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection method. |
| 97 | `COLLECTION_SITE_CODE` | VARCHAR(6) |  |  | The SNOMED CT code for collection site from an HL7 file. |
| 98 | `COLLECTION_SITE_DESC` | VARCHAR(40) |  |  | The collection site for the microbiology specimen. |
| 99 | `COLLECTION_SITE_ID` | DOUBLE | NOT NULL |  | The dim table key for the collection site of the isolate. |
| 100 | `COLLECTION_SITE_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the body site modifier. A modifier is the left, right, upper, lower location for the site. |
| 101 | `COLLECTION_SITE_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED code for the body site modifier. A modifier is the left, right, upper, lower location for the body site. |
| 102 | `COLLECTION_SITE_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection site. |
| 103 | `COLLECTION_SOURCE_CODE` | VARCHAR(6) |  |  | The SNOMED CT code for specimen. |
| 104 | `COLLECTION_SOURCE_DESC` | VARCHAR(40) |  |  | The collection specimen for the microbiology order. |
| 105 | `COLLECTION_SOURCE_ID` | DOUBLE | NOT NULL |  | The dim table key for the collection specimen of the isolate. |
| 106 | `COLLECTION_SOURCE_SNOMED` | VARCHAR(10) |  |  | The HealthSentry assigned SNOMED CT for the collection specimen. |
| 107 | `COLLECTION_SRC_MOD_DESC` | VARCHAR(100) |  |  | The standard modifier description for the collection specimen modifier. A modifier is the left, right, upper, lower location for the specimen. |
| 108 | `COLLECTION_SRC_MOD_SNOMED` | VARCHAR(10) |  |  | The SNOMED CT code for the collection specimen modifier. A modifier is the left, right, upper, lower location for the specimen. |
| 109 | `COUNTY_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital three digit county FIPS code. |
| 110 | `DECEASED_DT_TM` | DATETIME |  |  | The date on which a person died or is officially deemed to have died. |
| 111 | `DIRECTOR_FIRST_NAME` | VARCHAR(100) |  |  | The hospital's director's first first name. |
| 112 | `DIRECTOR_LAST_NAME` | VARCHAR(100) |  |  | The hospital's director's last name. |
| 113 | `DIRECTOR_MIDDLE_NAME` | VARCHAR(100) |  |  | The hospital's director's middle name. |
| 114 | `DIRECTOR_PREFIX` | VARCHAR(10) |  |  | The hospital's director's prefix. |
| 115 | `DIRECTOR_SUFFIX` | VARCHAR(10) |  |  | The hospital's director's suffix. |
| 116 | `DIRECTOR_TITLE` | VARCHAR(10) |  |  | The hospital's director's title. |
| 117 | `DISCHARGED_DT_TM` | DATETIME |  |  | The date time in which the patient was discharged. |
| 118 | `DISCHARGE_DISP_DESC` | VARCHAR(190) |  |  | The mapped description for discharge disposition. |
| 119 | `EMAIL_ADDRESS` | VARCHAR(100) |  |  | The patient's email address |
| 120 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The encounter unique identifier used within the Cerner Health Facts Data Warehouse. This is the visit identifier for the patient that this record is associated. This number is unique to the patient. |
| 121 | `ETHNICITY` | VARCHAR(40) |  |  | The mapped ethnicity for the person. Identifies a religious national racial or cultural group of the person. |
| 122 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time of the contributor extraction of data. |
| 123 | `FINANCIAL_NBR` | VARCHAR(40) |  |  | This number identifies the encounter or visit typically for financial and medical record identification. This financial number should be unique per encounter and crosses clinical and billing systems. |
| 124 | `FINANCIAL_NBR_RAW` | VARCHAR(40) |  |  | This unformatted number identifies the encounter or visit typically for financial and medical record identification. This financial number should be unique per encounter and crosses clinical and billing systems. |
| 125 | `GENDER` | VARCHAR(60) |  |  | The gender of the patient. |
| 126 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The health system that the hospital belongs to. |
| 127 | `HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | The address of the hospital as defined by HealthSentry. |
| 128 | `HOSPITAL_ADDRESS_2` | VARCHAR(100) |  |  | The second line of the hospital's address. |
| 129 | `HOSPITAL_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the hospital number. |
| 130 | `HOSPITAL_CITY` | VARCHAR(50) |  |  | The city of the hospital as defined by HealthSentry. |
| 131 | `HOSPITAL_CODE` | DOUBLE |  |  | The hospital code. |
| 132 | `HOSPITAL_COUNTRY` | VARCHAR(100) |  |  | The country of the hospital for the ordering hospital. |
| 133 | `HOSPITAL_COUNTY` | VARCHAR(100) |  |  | The county of the hospital for the ordering hospital. |
| 134 | `HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display value of the hospital name. |
| 135 | `HOSPITAL_EXTENSION` | VARCHAR(100) |  |  | The phone extension of the hospital. |
| 136 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | The unique identifier of the hospital from the hf_d_hospital. Assigned per the organization roll up for the ordering facility. |
| 137 | `HOSPITAL_NAME` | VARCHAR(50) |  |  | The name of the ordering hospital as defined by HealthSentry. |
| 138 | `HOSPITAL_OID` | VARCHAR(100) | NOT NULL |  | The OID (HL7 Object Identifier) for the facility. http://www.hl7.org/oid/index.cfm |
| 139 | `HOSPITAL_PHONE` | VARCHAR(30) |  |  | The primary phone number of the hospital as defined by HealthSentry. |
| 140 | `HOSPITAL_STATE` | VARCHAR(2) |  |  | The state of the hospital as defined by HealthSentry. |
| 141 | `HOSPITAL_ZIP` | VARCHAR(20) |  |  | The zip code of the hospital as defined by HealthSentry. |
| 142 | `INTERP_RESULT_DESC` | VARCHAR(60) |  |  | The textual description of an interpretative result |
| 143 | `INTERP_RESULT_ID` | DOUBLE | NOT NULL |  | The dim table key for the interpretive result. |
| 144 | `ISOLATE_ID` | DOUBLE | NOT NULL |  | The dim table key for the isolate against which the susceptibility test is run |
| 145 | `ISOLATE_NAME` | VARCHAR(50) |  |  | The mapped description for the isolate. |
| 146 | `ISOLATE_REPT_CATEGORY` | VARCHAR(30) |  |  | The reporting category for the isolate. Typically the genus; however sometimes this is at a finer grain than the genus |
| 147 | `ISOLATE_TYPE` | VARCHAR(25) |  |  | A high level category for the isolate such as Bacteria, Virus, Fungus. |
| 148 | `LAB_COMPLETED_DT_TM` | DATETIME |  |  | The date/time the micro order was completed |
| 149 | `LAB_DRAWN_DT_TM` | DATETIME |  |  | The date/time the specimen was drawn |
| 150 | `LAB_PERFORMED_DT_TM` | DATETIME |  |  | The date and time in which the lab was performed. |
| 151 | `LAB_PROCEDURE_NAME` | VARCHAR(100) |  |  | The mapped lab procedure name for the detail test if general lab or orderable for microbiology. |
| 152 | `LAB_RECEIVED_DT_TM` | DATETIME |  |  | The date/time the specimen was received |
| 153 | `LOINC_CODE` | VARCHAR(10) |  |  | The PHIN approved LOINC codes used for reporting purposes. |
| 154 | `MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | The patient's medical record number. |
| 155 | `MEDICAL_RECORD_NBR_RAW` | VARCHAR(40) |  |  | The unformatted patient medical record number. |
| 156 | `MEDICAL_SERVICE_CODE` | VARCHAR(40) |  |  | A PHINVads standard abbreviation for the type of medical service for the visit. |
| 157 | `MEDICAL_SERVICE_DESC` | VARCHAR(100) |  |  | A PHINVads standard description for the type of medical service for the visit. |
| 158 | `MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the type or category of medical service that was received. |
| 159 | `MICRO_RESULT_TYPE_DESC` | VARCHAR(60) |  |  | The description for the micro result type. This is similar to micro_result_type and more specific for the stains. |
| 160 | `MICRO_RESULT_TYPE_ID` | DOUBLE | NOT NULL |  | The dim table key for the type of micro result (preliminary, final, etc.) |
| 161 | `MOBILE_NUMBER` | VARCHAR(100) |  |  | The patient's mobile phone number. |
| 162 | `MOTHER_MAIDEN_FIRST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden first name. |
| 163 | `MOTHER_MAIDEN_LAST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden last name. |
| 164 | `MOTHER_MAIDEN_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's mother's maiden name initials. |
| 165 | `MOTHER_MAIDEN_NAME_PREFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name prefix. |
| 166 | `MOTHER_MAIDEN_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name suffix. |
| 167 | `MOTHER_MAIDEN_NAME_TITLE` | VARCHAR(100) |  |  | The patient's mother's maiden name title. |
| 168 | `NAME_INITIALS` | VARCHAR(100) |  |  | The initials for the person's name. |
| 169 | `NAME_PREFIX` | VARCHAR(100) |  |  | The prefix for the person's name. |
| 170 | `NAME_SUFFIX` | VARCHAR(100) |  |  | The suffix for the person's name. |
| 171 | `NAME_TITLE` | VARCHAR(100) |  |  | The title for the person's name. |
| 172 | `NEXT_OF_KIN_ADDRESS_1` | VARCHAR(100) |  |  | The patient's next of kin's address. |
| 173 | `NEXT_OF_KIN_ADDRESS_2` | VARCHAR(100) |  |  | The patient's next of kin's address. |
| 174 | `NEXT_OF_KIN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the next of kin number. |
| 175 | `NEXT_OF_KIN_CITY` | VARCHAR(100) |  |  | The patient's next of kin's city. |
| 176 | `NEXT_OF_KIN_FIRST_NAME` | VARCHAR(40) |  |  | The patient's next of kin's first name. |
| 177 | `NEXT_OF_KIN_LAST_NAME` | VARCHAR(100) |  |  | The patient's next of kin's last name. |
| 178 | `NEXT_OF_KIN_MIDDLE_NAME` | VARCHAR(40) |  |  | The patient's next of kin's middle name. |
| 179 | `NEXT_OF_KIN_NAME` | VARCHAR(100) |  |  | The patient's next of kin's name. |
| 180 | `NEXT_OF_KIN_PHONE` | VARCHAR(30) |  |  | The patient's next of kin's primary phone number. |
| 181 | `NEXT_OF_KIN_PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's next of kin's phone extension. |
| 182 | `NEXT_OF_KIN_RELATION` | VARCHAR(40) |  |  | The relation of the next of kin to the patient. |
| 183 | `NEXT_OF_KIN_RELATION_CODE` | VARCHAR(40) |  |  | The mapped person relationship for the next of kin. |
| 184 | `NEXT_OF_KIN_STATE` | VARCHAR(50) |  |  | The patient's next of kin's state. |
| 185 | `NEXT_OF_KIN_ZIP_CODE` | VARCHAR(25) |  |  | The patient's next of kin's zip code. |
| 186 | `NOK_COUNTRY` | VARCHAR(50) |  |  | The country of the patient's next of kin. |
| 187 | `NOK_COUNTY` | VARCHAR(50) |  |  | The county of the patient's next of kin. |
| 188 | `NOK_EMAIL` | VARCHAR(100) |  |  | The email address of the patient's next of kin. |
| 189 | `NOK_NAME_INITIALS` | VARCHAR(100) |  |  | The initials of the patient's next of kin name. |
| 190 | `NOK_NAME_PREFIX` | VARCHAR(100) |  |  | The prefix of the patient's next of kin name. |
| 191 | `NOK_NAME_SUFFIX` | VARCHAR(100) |  |  | The suffix of the patient's next of kin name. |
| 192 | `NOK_NAME_TITLE` | VARCHAR(100) |  |  | The title of the patient's next of kin name. |
| 193 | `NPI` | VARCHAR(10) |  |  | The NPI for the perform hospital. |
| 194 | `NUMERIC_RESULT` | VARCHAR(40) |  |  | A numeric/alpha numeric result for this susceptibility test. |
| 195 | `ORDERABLE_LOINC_CODE` | VARCHAR(10) |  |  | The LOINC code for the orderable. |
| 196 | `ORDERABLE_LOINC_CODE_LONG` | VARCHAR(255) |  |  | The long RELMA description for the mapped orderable LOINC. |
| 197 | `ORDERABLE_LOINC_CODE_SHORT` | VARCHAR(60) |  |  | The short RELMA description for the mapped orderable LOINC |
| 198 | `ORDERED_DT_TM` | DATETIME |  |  | The date/time an order was placed. |
| 199 | `ORDER_CARESETTING_RAW` | VARCHAR(40) |  |  | The client value representing the location (nursing or ambulatory unit) where the test was ordered. |
| 200 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE | NOT NULL |  | The dim table key for the ordered lab procedure. |
| 201 | `ORDER_PHYSICIAN_ADDRESS` | VARCHAR(100) |  |  | The ordering physician's address. |
| 202 | `ORDER_PHYSICIAN_ADDRESS_2` | VARCHAR(255) |  |  | The second line of the ordering physician's address. |
| 203 | `ORDER_PHYSICIAN_CITY` | VARCHAR(100) |  |  | The ordering physician's city. |
| 204 | `ORDER_PHYSICIAN_COUNTRY` | VARCHAR(100) |  |  | The country of the ordering physician. |
| 205 | `ORDER_PHYSICIAN_COUNTY` | VARCHAR(100) |  |  | The county of the ordering physician. |
| 206 | `ORDER_PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The ordering physician's email address. |
| 207 | `ORDER_PHYSICIAN_EXTENSION` | VARCHAR(100) |  |  | The phone extension of the ordering physician. |
| 208 | `ORDER_PHYSICIAN_FAX` | VARCHAR(50) |  |  | The ordering physician's fax number. |
| 209 | `ORDER_PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | The ordering physician's first name. |
| 210 | `ORDER_PHYSICIAN_INITIALS` | VARCHAR(100) |  |  | The three character initial abbreviation of the ordering physician's name. |
| 211 | `ORDER_PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | The ordering physician's last name. |
| 212 | `ORDER_PHYSICIAN_MIDDLE_NAME` | VARCHAR(100) |  |  | The ordering physician's middle name. |
| 213 | `ORDER_PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The ordering physician's mobile phone number. |
| 214 | `ORDER_PHYSICIAN_NAME` | VARCHAR(100) |  |  | The ordering physician's full name. |
| 215 | `ORDER_PHYSICIAN_NPI` | VARCHAR(200) |  |  | The NPI for the ordering physician. |
| 216 | `ORDER_PHYSICIAN_PHONE` | VARCHAR(30) |  |  | The ordering physician's primary phone number. |
| 217 | `ORDER_PHYSICIAN_PREFIX` | VARCHAR(100) |  |  | The prefix of the ordering physician. |
| 218 | `ORDER_PHYSICIAN_STATE` | VARCHAR(100) |  |  | The ordering physician's state. |
| 219 | `ORDER_PHYSICIAN_SUFFIX` | VARCHAR(100) |  |  | The suffix of the ordering physician. |
| 220 | `ORDER_PHYSICIAN_TITLE` | VARCHAR(100) |  |  | The title of the ordering physician. |
| 221 | `ORDER_PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The ordering physician's zip code. |
| 222 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE |  |  | Within microbiology, the organisms have a sequence. This is the sequence number of the organism that is associated with the susceptibility results. |
| 223 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The encounter identifier from the source system. |
| 224 | `OUTBOUND_HSS_ID` | DOUBLE | NOT NULL |  | The unique identifier of the organization that this result will be reported to. |
| 225 | `O_PHYSICIAN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the physician number. |
| 226 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 227 | `PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | The first line of the patient's address. |
| 228 | `PATIENT_ADDRESS_2` | VARCHAR(100) |  |  | The second line of the patient's address. |
| 229 | `PATIENT_CITY` | VARCHAR(100) |  |  | The city that the patient lives in. |
| 230 | `PATIENT_COUNTRY` | VARCHAR(50) |  |  | The country that the patient lives in. |
| 231 | `PATIENT_COUNTRY_CODE` | VARCHAR(10) |  |  | The patient's country standard PHINVads code. |
| 232 | `PATIENT_COUNTY` | VARCHAR(50) |  |  | The county that the patient lives in. |
| 233 | `PATIENT_COUNTY_CODE` | VARCHAR(40) |  |  | The county code that the patient lives in. |
| 234 | `PATIENT_FIRST_NAME` | VARCHAR(40) |  |  | The first name of the patient. |
| 235 | `PATIENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the patient. |
| 236 | `PATIENT_LAST_NAME` | VARCHAR(100) |  |  | The last name of the patient. |
| 237 | `PATIENT_MAIDEN_LAST_NAME` | VARCHAR(200) |  |  | The patient's maiden last name. |
| 238 | `PATIENT_MIDDLE_NAME` | VARCHAR(40) |  |  | The middle name of the patient. |
| 239 | `PATIENT_NAME` | VARCHAR(100) |  |  | The full name of the patient. |
| 240 | `PATIENT_PHONE` | VARCHAR(40) |  |  | The primary phone number of the patient. |
| 241 | `PATIENT_SSN` | VARCHAR(40) |  |  | The social security number of the patient. |
| 242 | `PATIENT_STATE` | VARCHAR(50) |  |  | The state that the patient lives in. |
| 243 | `PATIENT_STATE_CODE` | VARCHAR(10) |  |  | The patient state FIP code per the zipcode. |
| 244 | `PATIENT_TYPE_DESC` | VARCHAR(60) |  |  | The mapped visit type for the encounter. |
| 245 | `PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | The zip code that the patient lives in. |
| 246 | `PERFORMED_BENCH_ADDRESS` | VARCHAR(100) |  |  | The mapped perform hospital address determined from the bench level. |
| 247 | `PERFORMED_BENCH_CITY` | VARCHAR(50) |  |  | The mapped perform hospital city determined from the bench level. |
| 248 | `PERFORMED_BENCH_CLIA_NBR` | VARCHAR(10) |  |  | The mapped perform hospital CLIA number determined from the bench level. |
| 249 | `PERFORMED_BENCH_CODE` | DOUBLE |  |  | N/A. Blank. |
| 250 | `PERFORMED_BENCH_COUNTRY` | VARCHAR(100) |  |  | The mapped perform hospital country determined from the bench level. |
| 251 | `PERFORMED_BENCH_COUNTY` | VARCHAR(100) |  |  | The mapped perform hospital county determined from the bench level. |
| 252 | `PERFORMED_BENCH_DISPLAY` | VARCHAR(30) |  |  | The mapped perform hospital display name determined from the bench level. |
| 253 | `PERFORMED_BENCH_ID` | DOUBLE | NOT NULL |  | The perform hospital mapped at the bench level. The ID from hf_d_hospital. |
| 254 | `PERFORMED_BENCH_NAME` | VARCHAR(50) |  |  | The mapped perform hospital name determined from the bench level. |
| 255 | `PERFORMED_BENCH_PHONE` | VARCHAR(30) |  |  | The mapped perform hospital phone number determined from the bench level. |
| 256 | `PERFORMED_BENCH_STATE` | VARCHAR(2) |  |  | The mapped perform hospital state determined from the bench level. |
| 257 | `PERFORMED_BENCH_ZIP` | VARCHAR(25) |  |  | The mapped perform hospital zip determined from the bench level. |
| 258 | `PERFORMED_HOSPITAL_ADDRESS` | VARCHAR(100) |  |  | The address of the hospital in which the action was performed. |
| 259 | `PERFORMED_HOSPITAL_CITY` | VARCHAR(50) |  |  | The city of the hospital in which the action was performed. |
| 260 | `PERFORMED_HOSPITAL_CLIA_NBR` | VARCHAR(10) |  |  | The CLIA number for the performing hospital. |
| 261 | `PERFORMED_HOSPITAL_CODE` | DOUBLE |  |  | The identifying code of the hospital in which the action was performed. |
| 262 | `PERFORMED_HOSPITAL_COUNTRY` | VARCHAR(100) |  |  | The country of the performing hospital. |
| 263 | `PERFORMED_HOSPITAL_COUNTY` | VARCHAR(100) |  |  | The county of the performing hospital. |
| 264 | `PERFORMED_HOSPITAL_DISPLAY` | VARCHAR(30) |  |  | The display value of the performed hospital name. |
| 265 | `PERFORMED_HOSPITAL_ID` | DOUBLE | NOT NULL |  | The unique identifier of the hospital in which the action was performed. |
| 266 | `PERFORMED_HOSPITAL_NAME` | VARCHAR(50) |  |  | The name of the hospital in which the action was performed. |
| 267 | `PERFORMED_HOSPITAL_PHONE` | VARCHAR(30) |  |  | The primary phone number of the hospital in which the action was performed. |
| 268 | `PERFORMED_HOSPITAL_STATE` | VARCHAR(2) |  |  | The state of the hospital in which the action was performed. |
| 269 | `PERFORMED_HOSPITAL_ZIP` | VARCHAR(25) |  |  | The zip code of the hospital in which the action was performed. |
| 270 | `PERFORMED_PRSNL_ADDRESS` | VARCHAR(100) |  |  | The mapped perform hospital address determined from action perform personnel. |
| 271 | `PERFORMED_PRSNL_CITY` | VARCHAR(50) |  |  | The mapped perform hospital city determined from action perform personnel. |
| 272 | `PERFORMED_PRSNL_CLIA_NBR` | VARCHAR(10) |  |  | The mapped perform hospital CLIA number determined from action perform personnel. |
| 273 | `PERFORMED_PRSNL_CODE` | DOUBLE |  |  | N/A. Blank. |
| 274 | `PERFORMED_PRSNL_COUNTRY` | VARCHAR(100) |  |  | The mapped perform hospital country determined from action perform personnel. |
| 275 | `PERFORMED_PRSNL_COUNTY` | VARCHAR(100) |  |  | The mapped perform hospital county determined from action perform personnel. |
| 276 | `PERFORMED_PRSNL_DISPLAY` | VARCHAR(30) |  |  | The mapped perform hospital display name determined from action perform personnel. |
| 277 | `PERFORMED_PRSNL_ID` | DOUBLE | NOT NULL |  | The mapped perform hospital id determined from action perform personnel from hf_d_hospital. |
| 278 | `PERFORMED_PRSNL_NAME` | VARCHAR(50) |  |  | The mapped perform hospital name determined from action perform personnel. |
| 279 | `PERFORMED_PRSNL_PHONE` | VARCHAR(30) |  |  | The mapped perform hospital phone determined from action perform personnel. |
| 280 | `PERFORMED_PRSNL_STATE` | VARCHAR(2) |  |  | The mapped perform hospital state determined from action perform personnel. |
| 281 | `PERFORMED_PRSNL_ZIP` | VARCHAR(25) |  |  | The mapped perform hospital zip code determined from action perform personnel. |
| 282 | `PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's phone extension |
| 283 | `RACE` | VARCHAR(40) |  |  | The mapped race for the person. |
| 284 | `RAW_FACILITY_ADDRESS` | VARCHAR(100) |  |  | The first address for the raw ordering facility. |
| 285 | `RAW_FACILITY_ADDRESS_2` | VARCHAR(100) |  |  | The second address for the raw facility. |
| 286 | `RAW_FACILITY_ADDRESS_3` | VARCHAR(100) |  |  | The third address for the raw facility. |
| 287 | `RAW_FACILITY_ADDRESS_4` | VARCHAR(100) |  |  | The fourth address for the raw facility. |
| 288 | `RAW_FACILITY_CITY` | VARCHAR(100) |  |  | The raw ordering facility city. |
| 289 | `RAW_FACILITY_NAME` | VARCHAR(100) |  |  | The raw ordering facility client description. |
| 290 | `RAW_FACILITY_PHONE` | VARCHAR(50) |  |  | The phone number for the raw ordering facility. |
| 291 | `RAW_FACILITY_STATE` | VARCHAR(50) |  |  | The raw ordering facility state. |
| 292 | `RAW_FACILITY_ZIP_CODE` | VARCHAR(25) |  |  | The raw ordering facility zip code. |
| 293 | `REASON_FOR_STUDY_DESC` | VARCHAR(1000) |  |  | ICD code and descriptions for the visit selected by a clinician. This is often missing. |
| 294 | `RELEASE_NUMBER` | VARCHAR(255) |  |  | The Health Data release number at the time of the record being updated. |
| 295 | `REMARK` | VARCHAR(100) |  |  | Blank. |
| 296 | `RESULT_INDICATOR_DESC` | VARCHAR(60) |  |  | The mapping description of the normality of the result (out of range, not normal, etc.). |
| 297 | `RESULT_TYPE_PROCEDURE_DESC` | VARCHAR(60) |  |  | A textual description of the detail procedure/report (preliminary, final, etc.) |
| 298 | `RESULT_TYPE_PROCEDURE_ID` | DOUBLE | NOT NULL |  | The dim table key for the type of procedure that was performed |
| 299 | `RESULT_UNIT_DESC` | VARCHAR(60) |  |  | The description for the result unit. |
| 300 | `RESULT_UNIT_DISPLAY` | VARCHAR(40) |  |  | The display of the unit of measure for the result. |
| 301 | `RESULT_UNIT_UCUM` | VARCHAR(250) |  |  | The standard UCUM description for the susceptibility result unit. |
| 302 | `SNOMEDCT_CODE` | VARCHAR(15) |  |  | The SNOMED CT code for the isolate. |
| 303 | `SNOMED_CODE` | VARCHAR(15) |  |  | The SNOMED code for the isolate. |
| 304 | `SRC_FCT_KEY` | VARCHAR(100) |  |  | The internal identifier of the fact table from which the record came. |
| 305 | `STATE_FIPS_CODE` | VARCHAR(10) |  |  | The ordering hospital two digit state FIPS code. |
| 306 | `TEST_TYPE_DESC` | VARCHAR(40) |  |  | The textual description for the type of susceptibility test (Minimum Inhibitory Concentration, Kirby Bauer, etc.) |
| 307 | `TEST_TYPE_ID` | DOUBLE | NOT NULL |  | The dim table key for the type of susceptibility test |
| 308 | `TEST_TYPE_MNEMONIC` | VARCHAR(25) |  |  | A standard abbreviation for the type of susceptibility test (MIC, KB, etc.) |
| 309 | `UNIQUE_ORDER_ID` | VARCHAR(80) |  |  | The unique identifier of the order. |
| 310 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 311 | `VERIFIED_DT_TM` | DATETIME |  |  | Date and time this result / event is verified |
| 312 | `VERIFIED_PRSNL_INITIALS` | VARCHAR(100) |  |  | The initials of the personnel that verified the results. |
| 313 | `VERIFIED_PRSNL_NAME` | VARCHAR(100) |  |  | The full name of the personnel that verified the results. |
| 314 | `VERIFIED_PRSNL_PREFIX` | VARCHAR(100) |  |  | The prefix of the personnel that verified the results. |
| 315 | `VERIFIED_PRSNL_SUFFIX` | VARCHAR(100) |  |  | The suffix of the personnel that verified the results. |
| 316 | `VERIFIED_PRSNL_TITLE` | VARCHAR(100) |  |  | The title of the personnel that verified the results. |
| 317 | `VITAL_STATUS` | VARCHAR(60) |  |  | The mapped vital status for there person: alive, deceased, or unknown. |
| 318 | `WEIGHT` | DOUBLE |  |  | The weight entered on the encounter record. Mostly blank or out of date. |
| 319 | `WEIGHT_UNIT_DISPLAY` | VARCHAR(40) |  |  | The unit for weight from the encounter record. Mostly blank. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

