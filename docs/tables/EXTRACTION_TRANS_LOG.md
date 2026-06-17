# EXTRACTION_TRANS_LOG

> This table is used to track processing status for each extraction request.

**Description:** Extraction Transaction Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASYNC_PUSH_STATUS` | DOUBLE |  |  | This flag indicates if the Async response is submitted to the client successfully or not. |
| 2 | `DEFAULT_CONSUMER_ROUTE` | VARCHAR(10) |  |  | Dex Async request requires consumer routing information to be passed by the client. The first route id is considered as a default consumer route. In case of Async server crash, This route information will be used to post the failure response to the client. |
| 3 | `DEX_EXTERNAL_REF` | VARCHAR(128) |  |  | DEX can not return any ID when the request is submitted to Async API, so it expects the client to provide a unique ID for every request. The ID will be used by the client to Map the response with the request. |
| 4 | `END_DT_TM` | DATETIME |  |  | The date/time of when the extraction process was completed. |
| 5 | `ERROR_MESSAGE` | LONGTEXT |  |  | The detailed stack trace if there is an error during the extraction. |
| 6 | `EXTRACTION_TRANS_LOG_ID` | DOUBLE | NOT NULL |  | The unique generated number that identifies a single row on the EXTRACTION_TRANS_LOG table. |
| 7 | `RUNNING_OPS` | DOUBLE |  |  | RUNNING_OPS is a virtual column and will be used only to assist with a query performance issue. The following CASE determines its value: ; (CASE when nvl(status_flag,0) = 0 then 1 end); (if status_flag is null or 0 then RUNNING_OPS will be 1, otherwise it is null) |
| 8 | `START_DT_TM` | DATETIME | NOT NULL |  | The date/time of when the extraction process was initiated. |
| 9 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of this extraction. 0 = In Progress; 1 = Complete; 2 = Failed |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

