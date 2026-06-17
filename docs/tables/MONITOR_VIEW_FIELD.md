# MONITOR_VIEW_FIELD

> This table defines the relationship between a monitor view and its column fields

**Description:** Monitor View Field  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRITICAL_DISPLAY_COLOR` | DOUBLE |  |  | RGB value of the color displayed at critical time. |
| 2 | `CRITICAL_TIME_MIN` | DOUBLE |  |  | %remaing% |
| 3 | `DISPLAY_LENGTH` | DOUBLE |  |  | Character length of the display field. |
| 4 | `FIELD_SEQUENCE` | DOUBLE |  |  | Sequence number determining the order in when column fields should be displayed on a monitor. |
| 5 | `MONITOR_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the monitor_field table. Defines a field to associate with a monitor. |
| 6 | `MONITOR_VIEW_FIELD_ID` | DOUBLE | NOT NULL |  | Meaningless number that uniquely defines a row on this table. |
| 7 | `MONITOR_VIEW_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to monitor_view table. Defines which monitor this field is related to. |
| 8 | `NORMAL_DISPLAY_COLOR` | DOUBLE |  |  | RGB value of the color normally displayed. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WARNING_DISPLAY_COLOR` | DOUBLE |  |  | %warningl% |
| 15 | `WARNING_TIME_MIN` | DOUBLE |  |  | %remaing% |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MONITOR_FIELD_ID` | [MONITOR_FIELD](MONITOR_FIELD.md) | `MONITOR_FIELD_ID` |
| `MONITOR_VIEW_ID` | [MONITOR_VIEW](MONITOR_VIEW.md) | `MONITOR_VIEW_ID` |

