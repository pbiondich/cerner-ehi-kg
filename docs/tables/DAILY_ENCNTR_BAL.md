# DAILY_ENCNTR_BAL

> Profits table to track the daily financial encounter balances

**Description:** DAILY ENCNTR BAL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_DT_TM` | DATETIME |  |  | Represents the last date and time a transactions was posted to the encounter. |
| 6 | `ADJUSTMENT_AMOUNT` | DOUBLE | NOT NULL |  | The total adjustment amount for the given activity date. |
| 7 | `ADJ_DR_CR_FLAG` | DOUBLE |  |  | The total adjustment amount debit credit flag for the given activity date. |
| 8 | `BEG_BALANCE` | DOUBLE | NOT NULL |  | The opening balance for the given activity date Copied from the previous activities days end_balance_dt_tm. |
| 9 | `BEG_DR_CR_FLAG` | DOUBLE |  |  | The opening balance for the given activity date Copied from the previous activities days end_balance_dt_tm. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key reference to the billing_entity table |
| 12 | `CALCULATED_END_BAL` | DOUBLE | NOT NULL |  | The Beginning Balance minus the charge,payment, and adjustments for the given activity date. |
| 13 | `CALC_DR_CR_FLAG` | DOUBLE |  |  | Calculated End Balance debit/credit flag. Total calculated end balance flag. |
| 14 | `CHARGE_AMOUNT` | DOUBLE | NOT NULL |  | The total charge amount for the given activity date. |
| 15 | `CHRG_DR_CR_FLAG` | DOUBLE |  |  | The total charge amount debit credit flag for the given activity date. |
| 16 | `DAILY_ENCNTR_BAL_ID` | DOUBLE | NOT NULL |  | Unique identifier to the Daily Encounter Balance table |
| 17 | `END_BALANCE` | DOUBLE | NOT NULL |  | The ending balance for the given activity date. |
| 18 | `END_DR_CR_FLAG` | DOUBLE |  |  | Ending balance debit/credit flag. Total ending balance flag. |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | The last date a payment, not equal to $0.00, was received for the associated profit encounter |
| 21 | `PAYMENT_AMOUNT` | DOUBLE | NOT NULL |  | The total payment amount for the given activity date. |
| 22 | `PAY_DR_CR_FLAG` | DOUBLE |  |  | The total payment amount debit credit flag for the given activity date. |
| 23 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the pft_encntr table |
| 24 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE |  |  | A running total of adjustments for the associated profit encounter up to and including this activity_dt_tm |
| 25 | `TOTAL_CHARGE_AMT` | DOUBLE |  |  | A running total of charges for the associated profit encounter up to and including this activity_dt_tm |
| 26 | `TOTAL_PAYMENT_AMT` | DOUBLE |  |  | A running total of payments for the associated profit encounter up to and including this activity_dt_tm |
| 27 | `TRANSFER_AMOUNT` | DOUBLE | NOT NULL |  | The total transfer amount for the given activity date. |
| 28 | `TRANSFER_DR_CR_FLAG` | DOUBLE |  |  | Transfer amount debit/credit flag |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

