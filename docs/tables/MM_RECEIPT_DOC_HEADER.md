# MM_RECEIPT_DOC_HEADER

> Used to store the header information of the T3 data that was passed from EDI 856 workflow. ;

**Description:** Receipt Document Header  
**Table type:** ACTIVITY  
**Primary key:** `MM_RECEIPT_DOC_HEADER_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INVOICE_NBR_TXT` | VARCHAR(40) |  |  | stores the invoice number passed by the vendor for historical reference. |
| 2 | `MM_RECEIPT_DOC_HEADER_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_RECEIPT_DOC_HEADER table. |
| 3 | `PO_NBR_TXT` | VARCHAR(40) |  |  | Stores the purchsae order number that the vendor passes for the historical reference. |
| 4 | `PURCHASE_ORDER_ID` | DOUBLE |  | FK→ | The identifier of the purchase order associated to the po_nbr on this row. |
| 5 | `SHIPMENT_DT_TM` | DATETIME |  |  | The date and time the shipment was sent. |
| 6 | `SHIP_FROM_ADDR` | VARCHAR(300) |  |  | Vendor address where the item was shipped from. |
| 7 | `SHIP_FROM_NAME` | VARCHAR(60) |  |  | Vendor name, where the item was shipped from. |
| 8 | `SHIP_TO_ADDR` | VARCHAR(300) |  |  | Address of the facility to which the item was shipped |
| 9 | `SHIP_TO_NAME` | VARCHAR(60) |  |  | Facility to which the item was shipped; |
| 10 | `TRANSACTION_STATEMENT_IND` | DOUBLE |  |  | Indicates if the vendor accepted the transaction. |
| 11 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VENDOR_COMMENT_TXT` | VARCHAR(300) |  |  | The vendor comments that were made for the purchase order. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PURCHASE_ORDER_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_RECEIPT_DOC_LINE](MM_RECEIPT_DOC_LINE.md) | `MM_RECEIPT_DOC_HEADER_ID` |

