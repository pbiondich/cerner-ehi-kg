# BB_INVLD_PROD_ORD_EXCEPTN

> Contains information for blood bank exceptions which are generated for dispense/modification without a valid product order.

**Description:** Blood Bank Product Order Exception  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_INVLD_PROD_ORD_EXCEPTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information for blood bank exceptions which are generated for dispense/modification without a valid product order. |
| 2 | `EXCEPTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related blood bank exception from the BB_EXCEPTION table. |
| 3 | `PRODUCT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related product order which was used at dispense/modification. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXCEPTION_ID` | [BB_EXCEPTION](BB_EXCEPTION.md) | `EXCEPTION_ID` |
| `PRODUCT_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

