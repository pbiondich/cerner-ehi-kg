# TRANSACTION_BATCH_LOG

> The Transaction Batch Log links groups of transactions to the parent process that initiated the batch.

**Description:** Transaction Batch Log  
**Table type:** ACTIVITY  
**Primary key:** `TRANSACTION_BATCH_LOG_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETE_DT_TM` | DATETIME |  |  | The date and time this batch completed processing. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The parent entity identifier to which the batch belongs. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The parent entity table name to which the batch belongs. |
| 4 | `SUBMIT_DT_TM` | DATETIME | NOT NULL |  | Date and time the batch was submitted for processing. |
| 5 | `TRANSACTION_BATCH_LOG_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the TRANSACTION_BATCH_LOG table. |
| 6 | `TRANSACTION_BATCH_RUN_TYPE_CD` | DOUBLE | NOT NULL |  | Denotes what type of process triggered the batch process. (e.g.: Custom, System) |
| 7 | `TRANSACTION_BATCH_TYPE_CD` | DOUBLE | NOT NULL |  | The type of transaction that was processed in a batch. (e.g.: Eligibility) |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRANSACTION_ELIGIBILITY](TRANSACTION_ELIGIBILITY.md) | `TRANSACTION_BATCH_LOG_ID` |

