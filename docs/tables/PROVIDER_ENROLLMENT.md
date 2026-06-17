# PROVIDER_ENROLLMENT

> Stores a relationship between a provider/facility and a payer/health plan for the credentialing process. It also stores:- start and end dates of that process- effective dates of the provider/facility and payer/health plan relationship- Date for timely filing- participation statusThe credentialing process is how providers or whole facilities work with payers to be able to receive payments from them on all or some of their health plans.

**Description:** Provider Enrollment  
**Table type:** REFERENCE  
**Primary key:** `PROVIDER_ENROLLMENT_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BILL_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the class (e.g. Claim, Letter, etc.) to which a bill record belongs. 0 - None, 1 - All, 2 - 1450 - Institutional Claim, 3 - 1500 Professional Claim |
| 6 | `ENROLL_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The beginning date that the provider and/or facility is officially enrolled with the payer. |
| 7 | `ENROLL_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date that the official enrollment with the payer |
| 8 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The health plan for which the provider and/or facility is being enrolled. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Generally a facility, but the location for the provider(s) that are being enrolled with the payer. |
| 10 | `LOCATION_PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Contains the priority sequence for each facility. |
| 11 | `PARTICIPATION_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates whether the provider and/or facility is participating or non-participating with the payer/health plan. |
| 12 | `PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | The organization with a type of INSCO which denotes a payer. |
| 13 | `PROCESS_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date that the process to get a provider and/or facility enrolled with a payer started. |
| 14 | `PROCESS_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The estimated date that the process for getting the provider and/or facility enrolled with the payer will be finished. |
| 15 | `PROVIDER_ENROLLMENT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the PROVIDER_ENROLLMENT table. |
| 16 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The provider that is being enrolled with the payer. |
| 17 | `RECEIVED_BY_PAYER_DT_TM` | DATETIME |  |  | The date/time that the enrollment request was submitted to the payer. |
| 18 | `SUBMITTED_TO_PAYER_DT_TM` | DATETIME |  |  | The date and time that the enrollment request was acknowledged as received by the payer. |
| 19 | `TIMELY_FILING_DT_TM` | DATETIME |  |  | The date that claims will need to be submitted to the payer to prevent timely filing issues. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_BR_EDIT_FAILURE_DETAIL](PFT_BR_EDIT_FAILURE_DETAIL.md) | `PROVIDER_ENROLLMENT_ID` |

