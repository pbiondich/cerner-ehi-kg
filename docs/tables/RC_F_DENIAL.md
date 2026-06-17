# RC_F_DENIAL

> This table contains data related to denials (remark codes) applied to transactions.

**Description:** Revenue Cycle Fact Denial  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total adjustment amount made to claim associated to the denial. |
| 2 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 3 | `BILL_NUMBER_IDENT` | VARCHAR(40) | NOT NULL |  | Contains the display value associated to a bill number. |
| 4 | `CLAIM_BILLED_AMT` | DOUBLE | NOT NULL |  | Contains the total amount of the claim billed to payor for the claim associated to the denial. |
| 5 | `DENIAL_BILLED_AMT` | DOUBLE | NOT NULL |  | Contains the dollar amount denied. |
| 6 | `DENIAL_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the denial date. References the key in the OMF_DATE table. |
| 7 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the OMF_DATE table. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 10 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the millennium database claim to which the denial fact information is related. |
| 11 | `MILL_DENIAL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the Denial table in the Millennium from which this data is derived. |
| 12 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 13 | `PATIENT_LIABILITY_AMT` | DOUBLE | NOT NULL |  | Contains the dollar amount tied to a patient liability remark. |
| 14 | `PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total payment amount made to the claim associated to the denial. |
| 15 | `RC_AF_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data related to the RC_F_Denial table. |
| 16 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity associated to the encounter associated to this denial. |
| 17 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 18 | `RC_D_DENIAL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the denial alias dimension row that is related to this fact row. |
| 19 | `RC_D_DRG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the DRG associated tot the encounter for which the denial is posted. |
| 20 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter associated to this denial. |
| 21 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class of the health plan associated to the claim for which this denial was posted. |
| 22 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 23 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the medical service of the encounter associated to this denial. |
| 24 | `RC_D_TRANSACTION_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the remittance batch from which this denial was posted. |
| 25 | `RC_F_DENIAL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data related to denials applied to transactions. |
| 26 | `SHR_D_ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending physician associated with this denial. |
| 27 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient encounter location at the time the denial was posted. |
| 28 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient associated with this denial. |
| 29 | `SHR_D_POSTED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person who posted this denial. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DENIAL_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_AF_PATIENT_AR_BALANCE_ID` | [RC_AF_PATIENT_AR_BALANCE](RC_AF_PATIENT_AR_BALANCE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_TYPE_ID` | [RC_D_BILL_TYPE](RC_D_BILL_TYPE.md) | `RC_D_BILL_TYPE_ID` |
| `RC_D_DENIAL_ALIAS_ID` | [RC_D_DENIAL_ALIAS](RC_D_DENIAL_ALIAS.md) | `RC_D_DENIAL_ALIAS_ID` |
| `RC_D_DRG_ID` | [RC_D_DRG](RC_D_DRG.md) | `RC_D_DRG_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_TRANSACTION_BATCH_ID` | [RC_D_TRANSACTION_BATCH](RC_D_TRANSACTION_BATCH.md) | `RC_D_TRANSACTION_BATCH_ID` |
| `SHR_D_ATTENDING_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_POSTED_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

