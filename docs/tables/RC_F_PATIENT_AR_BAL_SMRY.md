# RC_F_PATIENT_AR_BAL_SMRY

> This table contains summarized patient AR balance data.

**Description:** Revenue Cycle Fact Patient AR Balance Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 3 | `INSURANCE_BALANCE_AMT` | DOUBLE |  |  | The total balance amount for insurance. |
| 4 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 5 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 6 | `RC_D_AGE_BY_LAST_PAYMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies an age category that represents the difference between the activity date and the last payment made to the encounter balance. |
| 7 | `RC_D_BALANCE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the balance type related to this fact row. |
| 8 | `RC_D_BAL_AMT_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the amount range category to which the total balance applies. |
| 9 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 10 | `RC_D_BILL_AGE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies an age category that represents the difference between the activity date and the first bill date for the encounter balance. |
| 11 | `RC_D_DISCHARGE_AGE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the age category to which this fact row is related based on the discharge age. |
| 12 | `RC_D_DNFB_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the current status and reason of the DNFB |
| 13 | `RC_D_DUNNING_LEVEL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the dunning level related to this fact row. |
| 14 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter. |
| 15 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 16 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 17 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary health plan of the financial encounter. |
| 18 | `RC_D_RESP_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the responsible financial class related to this fact row. |
| 19 | `RC_D_RESP_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the responsible health plan of the financial encounter. |
| 20 | `RC_D_UNBILLED_BAL_AMT_CAT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the amount range category to which the total unbilled balance applies. |
| 21 | `RC_F_PATIENT_AR_BAL_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies summarized patient AR balance data. |
| 22 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location related to this fact row. |
| 23 | `SP_BALANCE_AMT` | DOUBLE | NOT NULL |  | The total balance amount for Selfpay. |
| 24 | `TOTAL_BALANCE_AMT` | DOUBLE | NOT NULL |  | The total balance for the patient AR accounts. |
| 25 | `TOTAL_ENCOUNTER_COUNT` | DOUBLE | NOT NULL |  | The number of encounters rolled up into this fact row. |
| 26 | `TOTAL_ENCOUNTER_FINAL_CODED` | DOUBLE | NOT NULL |  | The total number of encounters that have been final coded within an end day established as a preference. |
| 27 | `TOTAL_UNBILLED_BALANCE_AMT` | DOUBLE | NOT NULL |  | Total balance amount that has not been billed on any claims. |
| 28 | `TOTAL_ZERO_BALANCE_CNT` | DOUBLE | NOT NULL |  | The total number of encounters resolved to a zero dollar balance for the given activity date. |
| 29 | `TOT_DSCHRG_FINAL_CODE_DAYS` | DOUBLE | NOT NULL |  | The total of days between the discharge date and the final coded date. |
| 30 | `TOT_ENCNTR_FINAL_CODE_BY_END` | DOUBLE | NOT NULL |  | The total number of encounters that have been final coded within an end day established as a preference. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_AGE_BY_LAST_PAYMENT_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_BALANCE_TYPE_ID` | [RC_D_BALANCE_TYPE](RC_D_BALANCE_TYPE.md) | `RC_D_BALANCE_TYPE_ID` |
| `RC_D_BAL_AMT_CATEGORY_ID` | [RC_D_AMOUNT_CATEGORY](RC_D_AMOUNT_CATEGORY.md) | `RC_D_AMOUNT_CATEGORY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_AGE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_DISCHARGE_AGE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_DNFB_STATUS_ID` | [RC_D_DNFB_STATUS](RC_D_DNFB_STATUS.md) | `RC_D_DNFB_STATUS_ID` |
| `RC_D_DUNNING_LEVEL_ID` | [RC_D_DUNNING_LEVEL](RC_D_DUNNING_LEVEL.md) | `RC_D_DUNNING_LEVEL_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_RESP_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_RESP_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_UNBILLED_BAL_AMT_CAT_ID` | [RC_D_AMOUNT_CATEGORY](RC_D_AMOUNT_CATEGORY.md) | `RC_D_AMOUNT_CATEGORY_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |

