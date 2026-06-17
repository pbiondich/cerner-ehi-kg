# RX_WORK_ITEM_QUEUE_HX

> History of pharmacy work items that have been removed.

**Description:** Pharmacy Work Item Queue History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The create_dt_tm from the original row on the RX_WORK_ITEM_QUEUE table. |
| 2 | `CREATE_TZ` | DOUBLE | NOT NULL |  | The create_tz from the original row on the RX_WORK_ITEM_QUEUE table. |
| 3 | `DELETE_DT_TM` | DATETIME | NOT NULL |  | The date and time that the row was delete from RX_WORK_TIME_QUEUE |
| 4 | `DELETE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that deleted the row on the RX_WORK_ITEM_QUEUE table. |
| 5 | `DELETE_TZ` | DOUBLE | NOT NULL |  | The time zone associated to the delete_dt_tm column. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order associated to the work item. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The med request that this queue item pertains to. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table that has more details about this work item. The only value to start with will be RXS_MED_REQUEST. |
| 9 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority code value for the work item. |
| 10 | `RX_WORK_ITEM_QUEUE_HX_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_WORK_ITEM_QUEUE_HX table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `WORK_ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | The type of work item on the deleted RX_WORK_ITEM_QUEUE row. Examples: ERX, Unverified Order, Med Request. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DELETE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

