# DEM_XTRCT

> Contains report extract meta-data information.

**Description:** Data Extract Management - Extract  
**Table type:** REFERENCE  
**Primary key:** `DEM_XTRCT_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEM_XTRCT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a row of report extract meta-data information. |
| 2 | `DLMTR_CHAR` | VARCHAR(100) |  |  | The type of character delimiter to be used in the extract expression: "\|", ",", etc. |
| 3 | `FILENAME_PREFIX` | VARCHAR(100) |  |  | The path and file name prefix for a given extract type. |
| 4 | `FORMAT_OBJ_NAME` | VARCHAR(30) |  |  | Name of the extract format script. |
| 5 | `QLFCTN_OBJ_NAME` | VARCHAR(100) |  |  | Name of the qualification service to be executed to retrieve data to extract. |
| 6 | `REXTRCT_DAYS` | DOUBLE | NOT NULL |  | Identifies the number of days to re-extract to validate that the data warehouse reflects any updates that have occurred in Millennium since the original extraction of an extract entity. |
| 7 | `SLICE_SIZE_CNT` | DOUBLE | NOT NULL |  | The number of Extract Instance Slice Items Per Slice |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `XTRCT_OBJ_NAME` | VARCHAR(100) |  |  | Name of the Extract service to be executed to retrieve the entity being extracted. |
| 14 | `XTRCT_TYPE_CD` | DOUBLE | NOT NULL |  | Type of entity to be extracted ( revenue, ATB, Payment/Adjustments, etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEM_XTRCT_NSTNC](DEM_XTRCT_NSTNC.md) | `DEM_XTRCT_ID` |

