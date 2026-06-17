# RC_D_TRANSACTION_TYPE

> This table stores the transaction type, its corresponding code value, sub type and reason.

**Description:** Revenue Cycle Dimension Transaction Type  
**Table type:** REFERENCE  
**Primary key:** `RC_D_TRANSACTION_TYPE_ID`  
**Columns:** 14  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 2 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 3 | `MILL_TRANSACTION_REASON_CD` | DOUBLE | NOT NULL |  | Holds the code associated with corresponding transaction reason |
| 4 | `MILL_TRANSACTION_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Holds the code associated with corresponding transaction sub type |
| 5 | `MILL_TRANSACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Holds the code associated with corresponding transaction type. |
| 6 | `RC_D_TRANSACTION_TYPE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RC_D_TRANSACTION _TYPE table. |
| 7 | `TRANSACTION_REASON` | VARCHAR(40) | NOT NULL |  | The transaction reason associated with the transaction type (i.e. bankruptcy, bad debt recovery, patient payment. |
| 8 | `TRANSACTION_SUB_TYPE` | VARCHAR(40) | NOT NULL |  | The transaction sub type associated with the transaction type (i.e. commercial insturance payment, refund payment). |
| 9 | `TRANSACTION_TYPE` | VARCHAR(40) | NOT NULL |  | The transaction type associated with the transaction type code value (i.e. adjustment, charge, payment). |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (7)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_TRANSACTION_TYPE_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_TRANSACTION_TYPE_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_TRANSACTION_TYPE_ID` |
| [RC_F_GENERAL_AR_BAL_TRANS](RC_F_GENERAL_AR_BAL_TRANS.md) | `RC_D_TRANSACTION_TYPE_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_TRANSACTION_TYPE_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_TRANSACTION_TYPE_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_TRANSACTION_TYPE_ID` |

