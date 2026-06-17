# TRACK_LIST

> Configuration data for Tracking List Views

**Description:** Tracking List configuation  
**Table type:** REFERENCE  
**Primary key:** `TRACK_LIST_ID`  
**Columns:** 18  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BED_VIEW_CD` | DOUBLE | NOT NULL |  | The list of beds to display in the tracking list |
| 2 | `LIST_COLOR_NBR` | DOUBLE | NOT NULL |  | Controls the color of the tab within FirstNet |
| 3 | `LIST_DISPLAY_TXT` | VARCHAR(64) | NOT NULL |  | The name of the tracking list that will be displayed to users |
| 4 | `LIST_NAME` | VARCHAR(64) | NOT NULL |  | Tracking List Name |
| 5 | `LIST_TYPE_FLAG` | DOUBLE | NOT NULL |  | Group List, Bed List, Pick List, etc.GROUP=1, BED=2, LOCATION=4, PROVIDER=8, CASE TRACKING = 16 |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The nursing unit from which to show patients |
| 7 | `LOCATION_VIEW_CD` | DOUBLE | NOT NULL |  | The list of locations to which a patient can be moved. |
| 8 | `REFRESH_INTERVAL` | DOUBLE | NOT NULL |  | Seconds between auto refreshes |
| 9 | `SCROLL_INTERVAL` | DOUBLE | NOT NULL |  | Milliseconds between scrolling to the next row or page. |
| 10 | `SOLUTION_FLAG` | DOUBLE | NOT NULL |  | Enumeration that specifies for which solution this tracking list is valid |
| 11 | `TRACK_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group Code |
| 12 | `TRACK_LIST_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 13 | `TRACK_VIEW_FIELD_LIST_ID` | DOUBLE | NOT NULL | FK→ | The list of fields to display in this tracking list |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_VIEW_FIELD_LIST_ID` | [TRACK_VIEW_FIELD_LIST](TRACK_VIEW_FIELD_LIST.md) | `TRACK_VIEW_FIELD_LIST_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [TRACK_LIST_ASSIGNMENT](TRACK_LIST_ASSIGNMENT.md) | `TRACK_LIST_ID` |
| [TRACK_LIST_FILTER_RELTN](TRACK_LIST_FILTER_RELTN.md) | `TRACK_LIST_ID` |
| [TRACK_LIST_PRSNL_RELTN](TRACK_LIST_PRSNL_RELTN.md) | `TRACK_LIST_ID` |

