# SI_BATCH

> Each row corresponds to a single outbound batch.

**Description:** This table holds descriptive information on an outbound batch.  
**Table type:** ACTIVITY  
**Primary key:** `BATCH_ID`  
**Columns:** 14  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | A non-unique descriptive string to identify the batch.Column |
| 2 | `BATCH_ID` | DOUBLE | NOT NULL | PK | Unique batch identifier. |
| 3 | `BATCH_NUMBER` | VARCHAR(25) | NOT NULL |  | Unique domain string to identify the outbound batch. |
| 4 | `BATCH_ORIGIN_CD` | DOUBLE | NOT NULL |  | Code Set (25452) that identifies the sending domain. |
| 5 | `BATCH_STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the current processing status of the outbound batch.Column |
| 6 | `INTERFACE_TYPE_CD` | DOUBLE | NOT NULL |  | Code Set (19169) that identifies the interface type. |
| 7 | `MESSAGE_FORMAT_CD` | DOUBLE | NOT NULL |  | Code Set (25453) that identifies the UI Message type. |
| 8 | `MESSAGE_LOCATION` | VARCHAR(255) | NOT NULL |  | This points to the storage location for the individual batch events. |
| 9 | `SYS_DIRECTION_CD` | DOUBLE | NOT NULL |  | Indicates the direction, Inbound or Outbound, the batch events are flowing.Column |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [GL_TRANS_LOG](GL_TRANS_LOG.md) | `SI_BATCH_ID` |
| [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `BATCH_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `BATCH_ID` |
| [SI_BATCH_EVENT](SI_BATCH_EVENT.md) | `BATCH_ID` |
| [SI_BATCH_STATS](SI_BATCH_STATS.md) | `BATCH_ID` |

