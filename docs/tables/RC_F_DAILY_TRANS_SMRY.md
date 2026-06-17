# RC_F_DAILY_TRANS_SMRY

> Contains payment, adjustment and charges aggregated at a daily level.

**Description:** Revenue Cycle Fact Daily Transaction Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 45

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `DISCHARGE_MONTH_ID` | DOUBLE | NOT NULL | FK→ | The month the patient who made the transaction was discharged. |
| 3 | `DISCHARGE_YEAR` | DOUBLE | NOT NULL |  | The year the patient who made the transaction was discharged. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 6 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 7 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 8 | `RC_D_ADMIT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the admitting physician in a given location in the fact table. |
| 9 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 10 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 11 | `RC_D_CONSULT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the consulting physician in a given location in the fact table. |
| 12 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter. |
| 13 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 14 | `RC_D_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the GL Alias information associated to the transaction. |
| 15 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan associated the Insurance AR balance or Self-Pay balance that the payment or adjustment was to. |
| 16 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the medical service of the encounter associated to the transaction. |
| 17 | `RC_D_ORDER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the ordering physician in a given location in the fact table. |
| 18 | `RC_D_PAYMENT_METHOD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a Payment Method Dimension Row related to this fact row. |
| 19 | `RC_D_PERFORM_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the performing physician in a given location in the fact table. |
| 20 | `RC_D_REFER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the refering physician in a given location in the fact table. |
| 21 | `RC_D_REND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the rendering physician in a given location in the fact table. |
| 22 | `RC_D_SUPERV_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the supervising physician in a given location in the fact table. |
| 23 | `RC_D_TIER_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the tier group to which a charge has been posted. |
| 24 | `RC_D_TRANSACTION_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the transaction alias related to this fact row. |
| 25 | `RC_D_TRANSACTION_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the transaction location information related to this fact row. |
| 26 | `RC_D_TRANSACTION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a Transaction Type Dimension row realted to this fact row |
| 27 | `RC_F_DAILY_TRANS_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies payments, adjustments and charges aggregated on a daily level. |
| 28 | `SHR_D_ADMIT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the admitting physician for the related fact row. |
| 29 | `SHR_D_ATTEND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the attending physician for the related fact row. |
| 30 | `SHR_D_CONSULT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the consulting physician for the related fact row. |
| 31 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient encounter location at the time the transaction was posted. |
| 32 | `SHR_D_ORDER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the ordering physician for the related fact rows. |
| 33 | `SHR_D_PERFORM_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the performing physician for the related fact row. |
| 34 | `SHR_D_REFER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the referring physician for the related fact row. |
| 35 | `SHR_D_REND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the shared person dimension table that represents the person who was the rendering/primary physician about the related fact row. |
| 36 | `SHR_D_SUPERV_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies supervising physician information related to this fact row. |
| 37 | `TOS_PAYMENT_AMOUNT` | DOUBLE | NOT NULL |  | The total payment amount made on the day the patient is registered to the hospital. |
| 38 | `TOTAL_SERVICE_UNITS` | DOUBLE | NOT NULL |  | Contains the total amount of units associated to an individual charge. |
| 39 | `TOTAL_TRANSACTIONS` | DOUBLE | NOT NULL |  | Contains the total number of transactions represented in this summary row. |
| 40 | `TOTAL_TRANSACTION_AMT` | DOUBLE | NOT NULL |  | Represents the total transaction amount of all the transactions aggregated into the summary row. |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_MONTH_ID` | [SHR_D_MONTH](SHR_D_MONTH.md) | `SHR_D_MONTH_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_ADMIT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_CONSULT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_GL_ALIAS_ID` | [RC_D_GL_ALIAS](RC_D_GL_ALIAS.md) | `RC_D_GL_ALIAS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_ORDER_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_PAYMENT_METHOD_ID` | [RC_D_PAYMENT_METHOD](RC_D_PAYMENT_METHOD.md) | `RC_D_PAYMENT_METHOD_ID` |
| `RC_D_PERFORM_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_REFER_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_REND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_SUPERV_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_TIER_GROUP_ID` | [RC_D_TIER_GROUP](RC_D_TIER_GROUP.md) | `RC_D_TIER_GROUP_ID` |
| `RC_D_TRANSACTION_ALIAS_ID` | [RC_D_TRANSACTION_ALIAS](RC_D_TRANSACTION_ALIAS.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| `RC_D_TRANSACTION_LOCATION_ID` | [RC_D_TRANSACTION_LOCATION](RC_D_TRANSACTION_LOCATION.md) | `RC_D_TRANSACTION_LOCATION_ID` |
| `RC_D_TRANSACTION_TYPE_ID` | [RC_D_TRANSACTION_TYPE](RC_D_TRANSACTION_TYPE.md) | `RC_D_TRANSACTION_TYPE_ID` |
| `SHR_D_ADMIT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ATTEND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CONSULT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_ORDER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PERFORM_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REFER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_SUPERV_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

