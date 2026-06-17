# PFT_EVENT_PATTERN

> pft event pattern

**Description:** pft event pattern  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CALENDAR_MONTH` | DOUBLE |  |  | Month of the year (e.g. January, February etc.) |
| 7 | `CALENDAR_MONTH_CD` | DOUBLE | NOT NULL |  | Code set for the calendar months - Not used, to be removed |
| 8 | `DAY_MASK` | DOUBLE |  |  | Day Mask |
| 9 | `DAY_OF_MONTH` | DOUBLE |  |  | Day of Month |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `INSTANCE` | DOUBLE |  |  | Instance of the event |
| 12 | `INTERVAL` | DOUBLE |  |  | Interval of the event |
| 13 | `MAX_END_DT_TM` | DATETIME |  |  | The recurrence will end on this date |
| 14 | `MAX_OCCURANCE` | DOUBLE |  |  | The maximumamount of times this event will happen |
| 15 | `PFT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key |
| 16 | `PFT_EVENT_PATTERN_ID` | DOUBLE | NOT NULL |  | Unique Key |
| 17 | `PFT_PATTERN_TYPE_CD` | DOUBLE | NOT NULL |  | Daily, Monthly, Yearly, etc. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_EVENT_ID` | [PFT_EVENT](PFT_EVENT.md) | `PFT_EVENT_ID` |

