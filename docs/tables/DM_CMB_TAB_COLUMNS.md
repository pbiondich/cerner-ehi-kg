# DM_CMB_TAB_COLUMNS

> Mirror table of user_tab_columns used for improved combine performance.

**Description:** DM CMB TAB COLUMNS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Name of columns in the table. |
| 2 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table in the database. |
| 3 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

