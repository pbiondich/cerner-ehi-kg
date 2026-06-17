# TASK_PUBLISH_QUEUE

> Stores information about failed attempts for publishing message notifications to IQHealth.

**Description:** Task Publish Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The time at which the message was created. |
| 2 | `REMIND_DT_TM` | DATETIME |  |  | The time at which a reminder becomes available. |
| 3 | `TASK_ACTIVITY_ASSIGN_ID` | DOUBLE | NOT NULL | FK→ | The task_activity_assignment row that this queue item pertains to. |
| 4 | `TASK_PUBLISH_QUEUE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the TASK_PUBLISH_QUEUE table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ACTIVITY_ASSIGN_ID` | [TASK_ACTIVITY_ASSIGNMENT](TASK_ACTIVITY_ASSIGNMENT.md) | `TASK_ACTIVITY_ASSIGN_ID` |

