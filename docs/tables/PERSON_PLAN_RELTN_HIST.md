# PERSON_PLAN_RELTN_HIST

> History table for the Person Plan Relation table

**Description:** Person Plan Relationship History  
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
| 5 | `ALT_MEMBER_NBR` | VARCHAR(100) |  |  | The alternate payer plan member number for the person. |
| 6 | `ARCHIVE_DT_TM` | DATETIME |  |  | The date and time at which the patient health plan relationship (coverage) was archived. Once the coverage is archived, it should not be allocated to future encounters. |
| 7 | `ARCHIVE_PRSNL_ID` | DOUBLE |  |  | The id of the personnel who archived the patient health plan relationship (coverage) |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the beg_effective_dt_tm column. |
| 10 | `CARD_CATEGORY_CD` | DOUBLE | NOT NULL |  | A categorization of the coverages and/or benefits available to the recipient. For some insurances this may be clearly identifiable based on characteristics of the beneficiary's coverage card. |
| 11 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `END_EFFECTIVE_TZ` | DOUBLE |  |  | The time zone associated with the end_effective_dt_tm column. |
| 15 | `EXT_PAYER_IDENT` | VARCHAR(100) |  |  | The primary identifier of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 16 | `EXT_PAYER_NAME` | VARCHAR(100) |  |  | The name of the organization (that does not exist in the Millennium build) providing the insurance plan (carrier). |
| 17 | `GENERIC_HEALTH_PLAN_NAME` | VARCHAR(100) |  |  | The name of the health plan when the health plan category is generic. |
| 18 | `GROUP_NAME` | VARCHAR(200) |  |  | The group name of the plan. |
| 19 | `GROUP_NBR` | VARCHAR(100) |  |  | The group number of the plan. |
| 20 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 21 | `INSURED_CARD_NAME` | VARCHAR(100) |  |  | Subscriber's/Patient's name as printed on the insurance card. |
| 22 | `INSURED_CARD_NAME_FIRST` | VARCHAR(100) |  |  | Person's first name as seen on the insurance card. |
| 23 | `INSURED_CARD_NAME_LAST` | VARCHAR(100) |  |  | Person's last name as seen on the insurance card. |
| 24 | `INSURED_CARD_NAME_MIDDLE` | VARCHAR(100) |  |  | Person's middle name as seen on the insurance card. |
| 25 | `INSURED_CARD_NAME_SUFFIX` | VARCHAR(100) |  |  | Person's name suffix as seen on the insurance card. |
| 26 | `INS_OFFICE_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the organization table of the health plan's insurance office. |
| 27 | `MEMBER_NBR` | VARCHAR(100) |  |  | The plan member number for the person. |
| 28 | `MEMBER_PERSON_CODE` | VARCHAR(100) |  |  | An additional attribute that the payer can use to uniquely identify the subscriber and their dependents within the context of a particular policy. The policy number in conjunction with the member person code typically comprise the member number. |
| 29 | `MILITARY_SERVICE_CD` | DOUBLE |  |  | The branch of military service through which the health plan coverage is being offered to the subscriber due to their current or past service. Examples may include, Army, Navy, Air Force, etc. |
| 30 | `ON_FILE_ADMIN_SEX_CD` | DOUBLE | NOT NULL |  | The person's gender code as it appears on file with the carrier. |
| 31 | `ON_FILE_BIRTH_DT_ISO` | VARCHAR(10) |  |  | The patient's date of birth as it appears on the file with the carrier. Stored in standard ISO format. |
| 32 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | The ID of the organization providing the insurance plan. |
| 33 | `PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person organization relationship table. It is an internal system assigned number. |
| 34 | `PERSON_PLAN_RELTN_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely identifies history for a given person plan relationship. |
| 35 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL |  | This is the ID from the PERSON_PLAN_RELTN row relating the PERSON and the HEALTH_PLAN to this ENCNTR_PLAN_RELTN row. For an encounter, a corresponding row can be maintained at the person level with the same information. |
| 36 | `PERSON_PLAN_R_CD` | DOUBLE | NOT NULL |  | Code value for the type of relationship between the insurance plan and the person. Examples are member and subscriber. |
| 37 | `PLAN_CLASS_CD` | DOUBLE | NOT NULL |  | Code value that indicates if the health plan is in the reference list of health plans or not. FREETEXT indicates it is not in the list, HEALTHPLAN indicates it is. |
| 38 | `PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that indicates the type of health plan. Examples are Medicaid, self pay, commercial, etc. |
| 39 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 40 | `POLICY_NBR` | VARCHAR(100) |  |  | The policy number of the subscriber's health plan at the time of the visit. The policy number in conjunction with the member person code typically comprise the member number. Sometimes the individual's member number is referred to as their policy number so care should be taken in order to make sure that the correct field is being used given a particular use case. |
| 41 | `PRIORITY_SEQ` | DOUBLE |  |  | this is a numeric number used to represent the order in which to considered this health plan for reimbursement, if the person is a member of more than one health plan. |
| 42 | `PROGRAM_STATUS_CD` | DOUBLE | NOT NULL |  | Represents the set of coverages and/or benefits available to the recipient based on the recipient's reason for eligibility. |
| 43 | `SIGNATURE_ON_FILE_CD` | DOUBLE | NOT NULL |  | Coed value that indicates what level a person is allowing the release of medical information. Some examples are , No, Informed Consent, Limited, etc. |
| 44 | `SPONSOR_PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | ID of sponsor's relationship to the employer. |
| 45 | `SUBSCRIBER_PERSON_ID` | DOUBLE | NOT NULL |  | The person ID of the plan subscriber. |
| 46 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 47 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 48 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the verification took place. |
| 54 | `VERIFY_PRSNL_ID` | DOUBLE | NOT NULL |  | The ID of the person that did the verification |
| 55 | `VERIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | The source by which the row was verified. |
| 56 | `VERIFY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the verification. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INS_OFFICE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

