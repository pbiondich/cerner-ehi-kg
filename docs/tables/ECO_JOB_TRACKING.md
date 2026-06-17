# ECO_JOB_TRACKING

> Tracks the progress of child order management on a job by job basis.

**Description:** Explode Child Order Job Progress Tracking  
**Table type:** ACTIVITY  
**Primary key:** `ECO_JOB_TRACKING_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_PROCESS_DT_TM` | DATETIME |  |  | The date/time (UTC) when the job began processing. |
| 2 | `CHILD_ORDER_CANCELED_CNT` | DOUBLE |  |  | The number of child orders cancelled while processing this template order. |
| 3 | `CHILD_ORDER_CREATED_CNT` | DOUBLE |  |  | The number of child orders created while processing this template order. |
| 4 | `CREATED_DT_TM` | DATETIME |  |  | The time at which the tracking row was created. |
| 5 | `ECO_JOB_TRACKING_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the ECO_JOB_TRACKING table. |
| 6 | `JOB_TYPE_FLAG` | DOUBLE | NOT NULL |  | Job type of this job. See flag definitions for individual values. |
| 7 | `PROCESSING_SECS` | DOUBLE |  |  | The number of seconds the job took to process. If process failed or was interrupted, will represent number of seconds until failure. |
| 8 | `SUCCESS_PROCESSING_CNT` | DOUBLE |  |  | Number of template orders successfully processed. |
| 9 | `TEMPLATES_TO_PROCESS_CNT` | DOUBLE |  |  | Number of template orders initially qualified to be processed in this job. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ECO_QUEUE](ECO_QUEUE.md) | `ECO_JOB_TRACKING_ID` |
| [ECO_TEMPLATE_TRACKING](ECO_TEMPLATE_TRACKING.md) | `ECO_JOB_TRACKING_ID` |

