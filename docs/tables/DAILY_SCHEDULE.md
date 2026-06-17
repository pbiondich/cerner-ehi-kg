# DAILY_SCHEDULE

> The daily schedule table represents the individual times associated with a specific time scheme.

**Description:** Daily Schedule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CUTOFF_WINDOW_IND` | DOUBLE |  |  | Indicates that additional transmissions will not be processed after the cutoff time. |
| 2 | `DAY_OF_WEEK` | DOUBLE | NOT NULL |  | Represents the day of week for this specific time frame for a time scheme. Day of week: 0 = Sun¿6 = Sat. |
| 3 | `END_TIME` | DOUBLE |  |  | Ending time for this specific day and time frame for a time scheme. (Military Time) |
| 4 | `QUALIFIER` | DOUBLE | NOT NULL |  | Needed for multiple times in the same day. |
| 5 | `START_TIME` | DOUBLE |  |  | Starting time for this specific day and time frame for a time scheme. (Military Time) |
| 6 | `TIME_SCHEME_ID` | DOUBLE | NOT NULL |  | Unique numeric identifier for each Time Scheme that the user defines.Column |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

