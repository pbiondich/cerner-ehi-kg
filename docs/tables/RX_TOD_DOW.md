# RX_TOD_DOW

> Stores unique combinations of times of day and days of week.

**Description:** Pharmacy Time of Day Day of Week  
**Table type:** REFERENCE  
**Primary key:** `RX_TOD_DOW_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DAYS_OF_WEEK_TEXT` | VARCHAR(15) | NOT NULL |  | String representation of the days of week of a VDA frequency. Expected format is DOW1;DOW2;DOW3;etc. For example a frequency with Monday, Wednesday, Friday will display as 2;4;6 |
| 2 | `RX_TOD_DOW_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_TOD_DOW table. |
| 3 | `TIMES_OF_DAY_TEXT` | VARCHAR(1000) | NOT NULL |  | String representation of the times of day of a VDA frequency in minutes from midnight. Expected format is TOD1;TOD2;TOD3;etc. For example, a frequency with 0800 and 2000 times of day will display as 480;1200 |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FREQUENCY_SCHEDULE](FREQUENCY_SCHEDULE.md) | `RX_TOD_DOW_ID` |

