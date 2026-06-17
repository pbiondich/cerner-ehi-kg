# RC_F_ADJUSTMENT

> This table contains data related to adjustments.

**Description:** Revenue Cycle Fact Adjustment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 63

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 3 | `BATCH_CREATED_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the date the batch was created. References the key in the OMF_DATE table. |
| 4 | `BILL_NUMBER_IDENT` | VARCHAR(40) | NOT NULL |  | Contains the display value associated to a bill number. |
| 5 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the discharge date. References the key in the OMF_DATE table. |
| 6 | `FEDERAL_TAX_ID_NBR` | VARCHAR(100) |  |  | An identifying federal tax number. |
| 7 | `FIN_NBR_IDENT` | VARCHAR(50) |  |  | Identifier of Financial Number |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 9 | `GL_ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | Contains the GL_ACTIVITY_DT_TM value from GL_TRANS_LOG table. |
| 10 | `GL_CREATED_DT_NBR` | DOUBLE | NOT NULL | FK→ | Contains the GL_CREATED_DT_TM number from the GL_TRANS_LOG table. |
| 11 | `GL_IMPACT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Contains the GL_IMPACT_DT_TM value from GL_TRANS_LOG table. |
| 12 | `INTERFACE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the interface date. References the key in the OMF_DATE table. |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 14 | `MILL_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row in the PFT_TRANS_RELTN table on the Millennium data base from which this data was derived. |
| 15 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row in the BILL_REC table on the Millennium data base from which this data was derived. |
| 16 | `MILL_GL_TRANS_LOG_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related record on the GL_TRANS_LOG table. |
| 17 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 18 | `MILL_PFT_CHARGE_ID` | DOUBLE | NOT NULL |  | Identifies the Millennium record from which the data on this row was derived. |
| 19 | `MRN_NBR_IDENT` | VARCHAR(50) |  |  | Identifier of Medical Record Number |
| 20 | `PLACE_OF_SERVICE_DESC` | VARCHAR(100) |  |  | Description of the place of service. |
| 21 | `POST_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the post date. References the key in the OMF_DATE table. |
| 22 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies account information related to this fact. |
| 23 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 24 | `RC_D_ADMIT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the admitting physician in a given location in the fact table. |
| 25 | `RC_D_AR_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies gl alias information such as company name and account name for the records with an account type of AR. |
| 26 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 27 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 28 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 29 | `RC_D_CONSULT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the consulting physician in a given location in the fact table. |
| 30 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter associated to the payment. |
| 31 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 32 | `RC_D_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the GL Alias related to this fact row. |
| 33 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 34 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information such as type or category, that the patient is receiving in relation to their encounter. |
| 35 | `RC_D_ORDER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the ordering physician in a given location in the fact table. |
| 36 | `RC_D_PERFORM_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the performing physician in a given location in the fact table. |
| 37 | `RC_D_REFER_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the refering physician in a given location in the fact table. |
| 38 | `RC_D_REND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the rendering physician in a given location in the fact table. |
| 39 | `RC_D_SUPERV_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the supervising physician in a given location in the fact table. |
| 40 | `RC_D_TRANSACTION_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the transaction alias related to this fact row. |
| 41 | `RC_D_TRANSACTION_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the transaction batch related to this fact row. |
| 42 | `RC_D_TRANSACTION_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the transaction location information related to this fact row. |
| 43 | `RC_D_TRANSACTION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a Transaction Type Dimension row realted to this fact row |
| 44 | `RC_F_ADJUSTMENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data related to adjustments. |
| 45 | `SERVICE_FACILITY_NAME` | VARCHAR(100) |  |  | The name of the facility where service was performed. |
| 46 | `SHR_D_ADMIT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the admitting physician for the related fact row. |
| 47 | `SHR_D_ATTEND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the attending physician for the related fact row. |
| 48 | `SHR_D_CONSULT_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the consulting physician for the related fact row. |
| 49 | `SHR_D_ORDER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the ordering physician for the related fact rows. |
| 50 | `SHR_D_PATIENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related patient location |
| 51 | `SHR_D_PERFORM_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the performing physician for the related fact row. |
| 52 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies person information related to this fact row. |
| 53 | `SHR_D_POSTING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the person who posted the information related to this fact row. |
| 54 | `SHR_D_REFER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the referring physician for the related fact row. |
| 55 | `SHR_D_REND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the shared person dimension table that represents the person who was the rendering/primary physician about the related fact row. |
| 56 | `SHR_D_SUPERV_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who was the supervising physician for the related fact table. |
| 57 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 58 | `TRANSACTION_AMT` | DOUBLE | NOT NULL |  | Contains the dollar amount associated to a transaction. |
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
| `GL_ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `GL_CREATED_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `GL_IMPACT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `INTERFACE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `POST_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_ADMIT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_AR_GL_ALIAS_ID` | [RC_D_GL_ALIAS](RC_D_GL_ALIAS.md) | `RC_D_GL_ALIAS_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_TYPE_ID` | [RC_D_BILL_TYPE](RC_D_BILL_TYPE.md) | `RC_D_BILL_TYPE_ID` |
| `RC_D_CONSULT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_GL_ALIAS_ID` | [RC_D_GL_ALIAS](RC_D_GL_ALIAS.md) | `RC_D_GL_ALIAS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_ORDER_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_PERFORM_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_REFER_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_REND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_SUPERV_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_TRANSACTION_ALIAS_ID` | [RC_D_TRANSACTION_ALIAS](RC_D_TRANSACTION_ALIAS.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| `RC_D_TRANSACTION_BATCH_ID` | [RC_D_TRANSACTION_BATCH](RC_D_TRANSACTION_BATCH.md) | `RC_D_TRANSACTION_BATCH_ID` |
| `RC_D_TRANSACTION_LOCATION_ID` | [RC_D_TRANSACTION_LOCATION](RC_D_TRANSACTION_LOCATION.md) | `RC_D_TRANSACTION_LOCATION_ID` |
| `RC_D_TRANSACTION_TYPE_ID` | [RC_D_TRANSACTION_TYPE](RC_D_TRANSACTION_TYPE.md) | `RC_D_TRANSACTION_TYPE_ID` |
| `SHR_D_ADMIT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ATTEND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CONSULT_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ORDER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PATIENT_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERFORM_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_POSTING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REFER_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_REND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_SUPERV_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

