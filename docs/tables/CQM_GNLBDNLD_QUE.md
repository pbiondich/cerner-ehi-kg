# CQM_GNLBDNLD_QUE

> Contains General Lab instrument orders for bi-directional interfaces.

**Description:** CQM GNLBDNLD QUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLASS` | VARCHAR(15) |  |  | Identifies the trigger explosion class of the transaction. |
| 3 | `CONTRIBUTOR_EVENT_DT_TM` | DATETIME |  |  | Significant date and time associated with the transaction row as supplied by the contributor application |
| 4 | `CONTRIBUTOR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the CQM contributor configuration table. It is an internal system assigned number. |
| 5 | `CONTRIBUTOR_REFNUM` | VARCHAR(48) | NOT NULL |  | A reference or key assigned to the transaction row by the contributor application. It recommended that this identifier be unique although it is not required. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 7 | `CREATE_RETURN_FLAG` | DOUBLE |  |  | create return flagColumn |
| 8 | `CREATE_RETURN_TEXT` | VARCHAR(132) |  |  | Return text string from the trigger explosion process of this transaction row. |
| 9 | `DEBUG_IND` | DOUBLE |  |  | Defines whether debugging is active or inactive for the queue transaction unidentified in this row. |
| 10 | `MESSAGE` | LONGBLOB |  |  | This is the binary longraw field which contains the contents of the original message. |
| 11 | `MESSAGE_LEN` | DOUBLE | NOT NULL |  | The length of the textual or binary object placed in the message field. |
| 12 | `PARAM_LIST_IND` | DOUBLE |  |  | Identifies whether there are row in the queue parameters table associated with this transaction row. |
| 13 | `PRIORITY` | DOUBLE | NOT NULL |  | Identifies the priority of this transaction row that may or may not be used to process in a prioritized method. The value range for priority is 1 through 99, highest to lowest, respectively. |
| 14 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | The current trigger explosion state for this transaction row. |
| 15 | `QUEUE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the CQM queue table. It is an internal system assigned number. |
| 16 | `SUBTYPE` | VARCHAR(15) |  |  | Identifies the trigger explosion subtype of the transaction. |
| 17 | `SUBTYPE_DETAIL` | VARCHAR(15) |  |  | Identifies the trigger explosion subtype detail of the transaction. |
| 18 | `TRIG_CREATE_END_DT_TM` | DATETIME |  |  | The date and time the trigger explosion completed on this transaction row. |
| 19 | `TRIG_CREATE_START_DT_TM` | DATETIME |  |  | The date and time the trigger explosion began on this transaction row. |
| 20 | `TRIG_MODULE_IDENTIFIER` | VARCHAR(16) |  |  | Future. Identifies the process/module which performs the trigger explosion on this transaction row. |
| 21 | `TYPE` | VARCHAR(15) |  |  | Identifies the trigger explosion type of the transaction. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VERBOSITY_FLAG` | DOUBLE |  |  | Defines the verbosity level during debugging for the processing of the transaction. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

