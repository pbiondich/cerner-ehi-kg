# SHARED_BLOB_GTTD

> This table is an Oracle global temporary table. It is used to improve performance for various queries. It typically will contain ids or other numerical values that will be used in a join clause or in-list in a select statement. The data in this table will be deleted by Oracle when a commit is executed.

**Description:** Shared BLOB Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SHARED_BLOB` | LONGBLOB |  |  | The BLOB field value to be temporarily stored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

