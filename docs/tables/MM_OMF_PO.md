# MM_OMF_PO

> Purchase Order Header: (Summary table)

**Description:** MM OMF PO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 64

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_TO_ADDRESS_ID` | DOUBLE | NOT NULL |  | Address ID of the billing to address |
| 2 | `BILL_TO_ATTN` | VARCHAR(40) |  |  | Bill to Attention |
| 3 | `BUYER_ID` | DOUBLE | NOT NULL |  | Buyer ID of the Buyer |
| 4 | `CLOSED_DT_NBR` | DOUBLE |  |  | Closed Date Number |
| 5 | `CLOSED_DT_TM` | DATETIME |  |  | Close Date and Time |
| 6 | `CLOSED_MIN_NBR` | DOUBLE |  |  | Close Minute Number |
| 7 | `COMMIT_DT_NBR` | DOUBLE |  |  | Commit Date Number |
| 8 | `COMMIT_DT_TM` | DATETIME |  |  | Commit Date and Time |
| 9 | `COMMIT_MIN_NBR` | DOUBLE |  |  | Commit Minute Number |
| 10 | `COMPANY_NBR` | VARCHAR(20) |  |  | Company Number |
| 11 | `CONFIRMED_BY` | VARCHAR(40) |  |  | %comfirm% |
| 12 | `CONTACT` | VARCHAR(40) |  |  | Name of the person to contact |
| 13 | `EFFECTIVE_DT_NBR` | DOUBLE |  |  | Effective Date Number value |
| 14 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 15 | `EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Effective Minute number value |
| 16 | `EXPIRATION_DT_NBR` | DOUBLE |  |  | Julian Date on which PO expires |
| 17 | `EXPIRATION_DT_TM` | DATETIME |  |  | Date on which a Purchase Order expires. |
| 18 | `EXPIRATION_MIN_NBR` | DOUBLE |  |  | Julian minute on which PO expires. |
| 19 | `FOB_CD` | DOUBLE | NOT NULL |  | Freight Terms Code |
| 20 | `LAST_RECEIPT_DT_NBR` | DOUBLE |  |  | Last Receipt Date Number |
| 21 | `LAST_RECEIPT_DT_TM` | DATETIME |  |  | Last Receipt Date and Time |
| 22 | `LAST_RECEIPT_MIN_NBR` | DOUBLE |  |  | Last Receipt Minute |
| 23 | `LAST_VOUCHER_DT_NBR` | DOUBLE |  |  | Last Voucher Date Number |
| 24 | `LAST_VOUCHER_DT_TM` | DATETIME |  |  | Last Voucher Date and Time |
| 25 | `LAST_VOUCHER_MIN_NBR` | DOUBLE |  |  | Last Voucher Minute |
| 26 | `LINE_COUNT` | DOUBLE |  |  | Line count under the purchase order |
| 27 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID |
| 28 | `PO_COUNT` | DOUBLE |  |  | Purchase Order Count |
| 29 | `PO_CREATE_DT_NBR` | DOUBLE |  |  | Purchase Order Create Date |
| 30 | `PO_CREATE_DT_TM` | DATETIME |  |  | Purchase Order Create Date and Time |
| 31 | `PO_CREATE_ID` | DOUBLE | NOT NULL |  | Purchase Order Create ID |
| 32 | `PO_CREATE_MIN_NBR` | DOUBLE |  |  | Purchase Order Create Minute |
| 33 | `PO_NBR` | VARCHAR(20) |  |  | Purchase Order Number |
| 34 | `PO_RELEASE` | VARCHAR(20) |  |  | How many times the purchase order released |
| 35 | `PO_UPDT_CNT` | DOUBLE |  |  | How may times the purchase order has been updated |
| 36 | `PO_UPDT_DT_NBR` | DOUBLE |  |  | Purchase Order Update Date |
| 37 | `PO_UPDT_DT_TM` | DATETIME |  |  | Purchase Order Update Date and Time |
| 38 | `PO_UPDT_ID` | DOUBLE | NOT NULL |  | Purchase Order Update ID |
| 39 | `PO_UPDT_MIN_NBR` | DOUBLE |  |  | Purchase Order Update Minute |
| 40 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Purchase Order ID : (Primary Key) |
| 41 | `PUR_PROFILE_ID` | DOUBLE | NOT NULL |  | Purchase Order Profile ID |
| 42 | `RECEIPT_COUNT` | DOUBLE |  |  | Number of receipts under the purchase order |
| 43 | `RECEIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Receive Status |
| 44 | `REFERENCE` | VARCHAR(40) |  |  | Reference |
| 45 | `SHIP_TO_ADDRESS_ID` | DOUBLE | NOT NULL |  | Ship to Address |
| 46 | `SHIP_TO_ATTN` | VARCHAR(40) |  |  | Ship to Attention (comment) |
| 47 | `SHIP_TO_LOC_CD` | DOUBLE | NOT NULL |  | Ship to Location Code |
| 48 | `SHIP_VIA_CD` | DOUBLE | NOT NULL |  | Ship Via Code |
| 49 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status code value |
| 50 | `TERMS_CD` | DOUBLE | NOT NULL |  | Payment Terms Code |
| 51 | `TOTAL_ORDER_PRICE` | DOUBLE |  |  | Total Order Price |
| 52 | `TOTAL_RECEIVED_PRICE` | DOUBLE |  |  | Total Receive Price |
| 53 | `TOTAL_VOUCHERED_PRICE` | DOUBLE |  |  | Total Voucher Price |
| 54 | `TYPE_CD` | DOUBLE | NOT NULL |  | Purchase Order Type |
| 55 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 58 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 59 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 60 | `VENDOR_ADDRESS_ID` | DOUBLE | NOT NULL |  | Vendor Address ID |
| 61 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 62 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL |  | Vendor Site ID |
| 63 | `VOUCHER_COUNT` | DOUBLE |  |  | Voucher Count |
| 64 | `VOUCHER_STATUS_CD` | DOUBLE | NOT NULL |  | Voucher Status Code |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

