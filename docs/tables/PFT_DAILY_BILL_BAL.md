# PFT_DAILY_BILL_BAL

> Stores a bill's balance on a daily basis.

**Description:** PFT DAILY BILL BAL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date and time the bill activity occurred. |
| 2 | `ADJUSTMENT_AMOUNT` | DOUBLE | NOT NULL |  | Total adjustments made on this bill rec for this day. |
| 3 | `ADJ_DR_CR_FLAG` | DOUBLE | NOT NULL |  | The debit/credit flag for the adjustment amount.0 |
| 4 | `BEG_BALANCE` | DOUBLE | NOT NULL |  | Beginning balance for the bill record for this day. |
| 5 | `BEG_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/credit flag for the beginning balance. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILLED_AMOUNT` | DOUBLE | NOT NULL |  | Original billed amount of the bill record. |
| 8 | `BILLED_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/credit flag for the billed amount. |
| 9 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the billing_entity table |
| 10 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to bill record |
| 11 | `CALCULATED_END_BAL` | DOUBLE | NOT NULL |  | Calculated balance of the bill record for this day. |
| 12 | `CALC_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/credit flag for the calculated balance. |
| 13 | `CHARGE_AMT` | DOUBLE | NOT NULL |  | The amount of the charges posted on this date. |
| 14 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Along with bill_vrsn_nbr, uniquely identifies a bill record |
| 15 | `END_BALANCE` | DOUBLE | NOT NULL |  | Ending balance of the bill record for this day. |
| 16 | `END_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/credit flag for the ending balance. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `ORIG_BILL_DT_TM` | DATETIME | NOT NULL |  | The date and time the bill was originally billed. |
| 19 | `PAYMENT_AMOUNT` | DOUBLE | NOT NULL |  | Total payments made on this bill record for this day. |
| 20 | `PAY_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/credit flag for the payments. |
| 21 | `PFT_DAILY_BILL_BAL_ID` | DOUBLE | NOT NULL |  | Unique identifier for the pft_daily_bill_bal table. |
| 22 | `TRANSFER_AMT` | DOUBLE | NOT NULL |  | Amount of transfer (balance transfer), if applicable. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |

