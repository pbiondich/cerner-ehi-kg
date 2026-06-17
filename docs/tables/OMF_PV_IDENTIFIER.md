# OMF_PV_IDENTIFIER

> Table to store identifiers as defined within the PowerVisionDemoBuilder

**Description:** OMF PV IDENTIFIER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY` | VARCHAR(80) |  |  | Display value as entered via the PowerVisionDemoBuilder (free text) |
| 2 | `OMF_ID` | DOUBLE | NOT NULL |  | Unique identifier |
| 3 | `PD_GRID_CD` | DOUBLE | NOT NULL |  | Grid_cd |
| 4 | `SG_TYPE` | VARCHAR(50) |  |  | Study group type |
| 5 | `ST_COLUMN_NAME` | VARCHAR(40) | NOT NULL |  | Summary table column name |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

