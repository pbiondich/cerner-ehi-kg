# DM_REFCHG_SQL_OBJ

> PL/SQL objects needed for RDDS. Will be loaded via a CSV import process. Will not merge.

**Description:** Dm_refchg_sql_obj  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CCL_DATA_TYPE` | VARCHAR(10) |  |  | Used to declare function return data types in CCL |
| 3 | `COLUMN_NAME` | VARCHAR(30) |  |  | Filled out if this object is used for custom translations. It tells whether which column it is used for. |
| 4 | `CREATION_LEVEL` | DOUBLE | NOT NULL |  | Order which object should be created in compared to other objects to be created. |
| 5 | `DM_REFCHG_SQL_OBJ_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `EXECUTION_FLAG` | DOUBLE | NOT NULL |  | 1 - If the column being translated is an MUI column use this execution flag 2 - Columns that are not in the MUI and are not the PK should use this execution flag 3 - If the column being translated is the Primary Key, use this execution flag. 4 - Special execution flag for DCP tables. Used for top level columns that are not the PK column. The top level column and PK column are never equal to each other. 5 - Special execution flag for MED. Used as a soft FK in conjuction with another column |
| 7 | `OBJECT_NAME` | VARCHAR(40) | NOT NULL |  | Name of PL/SQL object |
| 8 | `OBJECT_TYPE` | VARCHAR(30) | NOT NULL |  | Type of PL/SQL object - e.g. FUNCTION, PROCEDURE, etc. |
| 9 | `TABLE_NAME` | VARCHAR(30) |  |  | Filled out if this object is used for custom translations. It tells whether which table it is used for. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

