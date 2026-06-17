# ORDER_ORDER_RELTN

> This table stores the different types of relationships between two orders. For example, a relationship between an existing order and a new order that is created by a reconciliation action on a new order.

**Description:** Order Order Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTERED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who created the order to order relation. (a row in this table) |
| 2 | `ORDER_ORDER_RELTN_ID` | DOUBLE | NOT NULL |  | The primary key of this table. |
| 3 | `RELATED_FROM_ACTION_SEQ` | DOUBLE | NOT NULL |  | The action sequence on the existing order from which the relationship to another order has been created. Along with order_ id, this field is a foreign key back to the order_action table. |
| 4 | `RELATED_FROM_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The existing order _id from which the relationship to another order has been created. This field is a foreign key back to the orders table. |
| 5 | `RELATED_TO_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order to which the other existing order (related_from_order_id) is related to. This too is a foreign key back to the orders table. |
| 6 | `RELATION_CREATED_DT_TM` | DATETIME | NOT NULL |  | The date and time when the relationship between the two orders was created. |
| 7 | `RELATION_CREATED_TZ` | DOUBLE | NOT NULL |  | The time zone associated with the relation_created_dt_tm column. This is a user centric time zone. |
| 8 | `RELATION_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value that indicates the type of relationship that exists between the two orders. For example, Covert, etc. |
| 9 | `RELTN_GROUP_ID` | DOUBLE |  | FK→ | The relation group id for the order to order relationship grouping. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENTERED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RELATED_FROM_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RELATED_TO_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RELTN_GROUP_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

