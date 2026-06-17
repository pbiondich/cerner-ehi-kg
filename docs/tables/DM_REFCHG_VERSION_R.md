# DM_REFCHG_VERSION_R

> Holds the list of child tables that have a VERSION_NBR type of column and the parent tables where the ultimate VERSION_NBR exists.

**Description:** Data management reference version table relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_ID_COL` | VARCHAR(30) |  |  | The column name on the child table that is a foreign key to the parent_id_col |
| 2 | `CHILD_TABLE` | VARCHAR(30) |  |  | The table name that the child_vers_col exists on |
| 3 | `CHILD_VERS_COL` | VARCHAR(30) |  |  | The column name on the child table that contains the same version data as parent_vers_col. |
| 4 | `DM_REFCHG_VERSION_R_ID` | DOUBLE | NOT NULL |  | Sequence generated primary key |
| 5 | `PARENT_ID_COL` | VARCHAR(30) |  |  | The column name on the parent table that the child_id_col points to. |
| 6 | `PARENT_TABLE` | VARCHAR(30) |  |  | The table name where the ultimate version_nbr column exists |
| 7 | `PARENT_VERS_COL` | VARCHAR(30) |  |  | The column name on the parent table that the child_vers_col points to. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

