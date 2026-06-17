# DM_COMBINE_REVIEW

> Stores additional information about combines, such as if a combine detail row was added when combine ran in "REVIEW" mode.

**Description:** Stores additional information about combines.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary key of the parent entity this row is related to. |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the parent table for this row. |
| 3 | `REVIEW_FLAG` | DOUBLE |  |  | Reason the row is in dm_combine_review. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

