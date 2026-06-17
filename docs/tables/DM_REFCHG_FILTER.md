# DM_REFCHG_FILTER

> Stores the tables which need special filtering of rows in RDDS.

**Description:** Data Management reference change filter  
**Table type:** REFERENCE  
**Primary key:** `TABLE_NAME`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FILTER_TYPE` | VARCHAR(30) | NOT NULL |  | Type of filtering done - INCLUDE values, EXCLUDE values, or NONE - only a statement exists |
| 3 | `FILTER_VERSION_NBR` | DOUBLE |  |  | A column to hold the version number of the resulting filter object |
| 4 | `STATEMENT_IND` | DOUBLE | NOT NULL |  | Indicates whether a statement (usually a Select) is used as part of the filtering. |
| 5 | `TABLE_NAME` | VARCHAR(30) | NOT NULL | PK | Name of the table which has a filter requirement on it. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_REFCHG_FILTER_PARM](DM_REFCHG_FILTER_PARM.md) | `TABLE_NAME` |
| [DM_REFCHG_FILTER_TEST](DM_REFCHG_FILTER_TEST.md) | `TABLE_NAME` |

