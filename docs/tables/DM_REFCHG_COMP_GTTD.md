# DM_REFCHG_COMP_GTTD

> Holds information used in reporting the differences between the RDDS temporary tables and LIVE tables

**Description:** Database Architecture Reference Comparison Global Temp Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) |  |  | Holds Column name of report data |
| 2 | `L_COLUMN_VALUE` | VARCHAR(4000) |  |  | Holds the Live Table/Column value of report data |
| 3 | `R_COLUMN_VALUE` | VARCHAR(4000) |  |  | Holds the $R Table/Column value of report data |
| 4 | `R_PTAM_HASH_VALUE` | DOUBLE |  |  | Holds the RDDS_PTAM_HASH_VALUE from the $R table for the row being audited |
| 5 | `R_ROWID` | VARCHAR(18) |  |  | Holds the ROWID from the $R table that is being audited |
| 6 | `STATUS` | VARCHAR(10) |  |  | Holds the status of the row |
| 7 | `TABLE_NAME` | VARCHAR(30) |  |  | Holds Table name of report data |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

