# DM_REFCHG_PROCESS

> This table will be used to track RDDS Processes

**Description:** Data Management REFCHG Processes  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_REFCHG_PROCESS_ID` | DOUBLE | NOT NULL |  | Primary Key of table |
| 2 | `ENV_SOURCE_ID` | DOUBLE | NOT NULL |  | The source environment where the process is grabbing data from |
| 3 | `LAST_ACTION_DT_TM` | DATETIME |  |  | The last time/date that the process running hit a check point. |
| 4 | `LOG_FILE` | VARCHAR(80) |  |  | Log File of Process that is running |
| 5 | `PROCESS_NAME` | VARCHAR(12) | NOT NULL |  | Current Process value from V$Session |
| 6 | `RDBHANDLE_VALUE` | DOUBLE | NOT NULL |  | Current RDBHANDLE of session |
| 7 | `REFCHG_STATUS` | VARCHAR(20) |  |  | Status of Process. The status that the process is currently in (Starting, In Process, Finished, etc.) |
| 8 | `REFCHG_TYPE` | VARCHAR(20) | NOT NULL |  | The type of process that is being run (RDDS MOVER, RDDS CUTOVER, etc.) |
| 9 | `SERIAL_NUMBER` | DOUBLE | NOT NULL |  | SERIAL# from GV$SESSION for process |
| 10 | `SESSION_SID` | DOUBLE | NOT NULL |  | SID from GV$SESSION for process |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

