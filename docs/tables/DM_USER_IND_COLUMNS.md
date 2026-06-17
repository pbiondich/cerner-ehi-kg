# DM_USER_IND_COLUMNS

> Contains information from USER_INDEXES and USER_IND_COLUMNS -- used in schema refresh tools

**Description:** Contains informaton from USER_INDEXES and USER_IND_COLUMNS.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | column name for an index |
| 2 | `COLUMN_POSITION` | DOUBLE | NOT NULL |  | column position |
| 3 | `INDEX_NAME` | VARCHAR(30) | NOT NULL |  | index name |
| 4 | `TABLESPACE_NAME` | VARCHAR(30) | NOT NULL |  | tablespace name for the index |
| 5 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | TABLE NAME |
| 6 | `TABLE_OWNER` | VARCHAR(30) | NOT NULL |  | table owner |
| 7 | `UNIQUENESS` | VARCHAR(9) |  |  | defines whether the index is unique |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

