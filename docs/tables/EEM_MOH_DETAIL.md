# EEM_MOH_DETAIL

> This table will be the summary table for the MOH transactions.

**Description:** MOH Detail Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BIRTH_DT_ISO` | VARCHAR(10) |  |  | The patient's birth date as returned by the moh. Stored in ISO-8601 extended date format. |
| 7 | `BIRTH_DT_TM` | DATETIME |  |  | Patient's birth date as returned from the MOH. ***Obsolete column *** |
| 8 | `BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column.***Obsolete column *** |
| 9 | `DATA_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of the data within the transaction (not of the transaction itself). 0 - pending/unknown, 1 - eligible, 2 - denied, 3 - returned/unknown or ambiguous, 4 - error, 5 - template, 6 - person is eligible but card is invalid. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `EXPIRY_DT_TM` | DATETIME |  |  | The expiry date of the patient's health card as returned from the MOH. |
| 12 | `FIRST_NAME` | VARCHAR(20) |  |  | Patient's first name as returned from the MOH. |
| 13 | `GENDER_CD` | DOUBLE | NOT NULL | FK→ | Patient's gender as returned from the MOH. |
| 14 | `HEALTH_CARD` | VARCHAR(10) |  |  | Patient's health card number as provided to the MOH. |
| 15 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Interchange id of the transaction that this detail data came from. |
| 16 | `LAST_NAME` | VARCHAR(30) |  |  | Patient's last name as returned from the MOH. |
| 17 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location from which the MOH Health Card Validation took place. |
| 18 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the organization that is the payer of the transaction also known as the carrier organization. |
| 19 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 20 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The profile id used in the transaction. |
| 21 | `REPLY_DT_TM` | DATETIME |  |  | Date and Time the response was received. |
| 22 | `RESPONSE_CD` | DOUBLE | NOT NULL | FK→ | The codified response to the Health Card Validation request from the MOH. |
| 23 | `SECOND_NAME` | VARCHAR(20) |  |  | Patient's second name as returned from the MOH. |
| 24 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel that initiated the Health Card Validation transaction. |
| 25 | `SENT_DT_TM` | DATETIME | NOT NULL |  | Date and Time the Transaction was sent. |
| 26 | `TRACK1` | VARCHAR(79) |  |  | Magnetic stripe track 1 information as provided to the MOH. |
| 27 | `TRACK2` | VARCHAR(40) |  |  | Magnetic stripe track 2 information as provided to the MOH. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `VERSION_CODE` | VARCHAR(2) |  |  | Patient's version code as provided to the MOH. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GENDER_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |
| `RESPONSE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

