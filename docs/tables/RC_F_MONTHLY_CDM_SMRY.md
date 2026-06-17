# RC_F_MONTHLY_CDM_SMRY

> Contains charges aggregated by CDM at a Monthly level.

**Description:** Revenue Cycle Fact Monthly CDM Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 55

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_YEAR` | DOUBLE | NOT NULL |  | Contains the year in which the activity took place. |
| 2 | `CDM_FULL_IMPL_FAC_RVU_NBR` | DOUBLE |  |  | This field contains the CDM fully implemented facility relative value units associated to a charge. |
| 3 | `CDM_FULL_IMPL_NON_FAC_RVU_NBR` | DOUBLE |  |  | This field contains the CDM fully implemented non-facility relative value units associated to a charge. |
| 4 | `CDM_MALPRACTICE_RVU_NBR` | DOUBLE |  |  | This field contains the CDM malpractice relative value units associated to a charge. |
| 5 | `CDM_RVU_NBR` | DOUBLE |  |  | This field contains the cdm relative value units associated to a charge. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 7 | `FULL_IMPL_FAC_RVU_NBR` | DOUBLE |  |  | This field contains the fully implemented facility relative value units associated to a charge. |
| 8 | `FULL_IMPL_NONFAC_RVU_NBR` | DOUBLE |  |  | This field contains the fully implemented non-facility relative value unites associated to a charge. |
| 9 | `HCPCS_FULL_IMPL_FAC_RVU_NBR` | DOUBLE |  |  | This field containes the HCPCS fully implemented facility relative value units associated to a charge. |
| 10 | `HCPCS_FULL_IMPL_NONFAC_RVU_NBR` | DOUBLE |  |  | This field contains the HCPCS fully implemented non-facility relative value units associated to a charge. |
| 11 | `HCPCS_MALPRACTICE_RVU_NBR` | DOUBLE |  |  | This field contains the HCPCS malpractice relative value units associated to a charge. |
| 12 | `HCPCS_RVU_NBR` | DOUBLE |  |  | This field contains the HCPCS work relative value units associated to a charge. |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 14 | `MALPRACTICE_RVU_NBR` | DOUBLE |  |  | This field contains the malpractice relative value units associated to a charge. |
| 15 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 16 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related account type. |
| 17 | `RC_D_ADMIT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the admitting physician in a given location in the fact table. |
| 18 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 19 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity associated to the encounter associated to this CDM summary record. |
| 20 | `RC_D_BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill item related to this fact row. |
| 21 | `RC_D_CONSULT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the consulting physician in a given location in the fact table. |
| 22 | `RC_D_CPT_MODIFIER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related CPT Modifier |
| 23 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter associated to this fact row. |
| 24 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class of the health plan associated to this fact row. |
| 25 | `RC_D_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the GL Alias information associated to this fact row. |
| 26 | `RC_D_HCPCS_MODIFIER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related HCPCS Modifier. |
| 27 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan associated to this fact row. |
| 28 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the medical service of the encounter associated to this fact row. |
| 29 | `RC_D_ORDER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the ordering physician in a given location in the fact table. |
| 30 | `RC_D_PERFORM_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the performing physician in a given location in the fact table. |
| 31 | `RC_D_REFER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the refering physician in a given location in the fact table. |
| 32 | `RC_D_REND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the rendering physician in a given location in the fact table. |
| 33 | `RC_D_SUPERV_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the supervising physician in a given location in the fact table. |
| 34 | `RC_D_TIER_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the tier group related to this fact row. |
| 35 | `RC_F_MONTHLY_CDM_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies charges by CDM aggregated at a Monthly level. |
| 36 | `RELATIVE_VALUE_UNITS_QTY` | DOUBLE | NOT NULL |  | Workload units associated to a charge. |
| 37 | `SHR_D_ADMIT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the admitting physician for the related fact row. |
| 38 | `SHR_D_ATTEND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the attending physician for the related fact row. |
| 39 | `SHR_D_CONSULT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the consulting physician for the related fact row. |
| 40 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient encounter location related to this fact row. |
| 41 | `SHR_D_MONTH_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the month related to this fact row. |
| 42 | `SHR_D_ORDER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the ordering physician for the related fact rows. |
| 43 | `SHR_D_PERFORM_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the performing physician for the related fact row. |
| 44 | `SHR_D_REFER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the referring physician for the related fact row. |
| 45 | `SHR_D_REND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the shared person dimension table that represents the person who was the rendering/primary physician about the related fact row. |
| 46 | `SHR_D_SUPERV_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies supervising physician information related to this fact row. |
| 47 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | Represents the total transaction amount of all the transactions aggregated into the summary row. |
| 48 | `TOTAL_SERVICE_UNITS` | DOUBLE | NOT NULL |  | The total amount of units associated to an individual charge. |
| 49 | `TOTAL_TRANSACTIONS` | DOUBLE | NOT NULL |  | The total number of transactions represented in this summary row. |
| 50 | `UNIT_PRICE_AMT` | DOUBLE | NOT NULL |  | The price per unit for the charge. |
| 51 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_ADMIT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_ITEM_ID` | [RC_D_BILL_ITEM](RC_D_BILL_ITEM.md) | `RC_D_BILL_ITEM_ID` |
| `RC_D_CONSULT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_CPT_MODIFIER_ID` | [RC_D_BILL_ITEM_MODIFIER](RC_D_BILL_ITEM_MODIFIER.md) | `RC_D_BILL_ITEM_MODIFIER_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_GL_ALIAS_ID` | [RC_D_GL_ALIAS](RC_D_GL_ALIAS.md) | `RC_D_GL_ALIAS_ID` |
| `RC_D_HCPCS_MODIFIER_ID` | [RC_D_BILL_ITEM_MODIFIER](RC_D_BILL_ITEM_MODIFIER.md) | `RC_D_BILL_ITEM_MODIFIER_ID` |
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
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_MONTH_ID` | [SHR_D_MONTH](SHR_D_MONTH.md) | `SHR_D_MONTH_ID` |
| `SHR_D_ORDER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PERFORM_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REFER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_SUPERV_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

