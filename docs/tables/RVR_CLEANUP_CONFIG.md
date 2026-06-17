# RVR_CLEANUP_CONFIG

> Revenue Cycle Registration - Used to store cleanup configuration information.

**Description:** Revenue Cycle Registration - Cleanup Configuration  
**Table type:** ACTIVITY  
**Primary key:** `RVR_CLEANUP_CONFIG_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_SIZE_NBR` | DOUBLE |  |  | The maximum number of rows used by each batch mode script. Changeable. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FREQUENCY_TXT` | VARCHAR(25) |  |  | The frequency a cleanup program is called. D-Daily, W-Weekly, M-Monthly |
| 9 | `LAST_PERSON_ID` | DOUBLE |  | FK→ | LAST_PERSON_ID changed. Used by Scripts in batch mode. |
| 10 | `LAST_RUN_BATCH_CNT` | DOUBLE |  |  | The batch number that was last processed in ALL mode. |
| 11 | `LAST_RUN_DT_TM` | DATETIME |  |  | The date this script was last run in ALL mode. |
| 12 | `MAX_ROWS_NBR` | DOUBLE |  |  | Maximum rows updated per execution in ALL mode. |
| 13 | `PROGRAM_NAME` | VARCHAR(100) |  |  | The name of the CCL program that is to be run during a clean up. |
| 14 | `RVR_CLEANUP_CONFIG_ID` | DOUBLE | NOT NULL | PK | A system generated number used to uniquely identify a row on the RVR_CLEANUP_CONFIG table. |
| 15 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RVR_CLEANUP_LOG](RVR_CLEANUP_LOG.md) | `RVR_CLEANUP_CONFIG_ID` |

