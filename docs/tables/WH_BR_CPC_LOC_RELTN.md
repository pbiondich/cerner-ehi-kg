# WH_BR_CPC_LOC_RELTN

> This table Stores the relationship between CPCs and locations.

**Description:** WH_BR_CPC_LOC_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CPC_ID` | DOUBLE | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `BR_CPC_LOC_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_CPC_LOC_RELTN table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which ETL extract was run |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date and time for which first ETL extract was run |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date and time for which last ETL extract was run |
| 11 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location that is a part of this CPC group. |
| 12 | `ORIG_BR_CPC_LOC_RELTN_ID` | DOUBLE | NOT NULL |  | Used for versioning. Contains the original PK value for BR_CPC_LOC_RELTN_ID |
| 13 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_USER` | VARCHAR(40) |  |  | The user that updated the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

