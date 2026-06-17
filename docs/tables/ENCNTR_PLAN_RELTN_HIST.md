# ENCNTR_PLAN_RELTN_HIST

> Used for tracking history of certain columns on the encntr_plan_reltn table.

**Description:** Encounter Plan Relation History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 103

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | Indicates the provider's acceptance for payment terms. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ALT_MEMBER_NBR` | VARCHAR(100) |  |  | The alternate payer plan member number for the person. |
| 7 | `ASSIGN_BENEFITS_CD` | DOUBLE | NOT NULL |  | codified column representing the nature/status of benefit assignment for the use of the health plan on this encounter. |
| 8 | `AUTH_REQUIRED_CD` | DOUBLE | NOT NULL |  | Documents whether or not authorization is required for given encounter health plan relation. |
| 9 | `BALANCE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of balance |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the beg_effective_dt_tm column. |
| 12 | `BENEFIT_VERIFY_DT_TM` | DATETIME |  |  | The data and time at which the health plan benefits were last verified. |
| 13 | `CARD_CATEGORY_CD` | DOUBLE | NOT NULL |  | A categorization of the coverages and/or benefits available to the recipient. For some insurances this may be clearly identifiable based on characteristics of the beneficiary's coverage card. |
| 14 | `CARD_ISSUE_NBR` | DOUBLE | NOT NULL |  | The card issue number is used to track the number of cards dispensed. The original card is typically issue number 00, with subsequent cards incremented. |
| 15 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 16 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 17 | `COORD_BENEFITS_CD` | DOUBLE | NOT NULL |  | codified value representing the coordination of benefits for this health plan for this encounter. |
| 18 | `COVERAGE_COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | An identifier that points to a row in the LONG_TEXT table where comments about the plan coverage are stored. |
| 19 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 20 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 21 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 22 | `DEDUCT_AMT` | DOUBLE |  |  | The amount of health plan deductible applied to this encounter. |
| 23 | `DEDUCT_MET_AMT` | DOUBLE |  |  | The amount of the deductible that has been met, or payed, by the subscriber. |
| 24 | `DEDUCT_MET_DT_TM` | DATETIME |  |  | The date and time that the deductible amount was payed. |
| 25 | `DENIAL_REASON_CD` | DOUBLE | NOT NULL |  | The code value for the reason the claim was denied. |
| 26 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | this is the value of the unique primary identifier of the encounter table. it is an internal system assigned number. |
| 27 | `ENCNTR_PLAN_RELTN_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCNTR_PLAN_RELTN_HIST table. |
| 28 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the parent table encntr_plan_reltn |
| 29 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 30 | `END_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the end_effective_dt_tm column. |
| 31 | `EXT_PAYER_IDENT` | VARCHAR(100) |  |  | The primary identifier of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 32 | `EXT_PAYER_NAME` | VARCHAR(100) |  |  | The name of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 33 | `GENERIC_HEALTH_PLAN_NAME` | VARCHAR(100) |  |  | The name of the health plan when the health plan category is GENERIC. |
| 34 | `GROUP_NAME` | VARCHAR(200) |  |  | The group name of the plan. |
| 35 | `GROUP_NBR` | VARCHAR(100) |  |  | The group number of the plan. |
| 36 | `HEALTH_CARD_EXPIRY_DT_TM` | DATETIME |  |  | the date and time for which this health card becomes ineffective or expired. |
| 37 | `HEALTH_CARD_ISSUE_DT_TM` | DATETIME |  |  | the date and time for which this health card becomes effective or issued. |
| 38 | `HEALTH_CARD_NBR` | CHAR(100) |  |  | the number on the subscriber's/patient's health card (generally used in non-us sites). |
| 39 | `HEALTH_CARD_PROVINCE` | CHAR(3) |  |  | province where the health card was issued (usually used in non-us sites such as Canada). |
| 40 | `HEALTH_CARD_TYPE` | VARCHAR(32) |  |  | type of health card which has a certain category or style. |
| 41 | `HEALTH_CARD_VER_CODE` | CHAR(3) |  |  | version code of the health card (usually used in non-u.s. sites such as Canada). |
| 42 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 43 | `INSURED_CARD_NAME` | VARCHAR(100) |  |  | Person's Name as seen on the insurance card. |
| 44 | `INSURED_CARD_NAME_FIRST` | VARCHAR(100) |  |  | Person's first name as seen on the insurance card. |
| 45 | `INSURED_CARD_NAME_LAST` | VARCHAR(100) |  |  | Person's last name as seen on the insurance card. |
| 46 | `INSURED_CARD_NAME_MIDDLE` | VARCHAR(100) |  |  | Person's middle name as seen on the insurance card. |
| 47 | `INSURED_CARD_NAME_SUFFIX` | VARCHAR(100) |  |  | Person's name suffix as seen on the insurance card. |
| 48 | `INSUR_SOURCE_INFO_CD` | DOUBLE | NOT NULL |  | codified value representing the source from which the insurance information for this health plan and encounter was obtained. |
| 49 | `INS_CARD_COPIED_CD` | DOUBLE | NOT NULL |  | a y/n field indicating whether a copy of the subscriber's insurance card has been obtained. |
| 50 | `INS_OFFICE_ORG_ID` | DOUBLE | NOT NULL |  | Identifier from the organization table of the health plan's insurance office. |
| 51 | `LIFE_RSV_DAILY_DED_AMT` | DOUBLE | NOT NULL |  | The daily deductible amount that is applicable when reserve days are used for coverage. |
| 52 | `LIFE_RSV_DAILY_DED_QUAL_CD` | DOUBLE | NOT NULL |  | The qualifier describing the amount entered in the Lifetime reserve daily deductible. |
| 53 | `LIFE_RSV_DAYS` | DOUBLE | NOT NULL |  | The predetermined number of coverage days held ""in reserve"" for use if needed. The reserve days can be used when all the days under a given service have been used, but continued coverage/care is needed. This number is static for the lifetime of the subscriber. |
| 54 | `LIFE_RSV_REMAIN_DAYS` | DOUBLE | NOT NULL |  | A static, manual-entry field obtained from taking the Lifetime reserve days and subtracting any days used from that reserve for coverage. |
| 55 | `MEMBER_NBR` | VARCHAR(100) |  |  | The plan member number for the person. |
| 56 | `MEMBER_PERSON_CODE` | VARCHAR(100) |  |  | An additional attribute that the payer can use to uniquely identify the subscriber and their dependents within the context of a particular policy. The policy number in conjunction with the member person code typically comprise the member number. |
| 57 | `MILITARY_BASE_LOCATION` | VARCHAR(100) |  |  | textual location of the military base on which the subscriber/patient resides. |
| 58 | `MILITARY_RANK_CD` | DOUBLE | NOT NULL |  | military ranking of the subscriber/patient. |
| 59 | `MILITARY_SERVICE_CD` | DOUBLE | NOT NULL |  | The branch of military service through which the health plan coverage is being offered to the subscriber due to their current or past service. Examples may include, Army, Navy, Air Force, etc. |
| 60 | `MILITARY_STATUS_CD` | DOUBLE | NOT NULL |  | military status of the subscriber/patient. |
| 61 | `NOTIFY_DT_TM` | DATETIME |  |  | Date and time the inpatient 278 Notification took place. |
| 62 | `NOTIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel that ran the inpatient 278 Notification. |
| 63 | `NOTIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | Source the inpatient 278 Notification came from. e.g. Phone, Electronic, etc. |
| 64 | `ON_FILE_ADMIN_SEX_CD` | DOUBLE | NOT NULL |  | The person's gender code as it appears on file with the carrier. |
| 65 | `ON_FILE_BIRTH_DT_ISO` | VARCHAR(10) |  |  | The patient's date of birth as it appears on the file with the carrier. Stored in standard ISO format. |
| 66 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | The ID of the organization providing the insurance plan. |
| 67 | `ORIG_PRIORITY_SEQ` | DOUBLE |  |  | this is a numeric number used to represent the order in which to considered this health plan for reimbursement, if the person is a member of more than one health plan. this is the original number from the person health plan relation table. |
| 68 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 69 | `PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person organization relationship table. It is an internal system assigned number. |
| 70 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the parent table Person_plan_reltn |
| 71 | `PLAN_CLASS_CD` | DOUBLE | NOT NULL |  | Code value that indicates if the health plan is in the reference list of health plans or not. FREETEXT indicates it is not in the list, HEALTHPLAN indicates it is. |
| 72 | `PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that indicates the type of health plan. Examples are Medicaid, self pay, commercial, etc. |
| 73 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 74 | `POLICY_NBR` | VARCHAR(100) |  |  | The policy number of the subscriber's health plan at the time of the visit. The policy number in conjunction with the member person code typically comprise the member number. Sometimes the individual's member number is referred to as their policy number so care should be taken in order to make sure that the correct field is being used given a particular use case. |
| 75 | `PRICING_AGENCY_CD` | DOUBLE | NOT NULL |  | a pricing agency is an entity that applies a discount to a claim based on a contract that the entity has negotiated with both providers and claims payers on behalf of the network. |
| 76 | `PRIORITY_SEQ` | DOUBLE |  |  | this is a numeric number used to represent the order in which to consider this health plan for reimbursement, if the person is a member of more than one health plan. this number may change from the original number depending on the encounter. |
| 77 | `PROGRAM_STATUS_CD` | DOUBLE | NOT NULL |  | Represents the set of coverages and/or benefits available to the recipient based on the recipient's reason for eligibility. |
| 78 | `PROP_CASUALTY_CLAIM_NBR_TXT` | VARCHAR(100) |  |  | this is the claim number the health plan has to the p&c claim. this number is submitted to the health plan along with, or in a place of, the policy number. |
| 79 | `RESUBMIT_278N_CD` | DOUBLE | NOT NULL |  | This field stores the responses for resubmitting eligibility. |
| 80 | `RX_PLAN_COB_SEQ` | DOUBLE | NOT NULL |  | indicates the order in which a health plan is considered for pharmacy coordination of benefits for a particular encounter. |
| 81 | `SIGNATURE_DT_TM` | DATETIME |  |  | patient signature date/time for claim form. |
| 82 | `SIGNATURE_ON_FILE_CD` | DOUBLE | NOT NULL |  | indicates whether a patient's signature for insurance has been obtained |
| 83 | `SIGNATURE_SOURCE_CD` | DOUBLE | NOT NULL |  | description of what claim form the patient signed. |
| 84 | `SPONSOR_PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | pointer to the relationship between the subscriber and their employer/sponsor organization. |
| 85 | `SUBSCRIBER_TYPE_CD` | DOUBLE | NOT NULL |  | value that represents the type of subscriber being used for this health plan. not used at this time. |
| 86 | `SUBS_INSURED_CARD_FIRST_NAME` | VARCHAR(100) |  |  | The Subscriber's first name as seen on the insurance card or as it appears on file with the carrier. |
| 87 | `SUBS_INSURED_CARD_LAST_NAME` | VARCHAR(100) |  |  | The Subscriber's last name as seen on the insurance card or as it appears on file with the carrier. |
| 88 | `SUBS_INSURED_CARD_MIDDLE_NAME` | VARCHAR(100) |  |  | The Subscriber's middle name as seen on the insurance card or as it appears on file with the carrier. |
| 89 | `SUBS_INSURED_CARD_SUFFIX_NAME` | VARCHAR(100) |  |  | The Subscriber's suffix name as seen on the insurance card or as it appears on file with the carrier. |
| 90 | `SUBS_MEMBER_NBR` | VARCHAR(100) |  |  | the member number of the subscriber to the health plan. |
| 91 | `SUBS_ON_FILE_ADMIN_SEX_CD` | DOUBLE | NOT NULL |  | The subscriber's gender code as it appears on file with the carrier. |
| 92 | `SUBS_ON_FILE_BIRTH_DT_ISO` | VARCHAR(10) |  |  | The subscriber's date of birth as it appears on file with the carrier. Stored in ISO format. |
| 93 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 94 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 95 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 96 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 97 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 98 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 99 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 100 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the verification took place. |
| 101 | `VERIFY_PRSNL_ID` | DOUBLE | NOT NULL |  | id of the prsnl who last updated the row. |
| 102 | `VERIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | The source by which the row was verified. |
| 103 | `VERIFY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the verification. Examples are Yes and No. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PLAN_RELTN_ID` | [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |
| `NOTIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

