# STORAGE_ITEM_DESCRIPTION

> Storage Item Description

**Description:** PathNet Storage Tracking reference table containing the properties of trays/rack  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BACK_FRONT_IND` | DOUBLE | NOT NULL |  | Indicates whether to fill from back to front or front to back. |
| 2 | `COLS_ALPHA_IND` | DOUBLE |  |  | Indicates whether to use numbers or letters for the columns. |
| 3 | `CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the type of inventory content a storage item with this description can hold. |
| 4 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates if this particular tray or rack is used as the default tray or rack type. |
| 5 | `LEFT_RIGHT_IND` | DOUBLE | NOT NULL |  | Indicates whether to fill the tray or rack left to right or right to left. |
| 6 | `MAX_COLUMNS` | DOUBLE | NOT NULL |  | The total number of columns of a tray or rack. |
| 7 | `MAX_ROWS` | DOUBLE | NOT NULL |  | The total number of rows of a tray or rack. |
| 8 | `ROWS_ALPHA_IND` | DOUBLE |  |  | Indicates whether the rows are numbered or lettered. |
| 9 | `ROW_COL_IND` | DOUBLE | NOT NULL |  | Indicates whether to fill up a whole row or column first. |
| 10 | `STORAGE_ITEM_DESCRIPTION_CD` | DOUBLE | NOT NULL |  | Unique system id for a tray or rack description. A description is the attrributes of a particular tray or rack. |
| 11 | `STORAGE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates if the description is a tray or rack. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

