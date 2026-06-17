# HF_D_DATE

> The HealthSentry Date table that contains the parts of the date for the calendar.

**Description:** HF_D_DATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATE_DT` | DATETIME |  |  | The date representation. |
| 2 | `DATE_DT_TM` | DATETIME |  |  | ** OBSOLETE -- use column DATE_DT |
| 3 | `DATE_ID` | DOUBLE |  |  | DATE IDENTIFIER |
| 4 | `DAY_NUMBER_IN_MONTH` | DOUBLE |  |  | The day of the month of the date. |
| 5 | `DAY_NUMBER_OF_WEEK` | DOUBLE |  |  | The numeric representation of the day of week of the date. |
| 6 | `DAY_OF_WEEK` | VARCHAR(9) |  |  | The display name of the day of week of the date. |
| 7 | `HOLIDAY_IND` | DOUBLE |  |  | Indicates if the day is a holiday. |
| 8 | `MONTH` | DOUBLE |  |  | The numeric representation of the month of the date. |
| 9 | `MONTH_NAME` | VARCHAR(9) |  |  | The display name of the month of the date. |
| 10 | `QUARTER` | DOUBLE |  |  | The quarter of the date. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |
| 14 | `WEEKDAY_IND` | DOUBLE |  |  | Indicates if the day is a weekend. |
| 15 | `WEEK_NUMBER_IN_YEAR` | DOUBLE |  |  | The week number of the date. |
| 16 | `YEAR` | DOUBLE |  |  | The year of the date. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

