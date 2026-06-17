# SCH_FREQ

> The table hold the scheduling frequencies for recurring scheduling entities such as default schedules or recurring events.

**Description:** Scheduling Frequencies  
**Table type:** ACTIVITY  
**Primary key:** `FREQUENCY_ID`  
**Columns:** 44  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLY_RANGE` | DOUBLE |  |  | Indicate how far the recurring application should apply. The unit of measure is Days. |
| 6 | `BEG_DT_TM` | DATETIME | NOT NULL |  | The start date time of recurring entity. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `COUNTER` | DOUBLE | NOT NULL |  | An internal counter. |
| 10 | `DAILY_APPT_INTERVAL_MINS` | DOUBLE | NOT NULL |  | Minimal minutes between two appointments in a recurrent instances in the same day. |
| 11 | `DAILY_FREQUENCY_NBR` | DOUBLE | NOT NULL |  | Number of appointments per day for a recurring event. |
| 12 | `DAYS_OF_WEEK` | VARCHAR(10) | NOT NULL |  | A character string used to store the valid days of the week. |
| 13 | `DAY_STRING` | VARCHAR(31) | NOT NULL |  | A character string used to store the valid days of the month. |
| 14 | `END_DT_TM` | DATETIME | NOT NULL |  | The end date time of recurring entity. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `END_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling frequency end type. |
| 17 | `END_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling frequency end type. |
| 18 | `FREQUENCY_ID` | DOUBLE | NOT NULL | PK | The unique identifier for a scheduling frequency. |
| 19 | `FREQ_PATTERN_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the frequency pattern. |
| 20 | `FREQ_PATTERN_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the frequency pattern. |
| 21 | `FREQ_STATE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the frequency state. |
| 22 | `FREQ_STATE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the frequency state. Examples are ACTIVE, COMPLETE, DISCONTINUE. |
| 23 | `FREQ_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the frequency type. |
| 24 | `FREQ_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the frequency type. Examples are SERVICE, DEFAULT SCHEDULE, RECURRING APPOINTMENT. |
| 25 | `INTERVAL` | DOUBLE | NOT NULL |  | Defines the time interval in minutes. |
| 26 | `MAX_OCCURANCE` | DOUBLE | NOT NULL |  | Defined the maximum number of occurrances for a frequency. |
| 27 | `MONTH_STRING` | VARCHAR(12) | NOT NULL |  | A string used to denote the valid months in a frequency. |
| 28 | `NEXT_DT_TM` | DATETIME | NOT NULL |  | The last date and time to be considered during the explosion of the frequency. |
| 29 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 30 | `OCCURANCE` | DOUBLE | NOT NULL |  | The sequence of the object in an ordered list. (1 of 2, etc.) |
| 31 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 32 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | The parent table associated to the scheduling frequency. It corresponds to the PARENT_ID. |
| 33 | `PATTERN_OPTION` | DOUBLE | NOT NULL |  | This field is used to store the frequency option chosen by the user. |
| 34 | `REF_FREQ_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling reference frequency. |
| 35 | `UNITS` | DOUBLE | NOT NULL |  | The number of unit such as 4 hours, 180 minutes, etc. |
| 36 | `UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier of the units of measure. |
| 37 | `UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the units of measure. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 44 | `WEEK_STRING` | VARCHAR(6) | NOT NULL |  | A character string used to denote the valid weeks within the month. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `END_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FREQ_PATTERN_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FREQ_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FREQ_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `REF_FREQ_ID` | [SCH_REF_FREQ](SCH_REF_FREQ.md) | `REF_FREQ_ID` |
| `UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SCH_DEF_APPLY](SCH_DEF_APPLY.md) | `FREQUENCY_ID` |
| [SCH_FREQ_DATE](SCH_FREQ_DATE.md) | `FREQUENCY_ID` |

