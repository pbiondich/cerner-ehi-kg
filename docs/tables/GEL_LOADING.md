# GEL_LOADING

> Identifies a specific molecular gel which is related to an order.

**Description:** Gel Loading  
**Table type:** ACTIVITY  
**Primary key:** `GEL_BATCH_ID`, `GEL_NUMBER`, `ORDER_ID`  
**Columns:** 8  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_BATCH_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies which gel batch this gel is associated with. It is a foreign key reference to the primary key of the gel_batch table. |
| 2 | `GEL_NUMBER` | DOUBLE | NOT NULL | PK FK→ | Identifies a gel which is related to an order. It is a foreign key reference to the primary key of the Gel table. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | Relates the gel to a specific order. It is a foreign key reference to the primary key of the orders table. |
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
| `GEL_NUMBER` | [GEL](GEL.md) | `GEL_NUMBER` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [ALLELE_PATTERN_MATCH](ALLELE_PATTERN_MATCH.md) | `GEL_BATCH_ID` |
| [ALLELE_PATTERN_MATCH](ALLELE_PATTERN_MATCH.md) | `GEL_NUMBER` |
| [ALLELE_PATTERN_MATCH](ALLELE_PATTERN_MATCH.md) | `ORDER_ID` |
| [GEL_LOADING_POSN](GEL_LOADING_POSN.md) | `GEL_BATCH_ID` |
| [GEL_LOADING_POSN](GEL_LOADING_POSN.md) | `GEL_NUMBER` |
| [GEL_LOADING_POSN](GEL_LOADING_POSN.md) | `ORDER_ID` |
| [SPEC_PTRN_MATCH](SPEC_PTRN_MATCH.md) | `GEL_BATCH_ID` |
| [SPEC_PTRN_MATCH](SPEC_PTRN_MATCH.md) | `GEL_NUMBER` |
| [SPEC_PTRN_MATCH](SPEC_PTRN_MATCH.md) | `ORDER_ID` |

