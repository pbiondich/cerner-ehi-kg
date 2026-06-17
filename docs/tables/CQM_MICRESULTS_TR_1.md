# CQM_MICRESULTS_TR_1

> he CQM listener trigger table contains the administrative data for the processing of a trigger exploded CQM transaction by a listener application. This table contains data for the MDI Results application.

**Description:** MDI Results CQM Listener Trigger #1  
**Table type:** ACTIVITY  
**Primary key:** `TRIGGER_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMPLETION_SEQUENCE_ID` | DOUBLE |  |  | This is the value that unique identifies the transaction completion order by the listener application. It is an internal system assigned number. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 4 | `DEBUG_IND` | DOUBLE |  |  | Defines whether debugging is active or inactive for the listener trigger explosion event unidentifie in this row. |
| 5 | `LAST_RETRY_DT_TM` | DATETIME |  |  | The date and time of the last retry to process this trigger exploded transaction row. This field may or may not be used by the listener application. |
| 6 | `LISTENER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CQM listener configuration table. It is an internal system assigned number. |
| 7 | `L_R_PROCESS_STATUS_FLAG` | DOUBLE |  |  | The last retry processing state for this trigger exploded transaction row. This field may or may not be used by the listener application. |
| 8 | `L_R_TRIGGER_STATUS_TEXT` | VARCHAR(132) |  |  | The last retry processing text for this trigger exploded transaction row. This field may or may not be used by the listener application. |
| 9 | `NUMBER_OF_RETRIES` | DOUBLE |  |  | Set to 0 on insert. Optionally incremented by 1 by the listener application to specify the number of times the listener attempted to process the trigger exploded transaction. |
| 10 | `PRIORITY` | DOUBLE | NOT NULL |  | Identifies the priority of this transaction row that may or may not be used to process in a prioritized method. The value range for priority is 1 throug 99, highest to lowest, respectively. |
| 11 | `PROCESS_START_DT_TM` | DATETIME |  |  | The date and time the listener application started processing on this exploded transaction. |
| 12 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | The current processing state for this trigger exploded transaction row. |
| 13 | `PROCESS_STOP_DT_TM` | DATETIME |  |  | The date and time the listener application completed processing on this exploded transaction. |
| 14 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | CQM Sequence ID |
| 15 | `SCHEDULE_DT_TM` | DATETIME | NOT NULL |  | The date and time this exploded transaction row is scheduled for processing. |
| 16 | `TRIGGER_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the CQM listener trigger table. It is an internal system assigned number. |
| 17 | `TRIGGER_STATUS_TEXT` | VARCHAR(132) |  |  | The status text associated with the processing status flag. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERBOSITY_FLAG` | DOUBLE |  |  | Defines the verbosity level during debugging for the processing of the transaction. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LISTENER_ID` | [CQM_LISTENER_CONFIG](CQM_LISTENER_CONFIG.md) | `LISTENER_ID` |
| `QUEUE_ID` | [CQM_MICRESULTS_QUE](CQM_MICRESULTS_QUE.md) | `QUEUE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CQM_MICRESULTS_LOG](CQM_MICRESULTS_LOG.md) | `TRIGGER_ID` |

