# DM_USER_TAB_COLS

> Contains the same information as USER_TAB_COLUMNS -- used by schema refresh tools

**Description:** Contains the same information as USER_TAB_COLUMNS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_ID` | DOUBLE | NOT NULL |  | column_id for the column |
| 2 | `COLUMN_NAME` | VARCHAR(30) |  |  | column name for the column |
| 3 | `DATA_DEFAULT` | VARCHAR(255) |  |  | data default |
| 4 | `DATA_LENGTH` | DOUBLE |  |  | data length of the column |
| 5 | `DATA_TYPE` | VARCHAR(9) |  |  | data type of the column |
| 6 | `NULLABLE` | VARCHAR(1) |  |  | NULLABLE property of the column |
| 7 | `TABLESPACE_NAME` | VARCHAR(30) |  |  | tablespace name for the table |
| 8 | `TABLE_NAME` | VARCHAR(30) |  |  | TABLE NAME |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

