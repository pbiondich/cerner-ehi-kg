# OMF_PRSNL_TIMEHOUR_ST

> omf_prsnl_timehour_st

**Description:** Operations Profiling - Hour level timesheet data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE |  |  | The internal Cerner date representation of the day on which the individual worked. |
| 2 | `ACTIVITY_MIN_NBR` | DOUBLE |  |  | The minute of day, that represents the hour in which the individual performed work. This also corresponds to the first minute of each hour (1, 61, 121, 181, 241 ... 1381 ). |
| 3 | `ACTIVITY_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `NUM_MIN` | DOUBLE |  |  | The number of minutes work was performed during the hour. |
| 5 | `OT_NUM_MIN` | DOUBLE |  |  | The number of overtime minutes that work was performed during the hour. |
| 6 | `PRSNL_PAYPERIOD_ID` | DOUBLE | NOT NULL |  | Not used |
| 7 | `PRSNL_TIMEDATE_ID` | DOUBLE | NOT NULL |  | The identifier for the person's work period that the hour corresponds to. |
| 8 | `PRSNL_TIMEHOUR_ID` | DOUBLE | NOT NULL |  | The unique row identifier for the table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

