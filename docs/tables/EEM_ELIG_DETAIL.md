# EEM_ELIG_DETAIL

> Discrete Data for the Eligibility Transaction.

**Description:** EEM Eligibility Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 56

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of the data w/in the transaction (not of the transaction itself). 0 - Error, 1 - Eligible, 2 - Denied, 3 - Unknown. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The health plan used for this transaction. |
| 9 | `IB_EMPLOYEE_ID_NUM` | VARCHAR(30) |  |  | The employee identification Number as indicated by the inbound transaction. |
| 10 | `IB_IDEN_CARD_NUM` | VARCHAR(50) |  |  | The identification card number as indicated by the inbound transaction. |
| 11 | `IB_INS_POL_NUM` | VARCHAR(50) |  |  | The insurance policy number as indicated by the inbound transaction. |
| 12 | `IB_ISSUE_NUM` | VARCHAR(50) |  |  | The issue number as indicated by the inbound transaction. |
| 13 | `IB_MEDICAID_RECPNT_ID_NUM` | VARCHAR(50) |  |  | The Medicaid recipient identification number as indicated by the inbound transaction. |
| 14 | `IB_MED_REC_ID_NUM` | VARCHAR(50) |  |  | The medical record identification number as indicated by the inbound transaction. |
| 15 | `IB_PAT_BIRTH_DT_TM` | VARCHAR(35) |  |  | The patient birth date as indicated by the inbound transaction. |
| 16 | `IB_PAT_FIRST_NAME` | VARCHAR(35) |  |  | The patient's first name as indicated by the inbound transaction. |
| 17 | `IB_PAT_LAST_NAME` | VARCHAR(60) |  |  | The patient's last name as indicated by the inbound transaction. |
| 18 | `IB_PAT_SSN` | VARCHAR(30) |  |  | The patient's social security number as indicated by the inbound transaction. |
| 19 | `IB_PLAN_NETWK_ID_NUM` | VARCHAR(50) |  |  | The plan network identification number as indicated by the inbound transaction. |
| 20 | `IB_PRIOR_ID_NUM` | VARCHAR(50) |  |  | The prior identification number as indicated by the inbound transaction. |
| 21 | `IB_SUB_BIRTH_DT_TM` | VARCHAR(35) |  |  | The subscriber's birth date as indicated by the inbound transaction. |
| 22 | `IB_SUB_FIRST_NAME` | VARCHAR(35) |  |  | The subscriber's first name as indicated by the inbound transaction. |
| 23 | `IB_SUB_GROUP_NUM` | VARCHAR(50) |  |  | The subscriber's group number as indicated by the inbound transaction. |
| 24 | `IB_SUB_GROUP_OR_POLICY_NUM` | VARCHAR(50) |  |  | The subscriber's group or policy number as indicated by the inbound transaction. |
| 25 | `IB_SUB_LAST_NAME` | VARCHAR(60) |  |  | The subscriber's last name as indicated by the inbound transaction. |
| 26 | `IB_SUB_MEMBER_ID` | VARCHAR(80) |  |  | The subscriber's member identification number as indicated by the inbound transaction. |
| 27 | `IB_SUB_POLICY_NUM` | VARCHAR(50) |  |  | The subscriber's policy number as indicated by the inbound transaction. |
| 28 | `IB_SUB_SSN` | VARCHAR(30) |  |  | The subscriber's social security number as indicated by the inbound transaction. |
| 29 | `INFO_SRC_PRIMARY_IDEN` | VARCHAR(80) |  |  | The value filled in the info_src_primary_iden field on the outbound transaction (aka: payer iden) |
| 30 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Interchange id of the transaction that this detail data came from. |
| 31 | `OB_BEG_SERVICE_DATE` | VARCHAR(12) | NOT NULL |  | This is the start time on the out bound 270 message for requesting a patient?s eligibility status. In conjunction with the service end date, it is used to check for eligibility through a range of days. If no end date is populated, then eligibility status is checked for the date stored in the begin date. |
| 32 | `OB_END_SERVICE_DATE` | VARCHAR(12) | NOT NULL |  | This is the end time on the out bound 270 message for requesting a patient?s eligibility status. In conjunction with the service begin date, it is used to check for eligibility through a range of days. If no end date is populated, then eligibility status is checked for the date stored in the begin date. |
| 33 | `OB_PAT_BIRTH_DT_TM` | VARCHAR(35) |  |  | The patient's birth date as indicated by the outbound transaction. |
| 34 | `OB_PAT_FIRST_NAME` | VARCHAR(35) |  |  | The patient's first name as indicated by the outbound transaction. |
| 35 | `OB_PAT_LAST_NAME` | VARCHAR(60) |  |  | The patient's last name as indicated by the outbound transaction. |
| 36 | `OB_PAT_SSN` | VARCHAR(30) |  |  | The patient's social security number as indicated by the outbound transaction. |
| 37 | `OB_SUB_BIRTH_DT_TM` | VARCHAR(35) |  |  | The subscriber's birth date as indicated by the outbound transaction. |
| 38 | `OB_SUB_FIRST_NAME` | VARCHAR(35) |  |  | The subscriber's first name as indicated by the outbound transaction. |
| 39 | `OB_SUB_GROUP_NUM` | VARCHAR(50) |  |  | The subscriber's group number as indicated by the outbound transaction. |
| 40 | `OB_SUB_GROUP_OR_POLICY_NUM` | VARCHAR(50) |  |  | The subscriber's group number as indicated by the outbound transaction. |
| 41 | `OB_SUB_LAST_NAME` | VARCHAR(60) |  |  | The subscriber's last name as indicated by the outbound transaction. |
| 42 | `OB_SUB_MEMBER_ID` | VARCHAR(80) |  |  | The subscriber's member id as indicated by the outbound transaction. |
| 43 | `OB_SUB_POLICY_NUM` | VARCHAR(50) |  |  | The subscriber's policy number as indicated by the outbound transaction. |
| 44 | `OB_SUB_SSN` | VARCHAR(30) |  |  | The subscriber's social security number as indicated by the outbound transaction. |
| 45 | `PAT_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Cerner person id of the patient |
| 46 | `PAYOR_ID` | DOUBLE | NOT NULL | FK→ | Cerner's payor ID |
| 47 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The profile ID used in the transaction |
| 48 | `REPLY_DT_TM` | DATETIME |  |  | The date and time that the transaction's reply came back. |
| 49 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person ID of the person that sent the transaction. |
| 50 | `SENT_DT_TM` | DATETIME | NOT NULL |  | The date and time that the transaction was sent. |
| 51 | `SUB_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person id of the Subscriber |
| 52 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 53 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 54 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 55 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 56 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PAT_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PAYOR_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SUB_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

