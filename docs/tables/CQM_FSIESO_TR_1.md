# CQM_FSIESO_TR_1

> The CQM listener trigger table contains the administrative data for the processing of a trigger exploded CQM transaction by a listener application. This table contains data for the FSI ESO application.

**Description:** FSI ESO Listener Trigger #1  
**Table type:** ACTIVITY  
**Primary key:** `TRIGGER_ID`  
**Columns:** 26  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMPLETION_SEQUENCE_ID` | DOUBLE | NOT NULL |  | This is the value that unique identifies the transaction completion order by the listener application. It is an internal system assigned number. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 4 | `DEBUG_IND` | DOUBLE |  |  | Defines whether debugging is active or inactive for the listener trigger explosion event unidentifie in this row. |
| 5 | `ESO_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the eso_trigger table. It is an internal system assigned number. |
| 6 | `LAST_RETRY_DT_TM` | DATETIME |  |  | The date and time of the last retry to process this trigger exploded transaction row. This field may or may not be used by the listener application. |
| 7 | `LISTENER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the CQM listener configuration table. It is an internal system assigned number. |
| 8 | `L_R_PROCESS_STATUS_FLAG` | DOUBLE |  |  | The last retry processing state for this trigger exploded transaction row. This field may or may not be used by the listener application. |
| 9 | `L_R_TRIGGER_STATUS_TEXT` | VARCHAR(132) |  |  | The last retry processing text for this trigger exploded transaction row. This field may or may not be used by the listener application. |
| 10 | `MESSAGE_SEQUENCE` | DOUBLE | NOT NULL |  | This is a numeric value that determines the order in which the messages will be processed. It is based on the date and time that the row was inserted. |
| 11 | `NUMBER_OF_RETRIES` | DOUBLE |  |  | Set to 0 on insert. Optionally incremented by 1 by the listener application to specify the number of times the listener attempted to process the trigger exploded transaction. |
| 12 | `PRIORITY` | DOUBLE |  |  | Identifies the priority of this transaction row that may or may not be used to process in a prioritized method. The value range for priority is 1 throug 99, highest to lowest, respectively. |
| 13 | `PROCESS_START_DT_TM` | DATETIME |  |  | The date and time the listener application started processing on this exploded transaction. |
| 14 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | The current processing state for this trigger exploded transaction row. |
| 15 | `PROCESS_STOP_DT_TM` | DATETIME |  |  | The date and time the listener application completed processing on this exploded transaction. |
| 16 | `QUEUE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the CQM queue table. It is an internal system assigned number. |
| 17 | `SCHEDULE_DT_TM` | DATETIME | NOT NULL |  | The date and time this exploded transaction row is scheduled for processing. |
| 18 | `TRANSACTION_TIME_IN_SECONDS` | DOUBLE |  |  | Stores the elapsed time in seconds for an entire transaction in ESO |
| 19 | `TRIGGER_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the CQM listener trigger table. It is an internal system assigned number. |
| 20 | `TRIGGER_STATUS_TEXT` | VARCHAR(132) |  |  | The status text associated with the processing status flag. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VERBOSITY_FLAG` | DOUBLE |  |  | Defines the verbosity level during debugging for the processing of the transaction. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ESO_TRIGGER_ID` | [ESO_TRIGGER](ESO_TRIGGER.md) | `TRIGGER_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `TRIGGER_ID` |
| [HOLD_QUEUE](HOLD_QUEUE.md) | `TRIGGER_ID` |
| [SI_ALERT_EVENT](SI_ALERT_EVENT.md) | `FSIESO_TRIGGER_ID` |
| [SI_DOCUMENT_TRANSACTION_LOG](SI_DOCUMENT_TRANSACTION_LOG.md) | `ESO_TRIGGER_ID` |

