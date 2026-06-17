# SI_ALERT_EVENT

> Table containing a record of alert events encountered during interface processing

**Description:** System Integration Alert Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_STATUS_TFLG` | VARCHAR(10) | NOT NULL |  | Text value that represents the status of this row. The possible values for alert_status_tflg are Active and Cleared |
| 2 | `ALERT_TYPE_TFLG` | VARCHAR(30) | NOT NULL |  | Text value that classifies the alert type. Current alert_type_tflg values are: LOAD_SCRIPT - ROUTE_SCRIPT - FORMAT_SCRIPT - TCP_IP - TERMINATION - INITIALIZATION - ROUTE_QUEUE - ROUTE_SRV -; ROUTE_FORMAT - NO_PERSONALITY - ROUTE_LIST - NO_CUST_ROUTE - FORWARD_TO_EJS - DATABASE - MEMORY_ALLOC - ESO_TERMINATE |
| 3 | `APPLICATION_NAME` | VARCHAR(12) | NOT NULL |  | The application name denotes a specific functional area of System Integration processing. |
| 4 | `CLEAR_DT_TM` | DATETIME |  |  | The date and time that the alert event ended. |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time that the alert event occurred. |
| 6 | `ERROR_TXT` | VARCHAR(500) |  |  | Error message from the process that created the alert event. |
| 7 | `EXPIRE_DT_TM` | DATETIME |  |  | The date and time when an extendable alert automatically clears. |
| 8 | `FSIESO_TRIGGER_ID` | DOUBLE |  | FK→ | the transaction trigger_id generated during the context of an ESO transaction and is stored in the cqm_fsieso_tr_1 as the trigger_id field. |
| 9 | `INSTANCE_NBR` | DOUBLE |  |  | Server instance number. |
| 10 | `LISTENER_ALIAS` | VARCHAR(48) | NOT NULL |  | LISTENER_ALIAS value from table cqm_listener_config |
| 11 | `NODE_NAME` | VARCHAR(64) |  |  | Node on which the server generating the alert is running on. |
| 12 | `OENINTERFACE_TRIGGER_ID` | DOUBLE |  | FK→ | the transaction trigger_id generated during the context of an OEN transaction and is stored in the cqm_oeninterface_tr_1 as the trigger_id field. |
| 13 | `PROCESS_NAME` | VARCHAR(32) | NOT NULL |  | The name of the interface server process. This a core server or interface communication server process. |
| 14 | `SCP_NBR` | DOUBLE |  |  | SCP entry number for the interface server. |
| 15 | `SI_ALERT_EVENT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 16 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FSIESO_TRIGGER_ID` | [CQM_FSIESO_TR_1](CQM_FSIESO_TR_1.md) | `TRIGGER_ID` |
| `OENINTERFACE_TRIGGER_ID` | [CQM_OENINTERFACE_TR_1](CQM_OENINTERFACE_TR_1.md) | `TRIGGER_ID` |

