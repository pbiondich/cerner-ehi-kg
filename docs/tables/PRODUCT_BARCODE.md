# PRODUCT_BARCODE

> A user-defined reference table that defines the barcode values for each type of product.

**Description:** Product Barcode  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PRODUCT_BARCODE` | CHAR(15) | NOT NULL |  | The barcode value of the product type that will be entered into the system with a barcode reader. This barcode value is on the bag of the blood product, both in barcode format and eye-readable format. |
| 6 | `PRODUCT_BARCODE_ID` | DOUBLE | NOT NULL |  | The primary key to this table. An internal system-assigned number that keeps each row unique. |
| 7 | `PRODUCT_CAT_CD` | DOUBLE | NOT NULL | FK→ | The category of the product type for which the barcode value is defined (ex. "Red Blood Cells"). |
| 8 | `PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | The product type to which this barcode value corresponds. |
| 9 | `PRODUCT_CLASS_CD` | DOUBLE | NOT NULL | FK→ | The class of products to which this product type belongs. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_CAT_CD` | [PRODUCT_CATEGORY](PRODUCT_CATEGORY.md) | `PRODUCT_CAT_CD` |
| `PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |
| `PRODUCT_CLASS_CD` | [PRODUCT_CLASS](PRODUCT_CLASS.md) | `PRODUCT_CLASS_CD` |

