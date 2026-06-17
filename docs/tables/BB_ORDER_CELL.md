# BB_ORDER_CELL

> Control cells that have been associated with a certain order on a patient in result entry.

**Description:** Blood Bank Order Cell  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_RESULT_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number. This ID is assigned for every row in the spreadsheet of the Result Entry application that involves entering cells under the accession. |
| 2 | `CELL_CD` | DOUBLE | NOT NULL |  | The cell entered in the Result Entry application for this order, ex. "Cell I", "Cell II", etc. |
| 3 | `ORDER_CELL_ID` | DOUBLE | NOT NULL |  | The primary key for this table. An internal system-assigned number that makes each row unique. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the ORDERS table. An internal system-assigned number. On this table, it corresponds to the order for which the cell was entered in the Result Entry application. |
| 5 | `PHASE_GROUP_CD` | DOUBLE | NOT NULL |  | The phase group entered in the Result Entry application for this order, ex. "Warm PhasesI", etc. |
| 6 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it corresponds to the product entered in the Result Entry application for this order. This column is optional. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

