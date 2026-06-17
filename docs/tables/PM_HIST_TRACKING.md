# PM_HIST_TRACKING

> Master audit tracking table that contains the creation information about a history audit.

**Description:** PM History Tracking  
**Table type:** ACTIVITY  
**Primary key:** `PM_HIST_TRACKING_ID`  
**Columns:** 25  
**Referenced by:** 73 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORIZATION_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the AUTHORIZATION table. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `CONVERSATION_UUID` | VARCHAR(100) |  |  | Will uniquely identify the registration conversation universally. |
| 4 | `CONV_TASK_NUMBER` | DOUBLE | NOT NULL |  | This is the conversation task used to create a history transaction. 0 when written from other than a conversation. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created. |
| 6 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person responsible for creating a history transaction. |
| 7 | `CREATE_TASK` | DOUBLE |  |  | This is the task responsible for creating a history transaction. |
| 8 | `DEVICE_LOCATION_TXT` | VARCHAR(255) |  |  | The location of the device (as configured through WTSLocation) where the user initiated the registration transaction. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 10 | `FACILITY_ORG_ID` | DOUBLE | NOT NULL | FK→ | Contains the foreign key to the organization table identifying the associated facility for this history tracking row |
| 11 | `HL7_EVENT` | VARCHAR(10) |  |  | Stores the according HL7 Event. |
| 12 | `OMIT_REBILL_IND` | DOUBLE | NOT NULL |  | Indicates that insurance payers should not be rebilled (claims resubmitted) based on changes made during the registration transaction. |
| 13 | `PCID_TXT` | VARCHAR(255) |  |  | The PC identifier (as configured through WTSLocation) where the user initiated registration transactions. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | PK | Unique Identifier. |
| 16 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and time the transaction, which triggered the history row, occurred. This field can be system assigned or manually manipulated by users. |
| 17 | `TRANSACTION_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason for the transaction. |
| 18 | `TRANSACTION_REASON_TXT` | VARCHAR(100) |  |  | Text that describes the reason for the transaction. |
| 19 | `TRANSACTION_TYPE_TXT` | VARCHAR(4) |  |  | Type of transaction that occurred. Example: UPDT, ATDS, etc. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `WORK_ITEM_PROC_IND` | DOUBLE | NOT NULL |  | Indicates whether the work item publication process has completed for the registration transaction. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZATION_ID` | [AUTHORIZATION](AUTHORIZATION.md) | `AUTHORIZATION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FACILITY_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (73)

| From table | Column |
|------------|--------|
| [ADDRESS_HIST](ADDRESS_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTHORIZATION_HIST](AUTHORIZATION_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTHORIZATION_ITEM_HIST](AUTHORIZATION_ITEM_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTH_CODE_VALUE_R_HIST](AUTH_CODE_VALUE_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTH_DETAIL_HIST](AUTH_DETAIL_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTH_ITEM_ORDER_R_HIST](AUTH_ITEM_ORDER_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTH_MANAGEMENT_HIST](AUTH_MANAGEMENT_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTH_REFERRAL_RELTN_HIST](AUTH_REFERRAL_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [AUTH_SCH_EVENT_RELTN_HIST](AUTH_SCH_EVENT_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_ACP_HIST](ENCNTR_ACP_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_ALIAS_HIST](ENCNTR_ALIAS_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_AMBULANCE_HIST](ENCNTR_AMBULANCE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_CATCHMENT_R_HIST](ENCNTR_CATCHMENT_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_CLASSIFICTN_HIST](ENCNTR_CLASSIFICTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_CNDTN_CODE_HIST](ENCNTR_CNDTN_CODE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_CODE_VALUE_R_HIST](ENCNTR_CODE_VALUE_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_FLEX_HIST](ENCNTR_FLEX_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_INFO_HIST](ENCNTR_INFO_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_INPTNT_REHAB_HIST](ENCNTR_INPTNT_REHAB_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_LEAVE_HISTORY](ENCNTR_LEAVE_HISTORY.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_LEGAL_AUTH_R_HIST](ENCNTR_LEGAL_AUTH_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_LOCATION_HIST](ENCNTR_LOCATION_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_MEDICARE_MGMT_HIST](ENCNTR_MEDICARE_MGMT_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_OCCURRENCE_CODE_HIST](ENCNTR_OCCURRENCE_CODE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PENDING_HIST](ENCNTR_PENDING_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PERSON_RELTN_HIST](ENCNTR_PERSON_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PLAN_AUTH_R_HIST](ENCNTR_PLAN_AUTH_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PLAN_COB_HIST](ENCNTR_PLAN_COB_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PLAN_COB_R_HIST](ENCNTR_PLAN_COB_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PLAN_DATE_PRD_HIST](ENCNTR_PLAN_DATE_PRD_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PLAN_ELIG_BNFT_HIST](ENCNTR_PLAN_ELIG_BNFT_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PLAN_ELIG_HIST](ENCNTR_PLAN_ELIG_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PLAN_RELTN_HIST](ENCNTR_PLAN_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_PRSNL_RELTN_HISTORY](ENCNTR_PRSNL_RELTN_HISTORY.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_SLICE_HIST](ENCNTR_SLICE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_SOCIAL_HEALTH_HIST](ENCNTR_SOCIAL_HEALTH_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_SPAN_CODE_HIST](ENCNTR_SPAN_CODE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [ENCNTR_VALUE_CODE_HIST](ENCNTR_VALUE_CODE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [GUAR_FINANCIAL_RESP_HIST](GUAR_FINANCIAL_RESP_HIST.md) | `PM_HIST_TRACKING_ID` |
| [GUAR_FIN_RESP_RELTN_HIST](GUAR_FIN_RESP_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PATIENT_EVENT_DETAIL_HIST](PATIENT_EVENT_DETAIL_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PATIENT_EVENT_HIST](PATIENT_EVENT_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_ALIAS_HIST](PERSON_ALIAS_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_CODE_VALUE_R_HIST](PERSON_CODE_VALUE_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_DATA_NOT_COLL_HIST](PERSON_DATA_NOT_COLL_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_DESIGNATION_HIST](PERSON_DESIGNATION_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_DISMISSAL_ACTN_HIST](PERSON_DISMISSAL_ACTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_DISMISSAL_HIST](PERSON_DISMISSAL_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_FIN_ASSET_HIST](PERSON_FIN_ASSET_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_FLEX_HIST](PERSON_FLEX_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_INFO_HIST](PERSON_INFO_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_MILITARY_HIST](PERSON_MILITARY_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_NAME_HIST](PERSON_NAME_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_ORG_RELTN_HIST](PERSON_ORG_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PATIENT_HIST](PERSON_PATIENT_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PAY_PROPENSITY_HIST](PERSON_PAY_PROPENSITY_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PERSON_RELTN_HIST](PERSON_PERSON_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PLAN_AUTH_R_HIST](PERSON_PLAN_AUTH_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PLAN_PROFILE_HIST](PERSON_PLAN_PROFILE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PLAN_PROFILE_R_HIST](PERSON_PLAN_PROFILE_R_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PLAN_RELTN_HIST](PERSON_PLAN_RELTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PORTAL_INVITE_HIST](PERSON_PORTAL_INVITE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PREF_COMM_HIST](PERSON_PREF_COMM_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_PREF_HIST](PERSON_PREF_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_SOCIAL_HEALTH_HIST](PERSON_SOCIAL_HEALTH_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_TRIBAL_AFLTN_HIST](PERSON_TRIBAL_AFLTN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PERSON_VETERAN_HIST](PERSON_VETERAN_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PHONE_HIST](PHONE_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `PM_HIST_TRACKING_ID` |
| [PM_USER_DEFINED_HIST](PM_USER_DEFINED_HIST.md) | `PM_HIST_TRACKING_ID` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `PM_HIST_TRACKING_ID` |
| [RVC_COMMENT_HIST](RVC_COMMENT_HIST.md) | `PM_HIST_TRACKING_ID` |

