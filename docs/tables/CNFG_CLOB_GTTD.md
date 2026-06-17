# CNFG_CLOB_GTTD

> Used by Smart Template Wizard framework to assist in producing Report documentation

**Description:** Configuration Management CLOB Global Temp Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNFG_CLOB` | LONGTEXT |  |  | A CLOB data type to store report documentation temporarily so it can be edited and combined with other CLOB data |
| 2 | `CNFG_CLOB_DT_TM` | DATETIME |  |  | A column that stores the date/time that the row was inserted into the table. |
| 3 | `CNFG_CLOB_FLAG` | DOUBLE | NOT NULL |  | A column to help denote the status of the CLOB. 0 = No data in CNFG_CLOB column. 1 = The data held in CNFG_CLOB is a portion of total CLOB. 2 = The data held in CNFG_CLOB is complete |
| 4 | `CNFG_CLOB_ID` | DOUBLE |  |  | PRIMARY KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

