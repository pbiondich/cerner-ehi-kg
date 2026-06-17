# CDI_WORK_QUEUE_TIME

> The table specifies the day of the week and times when each work queue is open.

**Description:** CDI Work Queue Time  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_WORK_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Work Queue the times apply to. |
| 2 | `CDI_WORK_QUEUE_TIME_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated number. |
| 3 | `CLOSE_TIME` | DOUBLE | NOT NULL |  | Time the queue closes on the days specified. |
| 4 | `OPEN_DAYS_BITMAP` | DOUBLE | NOT NULL |  | Bitmap of days the queue is open (Sun=1, Mon=2, Tue=4, Wed=8, Thu=16, Fri=32, Sat=64). |
| 5 | `OPEN_TIME` | DOUBLE | NOT NULL |  | Time the queue opens on the days specified. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_WORK_QUEUE_ID` | [CDI_WORK_QUEUE](CDI_WORK_QUEUE.md) | `CDI_WORK_QUEUE_ID` |

