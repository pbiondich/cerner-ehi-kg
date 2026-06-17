# ECO_ACTION_QUEUE

> A queue of actions that the ECO server must process for a given order.

**Description:** Explode Continuing Orders Action Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the actions that have been taken on an order. This is part of the primary key. |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of action that was taken on the order. |
| 3 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time the action takes effect. |
| 4 | `NEXT_INSTANCE_DT_TM` | DATETIME |  |  | The next instance that will be exploded by the eco server. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL |  | Points to the order that the eco needs to reference to explode the order. |
| 6 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the order after the action was taken on it. |
| 7 | `PROCESSED_DT_TM` | DATETIME |  |  | When the action was processed by the eco server. |
| 8 | `QUEUE_MODIFIER_BIT` | DOUBLE |  |  | This bitset will hold qualifiers on the actions being queued up for ECO processing. Intended use is only to manage the queue itself, rather than what will be done to the order via the order action. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

