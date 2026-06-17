# OMF_PVB_DATA

> Result set data for PowerVision scheduled views.

**Description:** OMF PVB DATA  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL |  | Id of the result set which this data is for. |
| 2 | `DATA_VALUE` | DOUBLE |  |  | Numeric value for a FACT column. |
| 3 | `DISP1` | VARCHAR(255) |  |  | Data to display. |
| 4 | `DISP2` | VARCHAR(255) |  |  | Data to display. |
| 5 | `DISP3` | VARCHAR(255) |  |  | Data to display. |
| 6 | `DISP4` | VARCHAR(255) |  |  | Data to display. |
| 7 | `D_COL` | DOUBLE | NOT NULL |  | The column portion of a row-column intersection (address). |
| 8 | `D_ROW` | DOUBLE | NOT NULL |  | The row portion of a row-column intersection (address). |
| 9 | `UNIQ` | VARCHAR(255) |  |  | Value which provides uniqueness to the column's data - e.g. person_id as opposed to person_name. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

