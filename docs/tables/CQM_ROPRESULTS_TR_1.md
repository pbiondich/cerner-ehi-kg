# CQM_ROPRESULTS_TR_1

> This table will send a notificiation to the MDI Result Client server telling it that there are records to be processed when new result records are inserted.

**Description:** Contains POC result trigger information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMPLETION_SEQUENCE_ID` | DOUBLE | NOT NULL |  | not applicable to MDIColumn |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Record creation date/time.Column |
| 4 | `DEBUG_IND` | DOUBLE |  |  | not applicable to MDIColumn |
| 5 | `LAST_RETRY_DT_TM` | DATETIME |  |  | not applicable to MDIColumn |
| 6 | `LISTENER_ID` | DOUBLE | NOT NULL |  | Represents what MDI server is going to be reading this record.Column |
| 7 | `L_R_PROCESS_STATUS_FLAG` | DOUBLE |  |  | Not applicable to MDIColumn |
| 8 | `L_R_TRIGGER_STATUS_TEXT` | VARCHAR(132) |  |  | Comment explaining the Process Status FlagColumn |
| 9 | `NUMBER_OF_RETRIES` | DOUBLE |  |  | Not applicable to MDIColumn |
| 10 | `PRIORITY` | DOUBLE | NOT NULL |  | Not applicable to MDIColumn |
| 11 | `PROCESS_START_DT_TM` | DATETIME |  |  | When the MDI Result server began processing the recordColumn |
| 12 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | Represents the status of the recordColumn |
| 13 | `PROCESS_STOP_DT_TM` | DATETIME |  |  | When the MDI Result Server completed processing of the recordColumn |
| 14 | `QUEUE_ID` | DOUBLE | NOT NULL |  | Represents a specific record found on the cqm_ropresults_que table.Column |
| 15 | `SCHEDULE_DT_TM` | DATETIME | NOT NULL |  | Not applicable to MDIColumn |
| 16 | `TRIGGER_ID` | DOUBLE | NOT NULL |  | table keyColumn |
| 17 | `TRIGGER_STATUS_TEXT` | VARCHAR(132) |  |  | Comment explaining the Process Status FlagColumn |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERBOSITY_FLAG` | DOUBLE |  |  | Not applicable to MDIColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

