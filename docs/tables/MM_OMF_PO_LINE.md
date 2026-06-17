# MM_OMF_PO_LINE

> PurchaseOrder line OMF table.

**Description:** MM OMF PO LINE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 97

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_BACKORDER_QTY` | DOUBLE |  |  | base back order quantity |
| 2 | `BASE_CANCEL_QTY` | DOUBLE |  |  | Base Cancel Quantity |
| 3 | `BASE_INVOICE_QTY` | DOUBLE |  |  | Base Invoice Quantity |
| 4 | `BASE_ORDER_QTY` | DOUBLE |  |  | Base Order Quantity |
| 5 | `BASE_PRICE` | DOUBLE |  |  | Base Package Type Price |
| 6 | `BASE_RECEIPT_QTY` | DOUBLE |  |  | Base Receipt Quantity |
| 7 | `BUYER_ID` | DOUBLE | NOT NULL |  | Buyer ID of the Buyer |
| 8 | `CNTRCT_BEG_EFF_DT_NBR` | DOUBLE |  |  | Contract Begin Effective Date Number |
| 9 | `CNTRCT_BEG_EFF_DT_TM` | DATETIME |  |  | Contract Begin Effective Date time |
| 10 | `CNTRCT_BEG_EFF_MIN_NBR` | DOUBLE |  |  | Contract Begin Effective minute number |
| 11 | `CNTRCT_END_EFF_DT_NBR` | DOUBLE |  |  | Contract end Effective date number |
| 12 | `CNTRCT_END_EFF_DT_TM` | DATETIME |  |  | Contract end Effective date time |
| 13 | `CNTRCT_END_EFF_MIN_NBR` | DOUBLE |  |  | Contract end Effective minute number |
| 14 | `CNTRCT_ID` | DOUBLE | NOT NULL |  | Contract number key |
| 15 | `CNTRCT_NBR` | VARCHAR(40) |  |  | Contract number |
| 16 | `CNTRCT_TYPE_CD` | DOUBLE | NOT NULL |  | Contract type code value |
| 17 | `COMPANY_NBR` | VARCHAR(20) |  |  | Company Number |
| 18 | `CONTRACT_DESC` | VARCHAR(100) |  |  | Contract Description |
| 19 | `CONTRACT_IND` | DOUBLE |  |  | Contract Indicator |
| 20 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 21 | `DELIVER_TO_LOC_CD` | DOUBLE | NOT NULL |  | Deliver to location |
| 22 | `DSL_IM_ORDER` | DOUBLE |  |  | Days since last item master ordered |
| 23 | `DSL_IM_RECEIPT` | DOUBLE |  |  | Days since last item master receipt |
| 24 | `DSL_VI_ORDER` | DOUBLE |  |  | Days since last vendor item order |
| 25 | `DSL_VI_RECEIPT` | DOUBLE |  |  | Days since last vendor item receipt |
| 26 | `ITEM_BASE_PKG_DESC` | VARCHAR(40) |  |  | Item Master Base Pkg type description |
| 27 | `ITEM_BASE_PKG_ID` | DOUBLE | NOT NULL |  | Foreign Key to package type table |
| 28 | `ITEM_BASE_PKG_QTY` | DOUBLE |  |  | Base Pkg Type Quantity |
| 29 | `ITEM_BASE_PKG_UOM_CD` | DOUBLE | NOT NULL |  | Base Pkg Unit Of Measure Code |
| 30 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL |  | Foreign Key to Item Master Table |
| 31 | `ITEM_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Sub Account |
| 32 | `LAST_RECEIPT_DT_NBR` | DOUBLE |  |  | Last Receipt Date Nbr |
| 33 | `LAST_RECEIPT_DT_TM` | DATETIME |  |  | Last Receipt Date Time |
| 34 | `LAST_RECEIPT_MIN_NBR` | DOUBLE |  |  | Last Receipt Min Nbr |
| 35 | `LAST_VOUCHER_DT_NBR` | DOUBLE |  |  | Last Voucher Date/Time Nbr |
| 36 | `LAST_VOUCHER_DT_TM` | DATETIME |  |  | Last Voucher Date/Time |
| 37 | `LAST_VOUCHER_MIN_NBR` | DOUBLE |  |  | Last Voucher Min Nbr |
| 38 | `LINE_COUNT` | DOUBLE |  |  | Line Count |
| 39 | `LINE_CREATE_BUYER_ID` | DOUBLE | NOT NULL |  | Line Create Buyer ID |
| 40 | `LINE_CREATE_DT_NBR` | DOUBLE |  |  | Line Create Date Nbr |
| 41 | `LINE_CREATE_DT_TM` | DATETIME |  |  | Line Create Date/Time |
| 42 | `LINE_CREATE_MIN_NBR` | DOUBLE |  |  | Line Create Min Nbr |
| 43 | `LINE_ITEM_ID` | DOUBLE | NOT NULL |  | Line Item ID : Primary Key |
| 44 | `LINE_NBR` | DOUBLE |  |  | Line Number |
| 45 | `LINE_STATUS_CD` | DOUBLE | NOT NULL |  | Line Status |
| 46 | `LINE_UPDT_BUYER_ID` | DOUBLE | NOT NULL |  | Update Buyer ID |
| 47 | `LINE_UPDT_DT_NBR` | DOUBLE |  |  | Line Update Nbr |
| 48 | `LINE_UPDT_DT_TM` | DATETIME |  |  | Line Update Date/Time |
| 49 | `LINE_UPDT_MIN_NBR` | DOUBLE |  |  | Line Update Min Nbr |
| 50 | `MFG_CD` | DOUBLE | NOT NULL |  | Manufacturer |
| 51 | `MFG_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign Key to Manufacturer Item |
| 52 | `NC_DESCRIPTION` | VARCHAR(255) |  |  | Non-catalog description |
| 53 | `NC_MFR` | VARCHAR(60) |  |  | Non-catalog manufacturer |
| 54 | `NC_MFR_CD` | DOUBLE | NOT NULL |  | If the non-catalog manufacturer exists in our current system. This is the code value for the corresponding manufacturer. |
| 55 | `NC_MFR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog manufacturer item number |
| 56 | `NC_VENDOR_ITEM_NBR` | VARCHAR(20) |  |  | Non-catalog vendor item number |
| 57 | `NON_CATALOG_IND` | DOUBLE |  |  | Indicator used to determine if the line is a non-catalog item |
| 58 | `ORDER_PKG_DESC` | VARCHAR(40) |  |  | Order Pkg Description |
| 59 | `ORDER_PKG_ID` | DOUBLE | NOT NULL |  | Foreign Key to Package_Type Table |
| 60 | `ORDER_PKG_QTY` | DOUBLE |  |  | Order Pkg Quantity |
| 61 | `ORDER_PKG_UOM_CD` | DOUBLE | NOT NULL |  | Order Pkg UOM |
| 62 | `ORDER_PRICE` | DOUBLE |  |  | Order Price |
| 63 | `ORDER_PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | Order Price Type |
| 64 | `ORDER_QTY` | DOUBLE |  |  | Order Quantity |
| 65 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to Organization Table |
| 66 | `PO_CLOSED_DT_NBR` | DOUBLE |  |  | Closed date nbr |
| 67 | `PO_CLOSED_DT_TM` | DATETIME |  |  | closed date/time |
| 68 | `PO_CLOSED_MIN_NBR` | DOUBLE |  |  | closed min nbr |
| 69 | `PO_COMMIT_DT_NBR` | DOUBLE |  |  | commit date nbr |
| 70 | `PO_COMMIT_DT_TM` | DATETIME |  |  | commit date/time |
| 71 | `PO_COMMIT_MIN_NBR` | DOUBLE |  |  | commit min nbr |
| 72 | `PO_CREATE_DT_NBR` | DOUBLE |  |  | create date nbr |
| 73 | `PO_CREATE_DT_TM` | DATETIME |  |  | create date/time |
| 74 | `PO_CREATE_MIN_NBR` | DOUBLE |  |  | create min nbr |
| 75 | `PO_EFFECTIVE_DT_NBR` | DOUBLE |  |  | effective date nbr |
| 76 | `PO_EFFECTIVE_DT_TM` | DATETIME |  |  | effective date/time |
| 77 | `PO_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | effective min nbr |
| 78 | `PO_NBR` | VARCHAR(20) |  |  | PO Nbr. |
| 79 | `PO_STATUS_CD` | DOUBLE | NOT NULL |  | PO Status |
| 80 | `PO_TYPE_CD` | DOUBLE | NOT NULL |  | PO Type |
| 81 | `PO_UPDT_DT_NBR` | DOUBLE |  |  | Update Nbr |
| 82 | `PO_UPDT_DT_TM` | DATETIME |  |  | Update Date/Time |
| 83 | `PO_UPDT_MIN_NBR` | DOUBLE |  |  | Update Min Nbr |
| 84 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Foreign Key to PurchaseOrder Table |
| 85 | `RECEIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Receipt Status |
| 86 | `SHIP_TO_LOC_CD` | DOUBLE | NOT NULL |  | Ship To Location |
| 87 | `SUBSTITUTION_IND` | DOUBLE |  |  | Indicator used to see if the item is being substituted. |
| 88 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Sub Account |
| 89 | `UNIT_TAX` | DOUBLE | NOT NULL |  | Unit Tax for the purchase Order line item. |
| 90 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 91 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 92 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 93 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 94 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 95 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 96 | `VENDOR_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign Key for the Vendor Item |
| 97 | `VOUCHER_STATUS_CD` | DOUBLE | NOT NULL |  | Voucher Status |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

