# BB_EDN_DSCRPNCY_OVRD

> This table contains override information for discrepancies that occurred with an Electronic Delivery Note file import.

**Description:** Blood Bank Electronic Delivery Note Discrepancy Override  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_EDN_ADMIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies administration information from an Electronic Delivery Note message structure related to this override. |
| 2 | `BB_EDN_DSCRPNCY_OVRD_ID` | DOUBLE | NOT NULL |  | Uniquely identifies override information for discrepancies that occurred with an electronic delivery note file import. |
| 3 | `BB_EDN_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the product related to this override. |
| 4 | `EDN_PRODUCT_NBR_IDENT` | VARCHAR(20) | NOT NULL |  | Contains the product number of the discrepant product. This number comes from the Electronic Delivery Note file. |
| 5 | `EXCEPTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the exception related to this discrepancy. |
| 6 | `OVRD_REASON_CD` | DOUBLE | NOT NULL |  | Contains the reason the discrepancy was overridden. |
| 7 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The product type of the discrepant product. |
| 8 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the product related to this discrepancy. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_EDN_ADMIN_ID` | [BB_EDN_ADMIN](BB_EDN_ADMIN.md) | `BB_EDN_ADMIN_ID` |
| `BB_EDN_PRODUCT_ID` | [BB_EDN_PRODUCT](BB_EDN_PRODUCT.md) | `BB_EDN_PRODUCT_ID` |
| `EXCEPTION_ID` | [BB_EXCEPTION](BB_EXCEPTION.md) | `EXCEPTION_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

