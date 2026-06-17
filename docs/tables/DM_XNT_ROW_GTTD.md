# DM_XNT_ROW_GTTD

> Global Temporary Table. Stores information during the retrieve proces about the datga that was extracted

**Description:** DB ARCH EXTRACT/TRANSFORM Global Temp Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) |  |  | Holds Column name of retrieved data |
| 2 | `COLUMN_VALUE` | VARCHAR(4000) |  |  | Holds Column value of retrieved data |
| 3 | `COL_SEQ` | DOUBLE |  |  | Holds column order of retrieved data |
| 4 | `FILE_ID` | DOUBLE | NOT NULL |  | Relation to DM_XNTR_EXTRACT_ID that represents each media file retrieved |
| 5 | `ROW_SEQ` | DOUBLE |  |  | Holds order of rows of retrieved data |
| 6 | `TABLE_NAME` | VARCHAR(30) |  |  | Holds Table name of retrieved data |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

