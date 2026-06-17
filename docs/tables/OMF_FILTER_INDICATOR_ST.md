# OMF_FILTER_INDICATOR_ST

> Stores number of times a given indicator was used as part of a filter

**Description:** OMF filter usage table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_CNT` | DOUBLE |  |  | Number of times the indicator was used in a filter |
| 2 | `FILTER_NAME` | VARCHAR(255) |  |  | Name of filter used when creating the view. |
| 3 | `GRID_CD` | DOUBLE | NOT NULL |  | PowerVision View which was filtered by the indicator. Other codesets can be used besides 14265 depending on the team defining the value. |
| 4 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | Indicator which was used in a filter. Other codesets can be used besides 14265 depending on the team defining the value. |
| 5 | `LAST_FILTER_DT_TM` | DATETIME |  |  | Last time this indicator was used as a filter for the view |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

