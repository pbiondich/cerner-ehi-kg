# SHARED_TXT_GTTD

> This table is an Oracle global temporary table. It is used to improve performance for various queries. It typically will contain strings or other text values. The data in this table will be deleted by Oracle when a commit is executed.

**Description:** Shared Test Global Temporary Table Delete  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SOURCE_ENTITY_NAME` | VARCHAR(100) |  |  | Usually contains the name of where the shared_entity_txt comes from. An example of this would be the table name where the text string comes from. However, it does not have to be a table name. It can be anything to distinguish one set of text values from another set. |
| 2 | `SOURCE_ENTITY_TXT` | VARCHAR(255) |  |  | This contains the text string that is being stored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

