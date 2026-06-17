# OMF_GRID

> Grids related to a view and grouped by product. Also, tells whether a total line should be displayed.

**Description:** OMF Grids.  
**Table type:** REFERENCE  
**Primary key:** `GRID_CD`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLIENT_SA_DESC` | VARCHAR(255) |  |  | Client defined description of a subject area in PowerVision. Not yet used. |
| 3 | `DISPLAY` | VARCHAR(40) |  |  | Subject area display name. This is optional. If not entered the code_value.display for the grid_cd will be used. |
| 4 | `GRID_CD` | DOUBLE | NOT NULL | PK | Grid code value. |
| 5 | `GRID_GROUP_CD` | DOUBLE | NOT NULL |  | The grid's group - for PowerVision/Admin Tool display. Other codesets can be used besides 14265 depending on the team defining the value. |
| 6 | `GRID_GROUP_DISPLAY` | VARCHAR(100) |  |  | Grid group display name. This is optional. If not entered, the code_value.display for the GRID_CD column will be used. |
| 7 | `OWNER` | VARCHAR(40) |  |  | Cerner team owner. Not used yet. |
| 8 | `PVDB_IND` | DOUBLE |  |  | Used to indicate that this grid was built using the data import process. |
| 9 | `PVDB_NAME` | VARCHAR(20) |  |  | Indicates the name that the Oracle view and CCL DBIMPORT program will be called. Only applicable when grid is created using the data import process. |
| 10 | `SA_DESC` | VARCHAR(255) |  |  | Subject area description. |
| 11 | `TOTAL_IND` | DOUBLE |  |  | No longer used. Indicates whether a total line should appear on the grid. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VIEW_CD` | DOUBLE | NOT NULL |  | cdf_meaning='VIEW', display = . Other codesets can be used besides 14265 depending on the team defining the value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OMF_AUDIT_CAT_GRID_RELTN](OMF_AUDIT_CAT_GRID_RELTN.md) | `GRID_CD` |
| [OMF_GRID_COLUMN](OMF_GRID_COLUMN.md) | `GRID_CD` |

