# MM_OMF_RECEIPT_LINE

> Receipt Line : (Summary Table)

**Description:** MM OMF RECEIPT LINE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 77

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_ITEM_ID` | DOUBLE | NOT NULL |  | System Generated Item ID |
| 2 | `ACTUAL_MFG_ITEM_ID` | DOUBLE | NOT NULL |  | Actual Manufacturer Item ID |
| 3 | `ACTUAL_VENDOR_ITEM_ID` | DOUBLE | NOT NULL |  | Actual Vendor Item ID |
| 4 | `BASE_ACCEPTED_QTY` | DOUBLE |  |  | Based Accepted Quantity |
| 5 | `BASE_BACK_ORDER_QTY` | DOUBLE |  |  | Base Back Order Quantity |
| 6 | `BASE_CANCEL_QTY` | DOUBLE |  |  | Base Cancel Quantity |
| 7 | `BASE_INVOICE_QTY` | DOUBLE |  |  | Base Invoice Quantity |
| 8 | `BASE_ORDER_QTY` | DOUBLE |  |  | Base Order Quantity |
| 9 | `BASE_PRICE` | DOUBLE |  |  | Base Price |
| 10 | `BASE_RECEIPT_QTY` | DOUBLE |  |  | Base Receipt Quantity |
| 11 | `COMPANY_NBR` | VARCHAR(20) |  |  | Company Number |
| 12 | `DELIVER_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | Deliver to Location Code |
| 13 | `EXTENDED_PRICE` | DOUBLE |  |  | Extended Price |
| 14 | `FROM_COST_CENTER_CD` | DOUBLE | NOT NULL |  | From Cost Center Code |
| 15 | `FROM_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | From Sub Account Code |
| 16 | `INVOICE_COUNT` | DOUBLE |  |  | Invoice Count |
| 17 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL |  | Item Master ID |
| 18 | `LINE_COUNT` | DOUBLE |  |  | Line Count |
| 19 | `LINE_CREATE_DT_NBR` | DOUBLE |  |  | Line Create Date |
| 20 | `LINE_CREATE_DT_TM` | DATETIME |  |  | Line Create Date and Time |
| 21 | `LINE_CREATE_ID` | DOUBLE | NOT NULL |  | Line Create ID |
| 22 | `LINE_CREATE_MIN_NBR` | DOUBLE |  |  | Line Create Minute |
| 23 | `LINE_ITEM_ID` | DOUBLE | NOT NULL |  | Line Item ID : Primary Key |
| 24 | `LINE_UPDT_DT_NBR` | DOUBLE |  |  | Line Update Date |
| 25 | `LINE_UPDT_DT_TM` | DATETIME |  |  | Line Update Date and Time |
| 26 | `LINE_UPDT_ID` | DOUBLE | NOT NULL |  | Line Update ID |
| 27 | `LINE_UPDT_MIN_NBR` | DOUBLE |  |  | Line Update Minute |
| 28 | `MFG_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign Key to Manufacturer Item |
| 29 | `NC_855_IND` | DOUBLE |  |  | When the non catalog item is created from the EDI workflow, stores the indicator as 1 |
| 30 | `NC_DESCRIPTION` | VARCHAR(255) |  |  | Non-catalog description |
| 31 | `NC_MFR` | VARCHAR(60) |  |  | Non-catalog manufacturer |
| 32 | `NC_MFR_CD` | DOUBLE | NOT NULL |  | If the non-catalog manufacturer exists in our current system. This is the code |
| 33 | `NC_MFR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog manufacturer item number |
| 34 | `NC_NDC_VALUE` | VARCHAR(50) |  |  | Stores the NDC value for the non catalog item. This field will be set to 1 when the T3 data exists for a receipt line. |
| 35 | `NC_VENDOR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog vendor item number |
| 36 | `NON_CATALOG_IND` | DOUBLE |  |  | Indicator used to determine if the line is a non-catalog item |
| 37 | `ORDER_DT_NBR` | DOUBLE |  |  | Order Date Number value |
| 38 | `ORDER_DT_TM` | DATETIME |  |  | Order Date and Time value |
| 39 | `ORDER_MIN_NBR` | DOUBLE |  |  | Order Minute |
| 40 | `ORDER_PERSON_ID` | DOUBLE | NOT NULL |  | Order Person ID |
| 41 | `ORDER_PKG_DESC` | VARCHAR(40) |  |  | Order Package Type Description |
| 42 | `ORDER_PKG_ID` | DOUBLE | NOT NULL |  | Order Package ID |
| 43 | `ORDER_PKG_QTY` | DOUBLE |  |  | Order Package Quantity |
| 44 | `ORDER_PKG_UOM_CD` | DOUBLE | NOT NULL |  | Order Package Unit of Measure Code |
| 45 | `ORDER_PRICE` | DOUBLE |  |  | Order Price |
| 46 | `ORDER_PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | Order Price Type Code |
| 47 | `ORDER_QTY` | DOUBLE |  |  | Order Quantity |
| 48 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID |
| 49 | `PO_EFFECTIVE_DT_NBR` | DOUBLE |  |  | Purchase Order Effective Date |
| 50 | `PO_EFFECTIVE_DT_TM` | DATETIME |  |  | Purchase Order Effective Date and Time |
| 51 | `PO_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Purchase Order Effective Minute |
| 52 | `PO_LINE_NBR` | DOUBLE |  |  | Purchase Order Line Number |
| 53 | `PO_NBR` | VARCHAR(20) |  |  | Purchase Order Number |
| 54 | `PO_RCV_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Receive Status Code |
| 55 | `PO_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Status Code |
| 56 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Purchase Order ID |
| 57 | `RCV_EFFECTIVE_DT_NBR` | DOUBLE |  |  | Receive Effective Date |
| 58 | `RCV_EFFECTIVE_DT_TM` | DATETIME |  |  | Receive Effective Date and Time |
| 59 | `RCV_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Receive Effective Minute |
| 60 | `RECEIPT_ID` | DOUBLE | NOT NULL |  | Receipt ID |
| 61 | `RECEIPT_LINE_ITEM_ID` | DOUBLE | NOT NULL |  | Receipt Line Item ID : (Primary Key) |
| 62 | `RECEIPT_PKG_DESC` | VARCHAR(40) |  |  | Receipt Package Description |
| 63 | `RECEIPT_PKG_ID` | DOUBLE | NOT NULL |  | Receipt Package ID |
| 64 | `RECEIPT_PKG_QTY` | DOUBLE |  |  | Receipt Package Quantity |
| 65 | `RECEIPT_PKG_UOM_CD` | DOUBLE | NOT NULL |  | Receipt Package Unit of Measure |
| 66 | `RECEIPT_PRICE` | DOUBLE |  |  | Receipt Price |
| 67 | `RECEIPT_QTY` | DOUBLE |  |  | Receipt Quantity |
| 68 | `SUBSTITUTION_IND` | DOUBLE |  |  | Indicator used to see if the item is being substituted. |
| 69 | `TO_COST_CENTER_CD` | DOUBLE | NOT NULL |  | To Cost Center Code |
| 70 | `TO_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | To Sub Account Code |
| 71 | `UNIT_TAX` | DOUBLE | NOT NULL |  | Unit Tax for the PO Receipt line item. |
| 72 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 73 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 74 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 75 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 76 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 77 | `VENDOR_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign Key for the Vendor Item |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

