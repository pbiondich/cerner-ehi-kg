# HF_D_PATIENT

> This is the HealthFacts dimension table that contains a patient

**Description:** HF_D_PATIENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 87

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | The patient alternative first address. |
| 2 | `ALT_PATIENT_ADDRESS_2` | VARCHAR(100) |  |  | The patient alternative second address. |
| 3 | `ALT_PATIENT_CITY` | VARCHAR(100) |  |  | The patient alternative city. |
| 4 | `ALT_PATIENT_COUNTRY` | VARCHAR(100) |  |  | The patient alternative country. |
| 5 | `ALT_PATIENT_COUNTY` | VARCHAR(100) |  |  | The patient alternative county. |
| 6 | `ALT_PATIENT_FIRST_NAME` | VARCHAR(100) |  |  | The patient alternative first name. |
| 7 | `ALT_PATIENT_LAST_NAME` | VARCHAR(100) |  |  | The patient alternative last name. |
| 8 | `ALT_PATIENT_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's alternative initials. |
| 9 | `ALT_PATIENT_NAME_PREFIX` | VARCHAR(100) |  |  | The patient alternative name prefix. |
| 10 | `ALT_PATIENT_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient alternative name suffix. |
| 11 | `ALT_PATIENT_NAME_TITLE` | VARCHAR(100) |  |  | The patient alternative name title. |
| 12 | `ALT_PATIENT_STATE` | VARCHAR(100) |  |  | The patient alternative state. |
| 13 | `ALT_PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | The patient alternative zip code. |
| 14 | `ARCHIVE_IND` | DOUBLE |  |  | An Indicator to show the which is the active, or most recent, record. |
| 15 | `BIRTH_DT_TM` | DATETIME |  |  | Patient's birth date and time |
| 16 | `BUSINESS_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the business phone number. |
| 17 | `BUSINESS_PHONE` | VARCHAR(100) |  |  | The patient's business phone number. |
| 18 | `BUSINESS_PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's business phone number extension. |
| 19 | `CALL_INSTRUCTION` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the business phone number. |
| 20 | `COMM_MED_RECORD_NBR_RAW` | VARCHAR(20) |  |  | The raw community medical record number |
| 21 | `COMM_MED_RECORD_NUMBER` | VARCHAR(40) |  |  | Patient community medical record number |
| 22 | `COUNTY_CODE` | VARCHAR(40) |  |  | The source key of the county from the source system |
| 23 | `DECEASED_DT_TM` | DATETIME |  |  | The date and time in which the patient expired. |
| 24 | `EMAIL_ADDRESS` | VARCHAR(100) |  |  | The patient's email address. |
| 25 | `ETHNICITY` | VARCHAR(40) |  |  | Identifies a religious national racial or cultural group of the person. |
| 26 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 27 | `GENDER` | VARCHAR(40) |  |  | Patient's gender |
| 28 | `LANGUAGE` | VARCHAR(120) |  |  | The dialect of the primary language spoken by the person. |
| 29 | `MARITAL_STATUS` | VARCHAR(40) |  |  | Patient's marital status |
| 30 | `MOTHER_MAIDEN_FIRST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden first name. |
| 31 | `MOTHER_MAIDEN_LAST_NAME` | VARCHAR(200) |  |  | The patient's mother's maiden last name. |
| 32 | `MOTHER_MAIDEN_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's mother's maiden name initials. |
| 33 | `MOTHER_MAIDEN_NAME_PREFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name prefix. |
| 34 | `MOTHER_MAIDEN_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient's mother's maiden name suffix. |
| 35 | `MOTHER_MAIDIN_NAME_TITLE` | VARCHAR(100) |  |  | The patient's mother's maiden name title. |
| 36 | `NAME_INITIALS` | VARCHAR(100) |  |  | The patient's initials. |
| 37 | `NAME_PREFIX` | VARCHAR(100) |  |  | The prefix of the patient name. |
| 38 | `NAME_SUFFIX` | VARCHAR(100) |  |  | The suffix of the patient name. |
| 39 | `NAME_TITLE` | VARCHAR(100) |  |  | The title of the patient. |
| 40 | `NEXT_OF_KIN_ADDRESS_1` | VARCHAR(100) |  |  | The address of the patient's closest living blood relative or relatives |
| 41 | `NEXT_OF_KIN_ADDRESS_2` | VARCHAR(100) |  |  | The address of the patient's closest living blood relative or relatives |
| 42 | `NEXT_OF_KIN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the next of kin number. |
| 43 | `NEXT_OF_KIN_CITY` | VARCHAR(100) |  |  | The city where the patient's closest living blood relative or relatives live |
| 44 | `NEXT_OF_KIN_FIRST_NAME` | VARCHAR(100) |  |  | The first name of the patient's closest living blood relative or relatives |
| 45 | `NEXT_OF_KIN_LAST_NAME` | VARCHAR(100) |  |  | The last name of the patient's closest living blood relative or relatives |
| 46 | `NEXT_OF_KIN_MIDDLE_NAME` | VARCHAR(100) |  |  | The middle name of the patient's closest living blood relative or relatives |
| 47 | `NEXT_OF_KIN_NAME` | VARCHAR(200) |  |  | The person name of the patient's closest living blood relative or relatives |
| 48 | `NEXT_OF_KIN_PHONE` | VARCHAR(50) |  |  | The phone number of the patient's closest living blood relative or relatives live |
| 49 | `NEXT_OF_KIN_PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's next of kin's phone extension. |
| 50 | `NEXT_OF_KIN_RELATION` | VARCHAR(40) |  |  | The relationship type of the patient's closest living blood relative to the patient |
| 51 | `NEXT_OF_KIN_RELATION_CODE` | VARCHAR(40) |  |  | The relationship of the next of kin to the patient. |
| 52 | `NEXT_OF_KIN_STATE` | VARCHAR(50) |  |  | The state where the patient's closest living blood relative or relatives live |
| 53 | `NEXT_OF_KIN_ZIP_CODE` | VARCHAR(25) |  |  | The zip code where the patient's closest living blood relative or relatives live |
| 54 | `NOK_COUNTRY` | VARCHAR(50) |  |  | The country of the patient's next of kin. |
| 55 | `NOK_COUNTY` | VARCHAR(50) |  |  | The county of the patient's next of kin. |
| 56 | `NOK_EMAIL_ADDRESS` | VARCHAR(100) |  |  | The email of the patient's next of kin. |
| 57 | `NOK_NAME_INITIALS` | VARCHAR(100) |  |  | The patient's next of kin initials. |
| 58 | `NOK_NAME_PREFIX` | VARCHAR(100) |  |  | The patient's next of kin's name prefix. |
| 59 | `NOK_NAME_SUFFIX` | VARCHAR(100) |  |  | The patient's next of kin's name suffix. |
| 60 | `NOK_NAME_TITLE` | VARCHAR(100) |  |  | The patient's next of kin's title. |
| 61 | `PATIENT_ADDRESS_1` | VARCHAR(100) |  |  | Patient's home address |
| 62 | `PATIENT_ADDRESS_2` | VARCHAR(100) |  |  | Patient's home address |
| 63 | `PATIENT_CITY` | VARCHAR(100) |  |  | City of the patient's home |
| 64 | `PATIENT_COUNTRY` | VARCHAR(50) |  |  | Country of the patient's home |
| 65 | `PATIENT_COUNTY` | VARCHAR(50) |  |  | County of the patient's home |
| 66 | `PATIENT_FIRST_NAME` | VARCHAR(100) |  |  | Patient's first name |
| 67 | `PATIENT_ID` | DOUBLE |  |  | Primary key to the table. Unique defines a physician |
| 68 | `PATIENT_LAST_NAME` | VARCHAR(100) |  |  | Patient's last name |
| 69 | `PATIENT_MAIDEN_LAST_NAME` | VARCHAR(100) |  |  | The patient's maiden last name. |
| 70 | `PATIENT_MIDDLE_NAME` | VARCHAR(100) |  |  | Patient's middle name |
| 71 | `PATIENT_MOBILE` | VARCHAR(100) |  |  | The patient's mobile phone number. |
| 72 | `PATIENT_NAME` | VARCHAR(200) |  |  | Patient's name |
| 73 | `PATIENT_PHONE` | VARCHAR(50) |  |  | Patient's phone number |
| 74 | `PATIENT_SK` | VARCHAR(45) |  |  | This is the value of the unique primary identifier of the patient table. It is an internal system assigned number. |
| 75 | `PATIENT_SSN` | VARCHAR(40) |  |  | Patient's social security number |
| 76 | `PATIENT_STATE` | VARCHAR(50) |  |  | State of the patient's home |
| 77 | `PATIENT_ZIP_CODE` | VARCHAR(25) |  |  | Zipcode of the patient's home |
| 78 | `PHONE_EXTENSION` | VARCHAR(100) |  |  | The patient's phone extension. |
| 79 | `RACE` | VARCHAR(40) |  |  | Patient's race |
| 80 | `RELIGION` | VARCHAR(120) |  |  | The religion of the patient registered (I.e. Baptist Catholic Methodist etc.) |
| 81 | `REMARK` | VARCHAR(100) |  |  | REMARKS |
| 82 | `TEST_PATIENT_IND` | DOUBLE |  |  | This field indicates if the record is a test patient based on internal logic on the patient name. |
| 83 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 84 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 85 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |
| 86 | `VIP_IND` | DOUBLE |  |  | An indicator to flag persons as VIPs or not. 0 no and 1 yes. |
| 87 | `VITAL_STATUS` | VARCHAR(60) |  |  | A field that identifies alive, deceased status. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

