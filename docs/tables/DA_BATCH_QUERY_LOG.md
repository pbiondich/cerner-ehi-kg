# DA_BATCH_QUERY_LOG

> Log containing the execution status of scheduled Discern Analytics 2.0 queries.

**Description:** Discern Analytics Batch Query Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_QUERY_END_DT_TM` | DATETIME |  |  | Date and time that the batch query finished. |
| 2 | `BATCH_QUERY_START_DT_TM` | DATETIME | NOT NULL |  | Date and time that the batch query began execution. |
| 3 | `CREATED_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | Document identifier that was created from the executed query |
| 4 | `DA_BATCH_QUERY_ID` | DOUBLE | NOT NULL | FK→ | The query that these statistics are for. |
| 5 | `DA_BATCH_QUERY_LOG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DA_BATCH_QUERY_LOG table. |
| 6 | `DA_BATCH_SCHED_LOG_ID` | DOUBLE | NOT NULL | FK→ | The statistics for the schedule that this query was part of. |
| 7 | `ERROR_TXT_ID` | DOUBLE | NOT NULL | FK→ | Error associated with the execution of the query. |
| 8 | `SUCCESS_IND` | DOUBLE | NOT NULL |  | Indicate if the batch query was actually successful or not. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_DOCUMENT_ID` | [DA_DOCUMENT](DA_DOCUMENT.md) | `DA_DOCUMENT_ID` |
| `DA_BATCH_QUERY_ID` | [DA_BATCH_QUERY](DA_BATCH_QUERY.md) | `DA_BATCH_QUERY_ID` |
| `DA_BATCH_SCHED_LOG_ID` | [DA_BATCH_SCHED_LOG](DA_BATCH_SCHED_LOG.md) | `DA_BATCH_SCHED_LOG_ID` |
| `ERROR_TXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

