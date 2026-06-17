# RC_D_ACCOUNT

> This table contains information related to an account such as account description and account sub type.

**Description:** Revenue Cycle Dimension Account  
**Table type:** ACTIVITY  
**Primary key:** `RC_D_ACCOUNT_ID`  
**Columns:** 19  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_DESCRIPTION` | VARCHAR(250) | NOT NULL |  | The description related to an account. |
| 2 | `ACCOUNT_IDENT` | VARCHAR(50) | NOT NULL |  | Contains the external account number that relates to an account. |
| 3 | `ACCOUNT_SUB_TYPE` | VARCHAR(40) | NOT NULL |  | The sub type associated with an account (i.e. Client or General) |
| 4 | `ACCOUNT_TYPE` | VARCHAR(40) | NOT NULL |  | Account type like AR, Non AR etc. |
| 5 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 10 | `MILL_ACCOUNT_ID` | DOUBLE | NOT NULL |  | The account id from the millennium database account table. |
| 11 | `MILL_ACCOUNT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the code value indicating the sub type of account. |
| 12 | `MILL_ACCOUNT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the code value indicating the type of account. |
| 13 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 14 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies information related to an account such as account description and account sub type. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (10)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_GENERAL_AR_BALANCE](RC_F_GENERAL_AR_BALANCE.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_GENERAL_AR_BAL_TRANS](RC_F_GENERAL_AR_BAL_TRANS.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_INVOICE_AR_BAL_INV](RC_F_INVOICE_AR_BAL_INV.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_INVOICE_AR_BAL_SMRY](RC_F_INVOICE_AR_BAL_SMRY.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_NON_AR_BALANCE](RC_F_NON_AR_BALANCE.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_ACCOUNT_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_ACCOUNT_ID` |

