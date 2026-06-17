# PFT_DAILY_BALANCE_BAL

> This table tracks the daily changes to individual insurance balances to perform accounting checks against existing account data.

**Description:** Daily Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Total adjustments made on this bill rec for this day. |
| 6 | `BEG_BALANCE_AMT` | DOUBLE | NOT NULL |  | This is the balance amount that this bo_hp was responsible for when this row became effective. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related billing entity. |
| 9 | `BO_HP_RELTN_ID` | DOUBLE |  | FK→ | Uniquely identifies the related BO_HP_RELTN record. |
| 10 | `BO_HP_STATUS_CD` | DOUBLE | NOT NULL |  | The status stored on the parent BO_HP_RELTN table can change as a balance progresses. This contains the historical status of the balance. |
| 11 | `CHARGE_AMT` | DOUBLE | NOT NULL |  | The amount of the charges posted on this date. |
| 12 | `END_BALANCE_AMT` | DOUBLE | NOT NULL |  | This is the balance amount that this bo_hp is either currently responsible for, or was responsible for when a new row was written out. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `ORIG_PFT_DAILY_BALANCE_BAL_ID` | DOUBLE | NOT NULL |  | Used to track versions of the daily balance information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 15 | `PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the amount of the related payment. |
| 16 | `PFT_DAILY_BALANCE_BAL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies individual insurance balances to perform accounting checks against existing account data and to track daily changes.. |
| 17 | `ROLL_IN_AMT` | DOUBLE | NOT NULL |  | This is the amount that represents a higher sequence health plan transferring monetary responsibility to this health plan. |
| 18 | `ROLL_OUT_AMT` | DOUBLE | NOT NULL |  | This is the amount that represents a this health plan transferring monetary responsibility to a lower sequence health plan. |
| 19 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total amount of the adjustment |
| 20 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | Contains the total amount of the charge. |
| 21 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total amount of the payment. |
| 22 | `TRANSFER_IN_AMT` | DOUBLE | NOT NULL |  | This is a generic monetary amount that was transferred in to this health plan. It could be an amalgem of charges, payments, and adjustment amounts. |
| 23 | `TRANSFER_OUT_AMT` | DOUBLE | NOT NULL |  | This is a generic monetary amount that was transferred away from this health plan. It could be an amalgem of charges, payments, and adjustment amounts. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |

