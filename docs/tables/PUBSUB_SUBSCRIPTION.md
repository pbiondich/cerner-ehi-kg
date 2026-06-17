# PUBSUB_SUBSCRIPTION

> The present of a row in this table will cause a message to be published to the consumers topic when that event occurs. Rows are added and deleted, never updated.

**Description:** PUBSUB_SUBSCRIPTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PUBSUB_CONSUMER_ID` | DOUBLE |  | FK→ | Consumer that wants the event published. |
| 2 | `PUBSUB_EVENT_ID` | DOUBLE |  | FK→ | The event that will be published |
| 3 | `PUBSUB_SUBSCRIPTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PUBSUB_CONSUMER_ID` | [PUBSUB_CONSUMER](PUBSUB_CONSUMER.md) | `PUBSUB_CONSUMER_ID` |
| `PUBSUB_EVENT_ID` | [PUBSUB_EVENT](PUBSUB_EVENT.md) | `PUBSUB_EVENT_ID` |

