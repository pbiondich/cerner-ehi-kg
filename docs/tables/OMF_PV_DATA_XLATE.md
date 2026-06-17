# OMF_PV_DATA_XLATE

> translates column headers in column headings in the imported data to summary table columns, also contains attributes for each field in the imported data

**Description:** translates column headers in imported data to summary table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(40) |  |  | The name of the column header in the imported CSV |
| 2 | `DATE_IND` | DOUBLE |  |  | Set to 1 if the imported data is a date. |
| 3 | `FILTER_IND` | DOUBLE |  |  | Indicates whether this column is filterable. |
| 4 | `PD_GRID_CD` | DOUBLE | NOT NULL |  | Uniquely defines the grid |
| 5 | `PK_IND` | DOUBLE |  |  | Indicates whether this column is part of the logical primary key for update/insert logic. |
| 6 | `ST_COLUMN_NAME` | VARCHAR(40) | NOT NULL |  | The name of the column in OMF_PV_DATA_ST where this column will be stored. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

