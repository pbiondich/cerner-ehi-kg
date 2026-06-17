# STORAGE_ITEM_CELL

> Storage Item Cell

**Description:** PathNet Storage Tracking activity table. The actual storage locations.  
**Table type:** ACTIVITY  
**Primary key:** `STORAGE_ITEM_CELL_ID`  
**Columns:** 11  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `STORAGE_CHILD_CD` | DOUBLE |  |  | Obsolete, No longer being used. Indicates the child id of this cell. Racks are children of trays and containers are children of racks. |
| 2 | `STORAGE_ITEM_CD` | DOUBLE | NOT NULL |  | The parent storage item of this cell. |
| 3 | `STORAGE_ITEM_CELL_ID` | DOUBLE | NOT NULL | PK | The unique id of a particular cell. |
| 4 | `STORAGE_ITEM_COL` | DOUBLE |  |  | Column of the cell. The storage_item_col and storage_item_row determines the cell's location. |
| 5 | `STORAGE_ITEM_ROW` | DOUBLE |  |  | Row of the cell. The storage_item_col and storage_item_row determines the cell's location. |
| 6 | `STORAGE_TYPE_CD` | DOUBLE | NOT NULL |  | Obsolete. No longer being used. rack or tray |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CONTAINER](CONTAINER.md) | `STORAGE_RACK_CELL_ID` |
| [CONTAINER_EVENT](CONTAINER_EVENT.md) | `STORAGE_RACK_CELL_ID` |
| [STORAGE_CONTENT](STORAGE_CONTENT.md) | `STORAGE_ITEM_CELL_ID` |
| [STORAGE_CONTENT_EVENT](STORAGE_CONTENT_EVENT.md) | `STORAGE_ITEM_CELL_ID` |

