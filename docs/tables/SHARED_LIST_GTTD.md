# SHARED_LIST_GTTD

> This table is an Oracle global temporary table. It is used to improve performance for various queries. It typically will contain ids or other numerical values that will be used in a join clause or in-list in a select statement. The data in this table will be deleted by Oracle when a commit is executed.

**Description:** Shared List Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SOURCE_ENTITY_DT_TM` | DATETIME |  |  | Contains Date/Time values. |
| 2 | `SOURCE_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains numeric ID values. It will be an F8 in CCL. An example of these would be primary key ids from a table. |
| 3 | `SOURCE_ENTITY_NBR` | DOUBLE |  |  | Contains numeric values. Defined as a number data type so it will be an I4 in CCL. |
| 4 | `SOURCE_ENTITY_SEQ` | DOUBLE |  |  | Contains numeric sequence values. Defined as a float data type so it will be an F8 in CCL. |
| 5 | `SOURCE_ENTITY_TXT` | VARCHAR(300) |  |  | Contains text values. |
| 6 | `SOURCE_ENTITY_VALUE` | DOUBLE |  |  | Contains numeric values. Defined as a float data type so it will be an F8 in CCL. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

