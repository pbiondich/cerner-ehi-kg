# WH_BR_ELIGIBLE_PROVIDER

> This table Store eligible providers, which are the subset of providers at the health system that are eligible for reimbursement from CMS (Centers for Medicare and Medicaid Services).

**Description:** WH_BR_ELIGIBLE_PROVIDER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_ELIGIBLE_PROVIDER table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ERX_SUBMISSION_IND` | DOUBLE |  |  | Indicates if the provider is eligible for using eRx submissions. |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which extracts were run. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_PLAN_TXT` | VARCHAR(50) |  |  | Indicates the health system that this provider is eligible to receive reimbursement from. Stores either ""MEDICARE"" or ""MEDICAID"". |
| 9 | `HEALTH_PLAN_TXT_DT_TM` | DATETIME |  |  | Stores the date and time that the health plan text was selected. |
| 10 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system id |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system source id |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 13 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 14 | `NATIONAL_PROVIDER_NBR_TXT` | VARCHAR(200) |  |  | Stores the eligible providers's national provider number. |
| 15 | `ORIG_BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Used for versioning. Contains the value of the PK for a particular set of rows in BR_ELIGIBLE_PROVIDER. |
| 16 | `PROVIDER_ID` | DOUBLE | NOT NULL |  | The eligible Provider. |
| 17 | `SPECIALTY_ID` | DOUBLE | NOT NULL |  | Stores the ID for the eligible providers's specialty from the br_name_value table. |
| 18 | `TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | Stores the eligible providers's tax id number. |
| 19 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_USER` | VARCHAR(40) |  |  | The user that performs the insert or update to the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

