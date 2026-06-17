# NURSING_TRANSACTION_INFO

> Keeps track of the transaction IDs tht have been or are in the process of being completed.

**Description:** Nursing Transaction Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_NURSING_TRANSACTION_ID` | DOUBLE | NOT NULL |  | Parent Transaction ID that groups together all attempts to process a given set of data. Each submittal of the same data will window up with the same parent ID. |
| 2 | `NURSING_TRANSACTION_INFO_ID` | DOUBLE | NOT NULL |  | Transaction ID used to track a particular transaction already being worked on or completed. This is a unique field. |
| 3 | `PRIMARY_TRANSACTION_IND` | DOUBLE | NOT NULL |  | Specifies if this row is the one where the transaction was processed. The other rows with the same parent_id with an indicator of 0 provide an audit. |
| 4 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time when the transaction ID started being processed. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

