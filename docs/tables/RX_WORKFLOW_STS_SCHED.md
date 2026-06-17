# RX_WORKFLOW_STS_SCHED

> Stores the schedule of a dispense event's workflow.

**Description:** Pharmacy Workflow Status Schedule  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_DT_TM` | DATETIME |  |  | The date and time a recurring event should begin. |
| 3 | `DAYS_OF_WEEK_BIT` | DOUBLE | NOT NULL |  | Day of week bitmap value for a dispense sequence's schedule. 0 - non scheduled, 1 - Monday, 2 - Tuesday, 4 - Wednesday, 8 - Thursday, 16 - Friday, 32 - Saturday, 64 - Sunday. |
| 4 | `DAY_NTRVL_NBR` | DOUBLE | NOT NULL |  | The number of days an event should reoccur. |
| 5 | `END_DT_TM` | DATETIME |  |  | The date and time a reocccurring event should end. |
| 6 | `MONTH_NTRVL_NBR` | DOUBLE | NOT NULL |  | The number of months an event should reoccur. For example, if an event were to occur every month, value should be 1. |
| 7 | `RX_WORKFLOW_STS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the rx_workflow_sts table. |
| 8 | `RX_WORKFLOW_STS_SCHED_ID` | DOUBLE | NOT NULL |  | Unique, generated identifier for the table. |
| 9 | `TIME_OF_DAY` | DOUBLE | NOT NULL |  | Time of day value in minutes of when a dispense sequence is scheduled to occur. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `UPDT_TZ` | DOUBLE | NOT NULL |  | Time zone for the updt_dt_tm field. |
| 16 | `WEEK_NTRVL_NBR` | DOUBLE | NOT NULL |  | The number of weeks between reoccurrences of an event.. For example, if an event were to occur every other week, value should be 2. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RX_WORKFLOW_STS_ID` | [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `RX_WORKFLOW_STS_ID` |

