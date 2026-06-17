# CPMPROCESS_ERROR

> When the Process Server encounters errors processing requests, those errors are written to this table.

**Description:** Process Server Errors  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESTINATION_STEP_ID` | DOUBLE | NOT NULL |  | This is the server where the request was trying to go when it encountered errors. |
| 2 | `ERROR_CODE` | DOUBLE |  |  | This is the current error status of this process. |
| 3 | `ERROR_ID` | DOUBLE | NOT NULL |  | This is the unique error number created by processing. |
| 4 | `FORMAT_SCRIPT` | VARCHAR(30) |  |  | This is the name of the script that formatted the target request when it got errors. |
| 5 | `ORIGINAL_ERROR_CODE` | DOUBLE |  |  | This is the error code before any recovery was attempted. |
| 6 | `QUE_ID` | DOUBLE | NOT NULL |  | This is the sequence in the error log for this processes errors. This number will wrap. |
| 7 | `QUE_SEQ` | DOUBLE |  |  | This is the unique number to identify this row in the cpmprocess_que table. It does not wrap. |
| 8 | `RECOVER_SEQ` | DOUBLE |  |  | This number represents the order in which the queued sequences will be recovered. |
| 9 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | This is the unique number of the step whose process is waiting in the recover queue. |
| 10 | `RETRY_ATTEMPTS` | DOUBLE |  |  | This is the number of times the process server has tried to recover this process in the queue. |
| 11 | `SERVICE` | VARCHAR(50) |  |  | This is the name of the server that the process was attempting to send to when the error occurred. |
| 12 | `SRVEXEC_STATUS` | DOUBLE |  |  | This is the specific status returned by SRVEXEC. |
| 13 | `TARGET_REQUEST_NUMBER` | DOUBLE |  |  | This is the process that was being serviced when this error occurred. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

