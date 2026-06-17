# PM_RPT_BATCH

> Batch reporting table for Person Management

**Description:** PM RPT BATCH  
**Table type:** REFERENCE  
**Primary key:** `BATCH_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_DESCRIPTION` | CHAR(100) |  |  | Free-text description of the defined batch of Person Management Reports |
| 6 | `BATCH_ID` | DOUBLE | NOT NULL | PK | Primary Key attribute |
| 7 | `BATCH_NAME` | CHAR(20) | NOT NULL |  | Name of the batch defined for Person Management Reporting |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `DATA_STATUS_CD` | DOUBLE |  |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 10 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 11 | `DATA_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the data_status_cd to be set or change. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_RPT_BATCH_PARAMS](PM_RPT_BATCH_PARAMS.md) | `BATCH_ID` |

