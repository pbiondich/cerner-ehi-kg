# CE_PRCS_QUEUE

> This table is used to store items that are waiting to be processed by other subsystems such as Messaging Service. When an item is processed, the status is updated to Processed and the item will be removed from the queue after an item is endorsed.

**Description:** Clinical Event Process Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_EVENT_ACTION_ID` | DOUBLE | NOT NULL | FK→ | A unique identifier use to associate the queue row to a CE_EVENT_ACTION row. |
| 2 | `CE_PRCS_QUEUE_ID` | DOUBLE | NOT NULL |  | A unique, generated number that is used to identify an individual CE_PRCS_QUEUE row. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | This field identifies when the process queue row was created. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | An identifier used to associate an action queue row to a clinical event row. |
| 5 | `PRCS_DT_TM` | DATETIME |  |  | This field identifies when the process queue row was processed by the subsystem such as Messaging Service. |
| 6 | `QUEUE_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the process queue row. |
| 7 | `QUEUE_TYPE_CD` | DOUBLE | NOT NULL |  | This field identifies the type of process queue item to be processed. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_EVENT_ACTION_ID` | [CE_EVENT_ACTION](CE_EVENT_ACTION.md) | `CE_EVENT_ACTION_ID` |

