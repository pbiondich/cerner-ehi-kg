# DAILY_ACCT_BAL

> ProFit table to track the daily account balances.

**Description:** Daily Account Balance  
**Table type:** ACTIVITY  
**Primary key:** `DAILY_ACCT_BAL_ID`  
**Columns:** 37  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the account table |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_DT_TM` | DATETIME |  |  | Represents the last date and time a transactions was posted to the encounter. |
| 7 | `ADJUSTMENT_AMOUNT` | DOUBLE |  |  | The total adjustment amount for the given activity date. |
| 8 | `ADJ_DR_CR_FLAG` | DOUBLE |  |  | The total adjustment amount debit credit flag for the given activity date. |
| 9 | `BEG_BALANCE` | DOUBLE |  |  | The opening balance for the given activity date copied from the previous activities days. |
| 10 | `BEG_DR_CR_FLAG` | DOUBLE |  |  | The opening balance for the debit/credit flag for the given activity date. |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the billing_entity table |
| 13 | `CALCULATED_END_BAL` | DOUBLE |  |  | The beginning balance minus the charge, payment, and adjustments for the given activity date. |
| 14 | `CALC_DR_CR_FLAG` | DOUBLE |  |  | The calculated end balance debit/credit flag for the given activity date. |
| 15 | `CHARGE_AMOUNT` | DOUBLE |  |  | The total charge amount for the given activity date. |
| 16 | `CHRG_DR_CR_FLAG` | DOUBLE |  |  | The total charge amount debit/credit flag for the given activity date. |
| 17 | `DAILY_ACCT_BAL_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 18 | `END_BALANCE` | DOUBLE |  |  | The ending balance for the given activity date. |
| 19 | `END_DR_CR_FLAG` | DOUBLE |  |  | Ending Balance Debit/Credit Flag for the given activity date. |
| 20 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 21 | `FINCHRG_AMOUNT` | DOUBLE |  |  | Finance Charge Amount - This column is no longer used. |
| 22 | `FINCHRG_DR_CR_FLAG` | DOUBLE |  |  | Finance Charge Amount Debit/Credit - This column is no longer used. |
| 23 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | The last date a payment, not equal to $0.00, was received for the associated account |
| 24 | `PAYMENT_AMOUNT` | DOUBLE |  |  | The total payment amount for the given activity date. |
| 25 | `PAY_DR_CR_FLAG` | DOUBLE |  |  | The total Payment Amount Debit/Credit Flag for the given activity date. |
| 26 | `RESPONSIBILITY_AMT` | DOUBLE |  |  | Guarantor account daily responsibility amount |
| 27 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE |  |  | The last date a payment, not equal to $0.00, was received for the associated account |
| 28 | `TOTAL_CHARGE_AMT` | DOUBLE |  |  | A running total of charges for the associated account up to and including this activity_dt_tm |
| 29 | `TOTAL_PAYMENT_AMT` | DOUBLE |  |  | A running total of payments for the associated account up to and including this activity_dt_tm |
| 30 | `TOTAL_RESPONSIBILITY_AMT` | DOUBLE |  |  | Total Guarantor account responsibility amount |
| 31 | `TRANSFER_AMOUNT` | DOUBLE |  |  | Amount of a transfer that moved an amount from one account to another |
| 32 | `TRANSFER_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit flag for the transferred amount |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DAILY_ACCT_BAL_RELTN](DAILY_ACCT_BAL_RELTN.md) | `DAILY_ACCT_BAL_ID` |

