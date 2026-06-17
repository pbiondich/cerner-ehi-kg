# PFT_DAILY_BO_HP_CHRG_BAL

> Maintains a daily balance for a charge associated to a Benefit Order Health Plan

**Description:** ProFit Daily Benefit Order Health Plan Charge Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date of the activity applied to the BO_HP_RELTN. |
| 2 | `ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | The amount of the adjustments posted on this date. |
| 3 | `BEG_BALANCE_AMT` | DOUBLE | NOT NULL |  | Beginning balance amount as related to the BOHP charge |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated BO_HP_RELTN to the BO_HP balance this day |
| 6 | `CHARGE_AMT` | DOUBLE | NOT NULL |  | The amount of the charges posted on this date. |
| 7 | `DENIAL_AMT` | DOUBLE | NOT NULL |  | Amount of the denial, if applicable. |
| 8 | `END_BALANCE_AMT` | DOUBLE | NOT NULL |  | End balance amount |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `NON_COVERED_AMT` | DOUBLE | NOT NULL |  | Amount not covered |
| 11 | `PAT_RESP_AMT` | DOUBLE | NOT NULL |  | Amount responsible to patient |
| 12 | `PAYMENT_AMT` | DOUBLE | NOT NULL |  | Payment Amount |
| 13 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated charge |
| 14 | `PFT_DAILY_BO_HP_CHRG_BAL_ID` | DOUBLE | NOT NULL |  | Identifies a daily benefit order health plan charge |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `PFT_CHARGE_ID` | [PFT_CHARGE](PFT_CHARGE.md) | `PFT_CHARGE_ID` |

