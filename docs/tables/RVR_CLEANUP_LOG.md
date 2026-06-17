# RVR_CLEANUP_LOG

> This Revenue Cycle Cleanup Log table will be used for scheduled cleanups.

**Description:** Revenue Cycle Registration Cleanup Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | The date and time the Cleanup Script Ended. |
| 2 | `GROUP_NAME` | VARCHAR(50) |  |  | A name assigned to a group of clean up scripts that ran together. |
| 3 | `MASTER_LOG_FILE_NAME` | VARCHAR(100) |  |  | Name of the master log file for the execution. |
| 4 | `PARAMETERS_TXT` | VARCHAR(200) |  |  | The set of parameters that were sent to the cleanup job. |
| 5 | `PERSON_ID` | DOUBLE |  | FK→ | Uniquely identifies the person related to this record. |
| 6 | `RVR_CLEANUP_CONFIG_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the RVR_CLEANUP_CONFIG table. |
| 7 | `RVR_CLEANUP_LOG_ID` | DOUBLE | NOT NULL |  | A system generated number to uniquely identify a row on the RVR_CLEANUP_LOG table. |
| 8 | `START_DT_TM` | DATETIME |  |  | The date and time the cleanup started. |
| 9 | `UPDATED_ROWS_CNT` | DOUBLE |  |  | Count of rosw updated by the cleanup. |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RVR_CLEANUP_CONFIG_ID` | [RVR_CLEANUP_CONFIG](RVR_CLEANUP_CONFIG.md) | `RVR_CLEANUP_CONFIG_ID` |

