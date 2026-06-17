# RX_HEALTH_PLAN

> Store Pharmacy specific attributes of Health Plan.

**Description:** RX HEALTH PLAN  
**Table type:** REFERENCE  
**Primary key:** `HEALTH_PLAN_ID`  
**Columns:** 37  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of identifiers (i.e., numbers). The alias pool code also determines the accept display format for the unique set of identifiers. |
| 2 | `ALT_OTHER_PAYER_NAME` | VARCHAR(10) |  |  | Alternate Other Payer for a specific health plan when coordination of benefits is used. |
| 3 | `BRAND_COPAY` | DOUBLE |  |  | Prescription copay amount for Brand products for a specific health plan |
| 4 | `BRAND_COPAY_PERCENT` | DOUBLE |  |  | Prescription copay percent amount for Brand products for a specific health plan |
| 5 | `CLAIM_CNT` | DOUBLE |  |  | Claim Count |
| 6 | `CLAIM_FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies an overall claim format for a specific health plan or a single ingredient format |
| 7 | `CLAIM_VALIDATION_CD` | DOUBLE | NOT NULL | FK→ | Identifies an overall claim validation for a specific health plan |
| 8 | `CMPD_CLAIM_CNT` | DOUBLE |  |  | maximum number of compound prescriptions allowed per Claim Transmission |
| 9 | `CMPD_ING_CNT` | DOUBLE |  |  | maximum number of ingredients allowed in a compound prescription |
| 10 | `COB_OTHER_PAYER_IND` | DOUBLE | NOT NULL |  | indicates Both the patient responsibility and the other payer amount should be sent in a claim request. 0 = Not send Both together, 1 = Send Both together |
| 11 | `COB_PATIENT_RESP_IND` | DOUBLE | NOT NULL |  | Indicates if the Patient Responsibility or the Other Payer Amount should be sent in a claim request. 0 = Other Payer, 1 = Patient Responsibility |
| 12 | `COB_SUBMISSION_TYPE_CD` | DOUBLE | NOT NULL |  | Coordination of benefits segment type used to submit claims. |
| 13 | `COB_TYPE_CD` | DOUBLE | NOT NULL |  | Co-ordination of benefits participation type |
| 14 | `COMPOUND_FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies a compound claim format for a specific health plan |
| 15 | `COPAY` | DOUBLE |  |  | Prescription copay amount for a specific health plan |
| 16 | `COPAY_OVERRIDE_IND` | DOUBLE |  |  | Copay override ind |
| 17 | `COPAY_PERCENT` | DOUBLE |  |  | Prescription copay percent for a specific health plan |
| 18 | `GENERIC_COPAY` | DOUBLE |  |  | Prescription copay amount for generic products for a specific health plan |
| 19 | `GENERIC_COPAY_PERCENT` | DOUBLE |  |  | Prescription copay percent amount for generic products for a specific health plan |
| 20 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | PK FK→ | ID generated for unique health plans. |
| 21 | `INCLUDE_INVESTIGATIONAL_IND` | DOUBLE |  |  | Indicator (0,1). Indicates whether or not to include investigational drugs on prescription claims. |
| 22 | `INCLUDE_OTC_IND` | DOUBLE |  |  | Indicator (0,1). Indicates whether or not to include Over-The-Counter drugs on prescription claims. |
| 23 | `INPATIENT_BILLING_FLAG` | DOUBLE | NOT NULL |  | Indicates that the health plan supports billing Inpatient dispenses via Outpatient claims |
| 24 | `OTH_PAYR_PAT_RESP_AMT_SUM_IND` | DOUBLE | NOT NULL |  | Indicates whether the current health plan expects all the Other Payer-Patient Responsibility Amount to be summed and sent under NQ with qualifier of NP=06. |
| 25 | `PARTIAL_FILL_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates if a health plan supports NCPDP 51 Partial Fill Submission Process. |
| 26 | `PRESCRIPTION_IND` | DOUBLE | NOT NULL |  | Indicates if the health plan is a prescription plan |
| 27 | `PRICE_CODE_CD` | DOUBLE | NOT NULL | FK→ | Identifies a price code for a health plan |
| 28 | `PROC_CONTROL_NUMBER` | CHAR(20) |  |  | Proc control number |
| 29 | `PRSNL_ALIAS_CD` | DOUBLE | NOT NULL |  | Personnel alias code |
| 30 | `TWO_STEP_DISPENSE_IND` | DOUBLE | NOT NULL |  | This column defines whether the orders should follow two step dispense process |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `USE_ALT_OTHER_PAYER_IND` | DOUBLE | NOT NULL |  | Indicates whether the Alternate Other Payer is selected or not when Coordination of Benefits is used. |
| 37 | `VENDOR_CERT_NBR_TXT` | CHAR(10) |  |  | An external ID assigned by the switch or processor to identify the software source. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLAIM_VALIDATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PRICE_CODE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RX_CLAIM_PENDING](RX_CLAIM_PENDING.md) | `HEALTH_PLAN_ID` |
| [RX_HEALTH_PLAN_CLAIM](RX_HEALTH_PLAN_CLAIM.md) | `HEALTH_PLAN_ID` |
| [RX_HEALTH_PLAN_SERV_RES_R](RX_HEALTH_PLAN_SERV_RES_R.md) | `HEALTH_PLAN_ID` |

