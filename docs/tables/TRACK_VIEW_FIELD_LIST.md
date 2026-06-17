# TRACK_VIEW_FIELD_LIST

> Stores display configuration and the list of fields that will be displayed in a tracking view.

**Description:** Tracking View Field List  
**Table type:** REFERENCE  
**Primary key:** `TRACK_VIEW_FIELD_LIST_ID`  
**Columns:** 23  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BACK_COLOR` | DOUBLE | NOT NULL |  | Background color for the tracking view |
| 2 | `FONT_COLOR` | DOUBLE | NOT NULL |  | Font color for view |
| 3 | `FONT_FACE` | VARCHAR(64) | NOT NULL |  | Font face for view |
| 4 | `FONT_SIZE` | DOUBLE | NOT NULL |  | Font size for view |
| 5 | `FONT_STYLE` | DOUBLE | NOT NULL |  | Font Style for view |
| 6 | `FREEZE_FIELD` | DOUBLE | NOT NULL |  | Field after which the spreadsheet will scroll |
| 7 | `GROUP_BACK_COLOR` | DOUBLE | NOT NULL |  | The background color for grouper rows |
| 8 | `GROUP_FONT_COLOR` | DOUBLE | NOT NULL |  | The font color for grouper rows |
| 9 | `GROUP_FONT_FACE` | VARCHAR(64) | NOT NULL |  | The font face for grouper rows |
| 10 | `GROUP_FONT_SIZE` | DOUBLE | NOT NULL |  | The font size for grouper rows |
| 11 | `GROUP_FONT_STYLE` | DOUBLE | NOT NULL |  | Bitmask of font styles, BOLD = 1, ITALIC = 2 |
| 12 | `GROUP_HEADER_TXT` | VARCHAR(64) | NOT NULL |  | Indicates what the rows are being grouped by. |
| 13 | `GROUP_MAX_ROW_CNT` | DOUBLE | NOT NULL |  | max row count for group |
| 14 | `GROUP_ROWS_IND` | DOUBLE | NOT NULL |  | Stores whether this tracking view will group rows according to the first sorted field or not. |
| 15 | `LIST_TYPE_FLAG` | DOUBLE | NOT NULL |  | Not Specified = 0, Group List = 1, Bed List = 2, Location List = 4, Provider List = 8, Case Tracking List = 16 |
| 16 | `SOLUTION_FLAG` | DOUBLE | NOT NULL |  | Flag that specifies for which solution this tracking view field list is valid. FirstNet, SurgiNet, etc. |
| 17 | `TRACK_VIEW_FIELD_LIST_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VIEW_NAME` | VARCHAR(64) | NOT NULL |  | View Name for tracking view |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [TRACK_FIELD_SPEC](TRACK_FIELD_SPEC.md) | `TRACK_VIEW_FIELD_LIST_ID` |
| [TRACK_LIST](TRACK_LIST.md) | `TRACK_VIEW_FIELD_LIST_ID` |

