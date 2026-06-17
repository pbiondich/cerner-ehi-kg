# DRR_TABLE_STMT_STG

> Stage table used to facilitate loading table DRR_TABLE_STMT

**Description:** DRR TABLE STATEMENT STAGING  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COL_STR` | VARCHAR(200) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 2 | `CHILD_TABLE` | VARCHAR(30) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 3 | `CUSTOM_PLSQL_IND` | DOUBLE | NOT NULL |  | See colmn definition for table DRR_TABLE_STMT |
| 4 | `DELETE_DUP_IND` | DOUBLE | NOT NULL |  | See colmn definition for table DRR_TABLE_STMT |
| 5 | `DELETE_ORDER` | DOUBLE |  |  | See colmn definition for table DRR_TABLE_STMT |
| 6 | `DELETE_STMT` | VARCHAR(4000) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 7 | `DRR_CHILD_TABLE` | VARCHAR(30) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 8 | `DRR_PARENT_TABLE` | VARCHAR(30) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 9 | `DRR_TABLE_STMT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 10 | `DRR_ZERO_RESTORE_IND` | DOUBLE |  |  | See colmn definition for table DRR_TABLE_STMT |
| 11 | `HIER_LEVEL` | DOUBLE |  |  | See colmn definition for table DRR_TABLE_STMT |
| 12 | `HIER_PATH` | VARCHAR(2000) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 13 | `PARENT_TABLE` | VARCHAR(30) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 14 | `PAR_COL_STR` | VARCHAR(200) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 15 | `RESTRICT_DUP_IND` | DOUBLE | NOT NULL |  | See colmn definition for table DRR_TABLE_STMT |
| 16 | `RESTRICT_ORDER` | DOUBLE |  |  | See colmn definition for table DRR_TABLE_STMT |
| 17 | `RESTRICT_STMT` | VARCHAR(4000) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 18 | `SELECT_STMT` | VARCHAR(4000) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 19 | `UNRESTRICT_DUP_IND` | DOUBLE | NOT NULL |  | See colmn definition for table DRR_TABLE_STMT |
| 20 | `UNRESTRICT_ORDER` | DOUBLE |  |  | See colmn definition for table DRR_TABLE_STMT |
| 21 | `UNRESTRICT_STMT` | VARCHAR(4000) |  |  | See colmn definition for table DRR_TABLE_STMT |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

