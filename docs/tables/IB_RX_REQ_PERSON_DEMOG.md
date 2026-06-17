# IB_RX_REQ_PERSON_DEMOG

> Contains the patient demographic information for the prescription request on the inbound pharmacy request. Multiple prescription request may be associated to the same patient demographics.multiple Inbound Rx Requests will be linked to this person.

**Description:** Inbound Rx Request Person Demographics  
**Table type:** ACTIVITY  
**Primary key:** `IB_RX_REQ_PERSON_DEMOG_ID`  
**Columns:** 24  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIRTH_DT_TM` | DATETIME |  |  | *** OBSOLETE *** |
| 2 | `BIRTH_DT_TXT` | VARCHAR(10) |  |  | Field used to store birth date for the patient associated to the RxChange formatted as YYYY-MM-DD |
| 3 | `BIRTH_PREC_FLAG` | DOUBLE |  |  | Used to denote what information was captured for birth date. A flag of 1 means the date is precise to the day, a flag of 2 means the date is precise to month and a flag of 3 means the date is precise to year. A flag of 0 means the date precision is not set and will default to precise to the day if the date exists. |
| 4 | `CITY_NAME` | VARCHAR(255) |  |  | The patient's city address. |
| 5 | `FIRST_NAME` | VARCHAR(255) |  |  | The patient's first name. |
| 6 | `GENDER_CD` | DOUBLE | NOT NULL |  | Gender of the patient. |
| 7 | `IB_RX_REQ_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 8 | `IB_RX_REQ_PERSON_DEMOG_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that is used to identify an individual person demographic. |
| 9 | `LAST_NAME` | VARCHAR(255) |  |  | The patient's last name. |
| 10 | `MIDDLE_NAME` | VARCHAR(255) |  |  | The patient's middle name. |
| 11 | `PATIENT_IDENTIFIER` | VARCHAR(255) |  |  | The value that comes from the foreign system and is their identification for the patient. |
| 12 | `PATIENT_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | The foreign system's method of identifying a patient. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 14 | `PREFIX_NAME` | VARCHAR(255) |  |  | The prefix of the patient's name. |
| 15 | `STATE_NAME` | VARCHAR(255) |  |  | The patient's state address. |
| 16 | `STREET2_ADDR` | VARCHAR(255) |  |  | The second line of the patient's street address. |
| 17 | `STREET_ADDR` | VARCHAR(255) |  |  | The first line of the patient's street address. |
| 18 | `SUFFIX_NAME` | VARCHAR(255) |  |  | The suffix of the patient's name. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `ZIP_CODE` | VARCHAR(255) |  |  | The patient's zip code. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [IB_RX_REQ](IB_RX_REQ.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |
| [IB_RX_REQ_CONTACT](IB_RX_REQ_CONTACT.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |
| [TASK_ACTIVITY_MSG_H](TASK_ACTIVITY_MSG_H.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |

