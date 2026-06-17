# ORD_RQSTN_ORD_R

> Relates the request to a specific order.

**Description:** Order Requisition Order Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely defines the order related to this request. |
| 2 | `ORD_RQSTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the request related to this order. |
| 3 | `ORD_RQSTN_ORD_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between an order and a request. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORD_RQSTN_ID` | [ORD_RQSTN](ORD_RQSTN.md) | `ORD_RQSTN_ID` |

