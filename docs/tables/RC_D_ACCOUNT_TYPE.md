# RC_D_ACCOUNT_TYPE

> Stores the details of the Account Type and Sub Type.

**Description:** Revenue Cycle Dimension Account Type  
**Table type:** REFERENCE  
**Primary key:** `RC_D_ACCOUNT_TYPE_ID`  
**Columns:** 12  
**Referenced by:** 14 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_SUB_TYPE` | VARCHAR(50) | NOT NULL |  | Description of the account sub type. |
| 2 | `ACCOUNT_TYPE` | VARCHAR(50) | NOT NULL |  | Description of the account type. For example: Patient, Cash, Revenue |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 4 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 5 | `MILL_ACCOUNT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Holds the account type code stored in the Millennium code set. |
| 6 | `MILL_ACCOUNT_TYPE_CD` | DOUBLE | NOT NULL |  | Holds the account type code number associated with the account type stored in Millennium. |
| 7 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | PK | Unique genereated number that identifies a single row on the rc_d_account_type table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (14)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_ALL_AR_SMRY](RC_F_ALL_AR_SMRY.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_GENERAL_AR_BAL_TRANS](RC_F_GENERAL_AR_BAL_TRANS.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_INVOICE_AR_BAL_INV](RC_F_INVOICE_AR_BAL_INV.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_INVOICE_AR_BAL_SMRY](RC_F_INVOICE_AR_BAL_SMRY.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_NON_AR_BALANCE](RC_F_NON_AR_BALANCE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_ACCOUNT_TYPE_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_ACCOUNT_TYPE_ID` |

