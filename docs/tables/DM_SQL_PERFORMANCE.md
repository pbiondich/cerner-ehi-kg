# DM_SQL_PERFORMANCE

> Stores tuning status, best optimizer mode for different queries used by Millennium applications.

**Description:** DM_SQL_PERFORMANCE  
**Table type:** REFERENCE  
**Primary key:** `DM_SQL_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEST_OPTIMIZER_MODE` | VARCHAR(40) | NOT NULL |  | UNKNOWN', 'RULE', 'FIRST ROWS', 'CHOOSE' |
| 2 | `COMMENTS` | VARCHAR(255) |  |  | Contains comments relating to the performance of this SQL. |
| 3 | `DM_SQL_ID` | DOUBLE | NOT NULL | PK | Primary key, pull value from DM_CLINICAL_SEQ |
| 4 | `FINAL_BUFFER_GETS_EXEC` | DOUBLE | NOT NULL |  | final ratio that was determined to be the best |
| 5 | `FINAL_EXECUTIONS_SEC` | DOUBLE | NOT NULL |  | final ratio of executions per second |
| 6 | `FINAL_ROWS_PROCESSED_EXEC` | DOUBLE | NOT NULL |  | Final number of rows processed executed |
| 7 | `HASH_VALUE` | DOUBLE | NOT NULL |  | Stores the hash value obtained from V$SQLAREA |
| 8 | `INITIAL_BUFFER_GETS_EXEC` | DOUBLE | NOT NULL |  | initial ratio that drove us to look at this statement |
| 9 | `INITIAL_EXECUTIONS_SEC` | DOUBLE | NOT NULL |  | initial ratio of executions per second |
| 10 | `INITIAL_ROWS_PROCESSED_EXEC` | DOUBLE | NOT NULL |  | Initial number of rows processed executed |
| 11 | `LAST_TUNING_DT_TM` | DATETIME | NOT NULL |  | last time we worked on this SQL |
| 12 | `OUTLINE_NAME` | VARCHAR(40) |  |  | name of the stored outline |
| 13 | `TUNING_STATUS` | VARCHAR(40) | NOT NULL |  | NOT TUNED, IN PROCESS, TUNED |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_SQL_PERF_DTL_PLAN](DM_SQL_PERF_DTL_PLAN.md) | `DM_SQL_ID` |
| [DM_SQL_PERF_TEXT](DM_SQL_PERF_TEXT.md) | `DM_SQL_ID` |

