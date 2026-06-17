# RC_F_DAILY_BAL_AR_SMRY

> Summarization of RC_F_Balance_AR table.

**Description:** Revenue Cycle Fact Daily Balance AR Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 3 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 4 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 5 | `RC_D_ACCOMMODATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the accommodation related to this fact row. |
| 6 | `RC_D_AGE_BY_DISCHARGE_ID` | DOUBLE | NOT NULL | FK→ | Relates this fact row to a specific age category based on the discharge age. |
| 7 | `RC_D_AGE_BY_FIRST_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies an age category that represents the difference between the activity date and the date the first charge was posted to the balance. |
| 8 | `RC_D_AGE_BY_ORIG_BILL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies an age category that represents the difference between the activity date and the first transmitted claim or submitted statement on a balance, regardless of whether or not the bill was cancelled. |
| 9 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 10 | `RC_D_BALANCE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the balance group related to this fact row. |
| 11 | `RC_D_BALANCE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the balance type related to this fact row |
| 12 | `RC_D_BAL_HOLD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the balance hold related to this fact row |
| 13 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 14 | `RC_D_ENCNTR_HOLD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter hold related to this fact row |
| 15 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter class and encounter type related to this fact row. |
| 16 | `RC_D_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 17 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row |
| 18 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the medical service related to this fact row. |
| 19 | `RC_D_PRI_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary financial class related to this fact row |
| 20 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary health plan related to this fact row |
| 21 | `RC_D_RESP_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the responsible financial class related to this fact row |
| 22 | `RC_D_RESP_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the responsible health plan related to this fact row |
| 23 | `RC_F_DAILY_BAL_AR_SMRY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_F_DAILY_BALANCE_AR_SMRY table. |
| 24 | `SHR_D_ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending physician related to this fact row |
| 25 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location related to this fact row |
| 26 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | The total adjustment amounts for the balances that make up the fact row. |
| 27 | `TOTAL_BALANCE_AMT` | DOUBLE | NOT NULL |  | The total outstanding balance amount for the payer. |
| 28 | `TOTAL_BALANCE_COUNT` | DOUBLE | NOT NULL |  | The number of balances rolled up into this fact row. |
| 29 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | The total charge amounts for the balances that make up the fact row. |
| 30 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | The total payment amounts for the balances that make up the fact row. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_D_ACCOMMODATION_ID` | [RC_D_ACCOMMODATION](RC_D_ACCOMMODATION.md) | `RC_D_ACCOMMODATION_ID` |
| `RC_D_AGE_BY_DISCHARGE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_FIRST_SERVICE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_ORIG_BILL_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_BALANCE_GROUP_ID` | [RC_D_BALANCE_GROUP](RC_D_BALANCE_GROUP.md) | `RC_D_BALANCE_GROUP_ID` |
| `RC_D_BALANCE_TYPE_ID` | [RC_D_BALANCE_TYPE](RC_D_BALANCE_TYPE.md) | `RC_D_BALANCE_TYPE_ID` |
| `RC_D_BAL_HOLD_ID` | [RC_D_HOLD](RC_D_HOLD.md) | `RC_D_HOLD_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_ENCNTR_HOLD_ID` | [RC_D_HOLD](RC_D_HOLD.md) | `RC_D_HOLD_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_PRI_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_RESP_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_RESP_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_ATTENDING_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |

