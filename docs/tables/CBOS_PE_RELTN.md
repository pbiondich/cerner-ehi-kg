# CBOS_PE_RELTN

> Relates a consolidated benefit order schedule record to a ProFit Encounter and its respective Statement Cycle and Dunning Level information.

**Description:** Consolidated Benefit Order Schedule ProFit Encounter Relationship  
**Table type:** ACTIVITY  
**Primary key:** `CBOS_PE_RELTN_ID`  
**Columns:** 31  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | Contains the guarantor account id responsible for the consolidated benefit order schedule - financial encounter relationship. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BALANCE_AMT` | DOUBLE | NOT NULL |  | The balance amount related to a ProFit Encounter. |
| 7 | `CBOS_PE_RELTN_ID` | DOUBLE | NOT NULL | PK | A Unique generated number that identifies a single row on the CBOS_PE_RELTN table. |
| 8 | `CONSOLIDATION_IND` | DOUBLE | NOT NULL |  | Indicator that this guarantor's financial responsibility for encounter is excluded from a consolidation statement. |
| 9 | `CONS_BO_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related consolidated benefit order schedule. |
| 10 | `DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag identifying the whether the balance is debit or credit.0 - Not Defined; 1 - Credit; 2 - Debit |
| 11 | `DUNNING_HOLD_IND` | DOUBLE | NOT NULL |  | Indicates if this financial encounter remains at the same dunning level regardless of other criteria. |
| 12 | `DUNNING_IND` | DOUBLE | NOT NULL |  | Indicator that this financial encounter is excluded from dunning messages. |
| 13 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value indicating collections state that a financial encounter is in. |
| 14 | `DUNNING_LEVEL_CHANGE_DT_TM` | DATETIME |  |  | Date the dunning level was changed by the bill record generation process. |
| 15 | `DUNNING_LEVEL_CNT` | DOUBLE |  |  | Indicates how many times a bill has been sent at the current dunning level code. |
| 16 | `DUNNING_NO_PAY_CNT` | DOUBLE |  |  | The number of times that no payment has been received at this dunning level. |
| 17 | `DUNNING_PAY_CNT` | DOUBLE |  |  | The number of times that an acceptable payment has been received at this dunning level. |
| 18 | `DUNNING_UNACC_PAY_CNT` | DOUBLE |  |  | The number of times that an unacceptable payment has been received at this dunning level. |
| 19 | `INS_PEND_BAL_FWD_AMT` | DOUBLE | NOT NULL |  | The amount of insurance pending that is being pulled forward at the pft_encntr level to the next month's statement. |
| 20 | `LAST_STMT_DT_TM` | DATETIME |  |  | Date of the last Statement made against this encounter. |
| 21 | `ORIG_BILL_DT_TM` | DATETIME |  |  | The date that the original bill was generated. |
| 22 | `PAT_BAL_FWD_AMT` | DOUBLE | NOT NULL |  | The amount the patient owes at the pft_encntr level that is being pulled forward to the next month's statement. |
| 23 | `PAYMENT_PLAN_FLAG` | DOUBLE | NOT NULL |  | Defines the Payment Plan. 1 - Informal Payment Plan; 2 - Formal Payment Plan |
| 24 | `PAYMENT_PLAN_STATUS_CD` | DOUBLE | NOT NULL |  | This field defines the status of the payment plan. |
| 25 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related ProFit Encounter |
| 26 | `STATEMENT_CYCLE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Statement Cycle. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `CONS_BO_SCHED_ID` | [CONS_BO_SCHED](CONS_BO_SCHED.md) | `CONS_BO_SCHED_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `STATEMENT_CYCLE_ID` | [STATEMENT_CYCLE](STATEMENT_CYCLE.md) | `STATEMENT_CYCLE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CBOS_ACTIVITY_RELTN](CBOS_ACTIVITY_RELTN.md) | `CBOS_PE_RELTN_ID` |
| [EXT_PAY_PLAN_PE_RELTN](EXT_PAY_PLAN_PE_RELTN.md) | `CBOS_PE_RELTN_ID` |
| [PFT_BAD_DEBT_BAL](PFT_BAD_DEBT_BAL.md) | `CBOS_PE_RELTN_ID` |
| [PFT_PAY_PLAN_PE_RELTN](PFT_PAY_PLAN_PE_RELTN.md) | `CBOS_PE_RELTN_ID` |

