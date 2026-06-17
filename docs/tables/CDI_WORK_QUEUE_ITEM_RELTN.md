# CDI_WORK_QUEUE_ITEM_RELTN

> This tables relates work items (CDI_WORK_ITEM table) with their assigned work queues (RX_IMAGE_QUEUE table).

**Description:** CDI Queue Work Item Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CDI_WORK_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the work item. |
| 3 | `CDI_WORK_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the work queue associated to the work item. |
| 4 | `CDI_WORK_QUEUE_ITEM_RELTN_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally assigned number. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_WORK_ITEM_ID` | [CDI_WORK_ITEM](CDI_WORK_ITEM.md) | `CDI_WORK_ITEM_ID` |
| `CDI_WORK_QUEUE_ID` | [CDI_WORK_QUEUE](CDI_WORK_QUEUE.md) | `CDI_WORK_QUEUE_ID` |

