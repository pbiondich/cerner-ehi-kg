# PUBSUB_EVENT_SCHEMA

> Stores list of Millennium pub/sub versioned payload schemas associated to event types

**Description:** PUBSUB_EVENT_SCHEMA  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARTITION_KEY_FIELD_NAME` | VARCHAR(400) |  |  | A structured string identifier used to extract a field in the payload schema used for grouping/ordering related events into assigned pub/sub partitions. |
| 2 | `PAYLOAD_SCHEMA_CLOB` | LONGTEXT |  |  | String representation of structured payload schema convertible to a data format (e.g. JSON) |
| 3 | `PAYLOAD_SCHEMA_ENCODING_TFLG` | VARCHAR(100) |  |  | Identifies data format associated to payload_schema (default: JSON) |
| 4 | `PUBSUB_EVENT_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the PUBSUB_EVENT table. It is an internal system assigned number. |
| 5 | `PUBSUB_EVENT_SCHEMA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `RELATION_KEY_FIELD_NAME` | VARCHAR(400) |  |  | A structured string identifier optionally used to extract a field in the payload schema used for grouping related events for consumer-facing processing purposes. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VERSION_NBR` | DOUBLE |  |  | This is the ascending verseion of the event schema - such that the row with the highest value for a given event type represents the latest version of the payload schema. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PUBSUB_EVENT_ID` | [PUBSUB_EVENT](PUBSUB_EVENT.md) | `PUBSUB_EVENT_ID` |

