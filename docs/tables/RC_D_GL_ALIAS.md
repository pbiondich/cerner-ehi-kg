# RC_D_GL_ALIAS

> This table contains GL alias information such as company name and account name.

**Description:** Revenue Cycle Dimension General Ledger Alias  
**Table type:** REFERENCE  
**Primary key:** `RC_D_GL_ALIAS_ID`  
**Columns:** 26  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_TYPE` | VARCHAR(40) | NOT NULL |  | Contains a description of the millennium account type code. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `GL_ACCOUNT_ALIAS_DESC` | VARCHAR(255) | NOT NULL |  | The description of the alias for the associated GL account. |
| 7 | `GL_ACCOUNT_NAME` | VARCHAR(100) | NOT NULL |  | The account name associated to a GL alias. |
| 8 | `GL_ACCOUNT_UNIT` | VARCHAR(100) | NOT NULL |  | The account unit associated to a GL alias. |
| 9 | `GL_ACCOUNT_UNIT_ALIAS_DESC` | VARCHAR(255) | NOT NULL |  | The description of the alias for the associated GL account unit. |
| 10 | `GL_COMPANY_ALIAS_DESC` | VARCHAR(255) | NOT NULL |  | The description of the alias for the associated GL company. |
| 11 | `GL_COMPANY_NAME` | VARCHAR(100) | NOT NULL |  | The company name associated to a GL alias. |
| 12 | `GL_COMPANY_UNIT` | VARCHAR(100) | NOT NULL |  | The company unit associated to a GL alias. |
| 13 | `GL_COMPANY_UNIT_ALIAS_DESC` | VARCHAR(255) | NOT NULL |  | The description of the alias for the associated GL company unit. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 15 | `MILL_ACCOUNT_ALIAS_ID` | DOUBLE | NOT NULL |  | Identifies the millennium record from which the account alias was derived. |
| 16 | `MILL_ACCOUNT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the code value indicating the type of account. |
| 17 | `MILL_ACCOUNT_UNIT_ALIAS_ID` | DOUBLE | NOT NULL |  | Identifies the millennium record from which the account unit alias was derived. |
| 18 | `MILL_COMPANY_ALIAS_ID` | DOUBLE | NOT NULL |  | Identifies the millennium record from which the company alias was derived. |
| 19 | `MILL_COMPANY_UNIT_ALIAS_ID` | DOUBLE | NOT NULL |  | Identifies the millennium record from which the company unit alias was derived. |
| 20 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 21 | `RC_D_GL_ALIAS_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies GL alias information such as company name and account name. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (12)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_AR_GL_ALIAS_ID` |
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_GL_ALIAS_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_AR_GL_ALIAS_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_GL_ALIAS_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_GL_ALIAS_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_GL_ALIAS_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_GL_ALIAS_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_GL_ALIAS_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_GL_ALIAS_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_OTHER_GL_ALIAS_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_AR_GL_ALIAS_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_GL_ALIAS_ID` |

