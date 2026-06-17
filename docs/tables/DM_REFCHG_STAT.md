# DM_REFCHG_STAT

> Statistics for RDDS data moves

**Description:** Data management reference change statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CUR_STMT_DT_TM` | DATETIME |  |  | Date/time that the current statement started. |
| 2 | `CUR_STMT_NBR` | DOUBLE |  |  | Current statement being run |
| 3 | `DEL_ROW_CNT` | DOUBLE | NOT NULL |  | count of Number of rows deleted |
| 4 | `DM_REFCHG_STAT_ID` | DOUBLE | NOT NULL |  | Unique identifier |
| 5 | `INS_ROW_CNT` | DOUBLE | NOT NULL |  | Count of Number of rows inserted |
| 6 | `MRG_ROW_CNT` | DOUBLE | NOT NULL |  | Count of Number of rows merged |
| 7 | `ROWS_TO_PROCESS` | DOUBLE |  |  | Number of rows on the table_name that needed to be processed when this row was first inserted. This value is not updated. |
| 8 | `SOURCE_ENV_ID` | DOUBLE | NOT NULL |  | Environment id being moved in. (the dm_environment.environment_id in the Admin database) |
| 9 | `STAT_TYPE` | VARCHAR(50) | NOT NULL |  | Type of warning - e.g. CUTOVER, MOVER |
| 10 | `STMT_CNT` | DOUBLE | NOT NULL |  | Number of DML statements needed to process this table |
| 11 | `TABLE_NAME` | VARCHAR(30) |  |  | Name of the table that the statistic is related to. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `UPD_ROW_CNT` | DOUBLE | NOT NULL |  | Count of Number of rows updated |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

