# LINE_ITEM

> Table used to store requisition and purchase order line activity information, and template reference info.

**Description:** Line Item  
**Table type:** ACTIVITY  
**Primary key:** `LINE_ITEM_ID`  
**Columns:** 71  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_MANUF_ITEM_DESC` | VARCHAR(100) |  |  | Acknowledgement Manufacturer Item Description |
| 2 | `ACK_MANUF_ITEM_NBR` | VARCHAR(40) |  |  | Acknowledgement Manufacturer Item Number |
| 3 | `ACK_PKG_TYPE_QTY` | DOUBLE |  |  | Acknowledgement Package Type Quantity |
| 4 | `ACK_UOM` | VARCHAR(40) |  |  | Acknowledgement Unit of Measure |
| 5 | `ACK_VENDOR_ITEM_DESC` | VARCHAR(100) |  |  | Acknowledgement Vendor Item Description |
| 6 | `ACK_VENDOR_ITEM_NBR` | VARCHAR(40) |  |  | Acknowledgement Vendor Item Number |
| 7 | `APPROVAL_STATUS_DT_TM` | DATETIME |  |  | Date of an approved or rejected action.. |
| 8 | `ATTENTION` | VARCHAR(100) |  |  | Attention |
| 9 | `AUTO_DISTRIBUTE_IND` | DOUBLE |  |  | Indicator used to determine if requisition line has been distributed. |
| 10 | `AUTO_RECEIVE_IND` | DOUBLE |  |  | Automatically receive |
| 11 | `BILL_ONLY_IND` | DOUBLE |  |  | Bill only indicator |
| 12 | `BUYER_ID` | DOUBLE | NOT NULL |  | Buyer ID of the Buyer |
| 13 | `CHARGE_FLAG` | DOUBLE | NOT NULL |  | charge flag |
| 14 | `CONSIGNMENT_IND` | DOUBLE |  |  | Consignment Indicator |
| 15 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost Center |
| 16 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was was inserted. |
| 18 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 19 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 20 | `DELIVER_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | Deliver to location. |
| 21 | `DUE_DT_TM` | DATETIME |  |  | Date this item is due. |
| 22 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | encounter identifier value |
| 23 | `FILL_LOCATION_CD` | DOUBLE | NOT NULL |  | Location this item is picked from. |
| 24 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to item master |
| 25 | `LINE_ACK_STATUS_CD` | DOUBLE | NOT NULL |  | Line Acknowledgement Status |
| 26 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 27 | `LINE_ITEM_VERSION` | DOUBLE |  |  | Line Item Version |
| 28 | `LOCKED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | locked by personnel identifier |
| 29 | `LOCKED_DT_TM` | DATETIME |  |  | locked date and time |
| 30 | `MANUF_CD` | DOUBLE | NOT NULL |  | Manufacturer Code Value |
| 31 | `MANUF_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign key to manufacturer_item table. |
| 32 | `MISC_CD` | DOUBLE | NOT NULL |  | Miscellaneous codes defined by the user. |
| 33 | `MM_PROJECT_NBR_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | The project that this line item is associated to. |
| 34 | `NC_855_IND` | DOUBLE |  |  | This field is to know the source of the non-catalog item - if the non-catalog item is created from EDI855 workflow - the indicator is set to 1 else it will be 0 |
| 35 | `NC_DESCRIPTION` | VARCHAR(255) |  |  | Non-Cataloged Description |
| 36 | `NC_MFR` | VARCHAR(60) |  |  | Non-catalog manufacturer |
| 37 | `NC_MFR_CD` | DOUBLE | NOT NULL |  | If the non-catalog manufacturer exists in our current system. This is the code value for the corresponding manufacturer (code set 221) |
| 38 | `NC_MFR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog manufacturer item number |
| 39 | `NC_NDC_VALUE` | VARCHAR(50) |  |  | This filed is to store the NDC values for the medication non catalog item |
| 40 | `NC_VENDOR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog vendor item number |
| 41 | `NEXT_VERSION_NBR` | DOUBLE |  |  | The next version number (used for versioning). |
| 42 | `NON_CATALOG_IND` | DOUBLE |  |  | Indicator used to determine if the line is a non-catalog item |
| 43 | `ORIGINAL_MANUF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Original Manufacturer Item |
| 44 | `ORIGINAL_VENDOR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Original Vendor Item |
| 45 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | person identifier |
| 46 | `PO_LINE_NBR` | DOUBLE |  |  | PO Number |
| 47 | `PO_LINE_STATUS_CD` | DOUBLE | NOT NULL |  | Status of line item |
| 48 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | priority code value |
| 49 | `PROJECT_CD` | DOUBLE | NOT NULL |  | Project code code value |
| 50 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Foreign key to purchase order |
| 51 | `PURCHASING_SVC_RES_CD` | DOUBLE | NOT NULL |  | Purchasing service resource |
| 52 | `REAL_TIME_OUTBOUND_IND` | DOUBLE | NOT NULL |  | Indicates if the line item is to be processed through the real-time outbound requisition interface. |
| 53 | `REFERENCE` | VARCHAR(40) |  |  | Reference |
| 54 | `REQUESTOR` | VARCHAR(100) |  |  | Requesting person |
| 55 | `REQUISITION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to requisition |
| 56 | `REQ_ALLOW_MOD_IND` | DOUBLE |  |  | Indicator used to determine if the requisition line can be modified. |
| 57 | `REQ_LINE_NBR` | DOUBLE |  |  | Requisition line number |
| 58 | `REQ_LINE_STATUS_CD` | DOUBLE | NOT NULL |  | Status |
| 59 | `REQ_TRANSMIT_DT_TM` | DATETIME |  |  | Field used to store the requisition transmit date/time for the line item. It will specify whether or not the requisition line item has been transmitted to a foreign MMIS system. |
| 60 | `SHIP_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | Ship to location |
| 61 | `SUBSTITUTION_IND` | DOUBLE |  |  | Indicator used to see if the item is being substituted. |
| 62 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Sub account |
| 63 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 67 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `VALID_PO_LINE_IND` | DOUBLE |  |  | Valid PO line indicator |
| 69 | `VALID_REQ_LINE_IND` | DOUBLE |  |  | Valid requisition line indicator |
| 70 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 71 | `VENDOR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to vendor item |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ITEM_MASTER_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `LOCKED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `MM_PROJECT_NBR_TRACKING_ID` | [MM_PROJECT_NBR_TRACKING](MM_PROJECT_NBR_TRACKING.md) | `MM_PROJECT_NBR_TRACKING_ID` |
| `ORIGINAL_MANUF_ITEM_ID` | [MANUFACTURER_ITEM](MANUFACTURER_ITEM.md) | `ITEM_ID` |
| `ORIGINAL_VENDOR_ITEM_ID` | [VENDOR_ITEM](VENDOR_ITEM.md) | `ITEM_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REQUISITION_ID` | [REQUISITION](REQUISITION.md) | `REQUISITION_ID` |
| `VENDOR_ITEM_ID` | [VENDOR_ITEM](VENDOR_ITEM.md) | `ITEM_ID` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [DIST_LINE_ITEM_R](DIST_LINE_ITEM_R.md) | `LINE_ITEM_ID` |
| [INVOICE_LINE_ITEM](INVOICE_LINE_ITEM.md) | `LINE_ITEM_ID` |
| [LINE_SCHEDULED_QTY](LINE_SCHEDULED_QTY.md) | `LINE_ITEM_ID` |
| [MM_APPROVAL_LOG](MM_APPROVAL_LOG.md) | `LINE_ITEM_ID` |
| [MM_APPROVAL_QUEUE](MM_APPROVAL_QUEUE.md) | `LINE_ITEM_ID` |
| [MM_APPROVAL_STG](MM_APPROVAL_STG.md) | `LINE_ITEM_ID` |
| [MM_ASN_LINE_DISCREPANCY](MM_ASN_LINE_DISCREPANCY.md) | `LINE_ITEM_ID` |
| [MM_EXT_SRC_Q](MM_EXT_SRC_Q.md) | `LINE_ITEM_ID` |
| [MM_RECEIPT_DOC_LINE](MM_RECEIPT_DOC_LINE.md) | `LINE_ITEM_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `LINE_ITEM_ID` |
| [RECEIPT_LINE_ITEM](RECEIPT_LINE_ITEM.md) | `LINE_ITEM_ID` |

