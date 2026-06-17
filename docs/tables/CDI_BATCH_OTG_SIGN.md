# CDI_BATCH_OTG_SIGN

> The CDI_BATCH_OTG_SIGN table contains rows representing "Completed Sign" clinical events stored as OTG documents. The status_cd for a row in the table changes as the document represented by the row is processed.

**Description:** CDI_BATCH_OTG_SIGN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Date & Time action was achieved. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel ID of person who carried out the action. |
| 3 | `ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | Resultant status of the action. Valid status are: cancelled; completed; requested; deleted; refused. |
| 4 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Type of action. Valid types are: author/creator; transcribe; cancel; verify; correct; review; sign; cosign; modify. |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 8 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `BLOB_EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the event table. |
| 11 | `BLOB_HANDLE` | VARCHAR(255) |  |  | Handle to remote blob |
| 12 | `CDI_BATCH_OTG_SIGN_ID` | DOUBLE | NOT NULL |  | Unique identifier generated for each row of data. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_CD` | DOUBLE | NOT NULL |  | It is the code that identifies the most basic unit of the storage, i.e. RBC, discharge summary, image. |
| 15 | `EVENT_ID` | DOUBLE | NOT NULL |  | Provides a mechanism for logical grouping of events. i.e. supergroup and group tests. Same as event_id if current row is the highest level parent. |
| 16 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical event prsnl row. There may be more than one row with the same event_prsnl_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 17 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Result status code. Valid values: authenticated, unauthenticated, unknown, cancelled, pending, in lab, active, modified, superseded, transcribed, not done. |
| 18 | `STATUS_CD` | DOUBLE | NOT NULL |  | Tracks the status of the process of signifying that the document tied to an event has been signed (i.e., a signature annotation has been affixed to the document). The status will reflect the most recent status of the document when processing was attempted. (PENDING, INPROCESS, OPENED, COMPLETE, INERROR) |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

