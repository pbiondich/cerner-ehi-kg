# DM_XNT_IDS_GTTD

> An ID value of a table that is being processed by the Extract and Transform archive process

**Description:** Data Management Extract and Transform Ids Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Table associated to ID value. |
| 2 | `XNT_ID` | DOUBLE | NOT NULL |  | Id to be processed in Extract and Transform |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

