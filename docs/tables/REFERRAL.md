# REFERRAL

> Stores all the information related to a referral.

**Description:** Referral  
**Table type:** ACTIVITY  
**Primary key:** `REFERRAL_ID`  
**Columns:** 57  
**Referenced by:** 14 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMINISTRATIVE_PROBLEM_CD` | DOUBLE |  |  | The administrative problem code associated to the referral. |
| 6 | `ADMIT_BOOKING_TYPE_CD` | DOUBLE | NOT NULL |  | Represents how quickly an appointment was booked for the referral. |
| 7 | `AUTHORIZATION_CODE_TXT` | VARCHAR(50) |  |  | A free text alpha numeric code that gets the information for contracts with organisations that will pay for the treatment. |
| 8 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE |  |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | Contains the date and time the row was created in the referral table. |
| 10 | `CREATE_SYSTEM_CD` | DOUBLE | NOT NULL |  | An indication of the system that created the referral. |
| 11 | `EXTERNAL_SCHEDULED_DT_TM` | DATETIME |  |  | The date of the scheduled referral if using a non-millennium scheduling system. |
| 12 | `EXT_RECEIVED_DT_TM` | DATETIME |  |  | The date and time the referral was received by an external system. |
| 13 | `HEALTHCARE_GUARANTEE_DT_TM` | DATETIME |  |  | The guaranteed appointment date calculated for the person for the referral. |
| 14 | `INBOUND_ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel that is coordinating the inbound referral when manually assigned. |
| 15 | `INSTRUCTIONS_TO_STAFF_TEXT_ID` | DOUBLE | NOT NULL | FK→ | FK to the long_text table. A free text field is provided to communicate special instructions to staff. |
| 16 | `INTENDED_BOOKING_TYPE_CD` | DOUBLE | NOT NULL |  | Represents how quickly an appointment should be booked for the referral based on factors such as urgency and referral type. |
| 17 | `LAST_PERFORMED_ACTION_CD` | DOUBLE | NOT NULL |  | The last performed action on the referral. |
| 18 | `LAST_PERFORMED_ACTION_DT_TM` | DATETIME |  |  | The date and time the last action was performed on the referral. |
| 19 | `MEDICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | The specialized service within which the patient is treated. |
| 20 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order that created the outbound referral |
| 21 | `OUTBOUND_ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel that is coordinating the outbound referral when manually assigned. |
| 22 | `OUTBOUND_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the encounter that created the outbound referral |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person id of the patient associated to the referral. |
| 24 | `REFERRAL_CATEGORY_CD` | DOUBLE | NOT NULL |  | The venue description of a referral. |
| 25 | `REFERRAL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the Referral table. |
| 26 | `REFERRAL_ORIG_RECEIVED_DT_TM` | DATETIME |  |  | The date and time the referral was originally received by the referring trust. |
| 27 | `REFERRAL_PRIORITY_CD` | DOUBLE | NOT NULL |  | The urgency of a request for services. |
| 28 | `REFERRAL_REASON_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The reason the referral was created. Foreign Key to the long_text table. |
| 29 | `REFERRAL_RECEIVED_DT_TM` | DATETIME |  |  | The date and time the referral was received by an inbound provider. |
| 30 | `REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | The origin from where the referral request is received. |
| 31 | `REFERRAL_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the referral across the sending or receiving system. |
| 32 | `REFERRAL_SUBSTATUS_CD` | DOUBLE | NOT NULL |  | The substatus of the referral across the sending or receiving system. |
| 33 | `REFERRAL_WRITTEN_DT_TM` | DATETIME |  |  | The date and time when the referral was written by the referring source. |
| 34 | `REFER_FROM_LOC_CD` | DOUBLE | NOT NULL | FK→ | The nursing unit location of the encounter at the time of referral creation |
| 35 | `REFER_FROM_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the organization that is sending the referral. |
| 36 | `REFER_FROM_PRACTICE_SITE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the practice site sending the referral. |
| 37 | `REFER_FROM_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the provider requesting the referral. |
| 38 | `REFER_TO_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization ID where the referral is being received. |
| 39 | `REFER_TO_PRACTICE_SITE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the practice site receiving the referral. |
| 40 | `REFER_TO_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the provider who is receiving the referral. |
| 41 | `REQUESTED_START_DT_TM` | DATETIME |  |  | The date that any treatment for the referral is asked to be delayed to. |
| 42 | `RESPONSIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | The personnel ID of the inbound provider who is responsible for the care of the patient. |
| 43 | `SERVICE_BY_DT_TM` | DATETIME |  |  | The date the referral must be completed by. |
| 44 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The specialty within which the consultant is recognized or contracted to the organization. |
| 45 | `SERVICE_TYPE_REQUESTED_CD` | DOUBLE | NOT NULL |  | The type of referral request. |
| 46 | `STAND_BY_CD` | DOUBLE | NOT NULL |  | The state of waiting to secure a place on the basis of earliest availability. |
| 47 | `SUSPECTED_CANCER_TYPE_CD` | DOUBLE | NOT NULL |  | The type of suspected cancer for which an urgent referral is made. |
| 48 | `TREATMENT_COMPLETED_DT_TM` | DATETIME |  |  | The date and time at which the treatment for the referral is deemed completed. |
| 49 | `TREATMENT_TO_DATE_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A free text field is provided to the user to capture notes on any treatment already provided. A foreign key to the long_text table. |
| 50 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `WAITLIST_REMOVAL_DT_TM` | DATETIME |  |  | The date and time the referral was attended or removed. |
| 56 | `WAIT_STATUS_CD` | DOUBLE | NOT NULL |  | The status representing the patient while waiting to be scheduled. |
| 57 | `WAIT_TIME_DAYS` | DOUBLE |  |  | The wait time in days between accepting a referral and seeing the patient for a referral. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INBOUND_ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `INSTRUCTIONS_TO_STAFF_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `OUTBOUND_ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `OUTBOUND_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REFERRAL_REASON_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REFER_FROM_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `REFER_FROM_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `REFER_FROM_PRACTICE_SITE_ID` | [PRACTICE_SITE](PRACTICE_SITE.md) | `PRACTICE_SITE_ID` |
| `REFER_FROM_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REFER_TO_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `REFER_TO_PRACTICE_SITE_ID` | [PRACTICE_SITE](PRACTICE_SITE.md) | `PRACTICE_SITE_ID` |
| `REFER_TO_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TREATMENT_TO_DATE_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (14)

| From table | Column |
|------------|--------|
| [AUTH_REFERRAL_RELTN](AUTH_REFERRAL_RELTN.md) | `REFERRAL_ID` |
| [AUTH_REFERRAL_RELTN_HIST](AUTH_REFERRAL_RELTN_HIST.md) | `REFERRAL_ID` |
| [ESI_LOG](ESI_LOG.md) | `REFERRAL_ID` |
| [REFERRAL_ACTION](REFERRAL_ACTION.md) | `REFERRAL_ID` |
| [REFERRAL_ALIAS](REFERRAL_ALIAS.md) | `REFERRAL_ID` |
| [REFERRAL_CONTACT](REFERRAL_CONTACT.md) | `REFERRAL_ID` |
| [REFERRAL_CUSTOM](REFERRAL_CUSTOM.md) | `REFERRAL_ID` |
| [REFERRAL_CUSTOM_HIST](REFERRAL_CUSTOM_HIST.md) | `REFERRAL_ID` |
| [REFERRAL_DOCUMENT](REFERRAL_DOCUMENT.md) | `REFERRAL_ID` |
| [REFERRAL_ENTITY_RELTN](REFERRAL_ENTITY_RELTN.md) | `REFERRAL_ID` |
| [REFERRAL_HIST](REFERRAL_HIST.md) | `REFERRAL_ID` |
| [REFERRAL_MONIKER](REFERRAL_MONIKER.md) | `REFERRAL_ID` |
| [REFERRAL_P_PLAN_RELTN](REFERRAL_P_PLAN_RELTN.md) | `REFERRAL_ID` |
| [TASK_SUBACTIVITY](TASK_SUBACTIVITY.md) | `REFERRAL_ID` |

