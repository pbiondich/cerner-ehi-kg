# RC_F_VARIANCE

> Contains the detail data associated to variance for reporting purposes.

**Description:** Revenue Cycle Fact Variance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 57

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date and time of the charge. |
| 3 | `ACTUAL_REIMBURSEMENT_AMT` | DOUBLE | NOT NULL |  | The actual amount of the reimbursement. |
| 4 | `ADJUSTED_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the adjusted original variance dollar amount that has been identified for this fact row. |
| 5 | `ADJUSTED_VARIANCE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the adjusted original variance identified date for this fact row. References the key in the omf_date table. |
| 6 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 7 | `APPEAL_IND` | DOUBLE | NOT NULL |  | An indicator that will be set to true only for the queue item ids that represent an appeal. |
| 8 | `BILLED_AMT` | DOUBLE | NOT NULL |  | The amount billed |
| 9 | `CLAIM_NBR_IDENT` | VARCHAR(50) |  |  | The claim number related to this fact row. |
| 10 | `CLAIM_SERVICE_ITEM_IDENT` | VARCHAR(50) |  |  | The claim service item related to this fact row. |
| 11 | `CLAIM_TRANSMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the claim transmission date. References the key in the OMF_DATE table. |
| 12 | `CPT` | VARCHAR(200) |  |  | This will store the CPT information. |
| 13 | `CURRENT_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the current variance dollar amount that has been identified for this fact row. |
| 14 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the OMF_DATE table. |
| 15 | `EST_CONTRACTUAL_AMT` | DOUBLE | NOT NULL |  | Contains the estimated contractual dollar amount on the claim. |
| 16 | `EST_REIMBURSEMENT_AMT` | DOUBLE | NOT NULL |  | Contains the estimated reimbursement dollar amount on the claim. |
| 17 | `FIN_NBR_IDENT` | VARCHAR(50) |  |  | identifier of a financial number. |
| 18 | `LAST_PAYMENT_AMT` | DOUBLE | NOT NULL |  | The last payment amount on the ProFit encounter. |
| 19 | `LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date of the last time a payment was made to the financial encounter. Related to the OMF_DATE table. |
| 20 | `LAST_VAR_ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | Stores the equivalent date number for the last date/time that the variance activity occurred. |
| 21 | `LAST_VAR_ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Stores the data and time of the last variance activity. |
| 22 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row in the BILL_REC table on the Millennium data base from which this data was derived. |
| 23 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 24 | `MILL_PFT_QUEUE_ITEM_ID` | DOUBLE | NOT NULL |  | Identifies the millennium related queue item for which the history data on the ID was derived. |
| 25 | `MILL_PFT_QUEUE_ITEM_WF_HIST_ID` | DOUBLE | NOT NULL |  | Identifies the millennium related workflow history for which the history data on the ID was derived. |
| 26 | `MRN_NBR_IDENT` | VARCHAR(50) |  |  | Identifier of a medical record number. |
| 27 | `ORIGINAL_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Contains the first variance dollar amount that has been identified for this fact row. |
| 28 | `ORIG_VARIANCE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the first variance identified date for this fact row. References the key in the omf_date table. |
| 29 | `PATIENT_RESPONSIBILITY_AMT` | DOUBLE | NOT NULL |  | Contains the patient responsibility dollar amount on the claim. |
| 30 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 31 | `RC_D_BILL_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data associated to claim attributes for reporting purposes. |
| 32 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 33 | `RC_D_DENIAL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related RC_D_DENIAL_ALIAS row. |
| 34 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data related to the clinical encounter type and class. |
| 35 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 36 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 37 | `RC_D_VARIANCE_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data associated to variance attributes for Reporting purposes. |
| 38 | `RC_D_VARIANCE_ORIGIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related RC_D_VARIANCE_ORIGIN row. |
| 39 | `RC_D_VARIANCE_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data associated to variance attributes for reporting purposes. |
| 40 | `RC_F_VARIANCE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data associated to a variance for reporting purposes. |
| 41 | `RECOVERY_AMT` | DOUBLE | NOT NULL |  | Contains the recovery dollar amount on the claim. |
| 42 | `SELF_PAY_BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the last self pay balance dollar amount for this fact row. |
| 43 | `SELF_PAY_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the selfpay payment dollar amount on the claim. |
| 44 | `SHR_D_ACTION_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this fact row. |
| 45 | `SHR_D_PATIENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient related to this fact row. |
| 46 | `SHR_D_PATIENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location of the patient. |
| 47 | `SHR_D_QUEUE_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person to whom the responsible financial encounter balance is assigned in a workflow. |
| 48 | `SHR_D_REND_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | This will store the related rendering physician ID from the shr_d_person table. Will be used to obtain the rendering physician name. |
| 49 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 50 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the adjustments of this balance fact row. |
| 51 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total payment dollar amount for this claim. |
| 52 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `VARIANCE_SEQUENCE` | DOUBLE | NOT NULL |  | A sequence number that uniquely identifies the sequence on actions on a particular variance. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADJUSTED_VARIANCE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `CLAIM_TRANSMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
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
| `SHR_D_REND_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

