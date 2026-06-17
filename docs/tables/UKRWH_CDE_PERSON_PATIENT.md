# UKRWH_CDE_PERSON_PATIENT

> Contains patient details pertinent to a specific Trust.

**Description:** UK Reporting Warehouse Consolidated Data Extract Person Patient  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDE_PERSON_PATIENT_KEY`  
**Columns:** 56  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIRTH_DT_TM` | DATETIME |  |  | The date and time of birth for the person. |
| 2 | `BUSINESS_PHONE_NBR` | VARCHAR(100) |  |  | The patients business phone number |
| 3 | `CITY` | VARCHAR(100) |  |  | The city field is the text name of the city associated with the address row. |
| 4 | `COUNTRY_REF` | VARCHAR(40) |  |  | The country code is the code set value which identifies the country for the address row. |
| 5 | `DECEASED_DT_TM` | DATETIME |  |  | The date and time of death for the person. |
| 6 | `DECEASED_REF` | VARCHAR(40) |  |  | Identifies if the person is deceased. |
| 7 | `DECEASED_SOURCE_REF` | VARCHAR(40) |  |  | Defines the particular source that gave deceased information concerning a person.. |
| 8 | `EMAIL_ADDR` | VARCHAR(100) |  |  | This field contains the patients email address |
| 9 | `ESTIMATED_BIRTH_DT_REF` | VARCHAR(40) |  |  | Birth date code indicates the kind of birth date and time value that is contained in the birth_dt_tm field. (i.e., estimated, still born, unknown, etc.) |
| 10 | `ETHNIC_GROUP_REF` | VARCHAR(40) |  |  | Identifies a religious, national, racial, or cultural group of the person. |
| 11 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 12 | `FIRST_NAME` | VARCHAR(200) |  |  | This is the person's given first name. |
| 13 | `FIRST_NAME_UNF` | VARCHAR(100) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 15 | `FULL_FORMATTED_NAME` | VARCHAR(100) |  |  | This is the complete person name including punctuation and formatting. |
| 16 | `GP_PRSNL` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the personnel table. This is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table |
| 17 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 18 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 19 | `HOME_PHONE_NBR` | VARCHAR(100) |  |  | The patients home phone number |
| 20 | `LAST_NAME` | VARCHAR(200) |  |  | This is the person's family name. |
| 21 | `LAST_NAME_UNF` | VARCHAR(100) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 22 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 23 | `LINE1_ADDR` | VARCHAR(100) |  |  | This is the first line of the street address. |
| 24 | `LINE2_ADDR` | VARCHAR(100) |  |  | This is the second line of the street address. |
| 25 | `LINE3_ADDR` | VARCHAR(100) |  |  | This is the third line of the street address. The third line of the street address will generally only be used for international addresses. |
| 26 | `LINE4_ADDR` | VARCHAR(100) |  |  | This is the fourth line of the street address. The fourth line of the street address will generally only be used for international addresses. |
| 27 | `LOCAL_PATIENT_IDENT` | VARCHAR(10) |  |  | This number is used to identify a patient uniquely within a Health Care Provider. |
| 28 | `LOCAL_PATIENT_IDENT_ALIAS_REF` | VARCHAR(40) |  |  | The alias is an identifier (I.e., SSN, medical record number, etc.) for a person. The alias may be unique or non-unique depending on the type of alias. |
| 29 | `MARITAL_TYPE_REF` | VARCHAR(40) |  |  | This field identifies the status of the person with regard to being married. |
| 30 | `MIDDLE_NAME` | VARCHAR(200) |  |  | This is the given middle name for the person. |
| 31 | `MOBILE_PHONE_NBR` | VARCHAR(100) |  |  | The patients mobile phone number |
| 32 | `NAME_PREFIX_NAME` | VARCHAR(100) |  |  | This field containsthe patients name prefix |
| 33 | `NHS_NBR_IDENT` | VARCHAR(20) |  |  | The alias is an identifier (I.e., SSN, medical record number, etc.) for a person. The alias may be unique or non-unique depending on the type of alias. |
| 34 | `NHS_NBR_IDENT_STATUS_REF` | VARCHAR(40) |  |  | Person Alias Status Code identifies the status of an alias( i.e. Verified, Not traced, Trace in Progress, etc.) |
| 35 | `ORGANIZATION_SK` | VARCHAR(40) |  |  | This field contains the unique identifier for the Trust |
| 36 | `ORGAN_DONOR_IND` | DOUBLE |  |  | A sequentially assigned number which uniquely identifies an Organ Donor record. |
| 37 | `PCT_RESIDENCE_NACS` | VARCHAR(5) |  |  | This field contains the NACS code for the PCT where the patient resides |
| 38 | `PERSON_ACTIVE_IND` | DOUBLE |  |  | The Millennium person table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 39 | `PERSON_CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the person table. |
| 40 | `PERSON_CREATE_PRSNL` | VARCHAR(40) |  |  | This is the person/personnel responsible for creating a row in the person table. |
| 41 | `PERSON_SK` | VARCHAR(40) | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 42 | `PERSON_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 43 | `PERSON_UPDT_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 44 | `POSTCODE` | VARCHAR(25) |  |  | This field contains the postal code for the street address in the address row. |
| 45 | `REGISTERED_GP_PRCTC_ORG_NACS` | VARCHAR(6) |  |  | The NACS code for the registered GP Practice |
| 46 | `RELIGION_REF` | VARCHAR(40) |  |  | A particular integrated system of belief in a supernatural power. |
| 47 | `SERIAL_CHANGE_NBR_IDENT` | DOUBLE |  |  | A number to provide a unique identifier for each serial change |
| 48 | `SEX_REF` | VARCHAR(40) |  |  | The gender of the patient (i.e., male, female, unknown). |
| 49 | `SHA_RESIDENCE_NACS` | VARCHAR(5) |  |  | This field contains the NACS code for the SHA where the patient resides |
| 50 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 51 | `UKRWH_CDE_PERSON_PATIENT_KEY` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ukrwh cde person patient table. It is an internal system assigned number. |
| 52 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 53 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block |
| 54 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row |
| 55 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 56 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_AE_ATTENDANCE](UKRWH_CDE_AE_ATTENDANCE.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |
| [UKRWH_CDE_EAL_ENTRY](UKRWH_CDE_EAL_ENTRY.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |
| [UKRWH_CDE_IP_ADMISSION](UKRWH_CDE_IP_ADMISSION.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |
| [UKRWH_CDE_OP_REFERRAL](UKRWH_CDE_OP_REFERRAL.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |
| [UKRWH_CDE_PERSON_PERSON_RELTN](UKRWH_CDE_PERSON_PERSON_RELTN.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |

