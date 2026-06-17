# SHARED_VALUE_GTTD

> This table is an Oracle global temporary table. It is used to improve performance for various queries. It typically will contain ids or other numerical values that will be used in a join clause or in-list in a select statement. The data in this table will be deleted by Oracle when a commit is executed.

**Description:** Shared Value Global Temporary Table Delete  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SOURCE_ENTITY_NAME` | VARCHAR(100) |  |  | Contains the name of where the shared_entity_values come from. An example of this would be table name if you were storing table ids in the value column. |
| 2 | `SOURCE_ENTITY_VALUE` | DOUBLE |  |  | Contains numeric values. An example of these would be primary key ids from a table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

