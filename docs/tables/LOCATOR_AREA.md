# LOCATOR_AREA

> Defines the placement and style of a location in the Locator application.

**Description:** Locator Area  
**Table type:** REFERENCE  
**Primary key:** `LOCATOR_AREA_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_TIME` | DOUBLE |  |  | Amount of time before this location is flagged as wait time being exceeded. |
| 2 | `BOTTOM` | DOUBLE |  |  | Used to calculate height of locator area. |
| 3 | `CAPTION` | VARCHAR(50) |  |  | Not Used. |
| 4 | `LEFT` | DOUBLE |  |  | X coordinate of locator area. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Unique identifier for the location the locator area represents. |
| 6 | `LOCATOR_AREA_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the locator area. |
| 7 | `MAX_ITEMS` | DOUBLE |  |  | Not Used. |
| 8 | `RIGHT` | DOUBLE |  |  | Used to calculate width of locator area. |
| 9 | `STYLE` | DOUBLE |  |  | Identifies the style of the location¿s display 0 = icon view 1 = column view. |
| 10 | `TOP` | DOUBLE |  |  | Y coordinate of locator area. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LOCATOR_VIEW_AREA_R](LOCATOR_VIEW_AREA_R.md) | `LOCATOR_AREA_ID` |

