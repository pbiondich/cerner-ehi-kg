# ORDER_COMMENT

> Stores comments associated with an order

**Description:** ORDER COMMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | which action sequence the comment goes with |
| 2 | `COMMENT_DT_TM` | DATETIME |  |  | when the comment was written |
| 3 | `COMMENT_PRSNL_ID` | DOUBLE | NOT NULL |  | **Obsolete Column - Column was never used** who wrote the comment |
| 4 | `COMMENT_TYPE_CD` | DOUBLE | NOT NULL |  | type of comment |
| 5 | `DISPLAY_MASK` | DOUBLE |  |  | Display bit mask to tell who needs to show the comment |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | the long text id for the long text table |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order Id from the orders table |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

