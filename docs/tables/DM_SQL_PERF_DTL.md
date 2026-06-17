# DM_SQL_PERF_DTL

> Detail data used by the CBO Implementer

**Description:** DM_SQL_PERF_DTL  
**Table type:** REFERENCE  
**Primary key:** `DM_SQL_PERF_DTL_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUFFER_GETS` | DOUBLE |  |  | Oracle Buffer gets count |
| 2 | `BUFFER_GETS_EXEC` | DOUBLE | NOT NULL |  | ratio buffer gets/execution for this statement and this optimizer mode |
| 3 | `CCL_OPT_MODE` | DOUBLE | NOT NULL |  | Cerner Optimizer Mode |
| 4 | `DM_SQL_ID` | DOUBLE | NOT NULL |  | primary key, pull value from DM_CLINICAL_SEQ |
| 5 | `DM_SQL_PERF_DTL_ID` | DOUBLE | NOT NULL | PK | data management SQL performance detail identifier |
| 6 | `EXECUTIONS` | DOUBLE |  |  | Oracle execution count |
| 7 | `EXECUTIONS_SEC` | DOUBLE | NOT NULL |  | ratio of executions per second |
| 8 | `OPTIMIZER_MODE` | VARCHAR(40) | NOT NULL |  | 'UNKNOWN', 'RULE','FIRST ROWS','CHOOSE' |
| 9 | `PLAN_DATA_EXISTS_IND` | DOUBLE |  |  | Indicates whether plan data exists. |
| 10 | `PLAN_HASH_VALUE` | DOUBLE |  |  | Oracle Plan Hash Value |
| 11 | `ROWS_PROCESSED` | DOUBLE |  |  | Oracle Rows Processed Count |
| 12 | `TUNING_DT_TM` | DATETIME | NOT NULL |  | last time we worked on this SQL |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_SQL_PERF_DTL_PLAN](DM_SQL_PERF_DTL_PLAN.md) | `DM_SQL_PERF_DTL_ID` |

