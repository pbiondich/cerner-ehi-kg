# PM_RBC_LONG_TEXT

> The PM_RBC_LONG_TEXT table stores long text information for room & bed charge process activity data.

**Description:** Person Management - Room and Board Charge Long Text  
**Table type:** ACTIVITY  
**Primary key:** `PM_RBC_LONG_TEXT_ID`  
**Columns:** 15  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LONG_CLOB` | LONGTEXT |  |  | Used to store the text for the long text identifier. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Used to store the identifier for the parent |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Used to store the name for the parent |
| 10 | `PM_RBC_LONG_TEXT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the PM_RBC_LONG_TEXT table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [PM_RBC_RS_ENCNTR_R](PM_RBC_RS_ENCNTR_R.md) | `LOG_LONG_TEXT_ID` |
| [PM_RBC_RS_ENCNTR_R](PM_RBC_RS_ENCNTR_R.md) | `QUERY_LONG_TEXT_ID` |
| [PM_RBC_RUN](PM_RBC_RUN.md) | `LOG_LONG_TEXT_ID` |
| [PM_RBC_RUN_SET](PM_RBC_RUN_SET.md) | `LOG_LONG_TEXT_ID` |
| [PM_RBC_RUN_SET](PM_RBC_RUN_SET.md) | `QUERY_LONG_TEXT_ID` |

