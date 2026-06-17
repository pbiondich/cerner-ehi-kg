# BR_PAL_COLUMNS

> holds patient access list information while building

**Description:** BR PAL COLUMNS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Bedrock Client ID from BR_CLIENT |
| 2 | `COLUMN_CD` | DOUBLE | NOT NULL |  | This is the unique identifier to the column from codeset 6023Column |
| 3 | `COLUMN_DESCRIPTION` | VARCHAR(150) |  |  | describes what the column is used for |
| 4 | `COLUMN_MEANING` | VARCHAR(15) |  |  | cdf_meaning from 6023 for certain columns |
| 5 | `COLUMN_NAME` | VARCHAR(40) |  |  | display for the PAL column |
| 6 | `COLUMN_NAME_KEY` | VARCHAR(40) | NOT NULL |  | uppercase column_name |
| 7 | `COLUMN_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the type of Patient Access List columns |
| 8 | `SECTION` | VARCHAR(20) |  |  | Display for the type of PAL section |
| 9 | `START_VERSION_NBR` | DOUBLE |  |  | Identifies which version of start has been loaded |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

