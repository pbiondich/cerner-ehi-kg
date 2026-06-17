# RC_D_TRANSACTION_BATCH

> This table contains transaction batch information such as batch alias and batch description.

**Description:** Revenue Cycle Dimension Transaction Batch  
**Table type:** ACTIVITY  
**Primary key:** `RC_D_TRANSACTION_BATCH_ID`  
**Columns:** 16  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BATCH_ALIAS` | VARCHAR(40) | NOT NULL |  | The user-defined batch alias for the associated transaction batch. |
| 3 | `BATCH_DESCRIPTION` | VARCHAR(100) | NOT NULL |  | The description associated with the transaction batch. |
| 4 | `BATCH_TYPE` | VARCHAR(40) | NOT NULL |  | Defines the type of batch, for example: EDI, Cash Drawer, IMAcs, etc. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 9 | `MILL_BATCH_TRANS_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Millennium batch transaction from which this data was derived. |
| 10 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 11 | `RC_D_TRANSACTION_BATCH_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies transaction batch information such as batch alias and batch description. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_TRANSACTION_BATCH_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_TRANSACTION_BATCH_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_TRANSACTION_BATCH_ID` |
| [RC_F_GENERAL_AR_BAL_TRANS](RC_F_GENERAL_AR_BAL_TRANS.md) | `RC_D_TRANSACTION_BATCH_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_TRANSACTION_BATCH_ID` |

