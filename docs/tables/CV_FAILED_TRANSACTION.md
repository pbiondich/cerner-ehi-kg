# CV_FAILED_TRANSACTION

> Stores the CVNet services Transaction failure information

**Description:** CV FAILED TRANSACTIONS  
**Table type:** ACTIVITY  
**Primary key:** `CV_FAILED_TRANSACTION_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CV_FAILED_TRANSACTION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `ORDER_ID` | DOUBLE |  | FK→ | An Unique ID which identifies the procedure (ORDER) for which the transaction is failed(can be duplicate) |
| 3 | `TRANSACTION_ACTION` | VARCHAR(255) |  |  | It signifies the transaction Action or workflow which is invoked when the transaction failed eg:save/sign/match/unlink |
| 4 | `TRANSACTION_CORRELATION_IDENT` | VARCHAR(2000) |  |  | It store the correlation id of the transaction which has failed. It is basically a unique id generated for every transaction(optional) requestid |
| 5 | `TRANSACTION_FAILURE_REASON` | VARCHAR(4000) |  |  | It stores the failure reason when a transaction fails. Usually the response status message(if any) when transaction fails. |
| 6 | `TRANSACTION_NAME` | VARCHAR(255) |  |  | It stores the information about the source where the transaction has failed. Eg. ExamStatusAPI v2reportstatusAPI CCL_script_name |
| 7 | `TRANSACTION_RETRY_CNT` | DOUBLE |  |  | Number of retry attempts |
| 8 | `TRANSACTION_SEQUENCE` | DOUBLE |  |  | The sequence of the transaction |
| 9 | `TRANSACTION_SOURCE` | VARCHAR(255) |  |  | It signifies the transaction source/module from where the transaction has failed Eg- report-inbound CCL |
| 10 | `TRANSACTION_SUCCESS_IND` | DOUBLE |  |  | This will capture the status of the transaction. By default it will be 0 indicating failed. Once replay action is success then it will be updated to True/1 |
| 11 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CV_FAILED_TRAN_BLOB](CV_FAILED_TRAN_BLOB.md) | `CV_FAILED_TRANSACTION_ID` |

