# OMF_PV_SCHED

> Schedule information for PowerVision views.

**Description:** OMF PV SCHED  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_NUMBER` | DOUBLE |  |  | Application this schedule is for - e.g. 950001 for PowerVision. |
| 3 | `DAY_OF_MONTH` | DOUBLE |  |  | Day of month. Either 1->31 for day of month; or 0 = first; 1 = second; 2 = third; 3 = fourth; 4 = last e.g. Sunday of the month. |
| 4 | `DAY_OF_WEEK` | VARCHAR(8) |  |  | String holding the days of week to run. 1=Sun through 7=Sat. 145 would indicator tor run this every Sunday, Wednesday, and Thursday. |
| 5 | `DEL_AFTER_DAYS` | DOUBLE |  |  | How many days after creating the result set should this data be kept. |
| 6 | `END_RUN_DT_NBR` | DOUBLE |  |  | Julian date when run finished. |
| 7 | `END_RUN_DT_TM` | DATETIME |  |  | Date when run finished. |
| 8 | `EVERY` | DOUBLE |  |  | How often is this to be run - e.g. every 2 days, 1 week, 3 months. |
| 9 | `LAST_RUN_DT_NBR` | DOUBLE |  |  | Julian date when this was last run. |
| 10 | `LAST_RUN_DT_TM` | DATETIME |  |  | Date when this was last run. |
| 11 | `LAST_RUN_MIN_NBR` | DOUBLE |  |  | Minute of day when this was last run. |
| 12 | `NEXT_RUN_DT_NBR` | DOUBLE |  |  | Julian date when this should be next run. |
| 13 | `NEXT_RUN_DT_TM` | DATETIME |  |  | Date when this should be next run. |
| 14 | `NEXT_RUN_MIN_NBR` | DOUBLE |  |  | Minute between 1 and 1440 when this should be next run. |
| 15 | `OMF_PV_ITEM_ID` | DOUBLE | NOT NULL |  | Saved view. |
| 16 | `RECURRENCE_FLAG` | DOUBLE |  |  | Daily, weekly, monthly indicator. |
| 17 | `TIME_OF_DAY` | VARCHAR(10) |  |  | String in HHMM format when this should be run. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `USER_ID` | DOUBLE | NOT NULL |  | Users person_id whose saved view is being run. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

