# EEM_TRANSACTION

> EEM Transaction is the parent table for all EEM transactions. One row represents a single outbound and inbound transaction with high level summary data pertaining to it's status.

**Description:** EEM transaction.  
**Table type:** ACTIVITY  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 28  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DATA_EXPIRE_DT_TM` | DATETIME | NOT NULL |  | Date and time that the data expires. |
| 4 | `DATA_FLAG` | DOUBLE | NOT NULL |  | Describes the current state of the transaction. 0 - Pending/Unknown, 1 - Eligible/Verified, 2 - Not Eligible/Denied, 3 - Returned/Ambiguous, 4 - Error, 5 - Template, 6 - Eligible (invalid card). |
| 5 | `DATA_SIZE` | DOUBLE | NOT NULL |  | Size, in bytes, of the data blob. |
| 6 | `EEM_BATCH_ID` | DOUBLE | NOT NULL | FK→ | obsolete column - creation of EEM_BATCH_JOB table renders this column no longer needed |
| 7 | `EEM_JOB_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the EEM job. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `HASH_KEY` | VARCHAR(60) | NOT NULL |  | Hash key of all required inputs. Used to determine duplicate transactions. |
| 10 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Interchange ID. refers to interchange_id on the EEM_TRANSACTION table. That column is a unique index on the table not the PK. |
| 11 | `INTERCHANGE_UUID` | VARCHAR(40) |  |  | Contains the universally unique identifier for a transaction. This is an alias of the interchange_id column. |
| 12 | `PARENT_ID` | DOUBLE | NOT NULL |  | ID of the parent table. |
| 13 | `PARENT_TABLE` | VARCHAR(32) | NOT NULL |  | Table name of parent. |
| 14 | `POLL_EXPIRE_DT_TM` | DATETIME | NOT NULL |  | Date and time that polling should expire. |
| 15 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the profile used for the transaction. A profile contains reference data for outbound messages and is optional. |
| 16 | `RECV_TIME` | DOUBLE |  |  | Time in milliseconds that message was received. (starting from 1/1/1970) |
| 17 | `SENT_TIME` | DOUBLE |  |  | Time in milliseconds that message was sent. (starting from 1/1/1970) |
| 18 | `TRANSACTION_CD` | DOUBLE | NOT NULL |  | The type of transaction the row represents. |
| 19 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Primary key of this table. |
| 20 | `TRANSACTION_MEANING` | VARCHAR(12) |  |  | The type of transaction the row represents. |
| 21 | `TRANS_DATA_CD` | DOUBLE | NOT NULL |  | Describes the status of a transaction message based on the system's business rules. |
| 22 | `TRANS_DATA_MOD_CD` | DOUBLE | NOT NULL |  | Describes the status of a transaction message as determined by a user's review of the message. |
| 23 | `TRANS_STATUS_CD` | DOUBLE | NOT NULL |  | This column can be used to check how far the transaction reached in case transactions are not working. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EEM_BATCH_ID` | [EEM_BATCH](EEM_BATCH.md) | `EEM_BATCH_ID` |
| `EEM_JOB_ID` | [EEM_JOB](EEM_JOB.md) | `EEM_JOB_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AUTHORIZATION](AUTHORIZATION.md) | `INTERCHANGE_ID` |
| [EEM_ELIG_SVC_DETAIL](EEM_ELIG_SVC_DETAIL.md) | `INTERCHANGE_ID` |

