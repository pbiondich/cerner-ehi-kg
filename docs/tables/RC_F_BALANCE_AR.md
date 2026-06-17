# RC_F_BALANCE_AR

> This table contains data related to balance level AR.

**Description:** Revenue Cycle Fact Balance AR  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 63

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | The Cerner Julian number representing the date for which the census data applies. |
| 2 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 3 | `BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the Balance of the AR account. |
| 4 | `BILL_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the current activity data and the transmission date of the bill. |
| 5 | `BILL_NUMBER` | VARCHAR(40) | NOT NULL |  | Bill number of this balance fact row. |
| 6 | `BILL_STATUS` | VARCHAR(20) | NOT NULL |  | The status of the bill of this balance fact row. |
| 7 | `DISCHARGE_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the current activity date and the discharge date. |
| 8 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the OMF_DATE table. |
| 9 | `ENCNTR_BALANCE_AMT` | DOUBLE | NOT NULL |  | The balance amount of the Patient AR Account. |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 11 | `FIRST_SERVICE_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the activity date and the date the first charge was posted to the balance. |
| 12 | `FIRST_SERVICE_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the first service date. References the key in the OMF_DATE table. |
| 13 | `LAST_ADJUSTMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the most recent adjustment date of this balance fact row. References the key in the OMF_DATE table. |
| 14 | `LAST_BILL_SUBMISSION_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the first submitted bill date for this balance row. References the key in the OMF_DATE table. |
| 15 | `LAST_BILL_TRANSMISSION_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the first transmitted bill date for this balance row. References the key in the OMF_DATE table. |
| 16 | `LAST_CHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the most recent posted charge date for this balance fact row. References the key in the OMF_DATE table. |
| 17 | `LAST_PAYMENT_AGE` | DOUBLE | NOT NULL |  | Days since the last payment has been made to the Financial Encounter. |
| 18 | `LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date of the last time a payment was made to the financial encounter. Related to the OMF_DATE table. |
| 19 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 20 | `MILL_BENEFIT_ORDER_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related benefit order. |
| 21 | `MILL_BO_HP_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related BO_HP_RELTN record. |
| 22 | `MILL_FIN_ENCNTR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related financial encounter record. |
| 23 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 24 | `ORIG_BILL_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the activity date and the first transmitted claim or submitted statement on a balance, regardless of whether or not the bill was cancelled. |
| 25 | `ORIG_BILL_SUBMISSION_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the first submitted bill date for this balance row. References the key in the OMF_DATE table. |
| 26 | `ORIG_BILL_TRANSMISSION_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the first transmitted bill date for this balance row. References the key in the OMF_DATE table |
| 27 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | A sequence that defines a hierarchy for Insurance, Self Pay responsibility. |
| 28 | `RC_AF_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data related to the RC_AF_PATIENT_AR_BALANCE table. |
| 29 | `RC_D_ACCOMMODATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the accommodation related to this fact row. |
| 30 | `RC_D_AGE_BY_BILL_ID` | DOUBLE | NOT NULL | FK→ | Relates this fact row to a specific age category. |
| 31 | `RC_D_AGE_BY_DISCHARGE_ID` | DOUBLE | NOT NULL | FK→ | Relates this fact row to a specific age category based on the discharge age. |
| 32 | `RC_D_AGE_BY_FIRST_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | A number representing the first service date. References the key in the OMF_DATE table. |
| 33 | `RC_D_AGE_BY_LAST_PAYMENT_ID` | DOUBLE | NOT NULL | FK→ | Relates the age by last payment to a specific age category. |
| 34 | `RC_D_AGE_BY_ORIG_BILL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies an age category that represents the difference between the activity date and the first transmitted claim or submitted statement on a balance, regardless of whether or not the bill was cancelled. |
| 35 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 36 | `RC_D_BALANCE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a balance group. |
| 37 | `RC_D_BALANCE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the different balance types to which an account can be associated. |
| 38 | `RC_D_BAL_HOLD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary balance level hold for this fact row. |
| 39 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity associated to the encounter associated to this denial. |
| 40 | `RC_D_BILL_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data associated to claim attributes for reporting purposes. |
| 41 | `RC_D_ENCNTR_HOLD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary encounter level hold for this fact row. |
| 42 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter associated to this row. |
| 43 | `RC_D_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the current financial class related to this fact row. |
| 44 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the current health plan related to this fact row. |
| 45 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 46 | `RC_D_PRI_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary financial class related to this fact row. |
| 47 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary health plan related to this fact row. |
| 48 | `RC_D_RESP_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the responsible financial class related to this fact row. |
| 49 | `RC_D_RESP_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the responsible health plan related to this fact row. |
| 50 | `RC_F_BALANCE_AR_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_F_BALANCE_AR table, which contains data related to balance level AR. |
| 51 | `REG_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the registration date. References the key in the OMF_DATE table. |
| 52 | `SHR_D_ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending physician for this fact row. |
| 53 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location information related to this fact row. |
| 54 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this fact row |
| 55 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 56 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the adjustments of this balance fact row. |
| 57 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | Contains the total of the charges of this balance fact row. |
| 58 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the payments of this balance fact row. |
| 59 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_ADJUSTMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_BILL_SUBMISSION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_BILL_TRANSMISSION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_CHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_AF_PATIENT_AR_BALANCE_ID` | [RC_AF_PATIENT_AR_BALANCE](RC_AF_PATIENT_AR_BALANCE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| `RC_D_ACCOMMODATION_ID` | [RC_D_ACCOMMODATION](RC_D_ACCOMMODATION.md) | `RC_D_ACCOMMODATION_ID` |
| `RC_D_AGE_BY_BILL_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_DISCHARGE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_FIRST_SERVICE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_LAST_PAYMENT_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_ORIG_BILL_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_BALANCE_GROUP_ID` | [RC_D_BALANCE_GROUP](RC_D_BALANCE_GROUP.md) | `RC_D_BALANCE_GROUP_ID` |
| `RC_D_BALANCE_TYPE_ID` | [RC_D_BALANCE_TYPE](RC_D_BALANCE_TYPE.md) | `RC_D_BALANCE_TYPE_ID` |
| `RC_D_BAL_HOLD_ID` | [RC_D_HOLD](RC_D_HOLD.md) | `RC_D_HOLD_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_PROPERTY_ID` | [RC_D_BILL_PROPERTY](RC_D_BILL_PROPERTY.md) | `RC_D_BILL_PROPERTY_ID` |
| `RC_D_ENCNTR_HOLD_ID` | [RC_D_HOLD](RC_D_HOLD.md) | `RC_D_HOLD_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_PRI_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_RESP_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_RESP_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `REG_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `SHR_D_ATTENDING_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

