# USAGE_SUMMARY

> Statistical summary table. Collects data pertaining to step and app usages.

**Description:** Usage Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CPU_TIME` | DOUBLE |  |  | amount of cpu time the component used |
| 2 | `ELAPSED_TIME` | DOUBLE |  |  | amount of time in the server |
| 3 | `FREQUENCY` | DOUBLE |  |  | count of usage |
| 4 | `METRIC_NAME` | VARCHAR(40) | NOT NULL |  | name |
| 5 | `METRIC_TYPE` | DOUBLE | NOT NULL |  | type |
| 6 | `MET_DT_TM` | DATETIME |  |  | unused |
| 7 | `MONTH` | DOUBLE | NOT NULL |  | month |
| 8 | `NODE` | VARCHAR(18) |  |  | unused |
| 9 | `PARENT_ID` | DOUBLE | NOT NULL |  | the app number or req number of the component |
| 10 | `SERVICE` | VARCHAR(50) |  |  | service the component executed from |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `YEAR` | DOUBLE | NOT NULL |  | year |
| 17 | `YEAR_SEQ` | DOUBLE | NOT NULL |  | year mod 2 |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

