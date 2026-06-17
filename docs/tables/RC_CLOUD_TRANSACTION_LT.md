# RC_CLOUD_TRANSACTION_LT

> Used to store long text data for requests and replies for revenue cycle cloud transactions

**Description:** Revenue Cycle Cloud Transaction Long Text  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LONG_CLOB` | LONGTEXT |  |  | Used to store large amounts of text. |
| 2 | `LONG_CLOB_FORMAT_FLAG` | DOUBLE | NOT NULL |  | The format of the long_clob text. |
| 3 | `LONG_CLOB_TYPE_FLAG` | DOUBLE | NOT NULL |  | The flag representing the type of the long text. |
| 4 | `RC_CLOUD_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | System Generated Identifer created to uniquely identify a row on the RC_CLOUD_TRANSACTION table. |
| 5 | `RC_CLOUD_TRANSACTION_LT_ID` | DOUBLE | NOT NULL |  | A system generated number to uniquely identify a row on the RC_CLOUD_TRANSACTION_LT table. |
| 6 | `RETRY_CNT` | DOUBLE |  |  | Represents the retry count of the service when the request was sent. |
| 7 | `TRANSACTION_DT_TM` | DATETIME |  |  | The date and time the transaction occurred. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_CLOUD_TRANSACTION_ID` | [RC_CLOUD_TRANSACTION](RC_CLOUD_TRANSACTION.md) | `RC_CLOUD_TRANSACTION_ID` |

