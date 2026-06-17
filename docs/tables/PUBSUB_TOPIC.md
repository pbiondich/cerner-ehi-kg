# PUBSUB_TOPIC

> Stores list of Millennium pub/sub topics and corresponding configuration - e.g. mapped TEQ queue name etc.

**Description:** PUBSUB_TOPIC  
**Table type:** REFERENCE  
**Primary key:** `PUBSUB_TOPIC_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERNAL_QNAME` | VARCHAR(24) |  |  | INTERAL QUEUE NAME |
| 2 | `NUM_PARTITIONS` | DOUBLE |  |  | When creating a TEQ associated to this topic, indicates the number of shards to configure on the TEQ queue |
| 3 | `PUBSUB_TOPIC_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `STICKY_IND` | DOUBLE |  |  | When creating a TEQ associated to this topic, indicates whether the TEQ queue should be configured as sticky (i.e. events enqueued in the same shard are dequeued in-order) |
| 5 | `TOPIC_DESC` | VARCHAR(100) |  |  | The description for the pub/sub topic |
| 6 | `TOPIC_NAME` | VARCHAR(255) |  |  | This is the unique name identifying the pub/sub topic |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PUBSUB_EVENT](PUBSUB_EVENT.md) | `PUBSUB_TOPIC_ID` |

