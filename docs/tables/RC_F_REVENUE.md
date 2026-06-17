# RC_F_REVENUE

> This table contains data related to revenue.

**Description:** Revenue Cycle Fact Revenue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 75

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 3 | `CDM_FULL_IMPL_FAC_RVU_NBR` | DOUBLE |  |  | This field contains the CDM fully implemented facility relative value units associated to a charge. |
| 4 | `CDM_FULL_IMPL_NON_FAC_RVU_NBR` | DOUBLE |  |  | This field contains the CDM fully implemented non-facility relative value units associated to a charge. |
| 5 | `CDM_MALPRACTICE_RVU_NBR` | DOUBLE |  |  | This field contains the CDM malpractice relative value units associated to a charge. |
| 6 | `CDM_RVU_NBR` | DOUBLE |  |  | This field contains the CDM relative value units associated to a charge. |
| 7 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the OMF_DATE table. |
| 8 | `FEDERAL_TAX_ID_NBR` | VARCHAR(100) |  |  | An identifying federal tax number. |
| 9 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 10 | `FULL_IMPL_FAC_RVU_NBR` | DOUBLE |  |  | This field contains the fully implemented facility relative value units associated to a charge. |
| 11 | `FULL_IMPL_NONFAC_RVU_NBR` | DOUBLE |  |  | This field contains the fully implemented non-facility relative value units associated to a charge. |
| 12 | `GL_ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | Contains the GL_ACTIVITY_DT_TM value from GL_TRANS_LOG table. |
| 13 | `GL_CREATED_DT_NBR` | DOUBLE | NOT NULL | FK→ | Contains the GL_CREATED_DT_TM number from the GL_TRANS_LOG table. |
| 14 | `GL_IMPACT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Contains the GL_IMPACT_DT_TM value from GL_TRANS_LOG table. |
| 15 | `GL_INTERFACE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the GL Interface Date. References the key in the OMF_DATE table. |
| 16 | `HCPCS_FULL_IMPL_FAC_RVU_NBR` | DOUBLE |  |  | This field containes the HCPCS fully implemented facility relative value units associated to a charge. |
| 17 | `HCPCS_FULL_IMPL_NONFAC_RVU_NBR` | DOUBLE |  |  | This field contains the HCPCS fully implemented non-facility relative value units associated to a charge. |
| 18 | `HCPCS_MALPRACTICE_RVU_NBR` | DOUBLE |  |  | This field contains the HCPCS malpractice relative value units associated to a charge. |
| 19 | `HCPCS_RVU_NBR` | DOUBLE |  |  | This field contains the HCPCS work relative value units associated to a charge. |
| 20 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 21 | `MALPRACTICE_RVU_NBR` | DOUBLE |  |  | This field contains the malpractice relative value units associated to a charge. |
| 22 | `MILL_GL_TRANS_LOG_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the row on the GL_TRANS_LOG on which this ID originated. |
| 23 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 24 | `MILL_PFT_CHARGE_ID` | DOUBLE | NOT NULL |  | Identifies the Millennium record from which the data on this row was derived. |
| 25 | `PLACE_OF_SERVICE_DESC` | VARCHAR(100) |  |  | Description of the place of service. |
| 26 | `RC_AF_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data related to the RC_F_Revenue table. |
| 27 | `RC_D_ACCOMMODATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies accommodation information related to this fact row. |
| 28 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies account information related to this fact. |
| 29 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 30 | `RC_D_ADMIT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the admitting physician in a given location in the fact table. |
| 31 | `RC_D_AR_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies gl alias information such as company name and account name for the records with an account type of AR. |
| 32 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 33 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 34 | `RC_D_BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill item related to this fact row. |
| 35 | `RC_D_CONSULT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the consulting physician in a given location in the fact table. |
| 36 | `RC_D_CPT_MODIFIER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related CPT Modifier |
| 37 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies encounter type class information related to this fact row. |
| 38 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 39 | `RC_D_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the GL Alias related to this fact row. |
| 40 | `RC_D_HCPCS_MODIFIER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related HCPCS Modifier. |
| 41 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 42 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 43 | `RC_D_ORDER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the ordering physician in a given location in the fact table. |
| 44 | `RC_D_PERFORM_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the performing physician in a given location in the fact table. |
| 45 | `RC_D_REFER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the refering physician in a given location in the fact table. |
| 46 | `RC_D_REND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the rendering physician in a given location in the fact table. |
| 47 | `RC_D_SUPERV_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the supervising physician in a given location in the fact table. |
| 48 | `RC_D_TIER_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the tier group related to the charge. |
| 49 | `RC_D_TRANSACTION_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the transaction alias information related to this fact row. |
| 50 | `RC_D_TRANSACTION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a Transaction Type Dimension row realted to this fact row |
| 51 | `RC_F_REVENUE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data related to revenue. |
| 52 | `RELATIVE_VALUE_UNITS_QTY` | DOUBLE | NOT NULL |  | Contains the workload units associated to a charge. |
| 53 | `SERVICE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the service date. References the key in the OMF_DATE table. |
| 54 | `SERVICE_FACILITY_NAME` | VARCHAR(100) |  |  | Contains the name of the service facility |
| 55 | `SHR_D_ADMIT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the admitting physician for the related fact row. |
| 56 | `SHR_D_ATTEND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies attending physician information related to this fact row. |
| 57 | `SHR_D_CONSULT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the consulting physician for the related fact row. |
| 58 | `SHR_D_CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifier the person related to this fact row who created this information. |
| 59 | `SHR_D_ORDER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies ordering physician information related to this fact row. |
| 60 | `SHR_D_PATIENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location of the patient. |
| 61 | `SHR_D_PERFORMING_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Contains a number to identify the performing location. |
| 62 | `SHR_D_PERFORM_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies performing physician information related to this fact row. |
| 63 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies person information related to this fact row. |
| 64 | `SHR_D_REFER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies referring physician information related to this fact row. |
| 65 | `SHR_D_REND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the shared person dimension table that represents the person who was the rendering/primary physician about the related fact row. |
| 66 | `SHR_D_SUPERV_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies supervising physician information related to this fact row. |
| 67 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 68 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | The total of the charges. |
| 69 | `TOTAL_QTY` | DOUBLE | NOT NULL |  | The total quantity. |
| 70 | `UNIT_PRICE_AMT` | DOUBLE | NOT NULL |  | Unit price for the charge. |
| 71 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 72 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 73 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 74 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 75 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `GL_ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `GL_CREATED_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `GL_IMPACT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `GL_INTERFACE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_AF_PATIENT_AR_BALANCE_ID` | [RC_AF_PATIENT_AR_BALANCE](RC_AF_PATIENT_AR_BALANCE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| `RC_D_ACCOMMODATION_ID` | [RC_D_ACCOMMODATION](RC_D_ACCOMMODATION.md) | `RC_D_ACCOMMODATION_ID` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_ADMIT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_AR_GL_ALIAS_ID` | [RC_D_GL_ALIAS](RC_D_GL_ALIAS.md) | `RC_D_GL_ALIAS_ID` |
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
| `RC_D_TRANSACTION_ALIAS_ID` | [RC_D_TRANSACTION_ALIAS](RC_D_TRANSACTION_ALIAS.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| `RC_D_TRANSACTION_TYPE_ID` | [RC_D_TRANSACTION_TYPE](RC_D_TRANSACTION_TYPE.md) | `RC_D_TRANSACTION_TYPE_ID` |
| `SERVICE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `SHR_D_ADMIT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ATTEND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CONSULT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CREATED_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ORDER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PATIENT_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERFORMING_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERFORM_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REFER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_SUPERV_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

