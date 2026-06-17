# DRR_DELETE_LOG

> Activity table that stores DRR delete DML statement for persons. It will use drr_table_stmt/drr_custom_plsql to gernate dml statements for persons in dm_process_queue

**Description:** DRR_DELETE_LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_COUNT` | DOUBLE |  |  | store number of rows found during audit |
| 2 | `AUDIT_DURATION` | DOUBLE |  |  | store how long delete takes from start to complete or fail in seconds |
| 3 | `AUDIT_END_DT_TM` | DATETIME |  |  | ending audit datetime |
| 4 | `AUDIT_START_DT_TM` | DATETIME |  |  | starting audit datetime |
| 5 | `AUDIT_STATUS` | VARCHAR(50) |  |  | store audit status like IN PROCESS, SUCCESS, FAILED |
| 6 | `CHILD_COL_STR` | VARCHAR(200) |  |  | child column names |
| 7 | `CHILD_TABLE` | VARCHAR(30) |  |  | child table name |
| 8 | `CUSTOM_PLSQL_IND` | DOUBLE | NOT NULL |  | indicator for custom delete type. 1 - zero type. 2 - custom pl/sql inserted by solution team. |
| 9 | `CUST_DELETE_STMT` | VARCHAR(100) |  |  | statement execute for custom delete |
| 10 | `DELETE_COUNT` | DOUBLE |  |  | store number of rows being deleted |
| 11 | `DELETE_DURATION` | DOUBLE |  |  | store how long delete takes from start to complete or fail in seconds |
| 12 | `DELETE_END_DT_TM` | DATETIME |  |  | ending delete datetime |
| 13 | `DELETE_ORDER` | DOUBLE |  |  | delete execution order |
| 14 | `DELETE_START_DT_TM` | DATETIME |  |  | starting delete datetime |
| 15 | `DELETE_STATUS` | VARCHAR(50) |  |  | store delete status like IN PROCESS, SUCCESS, FAILED |
| 16 | `DELETE_STMT` | VARCHAR(4000) |  |  | statement execute for delete |
| 17 | `DRR_CHILD_TABLE` | VARCHAR(30) |  |  | drr shadow child table name |
| 18 | `DRR_DELETE_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY. |
| 19 | `DRR_IDENT_ID` | DOUBLE |  |  | Unique sequence generated to identify each person being restricted. In combine scenario, one unique value is used for both combined away person and the combined to person. |
| 20 | `DRR_PARENT_TABLE` | VARCHAR(30) |  |  | drr shadow parent table name |
| 21 | `DRR_PROCESS_PLAN_ID` | DOUBLE | NOT NULL |  | drr_process_plan_id generated for delete on DRR_PROCESS_PLAN table. |
| 22 | `DRR_RESTRICT_PLAN_ID` | DOUBLE | NOT NULL |  | drr_process_plan_id generated for restrict on DRR_PROCESS_PLAN table. |
| 23 | `ERROR_MSG` | VARCHAR(4000) |  |  | store error message |
| 24 | `PARENT_TABLE` | VARCHAR(30) |  |  | parent table name |
| 25 | `PAR_COL_STR` | VARCHAR(200) |  |  | parent column names |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL |  | person_id being delete. |
| 27 | `PRIMARY_PERSON_ID` | DOUBLE |  |  | When person_id column stores combined away person, this column will store the final combined to person_id. |
| 28 | `RETRY_COUNT` | DOUBLE |  |  | number of times retried |
| 29 | `SELECT_STMT` | VARCHAR(4000) |  |  | statement execute for audit |
| 30 | `SESSIONID` | DOUBLE |  |  | store process sessionid to_number(sys_context('USERENV','SESSIONID')) |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

