# ENCNTR_SOCIAL_HEALTHCARE

> Records the eligibility status of a person for an entity offering social healthcare at the time of visit.

**Description:** Encounter Social Healthcare  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_SOCIAL_HEALTHCARE_ID`  
**Columns:** 27  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_DISTRICT_CD` | DOUBLE | NOT NULL |  | The administrative district defines the division within the administrative sub-region where the patient is located for the purpose of defining the responsible entity for financial obligations (CS27164). |
| 6 | `ADMIN_REGION_CD` | DOUBLE | NOT NULL |  | The administrative region defines where the patient is located for the purpose of defining the responsible entity for financial obligations (CS27161). |
| 7 | `ADMIN_SUBREGION_CD` | DOUBLE | NOT NULL |  | The administrative sub-region defines the division within the administrative region where the patient is located for the purpose of defining the responsible entity for financial obligations (CS27163). |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CHARGING_CATEGORY_CD` | DOUBLE | NOT NULL |  | The charging category determines who is responsible for payment of a patient¿s treatment expenses within the social healthcare system. For example, a patient may not be covered as a foreign visitor (self-pay) or may be fully covered due to residency or contract with the patient¿s country of origin (CS 27155). |
| 10 | `DEREGISTRATION_DT_ISO` | VARCHAR(10) |  |  | The deregistration date defines the date the patient was deregistered as a taxable member of the revenue service, revenue agency, or taxation authority. |
| 11 | `DEREGISTRATION_REASON_CD` | DOUBLE | NOT NULL |  | The deregistration reason defines why the patient's social healthcare coverage has ended. For example, the patient may be deceased or may have emigrated out of the country (CS 27165). |
| 12 | `ELIGIBILITY_EXPIRE_DT_TM` | DATETIME |  |  | The date and time the eligibility status will expire. |
| 13 | `ELIGIBILITY_STATUS_CD` | DOUBLE | NOT NULL |  | The eligibility status of the person within the social healthcare system at the time of visit. |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter for which the eligibility status applies. |
| 15 | `ENCNTR_SOCIAL_HEALTHCARE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the ENCNTR_SOCIAL_HEALTHCARE table. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `PATIENT_CATEGORY_CD` | DOUBLE | NOT NULL |  | The patient category defines the status of the patient as it pertains to determining charge codes for treatment of the patient within the social healthcare system. For example, a patient may be an asylum seeker, a tourist, anonymous (e.g. for HIV testing), or an undocumented immigrant (CS 27159). |
| 18 | `PAYMENT_CATEGORY_CD` | DOUBLE | NOT NULL |  | The payment category further defines the status of the patient as it pertains to determining the responsible entity for financial obligations generated from a visit (CS 27160). |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the eligibility status was last verified. |
| 25 | `VERIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel that last verified the eligibility status. |
| 26 | `VERIFY_SOURCE_CD` | DOUBLE | NOT NULL |  | Defines the source by which the eligibility status was last verified. |
| 27 | `VERIFY_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the verification status of the person's eligibility qualifications within the social healthcare system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `VERIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_SOCIAL_HEALTH_HIST](ENCNTR_SOCIAL_HEALTH_HIST.md) | `ENCNTR_SOCIAL_HEALTHCARE_ID` |

