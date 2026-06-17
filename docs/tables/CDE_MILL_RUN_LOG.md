# CDE_MILL_RUN_LOG

> Contains extract run history for PowerInsight

**Description:** CDE_MILL_RUN_LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDE_MILL_RUN_LOG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDE_MILL_RUN_LOG table. |
| 2 | `CONFIG_BITMAP` | DOUBLE |  |  | Is a bit mask used for configuration. |
| 3 | `EXTRACT_BEGIN_DT_TM` | DATETIME |  |  | The range begin date time for the extract. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the extract started. |
| 5 | `EXTRACT_END_DT_TM` | DATETIME |  |  | The range end date time for the extract. |
| 6 | `FILE_TYPE` | VARCHAR(100) |  |  | File type of the script. |
| 7 | `PARENT_PROCESS_NBR` | DOUBLE |  |  | The parent process id from the Unix server. |
| 8 | `PROCESS_NBR` | DOUBLE |  |  | The process id from the Unix server. |
| 9 | `RUN_FLAG` | DOUBLE |  |  | The type of extract run. 1- Daily, 2 - Historical, 3 - Manual. |
| 10 | `SCRIPT_BEGIN_DT_TM` | DATETIME |  |  | The date and time the extract script started running. |
| 11 | `SCRIPT_END_DT_TM` | DATETIME |  |  | The date and time the extract script stopped running. |
| 12 | `SCRIPT_NAME` | VARCHAR(100) |  |  | Name of the extract CCL script |
| 13 | `SOURCE_CNT` | DOUBLE |  |  | The number of records the extracted scripted extracted. |
| 14 | `STATUS_FLAG` | DOUBLE |  |  | The status of the extract. 1 - Not run, 2 - Running, 3 - Succeeded, 4 - Failed, 5 - Skipped. |
| 15 | `SUBJECT_AREA_NAME` | VARCHAR(100) |  |  | The name of the subject area. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

