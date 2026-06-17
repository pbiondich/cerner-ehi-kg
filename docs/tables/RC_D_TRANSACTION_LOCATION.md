# RC_D_TRANSACTION_LOCATION

> Contains information about the transaction location.

**Description:** Revenue Cycle Dimension Transaction Location  
**Table type:** REFERENCE  
**Primary key:** `RC_D_TRANSACTION_LOCATION_ID`  
**Columns:** 17  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 6 | `LOCATION_DESCRIPTION` | VARCHAR(255) |  |  | Represents the full description of the transaction's location |
| 7 | `LOCATION_NAME` | VARCHAR(255) |  |  | Represents the name of the transaction's location |
| 8 | `LOCATION_NAME_KEY` | VARCHAR(255) |  |  | Represents the transaction's location in uppercase with all spaces and symbols removed. |
| 9 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Represents the transaction's logical domain. |
| 10 | `MILL_ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Represents the transaction's organization |
| 11 | `MILL_PAYMENT_LOCATION_ID` | DOUBLE | NOT NULL |  | Represents the payment location for the transaction |
| 12 | `RC_D_TRANSACTION_LOCATION_ID` | DOUBLE | NOT NULL | PK | Contains information on the location of the transactions. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_TRANSACTION_LOCATION_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_TRANSACTION_LOCATION_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_TRANSACTION_LOCATION_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_TRANSACTION_LOCATION_ID` |

