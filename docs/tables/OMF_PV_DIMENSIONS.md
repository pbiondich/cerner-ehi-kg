# OMF_PV_DIMENSIONS

> Contains IDs for filterable columns. Used to store the display values for strings that will be used as filters.

**Description:** Contains IDs for filterable columns  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY` | VARCHAR(80) |  |  | Contains the text that should be displayed for this dimension |
| 2 | `OMF_ID` | DOUBLE | NOT NULL |  | Unique number for this string value. This is what will be stored in the OMF_PV_DATA_ST table in one of the NUM columns. |
| 3 | `PD_GRID_CD` | DOUBLE |  |  | Defines the grid that this data is used for. |
| 4 | `ST_COLUMN_NAME` | VARCHAR(40) |  |  | This is the summary table column where this data will be stored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

