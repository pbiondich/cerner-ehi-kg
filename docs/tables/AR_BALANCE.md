# AR_BALANCE

> Stores the balance information related to an A/R account.

**Description:** AR BALANCE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value identifying the type of account (e.g. A/R, Cash, Revenue etc.) |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ADJUSTMENTS` | DOUBLE |  |  | Adjustment on an A/R account. |
| 7 | `ADJ_DR_CR_FLAG` | DOUBLE |  |  | Identifies the type of adjustment, debit or credit. |
| 8 | `AR_BALANCE` | DOUBLE |  |  | Balance on an A/R account. |
| 9 | `AR_BALANCE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 10 | `AR_DR_CR_FLAG` | DOUBLE |  |  | Identifies debit or credit. |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key reference to the billing_entity table. |
| 13 | `CHARGES` | DOUBLE |  |  | Charges on an A/R account. |
| 14 | `CHRG_DR_CR_FLAG` | DOUBLE |  |  | Identifies the type of charge, debit or credit. |
| 15 | `ENDING_BALANCE` | DOUBLE |  |  | Ending Balance on an A/R account. |
| 16 | `ENDING_DR_CR_FLAG` | DOUBLE |  |  | Identifies the type of ending balance, debit or credit. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `OPENING_BALANCE` | DOUBLE |  |  | Opening balance on an A/R account. |
| 19 | `OPENING_DR_CR_FLAG` | DOUBLE |  |  | Identifies the type of opening balance, debit or credit. |
| 20 | `PAYMENTS` | DOUBLE |  |  | Payment on an A/R account. |
| 21 | `PMTS_DR_CR_FLAG` | DOUBLE |  |  | Identifies the type of payment, debit or credit. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

