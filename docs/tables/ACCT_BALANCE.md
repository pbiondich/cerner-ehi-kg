# ACCT_BALANCE

> Account Balance

**Description:** Acct_Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Code value identifying the account subtype (e.g. Patient, Client etc.) |
| 2 | `ACCOUNT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value identifying the type of account (e.g. A/R, Cash, Revenue) |
| 3 | `ACCT_BALANCE` | DOUBLE |  |  | Balance of an account. |
| 4 | `ACCT_BALANCE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 5 | `ACCT_BAL_DR_CR_FLAG` | DOUBLE |  |  | Flag indicating whether the account balance is debit or credit. |
| 6 | `ACCT_ID` | DOUBLE | NOT NULL |  | Foreign key to the account table. |
| 7 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 9 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 10 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 11 | `ADJUSTMENTS` | DOUBLE |  |  | Adjustments made to the account. |
| 12 | `ADJ_DR_CR_FLAG` | DOUBLE |  |  | Flag indicating the type of adjustment, debit or credit. |
| 13 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 14 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key reference to the billing_entity table. |
| 15 | `CHARGES` | DOUBLE |  |  | Charges associated to an account. |
| 16 | `CHRG_DR_CR_FLAG` | DOUBLE |  |  | Indicates the type to charge, debit or credit. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `EXT_ACCT_ID_TXT` | CHAR(50) |  |  | Extended account id from the account table. This is used defined. |
| 19 | `PAYMENTS` | DOUBLE |  |  | Payments associated to an account. |
| 20 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 21 | `PMTS_DR_CR_FLAG` | DOUBLE |  |  | Identifies the type of payment, debit or credit. |
| 22 | `PREVIOUS_BALANCE` | DOUBLE |  |  | Previous balance on an account. |
| 23 | `PREVIOUS_DR_CR_FLAG` | DOUBLE |  |  | Identifies the type of the previous balance, debit or credit. |
| 24 | `RAW_ACCT_BALANCE` | DOUBLE |  |  | Account balance from the account table. |
| 25 | `RAW_ACCT_BALANCE_FLAG` | DOUBLE |  |  | Raw Account Balance Flag |
| 26 | `TRANSFER_AMOUNT` | DOUBLE |  |  | Amount of a transfer that moved an amount from one account to another |
| 27 | `TRANSFER_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit flag for the transfer amount |
| 28 | `UPDATE_IND` | DOUBLE |  |  | Update Indicator |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

