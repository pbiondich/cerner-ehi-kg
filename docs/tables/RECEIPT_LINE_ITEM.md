# RECEIPT_LINE_ITEM

> Stores inventory purchase order receipt information about the items on a purchase order.

**Description:** Receipt Line Item  
**Table type:** ACTIVITY  
**Primary key:** `RECEIPT_LINE_ITEM_ID`  
**Columns:** 28  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item actually received for a purchase order. In the case of automatic substitution, the item may differ from the original item ordered. |
| 2 | `ACTUAL_MANF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The manufacturer's item number for the item received. This is used to track compliance issues. |
| 3 | `ACTUAL_VENDOR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The vendor's item identifier for the item received. |
| 4 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 7 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 8 | `DELIVERY_STATUS_CD` | DOUBLE | NOT NULL |  | The delivery status for the line item. The delivery status is open or closed. |
| 9 | `DELIVERY_TICKET_ID` | DOUBLE | NOT NULL |  | OBSOLETE |
| 10 | `DELIVER_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | The location which this line item will be delivered to. |
| 11 | `FROM_COST_CENTER_CD` | DOUBLE | NOT NULL |  | From Cost Center |
| 12 | `FROM_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | From Sub Account |
| 13 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The identifier assigned to lines of a requisition and/or purchase order. |
| 14 | `MATCHED_STATUS_IND` | DOUBLE |  |  | This field determines if the line has been matched to an invoice. |
| 15 | `PO_LINE_NBR` | DOUBLE |  |  | The line number assigned to the purchase order line. |
| 16 | `PO_RECEIPT_ID` | DOUBLE | NOT NULL | FK→ | The identifier assigned to the purchase order receipt. |
| 17 | `RECEIPT_LINE_ITEM_ID` | DOUBLE | NOT NULL | PK | The identifier used to define a receipt line item. |
| 18 | `REQUISITION_ID` | DOUBLE | NOT NULL |  | The identifier of the requisition that initiated the request. |
| 19 | `T3_DOC_EXISTS_IND` | DOUBLE |  |  | This field will be set to 1 when the T3 data exists for a receipt line. |
| 20 | `TO_COST_CENTER_CD` | DOUBLE | NOT NULL |  | To Cost Center |
| 21 | `TO_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | To Sub Account |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `VALID_LINE_IND` | DOUBLE |  |  | Indicates a valid line item |
| 28 | `WEIGHT` | DOUBLE |  |  | The weight of the delivered line items. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTUAL_ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `ACTUAL_MANF_ITEM_ID` | [MANUFACTURER_ITEM](MANUFACTURER_ITEM.md) | `ITEM_ID` |
| `ACTUAL_VENDOR_ITEM_ID` | [VENDOR_ITEM](VENDOR_ITEM.md) | `ITEM_ID` |
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |
| `PO_RECEIPT_ID` | [PO_RECEIPT](PO_RECEIPT.md) | `PO_RECEIPT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `RECEIPT_LINE_ITEM_ID` |

