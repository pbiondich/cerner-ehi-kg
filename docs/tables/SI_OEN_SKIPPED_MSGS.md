# SI_OEN_SKIPPED_MSGS

> Table containing a record of transactions skipped due to processing issues

**Description:** System Integration OEN Skipped Messages  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ERROR_TXT` | VARCHAR(500) |  |  | Error message for the event that resulted in the transaction getting skipped by the interface |
| 2 | `ERROR_TYPE_TXT` | VARCHAR(30) |  |  | Text value that classifies the error. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier of the interface from the appropriate configuration model. A PK value from the table identified in PARENT_ENTITY_NAME. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the configuration model for the interface ( A table name - currently either OEN_PROCINFO or SI_OEN_COMCHANNEL ) |
| 5 | `PROCESS_PHASE_TXT` | VARCHAR(30) |  |  | Text value that indicates what phase of processing the interface was in when the error occurred. |
| 6 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The queue_id of the transaction from the cqm_oeninterface_que table, if available. |
| 7 | `SCRIPT_NAME` | VARCHAR(50) |  |  | Name of the script that was being executed when the error occurred, if applicable. |
| 8 | `SI_OEN_SKIPPED_MSGS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `SKIPPED_DT_TM` | DATETIME |  |  | The date and time that the transaction was skipped by the interface |
| 10 | `STATUS_DT_TM` | DATETIME |  |  | The date and time of the last change in the status of the row. |
| 11 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the last user to change the status of the row. |
| 12 | `STATUS_TXT` | VARCHAR(20) |  |  | Text value that represents the status of this row. It is used to indicate if a user has looked at the message that was skipped and what action the user might have taken. |
| 13 | `TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | The trigger_id of the transaction from the cqm_oeninterface_tr_1 table, if available. |
| 14 | `TX_KEY_TXT` | VARCHAR(27) |  |  | Key for the transaction stored on the OEN_TXLOG table, if available. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `STATUS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRIGGER_ID` | [CQM_OENINTERFACE_TR_1](CQM_OENINTERFACE_TR_1.md) | `TRIGGER_ID` |

