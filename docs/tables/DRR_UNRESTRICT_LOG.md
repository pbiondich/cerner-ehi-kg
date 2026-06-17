# DRR_UNRESTRICT_LOG

> Activity table that stores DRR Unrestrict DML statement for persons. It will use drr_table_stmt/drr_custom_plsql to gernate dml statements for persons in dm_process_queue

**Description:** DRR_UNRESTRICT_LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

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
| 8 | `CUSTOM_PLSQL_IND` | DOUBLE | NOT NULL |  | indicator for custom unrestrict type. 1 - zero type. 2 - custom pl/sql inserted by solution team |
| 9 | `CUST_UNRESTRICT_STMT` | VARCHAR(200) |  |  | statement execute for custom unrestrict |
| 10 | `DRR_CHILD_TABLE` | VARCHAR(30) |  |  | drr shadow child table name |
| 11 | `DRR_IDENT_ID` | DOUBLE |  |  | Unique sequence generated to identify each person being restricted. In combine scenario, one unique value is used for both combined away person and the combined to person. |
| 12 | `DRR_PARENT_TABLE` | VARCHAR(30) |  |  | drr shadow parent table name |
| 13 | `DRR_PROCESS_PLAN_ID` | DOUBLE | NOT NULL |  | drr_process_plan_id generated for unrestrict on DRR_PROCESS_PLAN table. |
| 14 | `DRR_RESTRICT_PLAN_ID` | DOUBLE | NOT NULL |  | drr_process_plan_id generated for restrict on DRR_PROCESS_PLAN table. |
| 15 | `DRR_UNRESTRICT_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY. |
| 16 | `ERROR_MSG` | VARCHAR(4000) |  |  | store error message |
| 17 | `PARENT_TABLE` | VARCHAR(30) |  |  | parent table name |
| 18 | `PAR_COL_STR` | VARCHAR(200) |  |  | parent column names |
| 19 | `PERSON_ID` | DOUBLE | NOT NULL |  | person_id being unrestricted. |
| 20 | `PRIMARY_PERSON_ID` | DOUBLE |  |  | When person_id column stores combined away person, this column will store the final combined to person_id. In other cases, primary_person_id will be same as person_id. |
| 21 | `RETRY_COUNT` | DOUBLE |  |  | number of times retried |
| 22 | `SELECT_STMT` | VARCHAR(4000) |  |  | statement execute for audit |
| 23 | `SESSIONID` | DOUBLE |  |  | store process sessionid to_number(sys_context('USERENV','SESSIONID')) |
| 24 | `UNRESTRICT_COUNT` | DOUBLE |  |  | store number of rows being unrestricted |
| 25 | `UNRESTRICT_DURATION` | DOUBLE |  |  | store how long audit takes from start to complete or fail in seconds |
| 26 | `UNRESTRICT_END_DT_TM` | DATETIME |  |  | ending unrestrict datetime |
| 27 | `UNRESTRICT_ORDER` | DOUBLE |  |  | unrestrict execution order |
| 28 | `UNRESTRICT_START_DT_TM` | DATETIME |  |  | starting unrestrict datetime |
| 29 | `UNRESTRICT_STATUS` | VARCHAR(50) |  |  | store unrestrict status like IN PROCESS, SUCCESS, FAILED |
| 30 | `UNRESTRICT_STMT` | VARCHAR(4000) |  |  | statement execute for unrestrict |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

