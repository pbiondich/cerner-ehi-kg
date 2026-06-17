# PFT_DAILY_BO_HP_BAL

> Stores a BO_HP's balances on a daily basis.

**Description:** PFT DAILY BO HP BAL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date of the activity applied to the BO_HP_RELTN. |
| 2 | `ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Total adjustments made on this bill rec for this day. |
| 3 | `ADJ_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit Credit flag for the adjustment amount.1 |
| 4 | `BEG_EST_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit Credit flag for the Beginning Estimated Balance. |
| 5 | `BEG_EST_RESP` | DOUBLE | NOT NULL |  | Beginning Estimated Responsibility |
| 6 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Billing Entity related to the given BO_HP Reltn. |
| 7 | `CALCULATED_END_BAL` | DOUBLE | NOT NULL |  | Calculated balance of the BO_HP Reltn for this day. |
| 8 | `CALC_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit Credit flag for the calculated balance. |
| 9 | `CHARGE_AMOUNT` | DOUBLE | NOT NULL |  | Total Charges applied on the BO_HP_RELTN for this day. |
| 10 | `CHARGE_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit Credit flag for the Charges. |
| 11 | `CO_INSURANCE_AMT` | DOUBLE | NOT NULL |  | Amount of the co-insurance, if applicable. |
| 12 | `CO_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Amount of the co-pay, if applicable. |
| 13 | `DEDUCTIBLE_AMT` | DOUBLE | NOT NULL |  | Amount of the deductible, if applicable. |
| 14 | `DENIAL_AMT` | DOUBLE | NOT NULL |  | Amount of the denial, if applicable |
| 15 | `END_EST_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Ending balance of the BO_HP reltn for this day. This relates to the Curr_Amount on the pft_proration table. |
| 16 | `END_EST_RESP` | DOUBLE | NOT NULL |  | Ending Estimated Responsibility |
| 17 | `MAN_ADJ_AMOUNT` | DOUBLE | NOT NULL |  | Total Manual Adjustments on the BO_HP_RELTN for this day. |
| 18 | `MAN_ADJ_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit Credit flag for the Manual Adjustments. |
| 19 | `NON_COVERED_CHARGE_AMT` | DOUBLE | NOT NULL |  | Amount of the non-covered charge, if applicable. |
| 20 | `PATIENT_RESP_AMT` | DOUBLE | NOT NULL |  | Amount of the patient responsibility, if applicable. |
| 21 | `PAYMENT_AMOUNT` | DOUBLE | NOT NULL |  | Total Payments made on this BO_HP Reltn for this day. |
| 22 | `PAY_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit Credit flag for the Payments. |
| 23 | `PFT_DAILY_BO_HP_BAL_ID` | DOUBLE | NOT NULL |  | Unique Identifier |
| 24 | `PFT_PRORATION_ID` | DOUBLE | NOT NULL | FK→ | Bill Record ID related to this daily balance. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `PFT_PRORATION_ID` | [PFT_PRORATION](PFT_PRORATION.md) | `PFT_PRORATION_ID` |

