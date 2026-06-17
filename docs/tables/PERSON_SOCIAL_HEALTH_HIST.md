# PERSON_SOCIAL_HEALTH_HIST

> Historical records of the eligibility status of a person for an entity offering social healthcare.

**Description:** Person Social Health History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_DISTRICT_CD` | DOUBLE | NOT NULL |  | The administrative district defines the district within the subregion and region that administers care for this person (CS 27164). |
| 6 | `ADMIN_REGION_CD` | DOUBLE | NOT NULL |  | The administrative region defines the region that administers care for this person (CS 27161). |
| 7 | `ADMIN_SUBREGION_CD` | DOUBLE | NOT NULL |  | The administrative subregion defines the subregion within the region that administers care for this person (CS 27163). |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 10 | `CHARGING_CATEGORY_CD` | DOUBLE | NOT NULL |  | The charging category determines how much of a patient's treatment expenses are covered by the social healthcare system. For example, a patient may not be covered as a foreign visitor or may be fully covered due to residency or contract with the patient's country of origin. |
| 11 | `DEREGISTRATION_DT_ISO` | VARCHAR(10) |  |  | The deregistration date defines the date the patient was deregistered as a taxable member of the revenue service, revenue agency, or taxation authority. |
| 12 | `DEREGISTRATION_REASON_CD` | DOUBLE | NOT NULL |  | The deregistration reason defines why the patient's social healthcare coverage has ended. For example, the patient may be deceased or may have emigrated out of the country (CS 27165). |
| 13 | `ELIGIBILITY_EXPIRE_DT_TM` | DATETIME |  |  | The date and time the eligibility status will expire. |
| 14 | `ELIGIBILITY_STATUS_CD` | DOUBLE | NOT NULL |  | The eligibility status of the patient. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `PATIENT_CATEGORY_CD` | DOUBLE | NOT NULL |  | The patient category represents the type of person. In most cases, it defines what charge code will be assigned for this type of person. For example, a patient may be an asylum seeker, anonymous (HIV sampling, Paperless), or a tourist (CS 27159). |
| 17 | `PAYMENT_CATEGORY_CD` | DOUBLE | NOT NULL |  | The payment category is used to control financial flows. This account code represents who is responsible for financing the visit (CS 27160). |
| 18 | `PERSON_SOCIAL_HEALTHCARE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the PERSON_SOCIAL_HEALTHCARE table. |
| 19 | `PERSON_SOCIAL_HEALTH_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PERSON_SOCIAL_HEALTH_HIST table. |
| 20 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 21 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 22 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the eligibility status was last verified. |
| 29 | `VERIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel that last verified the eligibility status. |
| 30 | `VERIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | Defines the source by which the eligibility status was last verified. |
| 31 | `VERIFY_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the verification status of the person's eligibility qualifications within the social healthcare system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_SOCIAL_HEALTHCARE_ID` | [PERSON_SOCIAL_HEALTHCARE](PERSON_SOCIAL_HEALTHCARE.md) | `PERSON_SOCIAL_HEALTHCARE_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `VERIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

