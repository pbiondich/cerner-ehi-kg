# PFT_ENCNTR_HIST

> ProFit's encounter history

**Description:** PFT ENCNTR HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 65

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL |  | Candidate key reference to an account. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ADJUSTMENT_BALANCE` | DOUBLE |  |  | Total adjustment balance for financial encounter in history. |
| 7 | `ADJ_BAL_DR_CR_FLAG` | DOUBLE |  |  | Determines if the Balance is a Debit or Credit Balance |
| 8 | `APPLIED_PAYMENT_BALANCE` | DOUBLE |  |  | Total applied payment balance for financial encounter in history. |
| 9 | `BAD_DEBT_BALANCE` | DOUBLE | NOT NULL |  | Bad debt balance on finanical encounter |
| 10 | `BAD_DEBT_BAL_DR_CR_FLAG` | DOUBLE | NOT NULL |  | debit/credit flag for bad_debt_balance field |
| 11 | `BALANCE` | DOUBLE |  |  | Total balance for financial encounter in history. |
| 12 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 13 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | Billing Entity ID |
| 14 | `BILL_STATUS_CD` | DOUBLE | NOT NULL |  | Billing status of an invoice. Examples: Complete, Inprocess, Generated |
| 15 | `CHARGE_BALANCE` | DOUBLE |  |  | Total Charge Balance for financial encounter in history. |
| 16 | `CHRG_BAL_DR_CR_FLAG` | DOUBLE |  |  | Charge Balance Debit Credit Flag for financial encounter in history.0 - Unknown or zero balance.1 - Debit Balance2 - Credit Balance |
| 17 | `COL_LETTER_IND` | DOUBLE | NOT NULL |  | Indicates this financial encounter is excluded from collection letters |
| 18 | `COMBINED_INTO_ID` | DOUBLE | NOT NULL |  | Candidate key reference to a PFT Encounter. |
| 19 | `CONSOLIDATION_IND` | DOUBLE | NOT NULL |  | Indicates this financial encounter is excluded from a consolidation statement |
| 20 | `CR_START_DT_TM` | DATETIME |  |  | stores the start of the cardiac rehab treatment |
| 21 | `CR_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of cardiac rehab treatment visits |
| 22 | `DISCH_DT_TM` | DATETIME |  |  | Discharged Date Time of financial encounter in history. |
| 23 | `DR_CR_FLAG` | DOUBLE |  |  | Flag identifying whether the balance is debit or credit. |
| 24 | `DUNNING_HOLD_IND` | DOUBLE | NOT NULL |  | Indicates if this financial encounter remains at the same dunning level regardless of other criteria |
| 25 | `DUNNING_IND` | DOUBLE | NOT NULL |  | Indicates this financial encounter is exluded from dunning messages |
| 26 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Dunning Level Cd for financial encounter in history. |
| 27 | `DUNNING_LEVEL_CHANGE_DT_TM` | DATETIME |  |  | Date and Time of Dunning Level Change for the financial encounter in history. |
| 28 | `DUNNING_LEVEL_CNT` | DOUBLE |  |  | Dunning Level Count for financial encounter in history. |
| 29 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 30 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 31 | `EXT_BILLING_IND` | DOUBLE |  |  | External Billing Indicator for financial encounter in history. |
| 32 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial Class Code |
| 33 | `GOOD_WILL_IND` | DOUBLE |  |  | Tells if the ProFit encounter is being paid off timely. |
| 34 | `INTERIM_BILL_IND` | DOUBLE |  |  | Indicates whether or not an encounter qualifies for interim billing. |
| 35 | `INTERIM_IND` | DOUBLE |  |  | Interim Indicator for financial encounter in history. |
| 36 | `LAST_ADJUSTMENT_DT_TM` | DATETIME |  |  | Date of the last adjustment made against this encounter |
| 37 | `LAST_CLAIM_DT_TM` | DATETIME |  |  | Date of the last claim made against this encounter |
| 38 | `LAST_PATIENT_PAY_DT_TM` | DATETIME |  |  | The latest date/time of a patient payment |
| 39 | `LAST_STMT_DT_TM` | DATETIME |  |  | Date of the last Statement made against this encounter |
| 40 | `OT_START_DT_TM` | DATETIME |  |  | stores the start of the occupational therapy treatment |
| 41 | `OT_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of occupational therapy treatment visits |
| 42 | `PAYMENT_PLAN_FLAG` | DOUBLE |  |  | This fields holds a flag value that defines the type of payment plan. |
| 43 | `PAYMENT_PLAN_STATUS_CD` | DOUBLE | NOT NULL |  | This field defines the status of the payment plan |
| 44 | `PFT_ENCNTR_HIST_ALIAS` | VARCHAR(215) |  |  | stores the financial encounter's alias which will be used to identify the financial encounter |
| 45 | `PFT_ENCNTR_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a historical record of a ProFit encounter. |
| 46 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Foreign key reference to a ProFit encounter. |
| 47 | `PFT_ENCNTR_STATUS_CD` | DOUBLE | NOT NULL |  | Active or Pending |
| 48 | `PT_START_DT_TM` | DATETIME |  |  | stores the start of the physical therapy visits |
| 49 | `PT_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of physical therapy treatment visits |
| 50 | `RECUR_BILL_GEN_IND` | DOUBLE |  |  | stores whether or not a bill has been generated for the recurring financial encounter |
| 51 | `RECUR_BILL_READY_IND` | DOUBLE |  |  | stores whether or not a recurring bill is ready to be generated for a financial encounter. Should only be valued if recur_ind = 1 |
| 52 | `RECUR_CURRENT_MONTH` | DOUBLE |  |  | stores the value for the current month for recurring billing. Valid values are limited to 1 - 12. |
| 53 | `RECUR_IND` | DOUBLE |  |  | stores whether or not the financial encounter is related to a recurring clinical encounter. Should only be valued if the encounter type class on the clinical encounter is "RECURRING" |
| 54 | `RECUR_SEQ` | DOUBLE |  |  | stores the sequence of the recurring financial encounters. Should only be valued if the recur_ind = 1. |
| 55 | `SELF_PAY_EDIT_FLAG` | DOUBLE |  |  | Values: (0) No edits to self-pay plan (1) Self-pay plan added (2) Self-pay plan removed (3) Self-pay plan out of sequence |
| 56 | `SEND_COL_IND` | DOUBLE | NOT NULL |  | Indicates this financial encounter is exluded from being sent to collections |
| 57 | `SLT_START_DT_TM` | DATETIME |  |  | stores the start of the speech language therapy treatment |
| 58 | `SLT_TOTAL_VISITS` | DOUBLE |  |  | stores the running total of speech language therapy treatment visits |
| 59 | `STMT_BILLING_LEVEL_CD` | DOUBLE |  |  | ** OBSOLETE ** This column is no longer used. This field indicates the level at which statements are billed for the financial encounter. (Ex. Encounter, Balance) ** Obsolete** |
| 60 | `UNAPPLIED_PAYMENT_BALANCE` | DOUBLE |  |  | Total amount of unapplied payments to the account |
| 61 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

