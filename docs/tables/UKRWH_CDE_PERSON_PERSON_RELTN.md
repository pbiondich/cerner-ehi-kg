# UKRWH_CDE_PERSON_PERSON_RELTN

> Contains Person Person relationships pertinent to pateints for a specific Trust.

**Description:** UK Reporting Warehouse Consolidated Data Extract Person Person Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUSINESS_PHONE_NBR` | VARCHAR(100) |  |  | The patients business phone number |
| 2 | `CITY` | VARCHAR(100) |  |  | The fifth text string comprising one line of an ADDRESS of the patient |
| 3 | `COUNTRY_REF` | VARCHAR(40) |  |  | The country code is the code set value which identifies the country for the address row. |
| 4 | `EMAIL_ADDR` | VARCHAR(100) |  |  | The code allocated by the Post Office to identify a group of postal delivery points |
| 5 | `EXTRACT_DT_M` | DATETIME |  |  | The date and time the row was extracted |
| 6 | `FIRST_NAME` | VARCHAR(200) |  |  | This is the person's first given name |
| 7 | `FIRST_NAME_UNF` | VARCHAR(100) |  |  | First name key |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 9 | `FULL_FORMATTED_NAME` | VARCHAR(100) |  |  | This is the complete person name including punctuation, formatting, prefix, and suffix |
| 10 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 12 | `HOME_PHONE_NBR` | VARCHAR(100) |  |  | The patients home phone number |
| 13 | `LAST_NAME` | VARCHAR(200) |  |  | This is the person's family name |
| 14 | `LAST_NAME_UNF` | VARCHAR(100) |  |  | Last name key |
| 15 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 16 | `LINE1_ADDR` | VARCHAR(100) |  |  | The first text string comprising one line of an ADDRESS of the patient |
| 17 | `LINE2_ADDR` | VARCHAR(100) |  |  | The second text string comprising one line of an ADDRESS of the patient |
| 18 | `LINE3_ADDR` | VARCHAR(100) |  |  | The third text string comprising one line of an ADDRESS of the patient |
| 19 | `LINE4_ADDR` | VARCHAR(100) |  |  | The fourth text string comprising one line of an ADDRESS of the patient |
| 20 | `MIDDLE_NAME` | VARCHAR(200) |  |  | This is the person's middle or secondary given name or names |
| 21 | `MOBILE_PHONE_NBR` | VARCHAR(100) |  |  | The patients mobile phone number |
| 22 | `PERSON_PERSON_RELTN_SK` | VARCHAR(40) |  |  | The identifying key of Millennium Person Person Relationship |
| 23 | `PERSON_RELTN_REF` | VARCHAR(40) |  |  | Person Relation Code Value |
| 24 | `PERSON_RELTN_TYPE_REF` | VARCHAR(40) |  |  | Code value indicating what type of relationship this is |
| 25 | `PERSON_SK` | VARCHAR(40) | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 26 | `POSTCODE` | CHAR(25) |  |  | This field contains the postal code for the street address in the address row. |
| 27 | `PREFIX_NAME` | VARCHAR(100) |  |  | Name prefix includes any titles that will precede the regular person name |
| 28 | `RELATED_PERSON_SK` | VARCHAR(40) |  |  | Millennium Related Person ID |
| 29 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 30 | `UKRWH_CDE_PERSON_PATIENT_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde person patient table. It is an internal system assigned number. |
| 31 | `UKRWH_CDE_PERS_PERS_RELTN_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde person person relation table. It is an internal system assigned number. |
| 32 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_PERSON_PATIENT_KEY` | [UKRWH_CDE_PERSON_PATIENT](UKRWH_CDE_PERSON_PATIENT.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |

