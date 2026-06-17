# DM_PARALLEL_README_STATS

> Timing metrics for the parallel readmes.

**Description:** DM_PARALLEL_README_STATS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LAST_BATCH_TM` | DOUBLE | NOT NULL |  | A time in seconds of the last batch time |
| 2 | `MAX_BATCH_TM` | DOUBLE | NOT NULL |  | A time value in seconds to track the longest batch size processed |
| 3 | `MIN_BATCH_TM` | DOUBLE | NOT NULL |  | A time value in seconds to track the shortest batch size processed |
| 4 | `RANGE_NAME` | VARCHAR(200) | NOT NULL |  | AN ASSIGNED NAME FOR THE RANGE |
| 5 | `README_ID` | DOUBLE | NOT NULL |  | Reference to the Readme ID logging this row. |
| 6 | `README_STATS_ID` | DOUBLE | NOT NULL |  | PRIMAR KEY |
| 7 | `STD_DVTN_SQUARE` | DOUBLE | NOT NULL |  | The standard deviation for batch execution |
| 8 | `TOTAL_ELAPSED_TM` | DOUBLE | NOT NULL |  | A time value in seconds to track readme execution time. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

