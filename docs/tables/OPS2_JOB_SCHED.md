# OPS2_JOB_SCHED

> The operations job schedule table stores information about the schedule of a job group or a job. A schedule relates one to one with a job group or job, never both.

**Description:** Operations Job Schedule  
**Table type:** REFERENCE  
**Primary key:** `OPS2_JOB_SCHED_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DATE_RECUR_INTERVAL_NBR` | DOUBLE | NOT NULL |  | The interval between each occurrence of the scheduled item. The unit of measurement for how this value is interpreted, flexes based on the schedule type. For example, this value will be an interval of days for daily jobs. |
| 4 | `END_DATE_DT_TM` | DATETIME |  |  | The last day the scheduled item will occur. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `END_TIME_DT_TM` | DATETIME |  |  | For scheduled items that occur more than once in a single day, the last time of the day that the scheduled item will occur. |
| 7 | `OPS2_DAY_OF_MONTH_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_DAY_OF_MONTH. Indicates which days of the month this schedule applies. |
| 8 | `OPS2_DAY_OF_WEEK_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_DAY_OF_WEEK. Indicates which days of the week this schedule applies. |
| 9 | `OPS2_JOB_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_JOB_GROUP. Indicates to which job group this schedule applies. |
| 10 | `OPS2_JOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_JOB. Indicates to which job or job within a job group this schedule applies. |
| 11 | `OPS2_JOB_SCHED_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the OPS2_JOB_SCHED table. |
| 12 | `OPS2_MONTH_OF_YEAR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_MONTH_OF_YEAR. Indicates which months of the year this schedule applies. |
| 13 | `OPS2_WEEK_OF_MONTH_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_WEEK_OF_MONTH. Indicates which weeks of the month this schedule applies. |
| 14 | `ORIG_OPS2_JOB_SCHED_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the job schedules. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 15 | `START_DATE_DT_TM` | DATETIME |  |  | The first day the scheduled item will occur. |
| 16 | `START_TIME_DT_TM` | DATETIME | NOT NULL |  | The first time of the day that the scheduled item will occur. |
| 17 | `TIME_RECUR_INTERVAL_NBR` | DOUBLE | NOT NULL |  | For scheduled items that occur more than once in a single day, the interval between each occurrence in a day of the scheduled item. The unit of measurement for how this value is interpreted, is defined by TIME_RECUR_INTERVAL_UOM_TXT. |
| 18 | `TIME_RECUR_INTERVAL_UOM_TXT` | VARCHAR(10) | NOT NULL |  | Indicates if a scheduled item occurs more than once in a single day, and if so, what unit of measurement is being used to signify the interval between occurrences. The schedule item may recur by the hour (TIME_RECUR_INTERVAL_UOM_TXT = 'H'), by the minute (TIME_RECUR_INTERVAL_UOM_TXT = 'M'), or not at all (TIME_RECUR_INTERVAL_UOM_TXT = ''). |
| 19 | `TIME_RECUR_SKIP_OVERDUE_IND` | DOUBLE | NOT NULL |  | For scheduled items that occur more than once in a single day, indicates if redundant occurrences of the item should be automatically skipped if multiple occurrences are found to be overdue (TIME_RECUR_SKIP_OVERDUE_IND = 1) or be redundantly executed (TIME_RECUR_SKIP_OVERDUE_IND = 0). |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS2_DAY_OF_MONTH_ID` | [OPS2_DAY_OF_MONTH](OPS2_DAY_OF_MONTH.md) | `OPS2_DAY_OF_MONTH_ID` |
| `OPS2_DAY_OF_WEEK_ID` | [OPS2_DAY_OF_WEEK](OPS2_DAY_OF_WEEK.md) | `OPS2_DAY_OF_WEEK_ID` |
| `OPS2_JOB_GROUP_ID` | [OPS2_JOB_GROUP](OPS2_JOB_GROUP.md) | `OPS2_JOB_GROUP_ID` |
| `OPS2_JOB_ID` | [OPS2_JOB](OPS2_JOB.md) | `OPS2_JOB_ID` |
| `OPS2_MONTH_OF_YEAR_ID` | [OPS2_MONTH_OF_YEAR](OPS2_MONTH_OF_YEAR.md) | `OPS2_MONTH_OF_YEAR_ID` |
| `OPS2_WEEK_OF_MONTH_ID` | [OPS2_WEEK_OF_MONTH](OPS2_WEEK_OF_MONTH.md) | `OPS2_WEEK_OF_MONTH_ID` |
| `ORIG_OPS2_JOB_SCHED_ID` | [OPS2_JOB_SCHED](OPS2_JOB_SCHED.md) | `OPS2_JOB_SCHED_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OPS2_JOB_SCHED](OPS2_JOB_SCHED.md) | `ORIG_OPS2_JOB_SCHED_ID` |

