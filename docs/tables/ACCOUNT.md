# ACCOUNT

> The account table will hold information about internal organization accounts as well as patient accounts

**Description:** Account  
**Table type:** REFERENCE  
**Primary key:** `ACCT_ID`  
**Columns:** 51  
**Referenced by:** 23 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_BALANCE` | DOUBLE |  |  | Stores the current balance on the account. |
| 2 | `ACCT_DESC` | VARCHAR(250) |  |  | Free Text Description |
| 3 | `ACCT_ID` | DOUBLE | NOT NULL | PK | Primary key and unique identifier of the Account Table |
| 4 | `ACCT_STATUS_CD` | DOUBLE | NOT NULL |  | Contains the current status of the account (in collections, review, active) |
| 5 | `ACCT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Further defines the account type. |
| 6 | `ACCT_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | No Longer Used |
| 7 | `ACCT_TYPE_CD` | DOUBLE | NOT NULL |  | Patient, Cash, Revenue... |
| 8 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 9 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 10 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 11 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 12 | `ADJUSTMENT_BALANCE` | DOUBLE |  |  | Total amount of adjustments posted to this account. |
| 13 | `ADJ_BAL_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit flag for the adjustment balance. |
| 14 | `APPLIED_PAYMENT_BALANCE` | DOUBLE |  |  | Total amount of payments posted to the account |
| 15 | `BAD_DEBT_BALANCE` | DOUBLE | NOT NULL |  | Bad debt balance on the account |
| 16 | `BAD_DEBT_BAL_DR_CR_FLAG` | DOUBLE | NOT NULL |  | debit/credit flag for bad_debt_balance field |
| 17 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 18 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the owning Billing Entity for the Account |
| 19 | `CHARGE_BALANCE` | DOUBLE |  |  | Total amount of charges posted to this account. |
| 20 | `CHRG_BAL_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit flag for the charge balance. |
| 21 | `COL_LETTER_IND` | DOUBLE |  |  | If 0 the account can be sent collection letters, otherwise the account can not be sent a collection letter. |
| 22 | `CONSOLIDATION_IND` | DOUBLE |  |  | No Longer Used |
| 23 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 24 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person who created the record |
| 25 | `DR_CR_FLAG` | DOUBLE |  |  | Stores whether the account has a debit or credit balance |
| 26 | `DUNNING_IND` | DOUBLE |  |  | If 0 then this account can be sent dunning letters, otherwise the account can not be sent dunning letters. |
| 27 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 28 | `EXT_ACCT_ID_TXT` | CHAR(50) |  |  | Allows the client to keep their original account id's separate from Cerner's Id's |
| 29 | `EXT_ACCT_ID_TXT_KEY` | VARCHAR(250) |  |  | A key field copy of the EXT_ACCT_ID_TXT that can be indexed for faster access |
| 30 | `GLOBAL_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Indicator that all financial encounters related to this account are on consolidation override |
| 31 | `HI_ACCT_BALANCE` | DOUBLE |  |  | Records the highest balance that the account has reached |
| 32 | `LAST_ADJUSTMENT_DT_TM` | DATETIME |  |  | Date of last adjustment made against this encounter |
| 33 | `LAST_CHARGE_DT_TM` | DATETIME |  |  | Stores the last charge date and time |
| 34 | `LAST_CLAIM_DT_TM` | DATETIME |  |  | Date of last claim made against this encounter |
| 35 | `LAST_PATIENT_PAY_DT_TM` | DATETIME |  |  | The latest date/time of a patient payment |
| 36 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | Stores the last payment date and time |
| 37 | `LAST_STMT_DT_TM` | DATETIME |  |  | Date of the last Statement made against this encounter |
| 38 | `PAYMENT_PLAN_IND` | DOUBLE |  |  | Indicates whether a payment plan is being enforced |
| 39 | `PENDING_ACCT_BAL` | DOUBLE |  |  | Like the account balance except this will include all pending charges also. |
| 40 | `PEND_DR_CR_FLAG` | DOUBLE |  |  | Indicates whether the pending balance would be a debit or credit. |
| 41 | `PRSNL_SEC_IND` | DOUBLE |  |  | Indicates that the account has special security requirements that override the default Billing Entity and Account Template security settings. See Acct_Prsnl_Reltn for security levels. |
| 42 | `SEND_COL_IND` | DOUBLE |  |  | If 0 then the account can be sent to collections, else if 1 then the account can not be sent to collections. |
| 43 | `STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Stores the reason for the account being in it's current status (non payment) |
| 44 | `SUPPRESS_FLAG` | DOUBLE | NOT NULL |  | Indicates suppression from statement |
| 45 | `SUPPRESS_IND` | DOUBLE | NOT NULL |  | Suppress this account from statements, this includes all encounters related |
| 46 | `UNAPPLIED_PAYMENT_BALANCE` | DOUBLE |  |  | Total amount of unapplied payments to the account - Not Used |
| 47 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_TEMPL_ID` | [ACCT_TEMPLATE](ACCT_TEMPLATE.md) | `ACCT_TEMPL_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (23)

| From table | Column |
|------------|--------|
| [ACCT_GROUP_RELTN](ACCT_GROUP_RELTN.md) | `ACCT_ID` |
| [ACCT_PRSNL_GROUP_R](ACCT_PRSNL_GROUP_R.md) | `ACCT_ID` |
| [AT_ACCT_RELTN](AT_ACCT_RELTN.md) | `ACCT_ID` |
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `GUAR_ACCT_ID` |
| [BE_GL_ALIAS_RELTN](BE_GL_ALIAS_RELTN.md) | `ACCT_ID` |
| [BILLING_ENTITY](BILLING_ENTITY.md) | `AR_ACCT_ID` |
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `ACCT_ID` |
| [CBOS_PE_RELTN](CBOS_PE_RELTN.md) | `ACCT_ID` |
| [CORSP_LOG_RELTN](CORSP_LOG_RELTN.md) | `ACCT_ID` |
| [DAILY_ACCT_BAL](DAILY_ACCT_BAL.md) | `ACCT_ID` |
| [EXT_REQ_STATUS](EXT_REQ_STATUS.md) | `ACCOUNT_ID` |
| [GL_TRANS_LOG_OFFSET](GL_TRANS_LOG_OFFSET.md) | `ACCOUNT_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `CLIENT_ACCOUNT_ID` |
| [PE_STATUS_REASON](PE_STATUS_REASON.md) | `GUAR_ACCT_ID` |
| [PFT_AP_REFUND](PFT_AP_REFUND.md) | `GUAR_ACCT_ID` |
| [PFT_BALANCE](PFT_BALANCE.md) | `ACCT_ID` |
| [PFT_BENEFIT_ORDER](PFT_BENEFIT_ORDER.md) | `ACCT_ID` |
| [PFT_BILL_SUMMARY](PFT_BILL_SUMMARY.md) | `ACCT_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `CR_ACCT_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `DR_ACCT_ID` |
| [PFT_ENCNTR](PFT_ENCNTR.md) | `ACCT_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `ACCT_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `ACCT_ID` |

