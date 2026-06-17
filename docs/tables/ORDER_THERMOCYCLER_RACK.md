# ORDER_THERMOCYCLER_RACK

> Associates a specific thermocycler rack to an order.

**Description:** Order Thermocycler Rack  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies the gel batch that this order is located on |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates a thermocycler rack to a specific order for which is being used. It is a foreign key reference to the primary key of the orders table. |
| 3 | `RACK_ID` | DOUBLE | NOT NULL |  | Identifies the thermocycler rack being used for HLA molecular typing. It is a foreign key reference to the primary key of the thermocycler_rack table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GEL_BATCH_ID` | [GEL_BATCH](GEL_BATCH.md) | `GEL_BATCH_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

