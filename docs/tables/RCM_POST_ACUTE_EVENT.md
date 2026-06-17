# RCM_POST_ACUTE_EVENT

> Stores referral event and booking information from post-acute providers

**Description:** RevWorks Care Management - Post Acute Event  
**Table type:** ACTIVITY  
**Primary key:** `RCM_POST_ACUTE_EVENT_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DIRECT_EMAIL_IND` | DOUBLE | NOT NULL |  | Indicates if the event provider has been sent an email. |
| 4 | `DISCHARGE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PRSNL_ID of the discharge planner who initiated the post-acute referral. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Encounter for this post-acute referral event. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EVENT_DT_TM` | DATETIME |  |  | The post-acute referral event date and time |
| 8 | `EVENT_IDENT` | VARCHAR(100) | NOT NULL |  | The external unique event identifier from the third party system. |
| 9 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of post-acute event. |
| 10 | `HOSPITAL_STATUS_CD` | DOUBLE | NOT NULL |  | The referral status from the hospital or the patient's facility. |
| 11 | `POST_ACUTE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the post-acute provider. |
| 12 | `PREV_POST_ACUTE_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the post-acute event. This field will always point back to the initial value created. This may be used to find the correct version when combined with the begin and end effective dates and times. |
| 13 | `PROVIDER_RESPONSE_CD` | DOUBLE | NOT NULL |  | The referral response status from the post-acute provider. |
| 14 | `RCM_POST_ACUTE_EVENT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies referral event and booking information from post-acute providers. |
| 15 | `SERVICE_CD` | DOUBLE | NOT NULL |  | The level of care or service type such as shelter, assisted living, durable medical equipment... of the referral that is provided by the post-acute provider. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISCHARGE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `POST_ACUTE_PROVIDER_ID` | [RCM_POST_ACUTE_PROVIDER](RCM_POST_ACUTE_PROVIDER.md) | `RCM_POST_ACUTE_PROVIDER_ID` |
| `PREV_POST_ACUTE_EVENT_ID` | [RCM_POST_ACUTE_EVENT](RCM_POST_ACUTE_EVENT.md) | `RCM_POST_ACUTE_EVENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_POST_ACUTE_EVENT](RCM_POST_ACUTE_EVENT.md) | `PREV_POST_ACUTE_EVENT_ID` |

