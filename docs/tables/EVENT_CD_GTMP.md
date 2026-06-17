# EVENT_CD_GTMP

> This table is an Oracle global temporary table. It is used to improve performance for various queries. It typically will contain strings or other text values. The data in this table will be deleted by Oracle when a commit is executed.

**Description:** Event Code Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_CD` | DOUBLE | NOT NULL |  | Contains a code from the CODE_VALUE table. |
| 2 | `EVENT_SET_CD` | DOUBLE | NOT NULL |  | Identifies the code set that the code value belongs to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

