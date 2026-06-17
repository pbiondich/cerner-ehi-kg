# RC_F_VAR_CLAIM_SMRY

> Contains the detail data associated to variance for reporting purposes.

**Description:** Revenue Cycle Fact Variance Claim Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 50

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 6 | `ADJUSTED_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the adjusted original variance dollar amount that has been identified for this fact row. |
| 7 | `ADJUSTED_VARIANCE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the adjusted original variance identified date for this fact row. References the key in the omf_date table. |
| 8 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 9 | `APPEAL_CNT` | DOUBLE | NOT NULL |  | Identifies the total number of appeals related to a specific claim. |
| 10 | `BILLED_AMT` | DOUBLE | NOT NULL |  | Contains the dollar amount billed on the claim. |
| 11 | `CLAIM_NBR_IDENT` | VARCHAR(40) |  |  | The claim number related to this fact row. |
| 12 | `CURRENT_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the current variance dollar amount that has been identified for this fact row. |
| 13 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the omf_date table. |
| 14 | `EST_CONTRACTUAL_AMT` | DOUBLE | NOT NULL |  | Contains the estimated contractual dollar amount on the claim. |
| 15 | `EST_REIMBURSEMENT_AMT` | DOUBLE | NOT NULL |  | Contains the estimated reimbursement dollar amount on the claim. |
| 16 | `FIN_NBR_IDENT` | VARCHAR(50) |  |  | Contains the financial number alias related to the patient encounter. |
| 17 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 18 | `LAST_APPEAL_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the appeal action code date for this fact row. References the key in the omf_date table. |
| 19 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 20 | `LAST_VAR_ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | Stores the equivalent date number for the last date/time that the variance activity occurred. |
| 21 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Number that identifies the row in the Bill_Rec Millennium database table from which this row was derived. |
| 22 | `MILL_PFT_QUEUE_ITEM_ID` | DOUBLE | NOT NULL |  | Identifies the millennium related queue item for which the history data on the ID was derived. |
| 23 | `MRN_NBR_IDENT` | VARCHAR(50) |  |  | Identifier of a medical record number. |
| 24 | `ORIGINAL_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the first variance dollar amount that has been identified for this fact row. |
| 25 | `ORIG_VARIANCE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the first variance identified date for this fact row. References the key in the omf_date table. |
| 26 | `PATIENT_RESPONSIBILITY_AMT` | DOUBLE | NOT NULL |  | Contains the patient responsibility dollar amount on the claim. |
| 27 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 28 | `RC_D_BILL_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the billing property related to this fact row. |
| 29 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 30 | `RC_D_DENIAL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the denial alias dimension row that is related to this fact row. |
| 31 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class information related to this fact row. |
| 32 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the primary financial class related to this fact row. |
| 33 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 34 | `RC_D_VARIANCE_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the variance attributes related to this fact row. |
| 35 | `RC_D_VARIANCE_ORIGIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related RC_D_VARIANCE_ORIGIN row. |
| 36 | `RC_D_VARIANCE_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the variance attributes related to this fact row. |
| 37 | `RC_F_VAR_CLAIM_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies detail data associated to variance for reporting purposes. |
| 38 | `RECOVERY_AMT` | DOUBLE | NOT NULL |  | Contains the recovery dollar amount on the claim. |
| 39 | `SELF_PAY_BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the last self pay balance dollar amount for this fact row. |
| 40 | `SHR_D_ACTION_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this fact row. |
| 41 | `SHR_D_PATIENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient related to this fact row. |
| 42 | `SHR_D_PATIENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location of the patient. |
| 43 | `SHR_D_QUEUE_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person to whom the responsible financial encounter balance is assigned in a workflow. |
| 44 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total adjustment dollar amount for this claim. |
| 45 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total payment dollar amount for this claim. |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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

