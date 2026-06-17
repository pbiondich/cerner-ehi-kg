# MM_OMF_INVOICE_LINE

> Invoice Line : (Summary Table)

**Description:** MM OMF INVOICE LINE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 77

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_ACCEPTED_QTY` | DOUBLE |  |  | Base Accepted Quantity |
| 2 | `BASE_BACK_ORDER_QTY` | DOUBLE |  |  | Base Back Order Quantity |
| 3 | `BASE_CANCEL_QTY` | DOUBLE |  |  | Base Cancel Quantity |
| 4 | `BASE_INVOICE_QTY` | DOUBLE |  |  | Base Invoice Quantity |
| 5 | `BASE_ORDER_QTY` | DOUBLE |  |  | Base Order Quantity |
| 6 | `BASE_PRICE` | DOUBLE |  |  | Base Price |
| 7 | `BASE_RECEIPT_QTY` | DOUBLE |  |  | Base Receipt Quantity |
| 8 | `BUYER_ID` | DOUBLE | NOT NULL |  | Buyer ID of the Buyer |
| 9 | `CHECKED_IND` | DOUBLE |  |  | Checked Indicator |
| 10 | `COMPANY_NBR` | VARCHAR(20) |  |  | Company Number |
| 11 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 12 | `DELIVER_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | Deliver to Location |
| 13 | `EXTENDED_PRICE` | DOUBLE |  |  | Extended Price |
| 14 | `INVOICE_AMOUNT` | DOUBLE |  |  | Invoice Amount |
| 15 | `INVOICE_ID` | DOUBLE | NOT NULL |  | Invoice ID |
| 16 | `INVOICE_LINE_ITEM_ID` | DOUBLE | NOT NULL |  | Invoice Line Item ID : (Primary Key) |
| 17 | `INVOICE_NBR` | VARCHAR(20) |  |  | Invoice Number |
| 18 | `INV_MATCHED_IND` | DOUBLE |  |  | Invoice Matched Indicator |
| 19 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL |  | Item Master ID |
| 20 | `LINE_COUNT` | DOUBLE |  |  | Line Count |
| 21 | `LINE_CREATE_DT_NBR` | DOUBLE |  |  | Line Create Date |
| 22 | `LINE_CREATE_DT_TM` | DATETIME |  |  | Line Create Date and Time |
| 23 | `LINE_CREATE_ID` | DOUBLE | NOT NULL |  | Line Create Date ID |
| 24 | `LINE_CREATE_MIN_NBR` | DOUBLE |  |  | Line Create Minute |
| 25 | `LINE_UPDT_DT_NBR` | DOUBLE |  |  | Line Update Date |
| 26 | `LINE_UPDT_DT_TM` | DATETIME |  |  | Line Update Date and Time |
| 27 | `LINE_UPDT_ID` | DOUBLE | NOT NULL |  | Line Update ID |
| 28 | `LINE_UPDT_MIN_NBR` | DOUBLE |  |  | Line Update Minute |
| 29 | `MFG_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign Key to Manufacturer Item |
| 30 | `NC_DESCRIPTION` | VARCHAR(255) |  |  | Non-catalog description |
| 31 | `NC_MFR` | VARCHAR(60) |  |  | Non-catalog manufacturer |
| 32 | `NC_MFR_CD` | DOUBLE | NOT NULL |  | If the non-catalog manufacturer exists in our current system. This is the code value for the corresponding manufacturer |
| 33 | `NC_MFR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog manufacturer item number |
| 34 | `NC_VENDOR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog vendor item number |
| 35 | `NON_CATALOG_IND` | DOUBLE |  |  | Indicator used to determine if the line is a non-catalog item |
| 36 | `ORDER_DT_NBR` | DOUBLE |  |  | Order Date Number value |
| 37 | `ORDER_DT_TM` | DATETIME |  |  | Order Date and Time value |
| 38 | `ORDER_EXTENDED_PRICE` | DOUBLE |  |  | Order Extended Price |
| 39 | `ORDER_MIN_NBR` | DOUBLE |  |  | Order Minimum Number |
| 40 | `ORDER_PKG_DESC` | VARCHAR(40) |  |  | Order Package Description |
| 41 | `ORDER_PKG_ID` | DOUBLE | NOT NULL |  | Order Package ID |
| 42 | `ORDER_PKG_QTY` | DOUBLE |  |  | Order Package Quantity |
| 43 | `ORDER_PKG_UOM_CD` | DOUBLE | NOT NULL |  | Order Package unit of Measure Code |
| 44 | `ORDER_PRICE` | DOUBLE |  |  | Order Price |
| 45 | `ORDER_PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | Order Price Type Code |
| 46 | `ORDER_QTY` | DOUBLE |  |  | Order Quantity |
| 47 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID |
| 48 | `PKG_DESC` | VARCHAR(40) |  |  | Package Description |
| 49 | `PKG_ID` | DOUBLE | NOT NULL |  | Package ID |
| 50 | `PKG_QTY` | DOUBLE |  |  | Package Quantity |
| 51 | `PKG_UOM_CD` | DOUBLE | NOT NULL |  | Package Unit of Measure |
| 52 | `PO_COST_CENTER_CD` | DOUBLE | NOT NULL |  | Purchase Order Cost Center Code |
| 53 | `PO_LINE_NBR` | DOUBLE |  |  | Purchase Order Line Number |
| 54 | `PO_NBR` | VARCHAR(20) |  |  | Purchase Order Number |
| 55 | `PO_RCV_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Receive Status Code |
| 56 | `PO_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Status Code |
| 57 | `PO_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Purchase Order Sub Account Code |
| 58 | `PO_VENDOR_CD` | DOUBLE | NOT NULL |  | Purchase Order Vendor Code |
| 59 | `PRICE` | DOUBLE |  |  | Price |
| 60 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Purchase Order ID |
| 61 | `QTY` | DOUBLE |  |  | Quantity |
| 62 | `REMIT_ADDRESS_ID` | DOUBLE | NOT NULL |  | Remit Address ID |
| 63 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status code value |
| 64 | `SUBSTITUTION_IND` | DOUBLE |  |  | Indicator used to see if the item is being substituted. |
| 65 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Sub Account Code |
| 66 | `TOTAL_ORDER_PRICE` | DOUBLE |  |  | Total Order Price |
| 67 | `TOTAL_RECEIPT_PRICE` | DOUBLE |  |  | Total Receipt Price |
| 68 | `TOTAL_VOUCHER_AMOUNT` | DOUBLE |  |  | Total Voucher Amount |
| 69 | `TRANSMIT_CD` | DOUBLE | NOT NULL |  | Transmit Code |
| 70 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 71 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 72 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 73 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 74 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 75 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 76 | `VENDOR_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign Key for the Vendor Item |
| 77 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL |  | Vendor Site ID |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

