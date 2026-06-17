# DM_TABLE_TREE2

> SHOW HIERARCHY OF THE TABLES WITHIN DM SECTION

**Description:** DM TBALE TREE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_MODEL_SECTION` | VARCHAR(80) |  |  | DATA_MODEL_SECTION |
| 2 | `PARENT_TABLE_NAME` | VARCHAR(30) |  |  | PARENT TABLE NAME |
| 3 | `SEQ` | DOUBLE |  |  | SEQUENCE |
| 4 | `TABLE_NAME` | VARCHAR(30) |  |  | TABLE NAME |
| 5 | `TREE_LEVEL` | DOUBLE |  |  | TREE LEVEL |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

