# SI_BATCH_EVENT

> Each row corresponds to a event for a given batch.

**Description:** This table holds all the batch events.  
**Table type:** ACTIVITY  
**Primary key:** `BATCH_EVENT_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_EVENT_ID` | DOUBLE | NOT NULL | PK | Unique batch event identifier. |
| 2 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | Unique batch identifier. |
| 3 | `BATCH_SORT_FLAG` | DOUBLE |  |  | Indicates the event type. |
| 4 | `SORT_STRING` | VARCHAR(255) |  |  | String in which the batch events can be sorted on. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_ID` | [SI_BATCH](SI_BATCH.md) | `BATCH_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BILL_REC](BILL_REC.md) | `BATCH_EVENT_ID` |
| [ESI_LOG](ESI_LOG.md) | `BATCH_EVENT_ID` |
| [SI_BATCH_EVENT_SYS](SI_BATCH_EVENT_SYS.md) | `BATCH_EVENT_ID` |

