# DM_VSQL

> Store SQL snapshot data

**Description:** DM_VSQL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUFFER_GETS` | DOUBLE |  |  | Oracle Buffer Gets Count |
| 2 | `CCL_OPT_MODE` | DOUBLE | NOT NULL |  | Cerner Optimizer Mode |
| 3 | `CCL_QUERY_NBR` | DOUBLE | NOT NULL |  | Cerner Query number |
| 4 | `CCL_QUERY_NBR_TEXT` | VARCHAR(7) | NOT NULL |  | Cerner Query Identifier |
| 5 | `CCL_SCRIPT_NAME` | VARCHAR(30) | NOT NULL |  | Cerner Script Name |
| 6 | `CHILD_NUMBER` | DOUBLE |  |  | Oracle Cursor Child Number |
| 7 | `EXECUTIONS` | DOUBLE |  |  | Oracle Execution Count |
| 8 | `FIRST_LOAD_TIME` | VARCHAR(19) |  |  | Oracle Cursor First Load Time |
| 9 | `INST_HASH_ADD` | VARCHAR(100) |  |  | Cerner combination of Oracle instance, Oracle hash_value, and Oracle address |
| 10 | `LAST_LOAD_TIME` | VARCHAR(19) |  |  | Oracle Cursor Last Load Time |
| 11 | `PLAN_HASH_VALUE` | DOUBLE |  |  | Oracle plan hash value |
| 12 | `ROWS_PROCESSED` | DOUBLE |  |  | Oracle rows processed count |
| 13 | `SQLTEXT_HASH_VALUE` | DOUBLE | NOT NULL |  | Cerner generated hash value on SQL_TEXT from GV$SQL |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

