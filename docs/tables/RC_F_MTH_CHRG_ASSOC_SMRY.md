# RC_F_MTH_CHRG_ASSOC_SMRY

> A table that has monthly summarized payment and adjustment amoujnts related to a charge for each physician.

**Description:** Revenue Cycle Fact Monthly Charge Association Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 2 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 3 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Represents the transaction's logical domain. |
| 4 | `RC_D_ADMIT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the admitting physician in a given location in the fact table. |
| 5 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 6 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 7 | `RC_D_BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies Bill Item information such as activity type and charge description. |
| 8 | `RC_D_CONSULT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the consulting physician in a given location in the fact table. |
| 9 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data related to the clinical encounter type and class. |
| 10 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 11 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 12 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 13 | `RC_D_ORDER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the ordering physician in a given location in the fact table. |
| 14 | `RC_D_PERFORM_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the performing physician in a given location in the fact table. |
| 15 | `RC_D_REFER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the refering physician in a given location in the fact table. |
| 16 | `RC_D_REND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the rendering physician in a given location in the fact table. |
| 17 | `RC_D_SUPERV_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the supervising physician in a given location in the fact table. |
| 18 | `RC_D_TIER_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the tier group related to the charge. |
| 19 | `RC_F_MTH_CHRG_ASSOC_SMRY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_F_MTH_CHRG_ASSOC_SMRY table. |
| 20 | `SERVICE_YEAR` | DOUBLE | NOT NULL |  | The year of service |
| 21 | `SHR_D_ADMIT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the admitting physician for the related fact row. |
| 22 | `SHR_D_ATTEND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the attending physician for the related fact row. |
| 23 | `SHR_D_CONSULT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the consulting physician for the related fact row. |
| 24 | `SHR_D_ORDER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the ordering physician for the related fact rows. |
| 25 | `SHR_D_PATIENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location of the patient. |
| 26 | `SHR_D_PERFORM_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the performing physician for the related fact row. |
| 27 | `SHR_D_REFER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the referring physician for the related fact row. |
| 28 | `SHR_D_REND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the shared person dimension table that represents the person who was the rendering/primary physician about the related fact row. |
| 29 | `SHR_D_SERVICE_MONTH_ID` | DOUBLE | NOT NULL | FK→ | Contains the month of service. |
| 30 | `SHR_D_SUPERV_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies supervising physician information related to this fact row. |
| 31 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the adjustments. |
| 32 | `TOTAL_ADJUSTMENT_COUNT` | DOUBLE | NOT NULL |  | The total count of the adjustments. |
| 33 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | The total of the charges. |
| 34 | `TOTAL_CHARGE_COUNT` | DOUBLE | NOT NULL |  | The total count of the charges. |
| 35 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total amount of the payments. |
| 36 | `TOTAL_PAYMENT_COUNT` | DOUBLE | NOT NULL |  | The total amount of the payments |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MILL_LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `RC_D_ADMIT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_ITEM_ID` | [RC_D_BILL_ITEM](RC_D_BILL_ITEM.md) | `RC_D_BILL_ITEM_ID` |
| `RC_D_CONSULT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_ORDER_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_PERFORM_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_REFER_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_REND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_SUPERV_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_TIER_GROUP_ID` | [RC_D_TIER_GROUP](RC_D_TIER_GROUP.md) | `RC_D_TIER_GROUP_ID` |
| `SHR_D_ADMIT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ATTEND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CONSULT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ORDER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PATIENT_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERFORM_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REFER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_SERVICE_MONTH_ID` | [SHR_D_MONTH](SHR_D_MONTH.md) | `SHR_D_MONTH_ID` |
| `SHR_D_SUPERV_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

