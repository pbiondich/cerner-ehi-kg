# PUBSUB_EVENT

> Stores list of producer-owned event types eligible for publishing in the Millennium pub/sub system.

**Description:** PUBSUB_EVENT  
**Table type:** REFERENCE  
**Primary key:** `PUBSUB_EVENT_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_DESC` | VARCHAR(100) |  |  | Description of the Event |
| 2 | `EVENT_NAME` | VARCHAR(64) |  |  | The unique name of the Event |
| 3 | `PUBSUB_EVENT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `PUBSUB_TOPIC_ID` | DOUBLE |  | FK→ | Events published for this consumer will be published to this topic |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PUBSUB_TOPIC_ID` | [PUBSUB_TOPIC](PUBSUB_TOPIC.md) | `PUBSUB_TOPIC_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PUBSUB_EVENT_SCHEMA](PUBSUB_EVENT_SCHEMA.md) | `PUBSUB_EVENT_ID` |
| [PUBSUB_SUBSCRIPTION](PUBSUB_SUBSCRIPTION.md) | `PUBSUB_EVENT_ID` |

