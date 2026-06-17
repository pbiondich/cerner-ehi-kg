# CQM_OENTXLOG_QUE

> This table holds the Open Engine transactions we've received and sent.

**Description:** CQM OENTXLOG QUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLASS` | VARCHAR(15) |  |  | Holds the Interface ID that wrote to the queue.Column |
| 3 | `CONTRIBUTOR_EVENT_DT_TM` | DATETIME |  |  | Holds date/time when a transaction was written to the queue.Column |
| 4 | `CONTRIBUTOR_ID` | DOUBLE | NOT NULL |  | Contributor ID of the contributor writing to the queue.Column |
| 5 | `CONTRIBUTOR_REFNUM` | VARCHAR(48) | NOT NULL |  | Reference number for contributor.Column |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date/time this transaction was written.Column |
| 7 | `CREATE_RETURN_FLAG` | DOUBLE |  |  | Return flag.Column |
| 8 | `CREATE_RETURN_TEXT` | VARCHAR(132) |  |  | Return text.Column |
| 9 | `DEBUG_IND` | DOUBLE |  |  | Debug indicator.Column |
| 10 | `MESSAGE` | LONGBLOB |  |  | The transaction receive/sent.Column |
| 11 | `MESSAGE_LEN` | DOUBLE | NOT NULL |  | Length of the transaction.Column |
| 12 | `PARAM_LIST_IND` | DOUBLE |  |  | Param list.Column |
| 13 | `PRIORITY` | DOUBLE | NOT NULL |  | If the transaction is replayed, this is the priority to be used when re-queuing.Column |
| 14 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | Used for replaying.Column |
| 15 | `QUEUE_ID` | DOUBLE | NOT NULL |  | Unique ID for this transaction.Column |
| 16 | `SUBTYPE` | VARCHAR(15) |  |  | Sub type of transaction.Column |
| 17 | `SUBTYPE_DETAIL` | VARCHAR(15) |  |  | Detail sub type of transaction.Column |
| 18 | `TRIG_CREATE_END_DT_TM` | DATETIME |  |  | Trigger end date/time.Column |
| 19 | `TRIG_CREATE_START_DT_TM` | DATETIME |  |  | Trigger start date/time.Column |
| 20 | `TRIG_MODULE_IDENTIFIER` | VARCHAR(16) |  |  | Trigger module identifier.Column |
| 21 | `TYPE` | VARCHAR(15) |  |  | Type of message.Column |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VERBOSITY_FLAG` | DOUBLE |  |  | Verbosity flag.Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

