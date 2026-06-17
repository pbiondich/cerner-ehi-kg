# RC_F_VAR_LINE_ITEM_SMRY

> Contains the detail data associated to variance for reporting purposes.

**Description:** Revenue Cycle Fact Variance Line Item Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 47

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `ADJUSTED_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the adjusted original variance dollar amount that has been identified for this fact row. |
| 3 | `ADJUSTED_VARIANCE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the adjusted original variance identified date for this fact row. References the key in the omf_date table. |
| 4 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 5 | `APPEAL_CNT` | DOUBLE | NOT NULL |  | Identifies the total number of appeals related to a specific claim. |
| 6 | `CLAIM_BILLED_AMT` | DOUBLE | NOT NULL |  | Contains the dollar amount billed on the claim. |
| 7 | `CLAIM_NBR_IDENT` | VARCHAR(40) |  |  | The claim number related to this fact row. |
| 8 | `CLAIM_SERVICE_ITEM_IDENT` | VARCHAR(50) | NOT NULL |  | The claim service item related to this fact row. |
| 9 | `CURRENT_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the current variance dollar amount that has been identified for this fact row. |
| 10 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the omf_date table. |
| 11 | `EST_CONTRACTUAL_AMT` | DOUBLE | NOT NULL |  | Contains the estimated contractual dollar amount on the claim. |
| 12 | `EST_REIMBURSEMENT_AMT` | DOUBLE | NOT NULL |  | Contains the estimated reimbursement dollar amount on the claim. |
| 13 | `FIN_NBR_IDENT` | VARCHAR(50) |  |  | Contains the financial number alias related to the patient encounter. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 15 | `LAST_APPEAL_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the appeal action code date for this fact row. References the key in the omf_date table. |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 17 | `LAST_VAR_ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | Stores the equivalent date number for the last date/time that the variance activity occurred. |
| 18 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Identifies the related row in the BILL_REC table in the millennium database from which the data for this table was derived. |
| 19 | `MILL_PFT_QUEUE_ITEM_ID` | DOUBLE | NOT NULL |  | Identifies the millennium related queue item for which the history data on the ID was derived. |
| 20 | `MRN_NBR_IDENT` | VARCHAR(50) |  |  | Identifier of a medical record number. |
| 21 | `ORIGINAL_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the first variance dollar amount that has been identified for this fact row. |
| 22 | `ORIG_VARIANCE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the first variance identified date for this fact row. References the key in the omf_date table. |
| 23 | `PATIENT_RESPONSIBILITY_AMT` | DOUBLE | NOT NULL |  | Contains the patient responsibility dollar amount on the claim. |
| 24 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 25 | `RC_D_BILL_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the billing property related to this fact row. |
| 26 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 27 | `RC_D_DENIAL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the denial alias dimension row that is related to this fact row. |
| 28 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class information related to this fact row. |
| 29 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the primary financial class related to this fact row. |
| 30 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 31 | `RC_D_VARIANCE_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the variance attributes related to this fact row. |
| 32 | `RC_D_VARIANCE_ORIGIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related RC_D_VARIANCE_ORIGIN row. |
| 33 | `RC_D_VARIANCE_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the variance attributes related to this fact row. |
| 34 | `RC_F_VAR_LINE_ITEM_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies detail data associated to variance for reporting purposes. |
| 35 | `RECOVERY_AMT` | DOUBLE | NOT NULL |  | Contains the recovery dollar amount on the claim. |
| 36 | `SELF_PAY_BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the last self pay balance dollar amount for this fact row. |
| 37 | `SHR_D_ACTION_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this fact row. |
| 38 | `SHR_D_PATIENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient related to this fact row. |
| 39 | `SHR_D_PATIENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location of the patient. |
| 40 | `SHR_D_QUEUE_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person to whom the responsible financial encounter balance is assigned in a workflow. |
| 41 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total adjustment dollar amount for this claim. |
| 42 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total payment dollar amount for this claim. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADJUSTED_VARIANCE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_APPEAL_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_VAR_ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ORIG_VARIANCE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_PROPERTY_ID` | [RC_D_BILL_PROPERTY](RC_D_BILL_PROPERTY.md) | `RC_D_BILL_PROPERTY_ID` |
| `RC_D_BILL_TYPE_ID` | [RC_D_BILL_TYPE](RC_D_BILL_TYPE.md) | `RC_D_BILL_TYPE_ID` |
| `RC_D_DENIAL_ALIAS_ID` | [RC_D_DENIAL_ALIAS](RC_D_DENIAL_ALIAS.md) | `RC_D_DENIAL_ALIAS_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `RC_D_VARIANCE_ACTION_ID` | [RC_D_VARIANCE_ACTION](RC_D_VARIANCE_ACTION.md) | `RC_D_VARIANCE_ACTION_ID` |
| `RC_D_VARIANCE_ORIGIN_ID` | [RC_D_VARIANCE_ORIGIN](RC_D_VARIANCE_ORIGIN.md) | `RC_D_VARIANCE_ORIGIN_ID` |
| `RC_D_VARIANCE_PROPERTY_ID` | [RC_D_VARIANCE_PROPERTY](RC_D_VARIANCE_PROPERTY.md) | `RC_D_VARIANCE_PROPERTY_ID` |
| `SHR_D_ACTION_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PATIENT_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_PATIENT_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_QUEUE_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

