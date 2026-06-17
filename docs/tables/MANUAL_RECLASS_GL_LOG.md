# MANUAL_RECLASS_GL_LOG

> We need to store a log when client runs the reclass utility tool pft_manual_reclass_gl. The log entries include starting time, ending time, user ID, the number of activity ids, and the input filename.

**Description:** Manual Reclass General Ledger Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME | NOT NULL |  | The beginning time of the reclass GL Alias job. |
| 2 | `END_DT_TM` | DATETIME | NOT NULL |  | The ending time of the reclass GL Alias job. |
| 3 | `ERROR_MSG_TXT` | VARCHAR(4000) |  |  | The error message of the finished reclass GL Alias job. |
| 4 | `INCOMING_ACTIVITY_IDS_CNT` | DOUBLE | NOT NULL |  | The total count of activity IDs in the input file. |
| 5 | `INPUT_FILE_NAME` | VARCHAR(300) | NOT NULL |  | The input file name used to reclass GL Alias. |
| 6 | `JOB_STATUS_TXT` | VARCHAR(30) | NOT NULL |  | The status of the finished reclass GL Alias Job. |
| 7 | `MANUAL_RECLASS_GL_LOG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MANUAL_RECLASS_GL_LOG table. |
| 8 | `RECLASSIFIED_ACTIVITY_IDS_CNT` | DOUBLE | NOT NULL |  | The count of the reclassified GL Alias of activity Identifiers. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

