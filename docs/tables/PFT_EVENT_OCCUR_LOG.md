# PFT_EVENT_OCCUR_LOG

> Contains the log entries of events that are run as part of the daily jobs.

**Description:** pft event occur log  
**Table type:** ACTIVITY  
**Primary key:** `PFT_EVENT_OCCUR_LOG_ID`  
**Columns:** 21  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_DT_TM` | DATETIME |  |  | End date / time that the event occurred |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LOG_FILE_PRODUCED_IND` | DOUBLE |  |  | log file produced indicator |
| 9 | `OCCURANCE_SEQ` | DOUBLE |  |  | The sequence this event occurred |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field will currently hold the batch_id from the si_batch table for claim resubmission. It will potentially be used for other purposes at a later date. |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(60) |  |  | This field holds the name of the entity ID stored in the parent_entity_id field. Currently, this is SI_BATCH for claim resubmission. |
| 12 | `PFT_EVENT_ID` | DOUBLE | NOT NULL |  | pft event id |
| 13 | `PFT_EVENT_OCCUR_LOG_ID` | DOUBLE | NOT NULL | PK | Unique Id |
| 14 | `PFT_EVENT_REASON_CD` | DOUBLE | NOT NULL |  | Reason for the event |
| 15 | `PFT_EVENT_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the event |
| 16 | `START_DT_TM` | DATETIME |  |  | Start date / time of the event |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BR_GEN_EVENT_LOG](BR_GEN_EVENT_LOG.md) | `PFT_EVENT_OCCUR_LOG_ID` |
| [PFT_EVENT_OCCUR_PARAM](PFT_EVENT_OCCUR_PARAM.md) | `PFT_EVENT_OCCUR_LOG_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `PFT_EVENT_OCCUR_LOG_ID` |
| [PFT_SYSTEM_ACTIVITY_LOG](PFT_SYSTEM_ACTIVITY_LOG.md) | `PFT_EVENT_OCCUR_LOG_ID` |
| [RC_CONT_PROCESS_GROUP](RC_CONT_PROCESS_GROUP.md) | `PFT_EVENT_OCCUR_LOG_ID` |

