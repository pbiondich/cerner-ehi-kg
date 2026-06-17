# PERSON_PLAN_RELTN

> The person-health plan relation table contains pointers to health plan(s) which represent the current health plans for a person. This table along with the person table can be preloaded with member and plan data or populated as this information is

**Description:** Person Health Plan Relationship  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PLAN_RELTN_ID`  
**Columns:** 69  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALT_MEMBER_NBR` | VARCHAR(100) |  |  | The alternate payer plan member number for the person. |
| 6 | `ARCHIVE_DT_TM` | DATETIME |  |  | The date and time at which the patient health plan relationship (coverage) was archived. Once the coverage is archived, it should not be allocated to future encounters. |
| 7 | `ARCHIVE_PRSNL_ID` | DOUBLE |  | FK→ | The id of the personnel who archived the patient health plan relationship (coverage) |
| 8 | `BALANCE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of balance. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the beg_effective_dt_tm column. |
| 11 | `CARD_CATEGORY_CD` | DOUBLE | NOT NULL |  | A categorization of the coverages and/or benefits available to the recipient. For some insurances this may be clearly identifiable based on characteristics of the beneficiary's coverage card. |
| 12 | `CARD_ISSUE_NBR` | DOUBLE | NOT NULL |  | The card issue number is used to track the number of cards dispensed. The original card is typically issue number 00, with subsequent cards incremented. |
| 13 | `CONTRACT_CODE` | VARCHAR(100) |  |  | Identifies a contract between a facility and a person's related health plan. |
| 14 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 15 | `COVERAGE_COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | An identifier that points to a row in the LONG_TEXT table where comments about the plan coverage are stored. |
| 16 | `COVERAGE_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the type of coverage of the plan. |
| 17 | `DEDUCT_AMT` | DOUBLE |  |  | The amount of the deductable for the plan. |
| 18 | `DEDUCT_MET_AMT` | DOUBLE |  |  | How much of the deductable has been met. |
| 19 | `DEDUCT_MET_DT_TM` | DATETIME |  |  | The date and time the deductable was met. |
| 20 | `DENIAL_REASON_CD` | DOUBLE | NOT NULL |  | The code value for the reason the claim was denied. |
| 21 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 22 | `END_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the end_effective_dt_tm column. |
| 23 | `EXT_PAYER_IDENT` | VARCHAR(100) |  |  | The primary identifier of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 24 | `EXT_PAYER_NAME` | VARCHAR(100) |  |  | The name of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 25 | `FAM_DEDUCT_MET_AMT` | DOUBLE |  |  | The amount of the family deductable that has been met. |
| 26 | `FAM_DEDUCT_MET_DT_TM` | DATETIME |  |  | The date and time the family deductable was met. |
| 27 | `GENERIC_HEALTH_PLAN_NAME` | VARCHAR(100) |  |  | The name of the health plan when the health plan category is GENERIC. |
| 28 | `GROUP_NAME` | VARCHAR(200) |  |  | The group name of the plan. |
| 29 | `GROUP_NBR` | VARCHAR(100) |  |  | The group number of the plan. |
| 30 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 31 | `INSURED_CARD_NAME` | VARCHAR(100) |  |  | Person's Name as seen on the insurance card. |
| 32 | `INSURED_CARD_NAME_FIRST` | VARCHAR(100) |  |  | Person's first name as seen on the insurance card. |
| 33 | `INSURED_CARD_NAME_LAST` | VARCHAR(100) |  |  | Person's last name as seen on the insurance card. |
| 34 | `INSURED_CARD_NAME_MIDDLE` | VARCHAR(100) |  |  | Person's middle name as seen on the insurance card. |
| 35 | `INSURED_CARD_NAME_SUFFIX` | VARCHAR(100) |  |  | Person's name suffix as seen on the insurance card. |
| 36 | `INS_OFFICE_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the organization table of the health plan's insurance office. |
| 37 | `LIFE_RSV_DAILY_DED_AMT` | DOUBLE | NOT NULL |  | The daily deductible amount that is applicable when reserve days are used for coverage. |
| 38 | `LIFE_RSV_DAILY_DED_QUAL_CD` | DOUBLE | NOT NULL |  | The qualifier describing the amount entered in the Lifetime reserve daily deductible. |
| 39 | `LIFE_RSV_DAYS` | DOUBLE | NOT NULL |  | The predetermined number of coverage days held "in reserve" for use if needed. The reserve days can be used when all the days under a given service have been used, but continued coverage/care is needed. This number is static for the lifetime of the subscriber. |
| 40 | `LIFE_RSV_REMAIN_DAYS` | DOUBLE | NOT NULL |  | A static, manual-entry field obtained from taking the Lifetime reserve days and subtracting any days used from that reserve for coverage. |
| 41 | `MAX_OUT_PCKT_AMT` | DOUBLE |  |  | The maximum out of pocket amount the person is responsible for. |
| 42 | `MAX_OUT_PCKT_DT_TM` | DATETIME |  |  | The date and time the person met the out of pocket amount. |
| 43 | `MEMBER_NBR` | VARCHAR(100) |  |  | The plan member number for the person. |
| 44 | `MEMBER_PERSON_CODE` | VARCHAR(100) |  |  | An additional attribute that the payer can use to uniquely identify the subscriber and their dependents within the context of a particular policy. The policy number in conjunction with the member person code typically comprise the member number.; |
| 45 | `MILITARY_SERVICE_CD` | DOUBLE |  |  | The branch of military service through which the health plan coverage is being offered to the subscriber due to their current or past service. Examples may include, Army, Navy, Air Force, etc. |
| 46 | `ON_FILE_ADMIN_SEX_CD` | DOUBLE | NOT NULL |  | The person's gender code as it appears on file with the carrier. |
| 47 | `ON_FILE_BIRTH_DT_ISO` | VARCHAR(10) |  |  | The patient's date of birth as it appears on the file with the carrier. Stored in standard ISO format. |
| 48 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The ID of the organization providing the insurance plan. |
| 49 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 50 | `PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person organization relationship table. It is an internal system assigned number. |
| 51 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person health plan relationship table. It is an internal system assigned number. |
| 52 | `PERSON_PLAN_R_CD` | DOUBLE | NOT NULL |  | Code value for the type of relationship between the insurance plan and the person. Examples are member and subscriber. |
| 53 | `PLAN_CLASS_CD` | DOUBLE | NOT NULL |  | Code value that indicates if the health plan is in the reference list of health plans or not. FREETEXT indicates it is not in the list, HEALTHPLAN indicates it is. |
| 54 | `PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that indicates the type of health plan. Examples are Medicaid, self pay, commercial, etc. |
| 55 | `POLICY_NBR` | VARCHAR(100) |  |  | The policy number of the subscriber's health plan at the time of the visit. The policy number in conjunction with the member person code typically comprise the member number. Sometimes the individual's member number is referred to as their policy number so care should be taken in order to make sure that the correct field is being used given a particular use case.; |
| 56 | `PRIORITY_SEQ` | DOUBLE |  |  | This is a numeric number used to represent the order in which to considered this health plan for reimbursement, if the person is a member of more than one health plan. |
| 57 | `PROGRAM_STATUS_CD` | DOUBLE | NOT NULL |  | Represents the set of coverages and/or benefits available to the recipient based on the recipient's reason for eligibility. |
| 58 | `SIGNATURE_ON_FILE_CD` | DOUBLE | NOT NULL |  | Coed value that indicates what level a person is allowing the release of medical information. Some examples are , No, Informed Consent, Limited, etc. |
| 59 | `SPONSOR_PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL | FK→ | ID of sponsor's relationship to the employer. |
| 60 | `SUBSCRIBER_PERSON_ID` | DOUBLE | NOT NULL |  | The person ID of the plan subscriber. |
| 61 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the verification took place. |
| 67 | `VERIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person that did the verification |
| 68 | `VERIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | The source by which the row was verified. |
| 69 | `VERIFY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the verification. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ARCHIVE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `COVERAGE_COMMENTS_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INS_OFFICE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_ORG_RELTN_ID` | [PERSON_ORG_RELTN](PERSON_ORG_RELTN.md) | `PERSON_ORG_RELTN_ID` |
| `SPONSOR_PERSON_ORG_RELTN_ID` | [PERSON_ORG_RELTN](PERSON_ORG_RELTN.md) | `PERSON_ORG_RELTN_ID` |
| `VERIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| [PERSON_BENEFIT_R](PERSON_BENEFIT_R.md) | `PERSON_PLAN_RELTN_ID` |
| [PERSON_PLAN_AUTH_R](PERSON_PLAN_AUTH_R.md) | `PERSON_PLAN_RELTN_ID` |
| [PERSON_PLAN_AUTH_R_HIST](PERSON_PLAN_AUTH_R_HIST.md) | `PERSON_PLAN_RELTN_ID` |
| [PERSON_PLAN_PROFILE_RELTN](PERSON_PLAN_PROFILE_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| [PERSON_PLAN_PROFILE_R_HIST](PERSON_PLAN_PROFILE_R_HIST.md) | `PERSON_PLAN_RELTN_ID` |
| [PREEXIST_CONDITION](PREEXIST_CONDITION.md) | `PERSON_PLAN_RELTN_ID` |
| [REFERRAL_P_PLAN_RELTN](REFERRAL_P_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| [TRANSACTION_ELIGIBILITY](TRANSACTION_ELIGIBILITY.md) | `PERSON_PLAN_RELTN_ID` |

