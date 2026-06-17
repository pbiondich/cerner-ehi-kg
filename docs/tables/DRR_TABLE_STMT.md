# DRR_TABLE_STMT

> Reference table to store DRR statement for domain specific schema. It is populated from metadata stored in dm_table_relationships

**Description:** DRR_TABLE_STMT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COL_STR` | VARCHAR(200) |  |  | CHILD COLUMN NAMES |
| 2 | `CHILD_TABLE` | VARCHAR(30) |  |  | child table name |
| 3 | `CUSTOM_PLSQL_IND` | DOUBLE | NOT NULL |  | indicator for custom pl/sql. 1 - custom zero type, 2 -custom pl/sql written by solution team |
| 4 | `DELETE_DUP_IND` | DOUBLE | NOT NULL |  | indicator for duplicate delete statements. 1 - duplicate not execute , 0 - not duplicate execute |
| 5 | `DELETE_ORDER` | DOUBLE |  |  | store delete execution order |
| 6 | `DELETE_STMT` | VARCHAR(4000) |  |  | store statement for delete process |
| 7 | `DRR_CHILD_TABLE` | VARCHAR(30) |  |  | drr shadow child table name |
| 8 | `DRR_PARENT_TABLE` | VARCHAR(30) |  |  | drr shadow parent table name |
| 9 | `DRR_TABLE_STMT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY. |
| 10 | `DRR_ZERO_RESTORE_IND` | DOUBLE |  |  | when custom_plsql_ind set to 1, this is populated with 1 or 0. 1 - Unrestrict restore column value, 0 - Unrestrict not restore column value |
| 11 | `HIER_LEVEL` | DOUBLE |  |  | relationship hierarchy level |
| 12 | `HIER_PATH` | VARCHAR(2000) |  |  | relationship hierarchy path |
| 13 | `PARENT_TABLE` | VARCHAR(30) |  |  | parent table name |
| 14 | `PAR_COL_STR` | VARCHAR(200) |  |  | parent column names |
| 15 | `RESTRICT_DUP_IND` | DOUBLE | NOT NULL |  | indicator for duplicate restrict statements. 1 - duplicate not execute , 0 - not duplicate execute |
| 16 | `RESTRICT_ORDER` | DOUBLE |  |  | store restrict execution order |
| 17 | `RESTRICT_STMT` | VARCHAR(4000) |  |  | store statement used for restrict process |
| 18 | `SELECT_STMT` | VARCHAR(4000) |  |  | store statement for audit process |
| 19 | `UNRESTRICT_DUP_IND` | DOUBLE | NOT NULL |  | indicator for duplicate unrestrict statements. 1 - duplicate not execute , 0 - not duplicate execute |
| 20 | `UNRESTRICT_ORDER` | DOUBLE |  |  | store unrestrict execution order |
| 21 | `UNRESTRICT_STMT` | VARCHAR(4000) |  |  | store statement used for unrestrict process |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

