# DRR_RESTRICT_LOG

> Activity table that stores DRR Restrict/delete_restrict DML statement for persons. It will use drr_table_stmt/drr_custom_plsql to gernate dml statements for persons in dm_process_queue

**Description:** DRR_RESTRICT_LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_COUNT` | DOUBLE |  |  | store number of rows found during audit |
| 2 | `AUDIT_DURATION` | DOUBLE |  |  | store how long audit takes from start to complete or fail in seconds |
| 3 | `AUDIT_END_DT_TM` | DATETIME |  |  | ending audit datetime |
| 4 | `AUDIT_START_DT_TM` | DATETIME |  |  | starting audit datetime |
| 5 | `AUDIT_STATUS` | VARCHAR(50) |  |  | store audit status like IN PROCESS, SUCCESS, FAILED |
| 6 | `CHILD_COL_STR` | VARCHAR(200) |  |  | child column names |
| 7 | `CHILD_TABLE` | VARCHAR(30) |  |  | child table name |
| 8 | `COLUMN_LIST` | LONGTEXT |  |  | A CLOB field containing the column list |
| 9 | `CUSTOM_PLSQL_IND` | DOUBLE | NOT NULL |  | indicator for custom restrict type. 1 - zero type. 2 - custom pl/sql inserted by solution team |
| 10 | `CUST_RESTRICT_STMT` | VARCHAR(200) |  |  | statement execute for custom restrict |
| 11 | `DRR_CHILD_TABLE` | VARCHAR(30) |  |  | drr shadow child table name |
| 12 | `DRR_IDENT_ID` | DOUBLE |  |  | Unique sequence generated to identify each person being restricted. In combine scenario, one unique value is used for both combined away person and the combined to person. |
| 13 | `DRR_PARENT_TABLE` | VARCHAR(30) |  |  | drr shadow parent table name |
| 14 | `DRR_PROCESS_PLAN_ID` | DOUBLE | NOT NULL |  | drr_process_plan_id generated on DRR_PROCESS_PLAN table. |
| 15 | `DRR_RESTRICT_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY. |
| 16 | `DRR_ZERO_RESTORE_IND` | DOUBLE |  |  | indicator use for ZERO type. 1 - Unrestrict restore column value. 0 - Unrestrict not restore column value |
| 17 | `ERROR_MSG` | VARCHAR(4000) |  |  | store error message |
| 18 | `PARENT_TABLE` | VARCHAR(30) |  |  | parent table name |
| 19 | `PAR_COL_STR` | VARCHAR(200) |  |  | parent column names |
| 20 | `PERSON_ID` | DOUBLE | NOT NULL |  | person ID being restricted. |
| 21 | `PRIMARY_PERSON_ID` | DOUBLE |  |  | When person_id column stores combined away person, this column will store the final combined to person_id. In other cases, primary_person_id will be same as person_id. |
| 22 | `RESTRICT_COUNT` | DOUBLE |  |  | store number of rows being restricted |
| 23 | `RESTRICT_DUP_IND` | DOUBLE | NOT NULL |  | indicator for duplicate restrict statements |
| 24 | `RESTRICT_DURATION` | DOUBLE |  |  | store how long audit takes from start to complete or fail in seconds |
| 25 | `RESTRICT_END_DT_TM` | DATETIME |  |  | ending restrict datetime |
| 26 | `RESTRICT_ORDER` | DOUBLE |  |  | restrict execution order |
| 27 | `RESTRICT_START_DT_TM` | DATETIME |  |  | starting restrict datetime |
| 28 | `RESTRICT_STATUS` | VARCHAR(50) |  |  | like NOT STARTED, IN PROCESS, COMPLETED |
| 29 | `RESTRICT_STMT` | VARCHAR(4000) |  |  | statement execute for restrict |
| 30 | `RETRY_COUNT` | DOUBLE |  |  | number of times retried |
| 31 | `SELECT_STMT` | VARCHAR(4000) |  |  | statement execute for audit |
| 32 | `SESSIONID` | DOUBLE |  |  | store process sessionid to_number(sys_context('USERENV','SESSIONID')) |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

