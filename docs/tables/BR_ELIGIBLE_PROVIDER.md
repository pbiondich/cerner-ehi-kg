# BR_ELIGIBLE_PROVIDER

> Store eligible providers, which are the subset of providers at the health system that are eligible for reimbursement from CMS (Centers for Medicare and Medicaid Services).

**Description:** Bedrock Eligible Provider  
**Table type:** REFERENCE  
**Primary key:** `BR_ELIGIBLE_PROVIDER_ID`  
**Columns:** 18  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_ELIGIBLE_PROVIDER table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ERX_SUBMISSION_IND` | DOUBLE | NOT NULL |  | Indicates if the provider is eligible for using eRx submissions. |
| 6 | `HEALTH_PLAN_TXT` | VARCHAR(20) | NOT NULL |  | Indicates the health system that this provider is eligible to receive reimbursement from. Stores either "MEDICARE" or "MEDICAID". |
| 7 | `HEALTH_PLAN_TXT_DT_TM` | DATETIME | NOT NULL |  | Stores the date and time that the health plan text was selected. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `NATIONAL_PROVIDER_NBR_TXT` | VARCHAR(200) | NOT NULL |  | Stores the eligible providers's national provider number. |
| 10 | `ORIG_BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the value of the PK for a particular set of rows in BR_ELIGIBLE_PROVIDER. |
| 11 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The eligible Provider. |
| 12 | `SPECIALTY_ID` | DOUBLE | NOT NULL |  | Stores the ID for the eligible providers's specialty from the br_name_value table. |
| 13 | `TAX_ID_NBR_TXT` | VARCHAR(50) | NOT NULL |  | Stores the eligible providers's tax id number. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_BR_ELIGIBLE_PROVIDER_ID` | [BR_ELIGIBLE_PROVIDER](BR_ELIGIBLE_PROVIDER.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BR_CPC_ELIG_PROV_RELTN](BR_CPC_ELIG_PROV_RELTN.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| [BR_ELIGIBLE_PROVIDER](BR_ELIGIBLE_PROVIDER.md) | `ORIG_BR_ELIGIBLE_PROVIDER_ID` |
| [BR_ELIG_PROV_EXTENSION](BR_ELIG_PROV_EXTENSION.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| [BR_ELIG_PROV_MEAS_RELTN](BR_ELIG_PROV_MEAS_RELTN.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| [BR_GPRO_SUB_RELTN](BR_GPRO_SUB_RELTN.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| [BR_PQRS_MEAS_PROVIDER_RELTN](BR_PQRS_MEAS_PROVIDER_RELTN.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| [LH_MU_METRIC_DETAILS](LH_MU_METRIC_DETAILS.md) | `BR_ELIGIBLE_PROVIDER_ID` |

