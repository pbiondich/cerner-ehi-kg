# UCMR_POSITION_MAP

> Stores the position map settings for a protocol worksheet.

**Description:** Unified Case Manager Reference - Position Map  
**Table type:** REFERENCE  
**Primary key:** `UCMR_POSITION_MAP_ID`  
**Columns:** 27  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ALPHA_COL_HEADER_IND` | DOUBLE | NOT NULL |  | Indicator whether the column headers are labeled using alpha characters. Otherwise, the column headers are labeled using numbers. |
| 4 | `ALPHA_ROW_HEADER_IND` | DOUBLE | NOT NULL |  | Indicator whether the row headers are labeledusing alpha characters. Otherwise, the row headers are labeledusing numbers. |
| 5 | `BACK_FRONT_IND` | DOUBLE | NOT NULL |  | Indicator whether the map is populated back-to-front (top-to-bottom) or front-to-back (bottom-to-top). |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CELLS_PER_BATCH_ITEM_CNT` | DOUBLE | NOT NULL |  | The number of cells that should be populated in the map for each order or container on the batch. |
| 8 | `COL_CNT` | DOUBLE | NOT NULL |  | The number of columns defined to appear for each map. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `FILL_BEFORE_START_IND` | DOUBLE | NOT NULL |  | Indicator whether the position map must be filled out prior to starting the protocol. |
| 11 | `LEFT_RIGHT_IND` | DOUBLE | NOT NULL |  | Indicator whether the map is populated left-to-right or right-to-left. |
| 12 | `LONG_TEXT_NOTES_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier to the formatted rich text associated with a position map. |
| 13 | `MAP_CNT` | DOUBLE | NOT NULL |  | The number of maps defined to appear. |
| 14 | `POSITION_MAP_DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | The position map name that is displayed in applications. This value is editable at anytime after creation. |
| 15 | `POSITION_MAP_NAME` | VARCHAR(40) | NOT NULL |  | The name of this position map. Every position map associated with a worksheet must have a unique name. Cannot be changed after it is created. |
| 16 | `ROWS_FIRST_IND` | DOUBLE | NOT NULL |  | Indicator whether the map is first populated by rows or columns. |
| 17 | `ROW_CNT` | DOUBLE | NOT NULL |  | The number of rows defined to appear for each map. |
| 18 | `SEQ_NBR_IND` | DOUBLE | NOT NULL |  | Indicator whether sequential numbering will be used for identifying each cell in a position map. Otherwise, each cell is identified using coordinates. |
| 19 | `UCMR_POSITION_MAP_ID` | DOUBLE | NOT NULL | PK | Stores unique position map settings for a protocol worksheet. |
| 20 | `UCMR_WORKSHEET_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the worksheet associated with this position map. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `USE_PATTERN_IND` | DOUBLE | NOT NULL |  | Indicator whether the position map will be filled out according to a pattern or manually. |
| 27 | `ZIG_ZAG_IND` | DOUBLE | NOT NULL |  | Indicator whether the map is populated in a zig zag pattern. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_NOTES_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `UCMR_WORKSHEET_ID` | [UCMR_WORKSHEET](UCMR_WORKSHEET.md) | `UCMR_WORKSHEET_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [UCMR_POSITION_MAP_CELL](UCMR_POSITION_MAP_CELL.md) | `UCMR_POSITION_MAP_ID` |
| [UCM_POSITION_MAP_CELL](UCM_POSITION_MAP_CELL.md) | `UCMR_POSITION_MAP_ID` |

