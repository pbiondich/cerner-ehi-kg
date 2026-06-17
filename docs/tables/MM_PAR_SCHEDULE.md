# MM_PAR_SCHEDULE

> Information about a route's schedule.

**Description:** MM PAR SCHEDULE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 4 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 5 | `DAY_F_IND` | DOUBLE |  |  | Indicates whether or not the route should run on Friday. |
| 6 | `DAY_M_IND` | DOUBLE |  |  | Indicates whether or not the route should run on Monday. |
| 7 | `DAY_R_IND` | DOUBLE |  |  | Indicates whether or not the route should run on Thursday. |
| 8 | `DAY_SU_IND` | DOUBLE |  |  | Indicates whether or not the route should run on Sunday. |
| 9 | `DAY_S_IND` | DOUBLE |  |  | Indicates whether or not the route should run on Saturday. |
| 10 | `DAY_T_IND` | DOUBLE |  |  | Indicates whether or not the route should run on Tuesday. |
| 11 | `DAY_W_IND` | DOUBLE |  |  | Indicates whether or not the route should run on Wednesday. |
| 12 | `MONTH_APR_IND` | DOUBLE |  |  | Indicates whether or not the route should run in April. |
| 13 | `MONTH_AUG_IND` | DOUBLE |  |  | Indicates whether or not the route should run in August. |
| 14 | `MONTH_DEC_IND` | DOUBLE |  |  | Indicates whether or not the route should run in December. |
| 15 | `MONTH_FEB_IND` | DOUBLE |  |  | Indicates whether or not the route should run in February. |
| 16 | `MONTH_JAN_IND` | DOUBLE |  |  | Indicates whether or not the route should run in January. |
| 17 | `MONTH_JUL_IND` | DOUBLE |  |  | Indicates whether or not the route should run in July. |
| 18 | `MONTH_JUN_IND` | DOUBLE |  |  | Indicates whether or not the route should run in June. |
| 19 | `MONTH_MAR_IND` | DOUBLE |  |  | Indicates whether or not the route should run in March. |
| 20 | `MONTH_MAY_IND` | DOUBLE |  |  | Indicates whether or not the route should run in May. |
| 21 | `MONTH_NOV_IND` | DOUBLE |  |  | Indicates whether or not the route should run in November. |
| 22 | `MONTH_OCT_IND` | DOUBLE |  |  | Indicates whether or not the route should run in October. |
| 23 | `MONTH_SEP_IND` | DOUBLE |  |  | Indicates whether or not the route should run in September. |
| 24 | `PAR_ROUTE_ID` | DOUBLE | NOT NULL |  | The unique id of the route this schedule belongs to. |
| 25 | `PAR_SCHEDULE_ID` | DOUBLE | NOT NULL |  | The unique id of this entry. |
| 26 | `START_TM` | DATETIME |  |  | The time this schedule is expected to run. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

