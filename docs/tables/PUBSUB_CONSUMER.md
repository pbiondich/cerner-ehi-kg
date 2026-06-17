# PUBSUB_CONSUMER

> A list of consumers and the topic where they expect events they subscribed to go.

**Description:** PUBSUB_CONSUMER  
**Table type:** REFERENCE  
**Primary key:** `PUBSUB_CONSUMER_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONSUMER_DESC` | VARCHAR(100) |  |  | Discription of a consumer |
| 2 | `CONSUMER_NAME` | VARCHAR(255) |  |  | The unique name of the Consumer |
| 3 | `MAPPED_TEQ_QUEUE_NAME` | VARCHAR(122) |  |  | Name of the internally-assigned TEQ queue on the Millennium database where events associated to this topic are published |
| 4 | `MAPPED_TEQ_SUBSCRIBER` | VARCHAR(122) |  |  | Name of the internally-assigned TEQ Subscriber |
| 5 | `PUBSUB_CONSUMER_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PUBSUB_SUBSCRIPTION](PUBSUB_SUBSCRIPTION.md) | `PUBSUB_CONSUMER_ID` |

