# PCS_SCHEDULE_SEGMENT

> Contains information about a schedule segment (a block of time). For example, it is used for automatic authorization and clinical validation of lab instruments. The parameters for this may vary by schedule segment.

**Description:** PCS Schedule Segment  
**Table type:** REFERENCE  
**Primary key:** `PCS_SCHEDULE_SEGMENT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism within catalog type code. |
| 2 | `BEG_TM_NBR` | DOUBLE | NOT NULL |  | The begin time of this schedule segment |
| 3 | `DAY_OF_WEEK_BIT` | DOUBLE | NOT NULL |  | The value that determines the day(s) of the week this schedule segment applies to. |
| 4 | `END_TM_NBR` | DOUBLE | NOT NULL |  | The end time of this schedule segment |
| 5 | `PCS_SCHEDULE_SEGMENT_ID` | DOUBLE | NOT NULL | PK | The primary key of this table |
| 6 | `SCHEDULE_CD` | DOUBLE | NOT NULL |  | The schedule that the group of segment rows are linked to. |
| 7 | `SYSTEM_ON_IND` | DOUBLE | NOT NULL |  | Indicates whether clinical validation and autoverification are in effect for this schedule segment. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCS_SCHEDULE_SEG_HLDY_R](PCS_SCHEDULE_SEG_HLDY_R.md) | `PCS_SCHEDULE_SEGMENT_ID` |

