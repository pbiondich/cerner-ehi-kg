# MM_OMF_INVOICE

> Invoice Header : (Summary Table)

**Description:** MM OMF INVOICE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 64

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUYER_ID` | DOUBLE | NOT NULL |  | Buyer ID of the Buyer |
| 2 | `CHECKED_RCV_CNT` | DOUBLE |  |  | Checked Received Count |
| 3 | `CITY_TAX` | DOUBLE |  |  | City Tax |
| 4 | `COMPANY_NBR` | VARCHAR(20) |  |  | Company Number |
| 5 | `FREIGHT_TAX` | DOUBLE |  |  | Freight Tax |
| 6 | `INVOICE_AMOUNT` | DOUBLE |  |  | Invoice Amount |
| 7 | `INVOICE_COUNT` | DOUBLE |  |  | Invoice Count |
| 8 | `INVOICE_DT_NBR` | DOUBLE |  |  | Invoice Date |
| 9 | `INVOICE_DT_TM` | DATETIME |  |  | Invoice Date and Time |
| 10 | `INVOICE_ID` | DOUBLE | NOT NULL |  | Invoice ID : Primary Key |
| 11 | `INVOICE_MIN_NBR` | DOUBLE |  |  | Invoice Minimum Number |
| 12 | `INVOICE_NBR` | VARCHAR(20) |  |  | Invoice Number |
| 13 | `INV_CREATE_APPLCTX` | DOUBLE |  |  | Invoice Create Application Context Number |
| 14 | `INV_CREATE_DT_NBR` | DOUBLE |  |  | Invoice Create Date |
| 15 | `INV_CREATE_DT_TM` | DATETIME |  |  | Invoice Create Date and Time |
| 16 | `INV_CREATE_ID` | DOUBLE | NOT NULL |  | Invoice Create ID |
| 17 | `INV_CREATE_MIN_NBR` | DOUBLE |  |  | Invoice Create Minimum Number |
| 18 | `INV_CREATE_TASK` | DOUBLE |  |  | Invoice Create Task |
| 19 | `INV_UPDT_APPLCTX` | DOUBLE |  |  | Invoice Update Application Context Number |
| 20 | `INV_UPDT_CNT` | DOUBLE |  |  | Invoice Update Count |
| 21 | `INV_UPDT_DT_NBR` | DOUBLE |  |  | Invoice Update Date |
| 22 | `INV_UPDT_DT_TM` | DATETIME |  |  | Invoice Update Date and Time |
| 23 | `INV_UPDT_ID` | DOUBLE | NOT NULL |  | Invoice Update Date ID |
| 24 | `INV_UPDT_MIN_NBR` | DOUBLE |  |  | Invoice Update Minimum Number |
| 25 | `INV_UPDT_TASK` | DOUBLE |  |  | Invoice Update Task |
| 26 | `MATCHED_IND` | DOUBLE |  |  | Matched Indicator |
| 27 | `ORDER_DT_NBR` | DOUBLE |  |  | Order Date Number value |
| 28 | `ORDER_DT_TM` | DATETIME |  |  | Order Date and Time value |
| 29 | `ORDER_MIN_NBR` | DOUBLE |  |  | Order Minute |
| 30 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID |
| 31 | `OTHER_TAX` | DOUBLE |  |  | Other Tax |
| 32 | `PO_NBR` | VARCHAR(20) |  |  | Purchase Order Number |
| 33 | `PO_RCV_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Receive Status Code |
| 34 | `PO_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Status Code |
| 35 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Purchase Order ID |
| 36 | `REMIT_ADDRESS_ID` | DOUBLE | NOT NULL |  | Remit Address ID |
| 37 | `SEQUENCE` | DOUBLE |  |  | Sequence value |
| 38 | `STATE_TAX` | DOUBLE |  |  | State Tax |
| 39 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status code value |
| 40 | `SYSTEM_GENERATED_IND` | DOUBLE |  |  | system generated indicator |
| 41 | `TAX` | DOUBLE |  |  | Tax |
| 42 | `TERMS_CD` | DOUBLE | NOT NULL |  | Payment Terms Code |
| 43 | `TOTAL_INVOICE_PRICE` | DOUBLE |  |  | Total Invoice Price |
| 44 | `TOTAL_ORDER_PRICE` | DOUBLE |  |  | Total Order Price |
| 45 | `TOTAL_RCV_CNT` | DOUBLE |  |  | Total Receive Count |
| 46 | `TOTAL_RECEIPT_PRICE` | DOUBLE |  |  | Total Receive Price |
| 47 | `TOTAL_VOUCHER_PRICE` | DOUBLE |  |  | Total Voucher Price |
| 48 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 49 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 50 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 51 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 52 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 53 | `VAT_TAX` | DOUBLE |  |  | Vat Tax |
| 54 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 55 | `VENDOR_PO_REF` | VARCHAR(20) |  |  | Vendor Purchase Order Preference |
| 56 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL |  | Vendor Site ID |
| 57 | `VOUCHER_DT_NBR` | DOUBLE |  |  | Voucher Date |
| 58 | `VOUCHER_DT_TM` | DATETIME |  |  | Voucher Date and Time |
| 59 | `VOUCHER_EFFECTIVE_DT_NBR` | DOUBLE |  |  | Voucher Effective Date |
| 60 | `VOUCHER_EFFECTIVE_DT_TM` | DATETIME |  |  | Voucher Effective Date and Time |
| 61 | `VOUCHER_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Voucher Effective Minimum Number |
| 62 | `VOUCHER_MIN_NBR` | DOUBLE |  |  | Voucher Minimum Number |
| 63 | `VOUCHER_STATUS_CD` | DOUBLE | NOT NULL |  | Voucher Status |
| 64 | `VOUCHER_USER_ID` | DOUBLE | NOT NULL |  | Voucher User ID |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

