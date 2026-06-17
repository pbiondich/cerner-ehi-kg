# GEL_LOADING_POSN

> Identifies the position a tube from an HLA molecular primer kit was placed on a specific gel for an order. Also records whether a positive reaction occured in this position.

**Description:** Gel Loading Position  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies which gel batch this gel is associated with. It is a foreign key reference to the primary key of the gel_batch table. |
| 2 | `GEL_NUMBER` | DOUBLE | NOT NULL | FK→ | Identifies the gel to which the placed aliquotted primer kit tube is related. It is a foreign key reference to the primary key of the orders table. |
| 3 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the inventory lot of the aliquotted primer kit the tube which was placed came from. It is a foreign key reference to the primary key of the lot_number_info table. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the placed aliquotted primer kit tube to an order. It is a foreign key reference to the primary key of the orders table. |
| 5 | `POSITIVE_IND` | DOUBLE |  |  | Indicates whether there was a positive reaction in the gel lane. |
| 6 | `TUBE_NUMBER` | DOUBLE |  |  | Number of the aliquotted primer kit tube which was placed on the gel at this position. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `X_POS` | DOUBLE | NOT NULL |  | Horizontal coordinate where the aliquotted primer kit tube was placed. |
| 13 | `Y_POS` | DOUBLE | NOT NULL |  | Vertical coordinate where the aliquotted primer kit tube was placed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GEL_BATCH_ID` | [GEL_LOADING](GEL_LOADING.md) | `GEL_BATCH_ID` |
| `GEL_NUMBER` | [GEL_LOADING](GEL_LOADING.md) | `GEL_NUMBER` |
| `LOT_NUMBER_ID` | [ALIQUOTTED_PRIMER_KIT](ALIQUOTTED_PRIMER_KIT.md) | `LOT_NUMBER_ID` |
| `ORDER_ID` | [GEL_LOADING](GEL_LOADING.md) | `ORDER_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

