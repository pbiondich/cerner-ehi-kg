# PFT_WF_ISSUE_EVENT

> Stores all the events information related to issues/work items.

**Description:** ProFit Work Flow Issue Event  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DAY_OF_MONTH` | DOUBLE | NOT NULL |  | The column has the day of the month on which the event will be processed. |
| 3 | `DELAYED_PROCESS_DT_TM` | DATETIME |  |  | The delayed date and time for a work item. |
| 4 | `DELAY_OFFSET_HRS` | DOUBLE |  |  | Stores the number of hours to delay processing the workflow issue |
| 5 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code of the event identifying the work item. |
| 6 | `EVENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of event: 0 - Undefined; 1 - Cancel Event; 2 - Complete Event |
| 7 | `PFT_WF_ISSUE_EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an event related to issues/work items. |
| 8 | `PFT_WF_ISSUE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related work flow issue. |
| 9 | `PROCESSING_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the processing key (asynchonous or synchronous_in_process) |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_WF_ISSUE_ID` | [PFT_WF_ISSUE](PFT_WF_ISSUE.md) | `PFT_WF_ISSUE_ID` |

