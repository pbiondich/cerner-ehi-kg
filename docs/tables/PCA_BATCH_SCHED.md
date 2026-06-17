# PCA_BATCH_SCHED

> Contains scheduling information for populating Quality Topics.

**Description:** PowerChrt Analytics Batch Schedule  
**Table type:** REFERENCE  
**Primary key:** `PCA_BATCH_SCHED_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DAYS_OF_WEEK` | VARCHAR(8) | NOT NULL |  | Indicates the days of the week this item should execute. E.g. 1=Sunday, 7 = Saturday so '145' indicates that the item should run on Sunday, Wednesday, and Thursday. |
| 3 | `DAY_OF_MONTH_NBR` | DOUBLE | NOT NULL |  | Indicates the day of month that this item is intended to execute. |
| 4 | `EXPECTED_END_RUN_DT_TM` | DATETIME |  |  | The last date/time that this item will execute. |
| 5 | `FREQ_NBR` | DOUBLE | NOT NULL |  | Together with RECURRENCE_FLAG, indicates how often this scheduled item will be executed. Indicates the frequency, e.g. "Every 2". |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | A foreign key from the table whose record is being associated with a schedule. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table whose record is being associated with a schedule. |
| 8 | `PCA_BATCH_SCHED_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCA_BATCH_SCHED table. |
| 9 | `PROCESS_SEQ` | DOUBLE | NOT NULL |  | Used to determine order for processing scheduled topics. |
| 10 | `RECURRENCE_FLAG` | DOUBLE | NOT NULL |  | Together with FREQ_NBR, indicates how frequently this scheduled item will be executed. Indicates the granularity, e.g. Daily, Weekly, Monthly, etc. |
| 11 | `TIME_OF_DAY_TXT` | VARCHAR(10) |  |  | Indicates the time of day this item is scheduled to execute. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCA_BATCH_SCHED_CONTROL](PCA_BATCH_SCHED_CONTROL.md) | `PCA_BATCH_SCHED_ID` |

