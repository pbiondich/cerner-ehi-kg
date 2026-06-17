# DM_SQL_PLAN

> Used to store the execution plan for sql statements captured by dm_sql_snapshot

**Description:** DM SQL PLAN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BYTES` | DOUBLE |  |  | used by the explain plan |
| 2 | `CARDINALITY` | DOUBLE |  |  | used by the explain plan |
| 3 | `COST` | DOUBLE |  |  | used by the explain plan |
| 4 | `ID` | DOUBLE |  |  | used by the explain plan |
| 5 | `INDEX_COLUMNS` | VARCHAR(255) |  |  | contains the column string for the index used |
| 6 | `OBJECT_INSTANCE` | DOUBLE |  |  | used by the explain plan |
| 7 | `OBJECT_NAME` | VARCHAR(30) |  |  | name of the table or index |
| 8 | `OBJECT_NODE` | VARCHAR(128) |  |  | used by the explain plan |
| 9 | `OBJECT_OWNER` | VARCHAR(30) |  |  | owner of the table or index |
| 10 | `OBJECT_TYPE` | VARCHAR(30) |  |  | table or index |
| 11 | `OPERATION` | VARCHAR(30) |  |  | used by the explain plan |
| 12 | `OPTIMIZER` | VARCHAR(255) |  |  | cost or rule optimizer |
| 13 | `OPTIONS` | VARCHAR(30) |  |  | used by the explain plan |
| 14 | `OTHER` | LONGTEXT |  |  | used by the explain plan |
| 15 | `OTHER_TAG` | VARCHAR(255) |  |  | used by the explain plan |
| 16 | `PARENT_ID` | DOUBLE |  |  | used by the explain plan |
| 17 | `POSITION` | DOUBLE |  |  | this is the order that this part of the plan occurred in |
| 18 | `REMARKS` | VARCHAR(80) |  |  | this is used by the explain plan |
| 19 | `SEARCH_COLUMNS` | DOUBLE |  |  | this is used by the explain plan |
| 20 | `STATEMENT_ID` | VARCHAR(30) |  |  | This is the unique identifier for this SQL statement |
| 21 | `TIMESTAMP` | DATETIME |  |  | this is used by the explain plan |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

