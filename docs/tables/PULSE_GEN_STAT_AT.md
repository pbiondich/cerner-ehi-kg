# PULSE_GEN_STAT_AT

> Contains statistics from a single Atrial Tachyarrhythmia event

**Description:** Pulse Generator Atrial Tachyarrhythmia Statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BURDEN_PERCENT` | DOUBLE |  |  | The percent of time in AT AF per day |
| 2 | `MODE_SW_COUNT` | DOUBLE |  |  | The number of mode switches |
| 3 | `MODE_SW_COUNT_PER_DAY` | DOUBLE |  |  | The average number of mode switches per day |
| 4 | `MODE_SW_MAX_DURATION` | DOUBLE |  |  | The maximum contiguous time the device is in AT mode switch |
| 5 | `MODE_SW_PERCENT_TIME` | DOUBLE |  |  | The percentage of time the device is in AT mode switch |
| 6 | `MODE_SW_PERCENT_TIME_PER_DAY` | DOUBLE |  |  | The percentage of time per day the device is in AT mode switch |
| 7 | `PULSE_GEN_STAT_AT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `PULSE_GEN_STAT_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator statistic associated with this AT statistic |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_STAT_ID` | [PULSE_GEN_STAT](PULSE_GEN_STAT.md) | `PULSE_GEN_STAT_ID` |

