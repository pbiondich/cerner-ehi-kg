# EXT_CODING_GTTD

> Global Temp Table to assist with qualifying external codes on searches.

**Description:** External Coding Global Temp Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_TXT` | VARCHAR(255) |  |  | Contains a codified string value |
| 2 | `CODING_SYSTEM_URI` | VARCHAR(255) |  |  | The URI of the coding system. |
| 3 | `INCLUDE_IND` | DOUBLE |  |  | Indicates whether the code should be included or excluded |
| 4 | `VERSION_TXT` | VARCHAR(255) |  |  | The version of the coding system, if applicable. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

