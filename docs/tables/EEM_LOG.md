# EEM_LOG

> EEM transactions are logged here.

**Description:** EEM transaction log.  
**Table type:** ACTIVITY  
**Primary key:** `LOG_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CD` | DOUBLE | NOT NULL |  | The Action that happened when this row was logged. |
| 2 | `ACTION_MEANING` | VARCHAR(12) |  |  | The meaning of the code value in the action_cd column. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CACHED_IND` | DOUBLE | NOT NULL |  | Indicates if the interchange ID used in the Tx is the same as a previous transaction. |
| 6 | `DATA_DT_TM` | DATETIME | NOT NULL |  | Data date and time. |
| 7 | `DATA_FLAG` | DOUBLE | NOT NULL |  | Data flag. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Interchange ID. Refers to interchange_id on the EEM_TRANSACTION table. It is the Primary identifier for a transaction but is not the PK of the EEM_TRANSACTION table. |
| 10 | `LOG_ID` | DOUBLE | NOT NULL | PK | Log ID. |
| 11 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Primary Key to LONG_TEXT_REFERENCE table. OBSOLETE, this column is no longer used. |
| 12 | `MODIFY_REASON_CD` | DOUBLE | NOT NULL |  | Reason for manually modifying the transactions data status. |
| 13 | `POLL_DT_TM` | DATETIME | NOT NULL |  | Poll date and time. |
| 14 | `POLL_RESPONSE_IND` | DOUBLE | NOT NULL |  | Indicates if data was returned or not on a POLL action. |
| 15 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The profile associated to this log. |
| 16 | `PROXY_FLAG` | DOUBLE | NOT NULL |  | Proxy flag. |
| 17 | `REPLY_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates if the reply action is a PENDING or a RECEIVED type. |
| 18 | `REPLY_STATUS_MEANING` | VARCHAR(12) |  |  | Indicates if the reply action is a PENDING or a RECEIVED type. |
| 19 | `TRANS_DATA_MOD_CD` | DOUBLE | NOT NULL |  | Describes the status of a transaction message as determined by a user's review of the message. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `USER_ID` | DOUBLE | NOT NULL |  | User ID. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EEM_LOG_BLOB](EEM_LOG_BLOB.md) | `EEM_LOG_ID` |

