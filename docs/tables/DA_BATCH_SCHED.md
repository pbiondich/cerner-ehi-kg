# DA_BATCH_SCHED

> Contains schedule details of schedules created in Discern Analytics 2.0.

**Description:** Discern Analytcs Batch Schedule  
**Table type:** REFERENCE  
**Primary key:** `DA_BATCH_SCHED_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | Date and time the batch schedule became effective. |
| 3 | `CREATED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that created the batch schedule. |
| 4 | `CREATED_DT_TM` | DATETIME |  |  | The date and time this batch schedule was created. |
| 5 | `DAYS_OF_WEEK` | VARCHAR(8) |  |  | Days of the week that the schedule is to be run (for example 134=Sun, Tues, Thur) |
| 6 | `DAY_OF_MONTH` | DOUBLE |  |  | Day of the month that the batch is to be run (1-31, 99=always use the last day of the month) |
| 7 | `DA_BATCH_COLLECTION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the collection this batch schedule belongs to. |
| 8 | `DA_BATCH_SCHED_DESC` | VARCHAR(100) |  |  | Description of the batch schedule. |
| 9 | `DA_BATCH_SCHED_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DA_BATCH_SCHED table. |
| 10 | `DA_SCHED_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the schedule is for reports or queries. 0=report, 1=query |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `FREQ_NBR` | DOUBLE | NOT NULL |  | How often the batch schedule occurs (every 1 day, 2 weeks, 3 months) |
| 13 | `RECURRENCE_FLAG` | DOUBLE | NOT NULL |  | How often the batch schedule occurs (every 1 day, 2 weeks, 3 months) |
| 14 | `TIME_OF_DAY_TXT` | VARCHAR(10) | NOT NULL |  | Time of day the batch schedule is to be run (24-hour format) |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DA_BATCH_COLLECTION_ID` | [DA_BATCH_COLLECTION](DA_BATCH_COLLECTION.md) | `DA_BATCH_COLLECTION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DA_BATCH_QUERY](DA_BATCH_QUERY.md) | `DA_BATCH_SCHED_ID` |
| [DA_BATCH_REPORT](DA_BATCH_REPORT.md) | `DA_BATCH_SCHED_ID` |
| [DA_BATCH_SCHED_LOG](DA_BATCH_SCHED_LOG.md) | `DA_BATCH_SCHED_ID` |

