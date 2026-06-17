# EA_PROCESSING_RECORD

> This table keeps records of services being processed for EA

**Description:** ENTERPRISE AUTHENTICATION PROCESSING REORDS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TXT` | VARCHAR(100) |  |  | The main service (Shadow Accounts) identifies actions performed - such as a password rotation (all user passwords are rotated to a new password based on an existing key), or a user sync where any new accounts are added and unnecessary accounts are removed. |
| 2 | `EA_PROCESSING_RECORD_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `INFO_TXT` | VARCHAR(1024) |  |  | Info just gives general information about the transaction that was taking place. It is stored as json info, with an example being { "insert":"200", "modify": "0", "no_change":"0", "failure_message" : "exception message"} |
| 4 | `SERVICE_TXT` | VARCHAR(100) |  |  | A Service is related to what is being "processed" which would be the shadow accounts agent for example. ; This field could be an indicator that the shadow accounts is the service being run. |
| 5 | `START_DT_TM` | DATETIME |  |  | Date and time the action began |
| 6 | `STATUS_FLAG` | DOUBLE |  |  | The status of the action. 0=Pending 1=In-progress 2=Failed 3=Cancelled |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

