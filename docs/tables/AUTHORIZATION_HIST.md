# AUTHORIZATION_HIST

> Contains historical records for the authorization table.

**Description:** Authorization History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 70

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
| 8 | `AUTHORIZATION_HIST_ID` | DOUBLE | NOT NULL |  | Contains history records from the Authorization table. |
| 9 | `AUTHORIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the record to which this history is related |
| 10 | `AUTH_CNT` | DOUBLE | NOT NULL |  | The number of visits, days, or treatments that are authorized by the carrier for payment. |
| 11 | `AUTH_CNT_TIME` | DOUBLE | NOT NULL |  | The time the count was authorized. |
| 12 | `AUTH_CNT_TIME_CD` | DOUBLE | NOT NULL |  | This code defines the authorized, numbered period of time in AUTH_CNT_TIME (HSD05) |
| 13 | `AUTH_CNT_UNIT` | DOUBLE | NOT NULL |  | The units that the authorization count is stored as. |
| 14 | `AUTH_CNT_UNIT_CD` | DOUBLE | NOT NULL |  | This code defines the authorized unit value in AUTH_CNT_UNIT (HSD03). |
| 15 | `AUTH_EXPIRE_DT_TM` | DATETIME |  |  | System computed value based on AUTH_CNT and ADMIT_DT_TM. |
| 16 | `AUTH_ID` | DOUBLE | NOT NULL |  | Due to packet passivity constraints, this field is marked for rev8 removal. Old primary key. Obsolete column. |
| 17 | `AUTH_NBR` | VARCHAR(50) |  |  | Auth number, contract code, or cert number (depends on auth codeset). |
| 18 | `AUTH_OBTAINED_DT_TM` | DATETIME |  |  | The Date on which the insurance company was obtained for approval of services being rendered to a patient. |
| 19 | `AUTH_QUAL_CD` | DOUBLE | NOT NULL |  | A qualifier to define both the Number Authorized and the Number Authorized Remaining fields. |
| 20 | `AUTH_REMAIN_CNT` | DOUBLE | NOT NULL |  | The remaining number of visits, days or treatments that are authorized by the carrier for payment. |
| 21 | `AUTH_REQUIRED_CD` | DOUBLE | NOT NULL |  | A Y/N field that indicates whether or not the insurance company must be contacted for approval prior to services being rendered. |
| 22 | `AUTH_SCHEDULED_CNT` | DOUBLE |  |  | The number of visits authorized by the carrier for payment that have been scheduled. |
| 23 | `AUTH_TRANS_STATE_FLAG` | DOUBLE | NOT NULL |  | The AUTH_TRANS_STATE_FLAG provides information on the current state of a registration conversation's authorization transaction. The valid values for EDI_FLAG are:0 - N/A, 1 - In Process, 2 - Current, 3 - Previous, 4 - Error, 5 - Resubmit |
| 24 | `AUTH_TYPE_CD` | DOUBLE | NOT NULL |  | Type of authorization. Authorization, Pre-cert for inpatient stay, or contract code. |
| 25 | `AUTH_USED_CNT` | DOUBLE |  |  | The number of visits, days, treatments, or the amount authorized by the carrier for payment that has been used. |
| 26 | `AUTH_USED_MANUAL_ADJ_CNT` | DOUBLE |  |  | The manual adjustment for the used number of visits, days, treatments, or the amount authorized by the carrier for payment that were captured as part of a different encounter or by an external system. For example, if not all of the authorizations were used at the same facility, the manual adjustment will contain the number used at a different facility. |
| 27 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 28 | `BNFT_TYPE_CD` | DOUBLE | NOT NULL |  | Some authorizations will have a meaningful relation to a benefit type. |
| 29 | `CERT_COMPANY` | VARCHAR(100) |  |  | Due to packet passivity constraints, this field is marked for rev8 removal. Old, obsolete column. |
| 30 | `CERT_NBR` | VARCHAR(50) |  |  | Due to packet passivity constraints, this field is marked for rev8 removal. Old obsolete column. |
| 31 | `CERT_PRSNL_ID` | DOUBLE | NOT NULL |  | *NOT USED*. Obsolete. |
| 32 | `CERT_STATUS_CD` | DOUBLE | NOT NULL |  | Reflects status of an authorization or precertification. |
| 33 | `CERT_TYPE_CD` | DOUBLE | NOT NULL |  | Certification Type Code (UM02). Identifies the type of certification. |
| 34 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 35 | `COMMENT_ID` | DOUBLE | NOT NULL |  | Comment Identifier which is stored on the LONG_TEXT table. |
| 36 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 37 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 38 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 39 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 40 | `DELAY_REASON_CD` | DOUBLE | NOT NULL |  | Delay Reason Code (UMO10). Identifies the reason for the delay. |
| 41 | `DELAY_REASON_COMMENT_ID` | DOUBLE | NOT NULL |  | The comment identifier for free text stored on the long_text table which represents comments for the delay reason. |
| 42 | `DESCRIPTION` | VARCHAR(200) |  |  | Describes the authorization or referral. |
| 43 | `DISCHARGE_DT_TM` | DATETIME |  |  | Authorization discharge date & time (DTP01 = 096). |
| 44 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 45 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 46 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility code for service (NM101 = FA) |
| 47 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL |  | Contains the related Health Plan for this authorization row. |
| 48 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Unique service authorization transaction identifier. |
| 49 | `LAST_UPDATE_DT_TM` | DATETIME |  |  | Date/time of last update to record |
| 50 | `PAYER_AUTH_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the payer authorization. |
| 51 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 52 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 53 | `PROVIDER_PRSNL_ID` | DOUBLE | NOT NULL |  | The provider's personnel id (NM101 = SJ). |
| 54 | `REFERENCE_NBR_TXT` | VARCHAR(100) |  |  | The reference number for the authorization. Stored in a text format. |
| 55 | `REJECT_REASON_CD` | DOUBLE | NOT NULL |  | Rejection Reason Code (HCR03). Identifies the reason for the rejection. |
| 56 | `SERVICE_BEG_DT_TM` | DATETIME |  |  | Authorization beginning service date & time (DTP01 = 472). |
| 57 | `SERVICE_END_DT_TM` | DATETIME |  |  | Authorization ending service date & time (DTP01 = 472). |
| 58 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Marked to delete as of Rev8. Old and obsolete. |
| 59 | `SURGICAL_DT_TM` | DATETIME |  |  | Authorization surgical date & time (DTP01 = 456). |
| 60 | `TAXONOMY_ID` | DOUBLE | NOT NULL |  | The taxonomy code used in the authorization transaction |
| 61 | `TOTAL_SERVICE_NBR` | DOUBLE |  |  | Marked for delete in Rev8. Old and obsolete. |
| 62 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 63 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 64 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 67 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `X12PROVIDER_CD` | DOUBLE | NOT NULL |  | Identifies the Provider's Role (PRV01). |
| 70 | `X12SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the Service Type Code (UM03). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZATION_ID` | [AUTHORIZATION](AUTHORIZATION.md) | `AUTHORIZATION_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

