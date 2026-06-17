# RC_D_TRANSACTION_ALIAS

> This table contains transaction alias information such as transaction alias and transaction type.

**Description:** Revenue Cycle Dimension Transaction Alias  
**Table type:** REFERENCE  
**Primary key:** `RC_D_TRANSACTION_ALIAS_ID`  
**Columns:** 17  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 6 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 7 | `MILL_TRANSACTION_ALIAS_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Millennium transaction alias from which this fact row was derived. |
| 8 | `RC_D_TRANSACTION_ALIAS_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies transaction alias information. |
| 9 | `TRANSACTION_ALIAS` | VARCHAR(40) | NOT NULL |  | The ProFit alias associated with the transaction alias. |
| 10 | `TRANSACTION_REASON` | VARCHAR(40) | NOT NULL |  | The transaction reason associated with the transaction alias (i.e. Bankruptcy, Bad Debt Recovery, Patient Payment). |
| 11 | `TRANSACTION_SUB_TYPE` | VARCHAR(40) | NOT NULL |  | The transaction sub type associated with the transaction alias (i.e. Commercial Insurance payment, Refund Payment). |
| 12 | `TRANSACTION_TYPE` | VARCHAR(40) | NOT NULL |  | The transaction type associated with the transaction alias (i.e. Adjustment, Charge, Payment). |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (7)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| [RC_F_GENERAL_AR_BAL_TRANS](RC_F_GENERAL_AR_BAL_TRANS.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_TRANSACTION_ALIAS_ID` |

