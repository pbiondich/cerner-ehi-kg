# PM_RBC_RUN

> The PM_RBC_RUN table stores information about each execution of the room & bed charge process.

**Description:** Patient Management Room and Bed Charge Run  
**Table type:** ACTIVITY  
**Primary key:** `PM_RBC_RUN_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time the room and bed charge process execution completed. |
| 2 | `LOG_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row on the pm_rbc_long_text table containing the general logging text for this execution of the room & bed charge process. |
| 3 | `PM_RBC_RUN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the PM_RBC_RUN table. |
| 4 | `RDB_HANDLE_NBR` | DOUBLE | NOT NULL |  | A unique identifier (handle) for database session used to execute run. |
| 5 | `RUN_MODE_CD` | DOUBLE | NOT NULL |  | Mode of execution for this instance of the room & bed charge process. |
| 6 | `RUN_TZ` | DOUBLE | NOT NULL |  | Time zone associated with this execution of the room & bed charge process. |
| 7 | `SERVICE_DT_TM` | DATETIME |  |  | Date of service for which the room & bed charge process was executed. |
| 8 | `START_DT_TM` | DATETIME |  |  | Date and time the room & bed charge process execution started. |
| 9 | `STATUS_CD` | DOUBLE | NOT NULL |  | Overall status of this execution of the room & bed charge process. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOG_LONG_TEXT_ID` | [PM_RBC_LONG_TEXT](PM_RBC_LONG_TEXT.md) | `PM_RBC_LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_RBC_RUN_SET](PM_RBC_RUN_SET.md) | `PM_RBC_RUN_ID` |

