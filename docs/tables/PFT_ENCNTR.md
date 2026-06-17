# PFT_ENCNTR

> pft encounter

**Description:** ProFit's Encounter Table  
**Table type:** ACTIVITY  
**Primary key:** `PFT_ENCNTR_ID`  
**Columns:** 103  
**Referenced by:** 25 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | Candidate key reference to an account. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ADJUSTMENT_BALANCE` | DOUBLE |  |  | Total amount of adjustments posted to this pft_encntr. |
| 7 | `ADJ_BAL_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit flag for the adjustment balance. |
| 8 | `ALIAS_SEQ` | DOUBLE |  |  | Current alias sequence according to Patient Accounting |
| 9 | `APPLIED_PAYMENT_BALANCE` | DOUBLE |  |  | Total amount of payments posted to the ProFit Encounter. |
| 10 | `BAD_DEBT_BALANCE` | DOUBLE | NOT NULL |  | Balance of bad debt on financial encounter |
| 11 | `BAD_DEBT_BAL_DR_CR_FLAG` | DOUBLE | NOT NULL |  | debit/credit flag for bad_debt_balance |
| 12 | `BAD_DEBT_DT_TM` | DATETIME |  |  | Date Encounter entered a state of Bad Debt. |
| 13 | `BALANCE` | DOUBLE |  |  | Balance related to a ProFit encounter. |
| 14 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 15 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from the billing_entity table |
| 16 | `BILL_COUNTER_TERM` | LONGTEXT |  |  | Obsolete, No longer used. |
| 17 | `BILL_STATUS_CD` | DOUBLE | NOT NULL |  | Billing status of an invoice. Examples :Complete, Inprocess, Generated |
| 18 | `CHARGE_BALANCE` | DOUBLE |  |  | Total amount of charges posted to a ProFit Encounter. |
| 19 | `CHRG_BAL_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit flag for the charge balance. |
| 20 | `COLLECTION_STATE_CD` | DOUBLE | NOT NULL |  | To be removed |
| 21 | `COL_LETTER_IND` | DOUBLE | NOT NULL |  | Indicator that this financial encounter is excluded from collection letters |
| 22 | `COMBINED_INTO_ID` | DOUBLE | NOT NULL | FK→ | Candidate key reference to a PFT Encounter. |
| 23 | `CONSOLIDATION_IND` | DOUBLE | NOT NULL |  | Indicator that this financial encounter is excluded from a consolidation statement |
| 24 | `CONVERSION_IND` | DOUBLE |  |  | Indicates that this encounter was created because of a conversion. |
| 25 | `COURTESY_STMT_IND` | DOUBLE | NOT NULL |  | Indicates whether this financial encounter has started sending out courtesy statements. |
| 26 | `CR_START_DT_TM` | DATETIME |  |  | stores the start of the cardiac rehab treatment |
| 27 | `CR_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of cardiac rehab treatment visits |
| 28 | `DISCH_DT_TM` | DATETIME |  |  | Date the person was discharged from the facility |
| 29 | `DR_CR_FLAG` | DOUBLE |  |  | Flag identifying whether the balance is debit or credit. |
| 30 | `DUNNING_HOLD_IND` | DOUBLE | NOT NULL |  | Indicates if this financial encounter remains at the same dunning level regardless of other criteria |
| 31 | `DUNNING_IND` | DOUBLE | NOT NULL |  | Indicator that this financial encounter is excluded from dunning messages |
| 32 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value indicating collections state that a ProFit encounter is in. |
| 33 | `DUNNING_LEVEL_CHANGE_DT_TM` | DATETIME |  |  | Date the dunning level was changed by the bill record generation process. |
| 34 | `DUNNING_LEVEL_CNT` | DOUBLE |  |  | Indicates how many times a bill has been sent at the current dunning level code. |
| 35 | `DUNNING_NO_PAY_CNT` | DOUBLE |  |  | The number of times that no payment has been received at this dunning level |
| 36 | `DUNNING_PAY_CNT` | DOUBLE |  |  | The number of times that an acceptable payment has been received at this dunning level |
| 37 | `DUNNING_UNACC_PAY_CNT` | DOUBLE |  |  | The number of times that an unacceptable payment has been received at this dunning level |
| 38 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 39 | `ENCNTR_PLAN_COB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter plan coordination of benefits related to this pft_encntr |
| 40 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Current encounter type according to Patient Accounting |
| 41 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Current encounter type class according to Patient Accounting |
| 42 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 43 | `EST_FINANCIAL_RESP_AMT` | DOUBLE |  |  | The estimated amount due for the encounter, which is set during registration. |
| 44 | `EXTRACTION_IND` | DOUBLE |  |  | Indicator displaying the status of the extraction (1=success, 0=fail) |
| 45 | `EXT_BILLING_IND` | DOUBLE |  |  | Indicates if the ProFit encounter needs to be send to the outside collection agency at the given dunning level. |
| 46 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class code value |
| 47 | `GOOD_WILL_IND` | DOUBLE |  |  | Tells if the ProFit encounter is being paid off timely. |
| 48 | `GUAR_EXT_IND` | DOUBLE |  |  | indicator displaying the status of the guarantor extraction (1=success, 0=fail) |
| 49 | `INPATIENT_ADMIT_DT_TM` | DATETIME |  |  | Current admit date and time according to Patient Accounting. |
| 50 | `INS_PEND_BAL_FWD` | DOUBLE | NOT NULL |  | The amount of insurance pending that is being pulled forward at the pft_encntr level to the next month's statement |
| 51 | `INTERIM_IND` | DOUBLE |  |  | Indicates whether or not an encounter qualifies for interim billing. |
| 52 | `LAST_ADJUSTMENT_DT_TM` | DATETIME |  |  | Date of the last adjustment made against this encounter |
| 53 | `LAST_CHARGE_DT_TM` | DATETIME |  |  | Stores the last charge date and time |
| 54 | `LAST_CLAIM_DT_TM` | DATETIME |  |  | Date of the last claim made against this encounter |
| 55 | `LAST_EXTRACTION_DT_TM` | DATETIME |  |  | Date and Time when the last extraction was made to the Sorian Financials system. |
| 56 | `LAST_PATIENT_PAY_DT_TM` | DATETIME |  |  | The latest date/time of a patient payment |
| 57 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | Stores the last payment date and time |
| 58 | `LAST_STMT_DT_TM` | DATETIME |  |  | Date of the last Statement made against this encounter |
| 59 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Current facility location according to Patient Accounting |
| 60 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Current nurse unit location according to Patient Accounting |
| 61 | `NBR_OF_STMTS` | DOUBLE |  |  | Total number of Statements that this Encounter is related to. |
| 62 | `ORIG_BILL_SUBMIT_DT_TM` | DATETIME |  |  | A date / time stamp that will identify the date/time the bill was originally submitted to a third party. |
| 63 | `ORIG_BILL_TRANSMIT_DT_TM` | DATETIME |  |  | A date / time stamp that will identify the date/time the bill was originally transmitted to a third party. |
| 64 | `OT_START_DT_TM` | DATETIME |  |  | stores the start of the occupational therapy treatment |
| 65 | `OT_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of occupational therapy treatment visits |
| 66 | `PACKAGE_STATUS_CD` | DOUBLE | NOT NULL |  | The package status code indicating whether this particular financial encounter has been package priced for all the eligible charges tied to it. |
| 67 | `PAT_BAL_FWD` | DOUBLE | NOT NULL |  | The amount the patient owes at the pft_encntr level that is being pulled forward to the next month's statement. |
| 68 | `PAYMENT_PLAN_FLAG` | DOUBLE |  |  | The field defines the payment plan. |
| 69 | `PAYMENT_PLAN_STATUS_CD` | DOUBLE | NOT NULL |  | This field defines the status of the payment plan |
| 70 | `PFT_ENCNTR_ALIAS` | VARCHAR(215) |  |  | stores the financial encounter's alias which will be used to identify the financial encounter |
| 71 | `PFT_ENCNTR_DATA_MODEL_VRSN_NBR` | DOUBLE | NOT NULL |  | Identifies this financial encounter's data model version. |
| 72 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 73 | `PFT_ENCNTR_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the encounter. Active / Pending |
| 74 | `PT_START_DT_TM` | DATETIME |  |  | stores the start of the physical therapy treatment |
| 75 | `PT_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of physical therapy treatment visits |
| 76 | `QUALIFIER_CD` | DOUBLE | NOT NULL |  | Allows a user-defined qualifier to be attached to each ProFit financial encounter. |
| 77 | `RC_CONT_PROCESS_GROUP_ID` | DOUBLE |  | FK→ | Uniquely identifies the related Id representing a group of processes on a specific model instance. |
| 78 | `RECUR_BILL_GEN_IND` | DOUBLE |  |  | stores whether or not a bill has been generated for the recurring financial encounter |
| 79 | `RECUR_BILL_READY_IND` | DOUBLE |  |  | stores whether or not a recurring bill is ready to be generated for a financial encounter |
| 80 | `RECUR_CURRENT_MONTH` | DOUBLE |  |  | Integer field to store the value for the current month for recurring billing. Valid values are limited to 1-12. |
| 81 | `RECUR_CURRENT_YEAR` | DOUBLE | NOT NULL |  | Integer field to store the value for the current year for recurring billing. |
| 82 | `RECUR_IND` | DOUBLE |  |  | stores whether or not the financial encounter is related to a recurring clinical encounter |
| 83 | `RECUR_SEQ` | DOUBLE |  |  | stores the sequence o the recurring financial encounters. Should only be valued if recur_ind = 1. |
| 84 | `RECUR_TYPE_CD` | DOUBLE | NOT NULL |  | Describes how often the encounter will re-occur. Valid values are Weekly, Monthly, or Daily. |
| 85 | `REG_DT_TM` | DATETIME |  |  | Current registration date time according to Patient Accounting |
| 86 | `REMAINING_EST_DUE_AMT` | DOUBLE |  |  | The remaining estimated amount due for the encounter, which is set during registration. This field will change based on payments/adjustments. |
| 87 | `ROUTE_USER_NAME` | VARCHAR(40) |  |  | This column is not used on this table, it was added by mistake |
| 88 | `SELF_PAY_EDIT_FLAG` | DOUBLE |  |  | Values: (0) No edits to self-pay plan (1) Self-pay plan added (2) Self-pay plan removed (3) Self-pay plan out of sequence |
| 89 | `SEND_COL_IND` | DOUBLE | NOT NULL |  | Indicator that this financial encounteris excluded from being sent to collections |
| 90 | `SLT_START_DT_TM` | DATETIME |  |  | stores the start of the speech language therapy treatment visits |
| 91 | `SLT_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of speech language therapy treatment visits |
| 92 | `STATEMENT_CYCLE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the statement cycle table |
| 93 | `STMT_BILLING_LEVEL_CD` | DOUBLE |  |  | This field indicates the level at which statements are billed for the financial encounter. (Ex. Encounter, Balance) |
| 94 | `SUBMISSION_ROUTE_CD` | DOUBLE | NOT NULL |  | This is the submission routing for this claim |
| 95 | `SVC_BEG_DT_TM` | DATETIME |  |  | The date and time this service began. |
| 96 | `SVC_END_DT_TM` | DATETIME |  |  | The date and time this service ended. |
| 97 | `UNAPPLIED_PAYMENT_BALANCE` | DOUBLE |  |  | Total amount of unapplied payments to the ProFit Encounter. |
| 98 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 99 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 100 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 101 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 102 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 103 | `ZERO_BALANCE_DT_TM` | DATETIME |  |  | This field will store the date that the Encounter and all related charge groups reached a zero balance in regards of actual balance and bad debt balance. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `COMBINED_INTO_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_PLAN_COB_ID` | [ENCNTR_PLAN_COB](ENCNTR_PLAN_COB.md) | `ENCNTR_PLAN_COB_ID` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `RC_CONT_PROCESS_GROUP_ID` | [RC_CONT_PROCESS_GROUP](RC_CONT_PROCESS_GROUP.md) | `RC_CONT_PROCESS_GROUP_ID` |
| `STATEMENT_CYCLE_ID` | [STATEMENT_CYCLE](STATEMENT_CYCLE.md) | `STATEMENT_CYCLE_ID` |

## Referenced by (25)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `PFT_ENCNTR_ID` |
| [BENEFIT_ORDER](BENEFIT_ORDER.md) | `PFT_ENCNTR_ID` |
| [CBOS_PE_RELTN](CBOS_PE_RELTN.md) | `PFT_ENCNTR_ID` |
| [CORSP_LOG_RELTN](CORSP_LOG_RELTN.md) | `PFT_ENCNTR_ID` |
| [DAILY_ENCNTR_BAL](DAILY_ENCNTR_BAL.md) | `PFT_ENCNTR_ID` |
| [EXT_PAY_PLAN_PE_RELTN](EXT_PAY_PLAN_PE_RELTN.md) | `PFT_ENCNTR_ID` |
| [GL_TRANS_LOG_OFFSET](GL_TRANS_LOG_OFFSET.md) | `PFT_ENCNTR_ID` |
| [PE_STATUS_REASON](PE_STATUS_REASON.md) | `PFT_ENCNTR_ID` |
| [PFT_BAD_DEBT_BAL](PFT_BAD_DEBT_BAL.md) | `PFT_ENCNTR_ID` |
| [PFT_BALANCE](PFT_BALANCE.md) | `PFT_ENCNTR_ID` |
| [PFT_BENEFIT_ORDER](PFT_BENEFIT_ORDER.md) | `PFT_ENCNTR_ID` |
| [PFT_BILL_SUMMARY](PFT_BILL_SUMMARY.md) | `PFT_ENCNTR_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `PFT_ENCNTR_ID` |
| [PFT_CHRG_GRP_RPRCS](PFT_CHRG_GRP_RPRCS.md) | `PFT_ENCNTR_ID` |
| [PFT_CHRG_GRP_RPRCS_HIST](PFT_CHRG_GRP_RPRCS_HIST.md) | `PFT_ENCNTR_ID` |
| [PFT_ENCNTR](PFT_ENCNTR.md) | `COMBINED_INTO_ID` |
| [PFT_ENCNTR_ALIAS](PFT_ENCNTR_ALIAS.md) | `PFT_ENCNTR_ID` |
| [PFT_ENCNTR_COLLECTION_RELTN](PFT_ENCNTR_COLLECTION_RELTN.md) | `PFT_ENCNTR_ID` |
| [PFT_ENCNTR_FACT](PFT_ENCNTR_FACT.md) | `PFT_ENCNTR_ID` |
| [PFT_PAY_PLAN_PE_RELTN](PFT_PAY_PLAN_PE_RELTN.md) | `PFT_ENCNTR_ID` |
| [PFT_PENDING_BILL](PFT_PENDING_BILL.md) | `PFT_ENCNTR_ID` |
| [PFT_PRORATION](PFT_PRORATION.md) | `PFT_ENCNTR_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `PFT_ENCNTR_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `PFT_ENCNTR_ID` |
| [RCR_TRANS_DIST](RCR_TRANS_DIST.md) | `PFT_ENCNTR_ID` |

