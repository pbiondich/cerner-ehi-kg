# AUTHORIZATION

> Stores information that indicates special authorizations for particular visits or procedures under a health plan's coverage

**Description:** Stores authorization/referral information  
**Table type:** ACTIVITY  
**Primary key:** `AUTHORIZATION_ID`  
**Columns:** 67  
**Referenced by:** 16 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMISSION_BEG_DT_TM` | DATETIME |  |  | The beginning of the admission period. |
| 6 | `ADMISSION_END_DT_TM` | DATETIME |  |  | The end of the admission period. |
| 7 | `APPEAL_REASON` | VARCHAR(100) |  |  | The reason an authorization/referral was appealed. |
| 8 | `AUTHORIZATION_ID` | DOUBLE | NOT NULL | PK | This is the primary key. |
| 9 | `AUTH_CNT` | DOUBLE | NOT NULL |  | The number of visits, days, or treatments that are authorized by the carrier for payment. |
| 10 | `AUTH_CNT_TIME` | DOUBLE | NOT NULL |  | The time the count was authorized. |
| 11 | `AUTH_CNT_TIME_CD` | DOUBLE | NOT NULL |  | This code defines the authorized, numbered period of time in AUTH_CNT_TIME (HSD05) |
| 12 | `AUTH_CNT_UNIT` | DOUBLE | NOT NULL |  | The units that the authorization count is stored as. |
| 13 | `AUTH_CNT_UNIT_CD` | DOUBLE | NOT NULL |  | This code defines the authorized unit value in AUTH_CNT_UNIT (HSD03). |
| 14 | `AUTH_EXPIRE_DT_TM` | DATETIME |  |  | System computed value based on AUTH_CNT and ADMIT_DT_TM. |
| 15 | `AUTH_ID` | DOUBLE | NOT NULL |  | Due to packet passivity constraints, this field is marked for rev8 removal. Old primary key. Obsolete column. |
| 16 | `AUTH_NBR` | VARCHAR(50) |  |  | Auth number, contract code, or cert number (depends on auth codeset). |
| 17 | `AUTH_OBTAINED_DT_TM` | DATETIME |  |  | The Date on which the insurance company was obtained for approval of services being rendered to a patient. |
| 18 | `AUTH_QUAL_CD` | DOUBLE | NOT NULL |  | A qualifier to define both the Number Authorized and the Number Authorized Remaining fields. |
| 19 | `AUTH_REMAIN_CNT` | DOUBLE | NOT NULL |  | The remaining number of visits, days or treatments that are authorized by the carrier for payment. |
| 20 | `AUTH_REQUIRED_CD` | DOUBLE | NOT NULL |  | A Y/N field that indicates whether or not the insurance company must be contacted for approval prior to services being rendered. |
| 21 | `AUTH_SCHEDULED_CNT` | DOUBLE |  |  | The number of visits authorized by the carrier for payment that have been scheduled. |
| 22 | `AUTH_TRANS_STATE_FLAG` | DOUBLE | NOT NULL |  | The AUTH_TRANS_STATE_FLAG provides information on the current state of a registration conversation's authorization transaction. The valid values for EDI_FLAG are:0 - N/A, 1 - In Process, 2 - Current, 3 - Previous, 4 - Error, 5 - Resubmit |
| 23 | `AUTH_TYPE_CD` | DOUBLE | NOT NULL |  | Type of authorization. Authorization, Pre-cert for inpatient stay, or contract code. |
| 24 | `AUTH_USED_CNT` | DOUBLE |  |  | The number of visits, days, treatments, or the amount authorized by the carrier for payment that has been used. |
| 25 | `AUTH_USED_MANUAL_ADJ_CNT` | DOUBLE |  |  | The manual adjustment for the used number of visits, days, treatments, or the amount authorized by the carrier for payment that were captured as part of a different encounter or by an external system. For example, if not all of the authorizations were used at the same facility, the manual adjustment will contain the number used at a different facility. |
| 26 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 27 | `BNFT_TYPE_CD` | DOUBLE | NOT NULL |  | Some authorizations will have a meaningful relation to a benefit type. |
| 28 | `CERT_COMPANY` | VARCHAR(100) |  |  | Due to packet passivity constraints, this field is marked for rev8 removal. Old, obsolete column. |
| 29 | `CERT_NBR` | VARCHAR(50) |  |  | Due to packet passivity constraints, this field is marked for rev8 removal. Old obsolete column. |
| 30 | `CERT_PRSNL_ID` | DOUBLE | NOT NULL |  | *NOT USED*. Obsolete. |
| 31 | `CERT_STATUS_CD` | DOUBLE | NOT NULL |  | Reflects status of an authorization or precertification. |
| 32 | `CERT_TYPE_CD` | DOUBLE | NOT NULL |  | Certification Type Code (UM02). Identifies the type of certification. |
| 33 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Comment Identifier which is stored on the LONG_TEXT table. |
| 34 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 35 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 36 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 37 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 38 | `DELAY_REASON_CD` | DOUBLE | NOT NULL |  | Delay Reason Code (UMO10). Identifies the reason for the delay. |
| 39 | `DELAY_REASON_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The comment identifier for free text stored on the long_text table which represents comments for the delay reason. |
| 40 | `DESCRIPTION` | VARCHAR(200) |  |  | Describes the authorization or referral. |
| 41 | `DISCHARGE_DT_TM` | DATETIME |  |  | Authorization discharge date & time (DTP01 = 096). |
| 42 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 43 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 44 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility code for service (NM101 = FA) |
| 45 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Contains the related Health Plan for this authorization row. |
| 46 | `INTERCHANGE_ID` | DOUBLE | NOT NULL | FK→ | Unique service authorization transaction identifier. |
| 47 | `LAST_UPDATE_DT_TM` | DATETIME |  |  | Date/time of last update to record |
| 48 | `MODEL_UPDT_CNT` | DOUBLE |  |  | The update count used to recognize update conflicts on the authorization model. Set to 0 on insert. Incremented by 1 on any update to a table in the authorization model. |
| 49 | `MODEL_UPDT_DT_TM` | DATETIME |  |  | The date and time a row within the authorization model was last inserted or updated. |
| 50 | `PAYER_AUTH_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the payer authorization. |
| 51 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 52 | `PROVIDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The provider's personnel id (NM101 = SJ). |
| 53 | `REFERENCE_NBR_TXT` | VARCHAR(100) |  |  | The reference number for the authorization. Stored in a text format. |
| 54 | `REJECT_REASON_CD` | DOUBLE | NOT NULL |  | Rejection Reason Code (HCR03). Identifies the reason for the rejection. |
| 55 | `SERVICE_BEG_DT_TM` | DATETIME |  |  | Authorization beginning service date & time (DTP01 = 472). |
| 56 | `SERVICE_END_DT_TM` | DATETIME |  |  | Authorization ending service date & time (DTP01 = 472). |
| 57 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Marked to delete as of Rev8. Old and obsolete. |
| 58 | `SURGICAL_DT_TM` | DATETIME |  |  | Authorization surgical date & time (DTP01 = 456). |
| 59 | `TAXONOMY_ID` | DOUBLE | NOT NULL | FK→ | The taxonomy code used in the authorization transaction |
| 60 | `TOTAL_SERVICE_NBR` | DOUBLE |  |  | Marked for delete in Rev8. Old and obsolete. |
| 61 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `X12PROVIDER_CD` | DOUBLE | NOT NULL |  | Identifies the Provider's Role (PRV01). |
| 67 | `X12SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the Service Type Code (UM03). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DELAY_REASON_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INTERCHANGE_ID` | [EEM_TRANSACTION](EEM_TRANSACTION.md) | `TRANSACTION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROVIDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TAXONOMY_ID` | [PROVIDER_TAXONOMY](PROVIDER_TAXONOMY.md) | `TAXONOMY_ID` |

## Referenced by (16)

| From table | Column |
|------------|--------|
| [AUTHORIZATION_CODE_VALUE_R](AUTHORIZATION_CODE_VALUE_R.md) | `AUTHORIZATION_ID` |
| [AUTHORIZATION_HIST](AUTHORIZATION_HIST.md) | `AUTHORIZATION_ID` |
| [AUTHORIZATION_ITEM](AUTHORIZATION_ITEM.md) | `AUTHORIZATION_ID` |
| [AUTHORIZATION_MANAGEMENT](AUTHORIZATION_MANAGEMENT.md) | `AUTHORIZATION_ID` |
| [AUTH_DETAIL](AUTH_DETAIL.md) | `AUTHORIZATION_ID` |
| [AUTH_REFERRAL_RELTN](AUTH_REFERRAL_RELTN.md) | `AUTHORIZATION_ID` |
| [AUTH_REFERRAL_RELTN_HIST](AUTH_REFERRAL_RELTN_HIST.md) | `AUTHORIZATION_ID` |
| [AUTH_SCH_EVENT_RELTN](AUTH_SCH_EVENT_RELTN.md) | `AUTHORIZATION_ID` |
| [AUTH_SCH_EVENT_RELTN_HIST](AUTH_SCH_EVENT_RELTN_HIST.md) | `AUTHORIZATION_ID` |
| [ENCNTR_PLAN_AUTH_R](ENCNTR_PLAN_AUTH_R.md) | `AUTHORIZATION_ID` |
| [ENCNTR_PLAN_AUTH_R_HIST](ENCNTR_PLAN_AUTH_R_HIST.md) | `AUTHORIZATION_ID` |
| [PERSON_PLAN_AUTH_R](PERSON_PLAN_AUTH_R.md) | `AUTHORIZATION_ID` |
| [PERSON_PLAN_AUTH_R_HIST](PERSON_PLAN_AUTH_R_HIST.md) | `AUTHORIZATION_ID` |
| [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `AUTHORIZATION_ID` |
| [REFERRAL_P_PLAN_AUTH_R](REFERRAL_P_PLAN_AUTH_R.md) | `AUTHORIZATION_ID` |
| [SCH_PEND_ENCNTR_AUTH_RELTN](SCH_PEND_ENCNTR_AUTH_RELTN.md) | `AUTHORIZATION_ID` |

