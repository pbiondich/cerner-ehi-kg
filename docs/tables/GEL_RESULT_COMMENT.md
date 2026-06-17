# GEL_RESULT_COMMENT

> Records the comments associated with a gel.

**Description:** Gel Result Comment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies which gel batch this gel is associated with. It is a foreign key reference to the primary key of the gel_batch table. |
| 2 | `GEL_NUMBER` | DOUBLE | NOT NULL | FK→ | A number which identifies the gel to which the specificity result relates. It is a foreign key reference to the primary key of the gel table. |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates the comment to a specific long_text record. It is a foreign key reference to the primary key of the long_text table. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the comment to a specific order and gel. It is a foreign key reference to the primary key of the orders table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GEL_BATCH_ID` | [GEL_BATCH](GEL_BATCH.md) | `GEL_BATCH_ID` |
| `GEL_NUMBER` | [GEL](GEL.md) | `GEL_NUMBER` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

