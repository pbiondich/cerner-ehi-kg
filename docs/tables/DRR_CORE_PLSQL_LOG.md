# DRR_CORE_PLSQL_LOG

> stores execution log for DRR core process

**Description:** DRR_CORE_PLSQL_LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | VARCHAR(100) |  |  | store PLSQL ACTION START/COMPLETE/FAILED sys_context('userenv','action') |
| 2 | `BACK_TRACE` | VARCHAR(4000) |  |  | store dbms_utility.format_error_backtrace |
| 3 | `CALL_STACK` | VARCHAR(4000) |  |  | store dbms_utility.format_call_stack |
| 4 | `CLIENT_INFO` | VARCHAR(64) |  |  |  |
| 5 | `DRR_CORE_PLSQL_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `ERROR_STACK` | VARCHAR(4000) |  |  | store error code from dbms_utility.format_error_stack |
| 7 | `LINE_NO` | VARCHAR(100) |  |  | line_no where error occured |
| 8 | `MODULE` | VARCHAR(100) | NOT NULL |  | store PLSQL MODULE sys_context('userenv','module') PROC/FUNC NAME |
| 9 | `PROCESS_INFO` | VARCHAR(255) |  |  |  |
| 10 | `SESSIONID` | DOUBLE |  |  | store process sessionid to_number(sys_context('USERENV','SESSIONID')) |
| 11 | `SID` | DOUBLE |  |  | store process SID to_number(sys_context('userenv','sid')) |
| 12 | `TIME_STAMP_TS` | DATETIME(6) |  |  | store logging timestamp |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

