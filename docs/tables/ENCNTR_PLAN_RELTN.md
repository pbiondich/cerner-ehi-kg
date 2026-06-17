# ENCNTR_PLAN_RELTN

> The encounter-health plan relation table contains pointers to health plans for a specific encounter. This table is similar to the person health plan relation table, except that the health plans relate to a specific encounter.

**Description:** Encounter Health Plan Relationship  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_PLAN_RELTN_ID`  
**Columns:** 98  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | Provider acceptance for payment terms. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ALT_MEMBER_NBR` | VARCHAR(100) |  |  | The alternate payer plan member number for the person. |
| 7 | `ASSIGN_BENEFITS_CD` | DOUBLE | NOT NULL |  | Codified column representing the nature/status of benefit assignment for the use of the health plan on this encounter. |
| 8 | `AUTH_REQUIRED_CD` | DOUBLE | NOT NULL |  | Documents whether or not authorization is required for given encounter health plan relation |
| 9 | `BALANCE_TYPE_CD` | DOUBLE | NOT NULL |  | Status/Type of the billing balance for this encounter and this health plan. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the beg_effective_dt_tm column. |
| 12 | `BENEFIT_VERIFY_DT_TM` | DATETIME |  |  | The data and time at which the health plan benefits were last verified. |
| 13 | `CARD_CATEGORY_CD` | DOUBLE | NOT NULL |  | A categorization of the coverages and/or benefits available to the recipient. For some insurances this may be clearly identifiable based on characteristics of the beneficiary's coverage card. |
| 14 | `CARD_ISSUE_NBR` | DOUBLE | NOT NULL |  | The card issue number is used to track the number of cards dispensed. The original card is typically issue number 00, with subsequent cards incremented. |
| 15 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 16 | `COORD_BENEFITS_CD` | DOUBLE | NOT NULL |  | Codified value representing the coordination of benefits for this health plan for this encounter. |
| 17 | `COVERAGE_COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | An identifier that points to a row in the LONG_TEXT table where comments about the plan coverage are stored. |
| 18 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 19 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 20 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 21 | `DEDUCT_AMT` | DOUBLE |  |  | Amount of health plan deductible applied to this encounter. |
| 22 | `DEDUCT_MET_AMT` | DOUBLE |  |  | Amount of the deductible that has been met, or payed, by the subscriber. |
| 23 | `DEDUCT_MET_DT_TM` | DATETIME |  |  | Date and time that the deductible amount was payed. |
| 24 | `DENIAL_REASON_CD` | DOUBLE | NOT NULL |  | The reason for the denial. |
| 25 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 26 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter health plan relationship table. It is an internal system assigned number. |
| 27 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 28 | `END_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the end_effective_dt_tm column. |
| 29 | `EXT_PAYER_IDENT` | VARCHAR(100) |  |  | The primary identifier of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 30 | `EXT_PAYER_NAME` | VARCHAR(100) |  |  | The name of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 31 | `GENERIC_HEALTH_PLAN_NAME` | VARCHAR(100) |  |  | The name of the health plan when the health plan category is GENERIC. |
| 32 | `GROUP_NAME` | VARCHAR(200) |  |  | Name of the health plan group used for this encounter (patient) and their association to the health plan through their sponsor (employer). |
| 33 | `GROUP_NBR` | VARCHAR(100) |  |  | Number of the health plan group used for this encounter (patient) and their association to the health plan through their sponsor (employer). |
| 34 | `HEALTH_CARD_EXPIRY_DT_TM` | DATETIME |  |  | The date and time for which this health card becomes ineffective or expired. |
| 35 | `HEALTH_CARD_ISSUE_DT_TM` | DATETIME |  |  | The date and time for which this health card becomes effective or issued. |
| 36 | `HEALTH_CARD_NBR` | CHAR(100) |  |  | The number on the subscriber's/patient's health card (generally used in non-US sites). |
| 37 | `HEALTH_CARD_PROVINCE` | CHAR(3) |  |  | Province where the Health Card was issued (usually used in non-US sites such as Canada). |
| 38 | `HEALTH_CARD_TYPE` | VARCHAR(32) |  |  | Type of health card which has a certain category or style. |
| 39 | `HEALTH_CARD_VER_CODE` | CHAR(3) |  |  | Version code of the Health Card (usually used in non-U.S. sites such as Canada). |
| 40 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 41 | `INSURED_CARD_NAME` | VARCHAR(100) |  |  | Subscriber's/Patient's name as printed on the insurance card. |
| 42 | `INSURED_CARD_NAME_FIRST` | VARCHAR(100) |  |  | Person's first name as seen on the insurance card. |
| 43 | `INSURED_CARD_NAME_LAST` | VARCHAR(100) |  |  | Person's last name as seen on the insurance card. |
| 44 | `INSURED_CARD_NAME_MIDDLE` | VARCHAR(100) |  |  | Person's middle name as seen on the insurance card. |
| 45 | `INSURED_CARD_NAME_SUFFIX` | VARCHAR(100) |  |  | Person's name suffix as seen on the insurance card. |
| 46 | `INSUR_SOURCE_INFO_CD` | DOUBLE | NOT NULL |  | Codified value representing the source from which the insurance information for this health plan and encounter was obtained. |
| 47 | `INS_CARD_COPIED_CD` | DOUBLE | NOT NULL |  | A y/n field indicating whether a copy of the subscriber's insurance card has been obtained. |
| 48 | `INS_OFFICE_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the organization table of the health plan's insurance office. |
| 49 | `LIFE_RSV_DAILY_DED_AMT` | DOUBLE | NOT NULL |  | The daily deductible amount that is applicable when reserve days are used for coverage. |
| 50 | `LIFE_RSV_DAILY_DED_QUAL_CD` | DOUBLE | NOT NULL |  | The qualifier describing the amount entered in the Lifetime reserve daily deductible. |
| 51 | `LIFE_RSV_DAYS` | DOUBLE | NOT NULL |  | The predetermined number of coverage days held "in reserve" for use if needed. The reserve days can be used when all the days under a given service have been used, but continued coverage/care is needed. This number is static for the lifetime of the subscriber. |
| 52 | `LIFE_RSV_REMAIN_DAYS` | DOUBLE | NOT NULL |  | A static, manual-entry field obtained from taking the Lifetime reserve days and subtracting any days used from that reserve for coverage. |
| 53 | `MEMBER_NBR` | VARCHAR(100) |  |  | Patient's member number for this health plan. |
| 54 | `MEMBER_PERSON_CODE` | VARCHAR(100) |  |  | An additional attribute that the payer can use to uniquely identify the subscriber and their dependents within the context of a particular policy. The policy number in conjunction with the member person code typically comprise the member number. |
| 55 | `MILITARY_BASE_LOCATION` | VARCHAR(100) |  |  | Textual location of the military base on which the subscriber/patient resides. |
| 56 | `MILITARY_RANK_CD` | DOUBLE | NOT NULL |  | Military ranking of the subscriber/patient. |
| 57 | `MILITARY_SERVICE_CD` | DOUBLE | NOT NULL |  | The branch of military service through which the health plan coverage is being offered to the subscriber due to their current or past service. Examples may include, Army, Navy, Air Force, etc. |
| 58 | `MILITARY_STATUS_CD` | DOUBLE | NOT NULL |  | Military status of the subscriber/patient. |
| 59 | `NOTIFY_DT_TM` | DATETIME |  |  | Date and time the inpatient 278 Notification took place. |
| 60 | `NOTIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel that ran the inpatient 278 Notification. |
| 61 | `NOTIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | Source the inpatient 278 Notification came from. e.g. Phone, Electronic, etc. |
| 62 | `ON_FILE_ADMIN_SEX_CD` | DOUBLE | NOT NULL |  | The person's gender code as it appears on file with the carrier. |
| 63 | `ON_FILE_BIRTH_DT_ISO` | VARCHAR(10) |  |  | The patient's date of birth as it appears on the file with the carrier. Stored in standard ISO format. |
| 64 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the organization table of the health plan's carrier. |
| 65 | `ORIG_PRIORITY_SEQ` | DOUBLE |  |  | This is a numeric number used to represent the order in which to considered this health plan for reimbursement, if the person is a member of more than one health plan. This is the original number from the person health plan relation table. |
| 66 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 67 | `PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This this the ID from the PERSON_ORG_RELTN table for the person and the organization that are related to this ENCNTR_PLAN_RELTN row. |
| 68 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the ID from the PERSON_PLAN_RELTN row relating the PERSON and the HEALTH_PLAN to this ENCNTR_PLAN_RELTN row. For an encounter, a corresponding row can be maintained at the person level with the same information. |
| 69 | `PLAN_CLASS_CD` | DOUBLE | NOT NULL |  | The classification/grouping of the health plan. Generally indicates whether or not the plan is free text. |
| 70 | `PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Value that signifies the type/grouping of the health plan. Examples may include Medicare, Commercial, Champus, HMO, others. |
| 71 | `POLICY_NBR` | VARCHAR(100) |  |  | The policy number of the subscriber's health plan at the time of the visit. The policy number in conjunction with the member person code typically comprise the member number. Sometimes the individual's member number is referred to as their policy number so care should be taken in order to make sure that the correct field is being used given a particular use case. |
| 72 | `PRICING_AGENCY_CD` | DOUBLE | NOT NULL |  | A Pricing Agency is an entity that applies a discount to a claim based on a contract that the entity has negotiated with both providers and claims payers on behalf of the network. |
| 73 | `PRIORITY_SEQ` | DOUBLE |  |  | This is a numeric number used to represent the order in which to consider this health plan for reimbursement, if the person is a member of more than one health plan. This number may change from the original number depending on the encounter. |
| 74 | `PROGRAM_STATUS_CD` | DOUBLE | NOT NULL |  | Represents the set of coverages and/or benefits available to the recipient based on the recipient's reason for eligibility. |
| 75 | `PROP_CASUALTY_CLAIM_NBR_TXT` | VARCHAR(100) |  |  | This is the claim number the health plan has to the P&C claim. This number is submitted to the health plan along with, or in a place of, the policy number. |
| 76 | `RESUBMIT_278N_CD` | DOUBLE | NOT NULL |  | This field stores the responses for resubmitting eligibility. |
| 77 | `RX_PLAN_COB_SEQ` | DOUBLE | NOT NULL |  | Indicates the order in which a health plan is considered for pharmacy coordination of benefits for a particular encounter. |
| 78 | `SIGNATURE_DT_TM` | DATETIME |  |  | Patient signature date/time for claim form. |
| 79 | `SIGNATURE_ON_FILE_CD` | DOUBLE | NOT NULL |  | Indicates whether a patient's signature for insurance has been obtained |
| 80 | `SIGNATURE_SOURCE_CD` | DOUBLE | NOT NULL |  | Description of what claim form the patient signed. |
| 81 | `SPONSOR_PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Pointer to the relationship between the subscriber and their employer/sponsor organization. |
| 82 | `SUBSCRIBER_TYPE_CD` | DOUBLE | NOT NULL |  | Value that represents the type of subscriber being used for this health plan. Not used at this time. |
| 83 | `SUBS_INSURED_CARD_FIRST_NAME` | VARCHAR(100) |  |  | The Subscriber's first name as seen on the insurance card or as it appears on file with the carrier. |
| 84 | `SUBS_INSURED_CARD_LAST_NAME` | VARCHAR(100) |  |  | The Subscriber's last name as seen on the insurance card or as it appears on file with the carrier. |
| 85 | `SUBS_INSURED_CARD_MIDDLE_NAME` | VARCHAR(100) |  |  | The Subscriber's middle name as seen on the insurance card or as it appears on file with the carrier. |
| 86 | `SUBS_INSURED_CARD_SUFFIX_NAME` | VARCHAR(100) |  |  | The Subscriber's suffix name as seen on the insurance card or as it appears on file with the carrier. |
| 87 | `SUBS_MEMBER_NBR` | VARCHAR(100) |  |  | The member number of the subscriber to the health plan. |
| 88 | `SUBS_ON_FILE_ADMIN_SEX_CD` | DOUBLE | NOT NULL |  | The subscriber's gender code as it appears on file with the carrier. |
| 89 | `SUBS_ON_FILE_BIRTH_DT_ISO` | VARCHAR(10) |  |  | The subscriber's date of birth as it appears on file with the carrier. Stored in ISO format. |
| 90 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 91 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 92 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 93 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 94 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 95 | `VERIFY_DT_TM` | DATETIME |  |  | Time that the row was last verified. |
| 96 | `VERIFY_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the prsnl who last updated the row. |
| 97 | `VERIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | The source by which the row was verified. |
| 98 | `VERIFY_STATUS_CD` | DOUBLE | NOT NULL |  | The last verified status entered. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COVERAGE_COMMENTS_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INS_OFFICE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `NOTIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_ORG_RELTN_ID` | [PERSON_ORG_RELTN](PERSON_ORG_RELTN.md) | `PERSON_ORG_RELTN_ID` |
| `PERSON_PLAN_RELTN_ID` | [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| `SPONSOR_PERSON_ORG_RELTN_ID` | [PERSON_ORG_RELTN](PERSON_ORG_RELTN.md) | `PERSON_ORG_RELTN_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [ENCNTR_BENEFIT_R](ENCNTR_BENEFIT_R.md) | `ENCNTR_PLAN_RELTN_ID` |
| [ENCNTR_PLAN_AUTH_R](ENCNTR_PLAN_AUTH_R.md) | `ENCNTR_PLAN_RELTN_ID` |
| [ENCNTR_PLAN_AUTH_R_HIST](ENCNTR_PLAN_AUTH_R_HIST.md) | `ENCNTR_PLAN_RELTN_ID` |
| [ENCNTR_PLAN_COB_RELTN](ENCNTR_PLAN_COB_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |
| [ENCNTR_PLAN_ELIGIBILITY](ENCNTR_PLAN_ELIGIBILITY.md) | `ENCNTR_PLAN_RELTN_ID` |
| [ENCNTR_PLAN_ELIG_HIST](ENCNTR_PLAN_ELIG_HIST.md) | `ENCNTR_PLAN_RELTN_ID` |
| [ENCNTR_PLAN_RELTN_HIST](ENCNTR_PLAN_RELTN_HIST.md) | `ENCNTR_PLAN_RELTN_ID` |
| [TRANSACTION_ADMIT_NOTIFY](TRANSACTION_ADMIT_NOTIFY.md) | `ENCNTR_PLAN_RELTN_ID` |
| [TRANSACTION_ELIGIBILITY](TRANSACTION_ELIGIBILITY.md) | `ENCNTR_PLAN_RELTN_ID` |

