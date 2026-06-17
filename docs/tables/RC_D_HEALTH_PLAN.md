# RC_D_HEALTH_PLAN

> This table contains health plan information such as insurance company and health plan name,

**Description:** Revenue Cycle Dimension Health Plan  
**Table type:** ACTIVITY  
**Primary key:** `RC_D_HEALTH_PLAN_ID`  
**Columns:** 20  
**Referenced by:** 33 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 5 | `GROUP_NAME` | VARCHAR(200) | NOT NULL |  | The Group to which a health plan belongs. |
| 6 | `GROUP_NBR_IDENT` | VARCHAR(100) | NOT NULL |  | The group number associated with the group name to which a health plan belongs. |
| 7 | `HEALTH_PLAN_CLASS` | VARCHAR(40) | NOT NULL |  | The class of a health plan (i.e. Free text Health Plan, Organization) |
| 8 | `HEALTH_PLAN_NAME` | VARCHAR(100) | NOT NULL |  | The name of a health plan. |
| 9 | `HEALTH_PLAN_PRODUCT_TYPE` | VARCHAR(40) | NOT NULL |  | Determines the product designation for a health plan (Commercial, Auto Insurance, etc.). Uses code set 26310. |
| 10 | `INSURANCE_COMPANY` | VARCHAR(100) | NOT NULL |  | The insurance company associated with a health plan. |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 12 | `MILL_HEALTH_PLAN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related Health Plan in Millennium from which this data is derived. |
| 13 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 14 | `POLICY_NBR_IDENT` | VARCHAR(100) | NOT NULL |  | The policy number associated with a Health Plan. |
| 15 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies information about a Health Plan such as insurance company and health plan name. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (33)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_RESP_HEALTH_PLAN_ID` |
| [RC_F_CASE_MIX](RC_F_CASE_MIX.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_CLAIM_EVENT](RC_F_CLAIM_EVENT.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_CODING_ACTIVITY](RC_F_CODING_ACTIVITY.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_RESP_HEALTH_PLAN_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_DAILY_CLAIM_EVENT_SMRY](RC_F_DAILY_CLAIM_EVENT_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_DAILY_DENIAL_SMRY](RC_F_DAILY_DENIAL_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_DLY_CHRG_ASSOC_SMRY](RC_F_DLY_CHRG_ASSOC_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_DLY_CODING_ACT_SMRY](RC_F_DLY_CODING_ACT_SMRY.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_MONTHLY_CLAIM_EVENT_SMRY](RC_F_MONTHLY_CLAIM_EVENT_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_MONTHLY_DENIAL_SMRY](RC_F_MONTHLY_DENIAL_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_MTH_CHRG_ASSOC_SMRY](RC_F_MTH_CHRG_ASSOC_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_MTH_CODING_ACT_SMRY](RC_F_MTH_CODING_ACT_SMRY.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_RESP_HEALTH_PLAN_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_PRI_HEALTH_PLAN_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_RESP_HEALTH_PLAN_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_HEALTH_PLAN_ID` |
| [SHR_F_ENCOUNTER_VISIT](SHR_F_ENCOUNTER_VISIT.md) | `RC_D_PRI_HEALTH_PLAN_ID` |

