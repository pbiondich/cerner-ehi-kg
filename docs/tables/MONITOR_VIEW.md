# MONITOR_VIEW

> This table contains reference data for a specific monitor(s).

**Description:** Monitor view  
**Table type:** REFERENCE  
**Primary key:** `MONITOR_VIEW_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(200) |  |  | The description of the monitor. |
| 2 | `DISCIPLINE_TYPE_CD` | DOUBLE | NOT NULL |  | Used to store the internal code for the discipline type. Used for filtering. |
| 3 | `DISPLAY` | VARCHAR(50) |  |  | Display value for the monitor. |
| 4 | `DISPLAY_HEADER_IND` | DOUBLE |  |  | The display_header_ind indicates if the display should be shown with the monitor |
| 5 | `DISPLAY_KEY_CAP` | VARCHAR(50) |  |  | This is the display name with all spaces removed and in all caps. Used as index |
| 6 | `MONITOR_VIEW_ID` | DOUBLE | NOT NULL | PK | The monitor view id uniquely idenitifies a row on the monitor view table |
| 7 | `REFRESH_TIME_SEC` | DOUBLE |  |  | The refresh time sec indicates how many seconds between each auto refresh |
| 8 | `SCROLL_TIME_SEC` | DOUBLE |  |  | The scroll time sec indicates how many seconds between each auto refresh |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MONITOR_VIEW_FIELD](MONITOR_VIEW_FIELD.md) | `MONITOR_VIEW_ID` |

