# ORDER_CONTAINER_R

> The resolution table between orders and containers. For a given order, this table will tell what container(s) it should be performed on. For a given container, this table will tell you what order(s) should be performed on it.

**Description:** Order Container Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | A system generated number uniquely identifying a specific catalog code item. |
| 2 | `COLLECTION_STATUS_FLAG` | DOUBLE |  |  | Field indicating the status of this order and container combination,.0 - Order Pending; 1 - Order Collected; 2 - Order Missed and On Hold; 3 - Order Missed and to be Recollected; 4 - Order Missed and Rescheduled; 5 - Order Cancelled; 6 - Order Missed and Omitted; 7 - Order Inactive |
| 3 | `COLL_INFO_SEQ` | DOUBLE | NOT NULL |  | The sequence value from the collection requirements which was responsible for the container to be associated to the order. |
| 4 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely identifies a container. |
| 5 | `DEST_CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the container to which the order was moved. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely identifies an order. |
| 7 | `REASON_MISSED_CD` | DOUBLE | NOT NULL |  | Code value that identifies the reason why a particular order is being missed. |
| 8 | `REASON_MISSED_DT_TM` | DATETIME |  |  | The date and time at which an order is missed. |
| 9 | `REASON_MISSED_ID` | DOUBLE | NOT NULL | FK→ | The person id of the individual who missed this order. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEST_CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `REASON_MISSED_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

