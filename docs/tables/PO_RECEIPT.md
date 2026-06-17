# PO_RECEIPT

> Stores inventory purchase order receipt header information.

**Description:** PO RECEIPT  
**Table type:** ACTIVITY  
**Primary key:** `PO_RECEIPT_ID`  
**Columns:** 23  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMIT_DT_TM` | DATETIME |  |  | The date that the receipt was committed. |
| 2 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 5 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 6 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time that the receipt becomes effective. |
| 7 | `INVOICE_NBR` | VARCHAR(40) |  |  | The reference number assigned to a purchase order by the vendor for tracking and payment. |
| 8 | `MATCHED_STATUS_CD` | DOUBLE |  |  | The voucher status for the receipt. The values are: Unmatched, In Process, and Matched. |
| 9 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 10 | `PACK_SLIP_NBR` | VARCHAR(40) |  |  | The reference number assigned by a vendor to a shipment. |
| 11 | `PERSON_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 12 | `PO_RECEIPT_ID` | DOUBLE | NOT NULL | PK | The identifier assigned to the purchase order receipt. |
| 13 | `PURCHASE_ORDER_ID` | DOUBLE |  | FK→ | The identifier of the purchase order for which the receipt is created. |
| 14 | `RECEIVE_DT_TM` | DATETIME |  |  | Actual date and time shipment was received. |
| 15 | `RECEIVE_LOCATION_CD` | DOUBLE |  |  | Location where the physical receiving of the purchase order was performed. |
| 16 | `SEQUENCE` | DOUBLE |  |  | The received shipment order for the purchase order. The first shipment received for a purchase order is assigned one (1), the second two(2), etc.,. |
| 17 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status assigned to the purchase order receipt. The valid values are Open and Closed. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VENDOR_CD` | DOUBLE |  |  | The vendor from which the purchase order receipt is received. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PURCHASE_ORDER_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [INVOICE_PO_RECEIPT_R](INVOICE_PO_RECEIPT_R.md) | `PO_RECEIPT_ID` |
| [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `PO_RECEIPT_ID` |
| [RECEIPT_LINE_ITEM](RECEIPT_LINE_ITEM.md) | `PO_RECEIPT_ID` |

