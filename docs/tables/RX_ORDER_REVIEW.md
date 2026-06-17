# RX_ORDER_REVIEW

> Stores the review information for outpatient orders, performed by Retail pharmacist.

**Description:** Order Review  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order_id from ORDERS table. |
| 3 | `ORDER_REVIEW_ID` | DOUBLE | NOT NULL |  | Unique id for the row |
| 4 | `REVIEWED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | person_id from PRSNL table. Indicates the personnel performing the review. |
| 5 | `REVIEW_ACTION_SEQ_NBR` | DOUBLE | NOT NULL |  | Last action sequence of the order, from Orders table, at the time order was rejected. |
| 6 | `REVIEW_DT_TM` | DATETIME |  |  | The date/time the review was performed. |
| 7 | `REVIEW_REASON_CD` | DOUBLE | NOT NULL |  | Reason for rejecting the order. |
| 8 | `REVIEW_SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence in which reviews have been performed. |
| 9 | `REVIEW_SR_CD` | DOUBLE | NOT NULL |  | Pharmacy Service Resource from which review has been performed. |
| 10 | `REVIEW_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of review performed. |
| 11 | `REVIEW_TZ` | DOUBLE | NOT NULL |  | Time zone of the pharmacy reviewing the order. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REVIEWED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

