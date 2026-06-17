# DA_BATCH_SCHED_LOG

> Log containing the execution status of the Discern Analytics 2.0 schedules.

**Description:** Discern Analytics Batch Schedule Log  
**Table type:** ACTIVITY  
**Primary key:** `DA_BATCH_SCHED_LOG_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_SCHED_END_DT_TM` | DATETIME |  |  | The data and time that the last report finished execution for this batch schedule. |
| 2 | `BATCH_SCHED_EXP_START_DT_TM` | DATETIME | NOT NULL |  | The date/time that this batch schedule should have been run (even if it is hours later). |
| 3 | `BATCH_SCHED_START_DT_TM` | DATETIME | NOT NULL |  | The date and time that this batch schedule began execution. |
| 4 | `DA_BATCH_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The batch schedule that this log entry pertains to. |
| 5 | `DA_BATCH_SCHED_LOG_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DA_BATCH_SCHED_LOG table. |
| 6 | `ERROR_TXT_ID` | DOUBLE | NOT NULL | FK→ | Error associated with the execution of the schedule. |
| 7 | `NODE_NAME` | VARCHAR(63) |  |  | Name of the node on which this schedule execution occurred |
| 8 | `SUCCESS_IND` | DOUBLE | NOT NULL |  | Indicate if the batch schedule was actually successful or not. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_BATCH_SCHED_ID` | [DA_BATCH_SCHED](DA_BATCH_SCHED.md) | `DA_BATCH_SCHED_ID` |
| `ERROR_TXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DA_BATCH_QUERY_LOG](DA_BATCH_QUERY_LOG.md) | `DA_BATCH_SCHED_LOG_ID` |
| [DA_BATCH_REPORT_LOG](DA_BATCH_REPORT_LOG.md) | `DA_BATCH_SCHED_LOG_ID` |

