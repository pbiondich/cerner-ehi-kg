# DAC_INDEX_COALESCE_LOG

> Logging table for DM2_ROUTINE_TASKS Index Coalesce Operations

**Description:** DAC_INDEX_COALESCE_LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COALESCE_LOG_ID` | DOUBLE | NOT NULL |  | Primary Key Column for the table, populated by DAC_LOGGING_SEQ. |
| 2 | `END_DT_TM` | DATETIME |  |  | Ending time of the coalesce task. |
| 3 | `INDEX_NAME` | VARCHAR(50) | NOT NULL |  | Name of the Index which was coalesced. |
| 4 | `START_DT_TM` | DATETIME |  |  | Starting time of the coalesce task. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

