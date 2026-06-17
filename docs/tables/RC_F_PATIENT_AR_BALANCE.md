# RC_F_PATIENT_AR_BALANCE

> This table contains data related to Patient AR Account Balances.

**Description:** Revenue Cycle Fact Patient AR Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 64

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `ACTUAL_BALANCE_AMT` | DOUBLE | NOT NULL |  | Original Balance Amount without offset consideration. |
| 3 | `ACTUAL_DLY_ADJ_AMT` | DOUBLE | NOT NULL |  | Original daily adjustment amount without offset consideration. |
| 4 | `ACTUAL_DLY_CHG_AMT` | DOUBLE | NOT NULL |  | Original daily charge amount without offset consideration. |
| 5 | `ACTUAL_DLY_PAY_AMT` | DOUBLE | NOT NULL |  | Original daily payment amount without offset consideration |
| 6 | `ACTUAL_TOT_ADJ_AMT` | DOUBLE | NOT NULL |  | Original total adjustment amount without offset consideration |
| 7 | `ACTUAL_TOT_CHG_AMT` | DOUBLE | NOT NULL |  | Original total charge amount without offset consideration |
| 8 | `ACTUAL_TOT_PAY_AMT` | DOUBLE | NOT NULL |  | Original total payment amount without offset consideration |
| 9 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 10 | `BALANCE_AMT` | DOUBLE | NOT NULL |  | The balance amount of the Patient AR Account. |
| 11 | `BILL_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the current activity date and the transmission date of the bill. |
| 12 | `DAILY_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the adjustment amount per day. |
| 13 | `DAILY_CHARGE_AMT` | DOUBLE | NOT NULL |  | Contains the daily charge amount per day. |
| 14 | `DAILY_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the payment amount per day. |
| 15 | `DISCHARGE_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the current activity date and the discharge date. |
| 16 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the OMF_DATE table. |
| 17 | `FINAL_CODED_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the final coded date. References the key in the OMF_DATE table. |
| 18 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 19 | `HARD_CLOSE_EVAL_DT_TM` | DATETIME |  |  | This field stores the datetime of when the particular encounter was evaluated for hard close. |
| 20 | `INSURANCE_BALANCE_AMT` | DOUBLE |  |  | The total balance amount for insurance. |
| 21 | `LAST_PAYMENT_AGE` | DOUBLE | NOT NULL |  | Days since the last payment has been made to the Financial Encounter. |
| 22 | `LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date of the last time a payment was made to the financial encounter. Related to the OMF_DATE table. |
| 23 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 24 | `MILL_ENCOUNTER_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Millennium Encounter record that relates to this fact row. |
| 25 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 26 | `RC_AF_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data related to the RC_F_Patient_AR_Balance table. |
| 27 | `RC_D_ACCOMMODATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies accommodation information related to this fact row. |
| 28 | `RC_D_AGE_BY_BILL_ID` | DOUBLE | NOT NULL | FK→ | Relates this fact row to a specific age category. |
| 29 | `RC_D_AGE_BY_DISCHARGE_ID` | DOUBLE | NOT NULL | FK→ | Relates this fact row to a specific age category based on the discharge age. |
| 30 | `RC_D_AGE_BY_LAST_PAYMENT_ID` | DOUBLE | NOT NULL | FK→ | Relates the age by last payment to a specific age category. |
| 31 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending Personnel in a given location in the fact table. |
| 32 | `RC_D_BALANCE_TYPE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the dunning level related to this fact row. |
| 33 | `RC_D_BAL_AMT_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the amount range category to which the balance applies. |
| 34 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 35 | `RC_D_DNFB_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the current status and reason if the encounter is DNFB. |
| 36 | `RC_D_DUNNING_LEVEL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the dunning level related to this fact row. |
| 37 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies encounter type class information related to this fact row. |
| 38 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 39 | `RC_D_PRI_DRG_ID` | DOUBLE |  | FK→ | Uniquely identifies the primary DRG related to this record. |
| 40 | `RC_D_PRI_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Number that uniquely identifies the primary financial class related to this fact row. |
| 41 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the primary health plan related to this fact row. |
| 42 | `RC_D_PRI_HOLD_ID` | DOUBLE | NOT NULL | FK→ | Number that uniquely identifies the primary hold for this fact row. |
| 43 | `RC_D_RESP_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the responsible financial class related to this fact row. |
| 44 | `RC_D_RESP_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Number that uniquely identifies the responsible health plan related to this fact row. |
| 45 | `RC_D_UNBILLED_BAL_AMT_CAT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the amount range category to which the unbilled balance applies. |
| 46 | `RC_F_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data related to Patient AR Account balances. |
| 47 | `RESP_PRIORITY_SEQ_NBR` | DOUBLE | NOT NULL |  | Sequence that defines a hierarchy for Insurance, Self Pay responsibility. |
| 48 | `SHR_D_ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending physician for this patient AR balance. |
| 49 | `SHR_D_CODING_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person who coded the clinical encounter. |
| 50 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies location information related to this fact row. |
| 51 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this fact row. |
| 52 | `SHR_D_QUEUE_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person to whom the responsible financial encounter balance is assigned to in a workflow. |
| 53 | `SP_BALANCE_AMT` | DOUBLE | NOT NULL |  | The total balance amount for Selfpay. |
| 54 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 55 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the adjustments. |
| 56 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | The total of the charges. |
| 57 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the payments. |
| 58 | `UNBILLED_BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the balance amount that has not been billed on any claims. |
| 59 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `ZERO_BAL_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the zero balance date. References the key in the OMF_DATE table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `FINAL_CODED_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_AF_PATIENT_AR_BALANCE_ID` | [RC_AF_PATIENT_AR_BALANCE](RC_AF_PATIENT_AR_BALANCE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| `RC_D_ACCOMMODATION_ID` | [RC_D_ACCOMMODATION](RC_D_ACCOMMODATION.md) | `RC_D_ACCOMMODATION_ID` |
| `RC_D_AGE_BY_BILL_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_DISCHARGE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_LAST_PAYMENT_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_BAL_AMT_CATEGORY_ID` | [RC_D_AMOUNT_CATEGORY](RC_D_AMOUNT_CATEGORY.md) | `RC_D_AMOUNT_CATEGORY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_DNFB_STATUS_ID` | [RC_D_DNFB_STATUS](RC_D_DNFB_STATUS.md) | `RC_D_DNFB_STATUS_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_PRI_DRG_ID` | [RC_D_DRG](RC_D_DRG.md) | `RC_D_DRG_ID` |
| `RC_D_PRI_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_PRI_HOLD_ID` | [RC_D_HOLD](RC_D_HOLD.md) | `RC_D_HOLD_ID` |
| `RC_D_RESP_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_RESP_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_UNBILLED_BAL_AMT_CAT_ID` | [RC_D_AMOUNT_CATEGORY](RC_D_AMOUNT_CATEGORY.md) | `RC_D_AMOUNT_CATEGORY_ID` |
| `SHR_D_ATTENDING_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CODING_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_QUEUE_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `ZERO_BAL_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |

