# DM_REFCHG_TAB_R

> Holds the list of tables that must be commit together when transferring reference data via RDDS. Tables are related via parent/child relationships and can be chained together to create a tree structure with a single root parent.

**Description:** Data management reference change table relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | Table which must have it's rows committed in the target environment at the same time as the parent table. |
| 2 | `DM_REFCHG_TAB_R_ID` | DOUBLE | NOT NULL |  | DM reference change table relationship id. Sequence generated primary key |
| 3 | `MD_VALUE_STR` | VARCHAR(500) |  |  | PL/SQL string to create the values needed for the merge delete unique identifier. |
| 4 | `MD_VAR_STR` | VARCHAR(500) |  |  | List of variables that the md_value_str will select into - e.g. select into from dual. These variables will be used the pk_where. |
| 5 | `PARENT_ID_COL` | VARCHAR(30) | NOT NULL |  | Name of the column on the child table that holds the primary key ID of the parent_table. |
| 6 | `PARENT_R_COL` | VARCHAR(30) |  |  | The column name on the parent table that the parent_id_col points to. This is needed for reverse relationships. |
| 7 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | Parent of a table in RDDS that must have its rows committed in the target environment at the same time as the child table. |
| 8 | `PARENT_TAB_COL` | VARCHAR(30) |  |  | Name of the column on the child table that holds the name of the parent_table. If this is not filled out then the parent_table is always 'parent_table'. |
| 9 | `PK_WHERE` | VARCHAR(2000) | NOT NULL |  | Procedure code needed to generate a pk_where clause to be placed in dm_chg_log. |
| 10 | `PROCESS_SEQ` | DOUBLE | NOT NULL |  | Used by the RDDS mover to determine what order to move children tables. The lowest values are processed first. |
| 11 | `PROCESS_TYPE` | VARCHAR(30) |  |  | process type column |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

