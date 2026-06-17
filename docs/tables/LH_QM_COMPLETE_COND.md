# LH_QM_COMPLETE_COND

> Keeps track of which measures are completing correctly with the new code.

**Description:** Lighthouse Quality Measures Complete Conditions  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETE_COND_BIT` | DOUBLE |  |  | Keeps track of which conditions successfully complete with the new code. |
| 2 | `FIRST_RUN_DT_TM` | DATETIME |  |  | The first script run that has this outcome. |
| 3 | `INCOMPLETE_COND_BIT` | DOUBLE |  |  | Keeps track of which conditions still rely on the old code to work. |
| 4 | `LH_QM_COMPLETE_COND_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QM_COMPLETE_CONDS table.; |
| 5 | `RUN_CNT` | DOUBLE |  |  | The number of runs that have had these specific outcomes. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 9 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

