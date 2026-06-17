# MM_OMF_RECEIPT

> Receipt : (Summary Table)

**Description:** MM OMF RECEIPT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 51

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_TO_ADDRESS_ID` | DOUBLE | NOT NULL |  | Address ID of the Bill to Address |
| 2 | `BILL_TO_ATTN` | VARCHAR(40) |  |  | Bill to Attention |
| 3 | `BUYER_ID` | DOUBLE | NOT NULL |  | Buyer ID of the Buyer |
| 4 | `COMMIT_DT_NBR` | DOUBLE |  |  | Commit Date |
| 5 | `COMMIT_DT_TM` | DATETIME |  |  | Commit Date and Time |
| 6 | `COMMIT_MIN_NBR` | DOUBLE |  |  | Commit Minute |
| 7 | `COMPANY_NBR` | VARCHAR(20) |  |  | Company Number |
| 8 | `CONFIRMED_BY` | VARCHAR(40) |  |  | %comfirm% |
| 9 | `CONTACT` | VARCHAR(40) |  |  | The person to contact |
| 10 | `EFFECTIVE_DT_NBR` | DOUBLE |  |  | Effective Date Number value |
| 11 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 12 | `EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Effective Minute number value |
| 13 | `FOB_CD` | DOUBLE | NOT NULL |  | Freight Terms Code |
| 14 | `LAST_VOUCHER_DT_NBR` | DOUBLE |  |  | Last voucher date |
| 15 | `LAST_VOUCHER_DT_TM` | DATETIME |  |  | Last Voucher Date and Time |
| 16 | `LAST_VOUCHER_MIN_NBR` | DOUBLE |  |  | Last Voucher Minute |
| 17 | `ORDER_DT_NBR` | DOUBLE |  |  | Order Date Number value |
| 18 | `ORDER_DT_TM` | DATETIME |  |  | Order Date and Time value |
| 19 | `ORDER_MIN_NBR` | DOUBLE |  |  | Order Minute |
| 20 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID |
| 21 | `PACK_SLIP_NBR` | VARCHAR(40) |  |  | Pack Slip Number |
| 22 | `PO_EFFECTIVE_DT_NBR` | DOUBLE |  |  | %Puchase% |
| 23 | `PO_EFFECTIVE_DT_TM` | DATETIME |  |  | %Puchase% |
| 24 | `PO_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | %Puchase% |
| 25 | `PO_NBR` | VARCHAR(20) |  |  | Purchase Order Number |
| 26 | `PO_RCV_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Receive Status Code |
| 27 | `PO_STATUS_CD` | DOUBLE | NOT NULL |  | Purchase Order Status Code |
| 28 | `PO_TYPE_CD` | DOUBLE | NOT NULL |  | Purchase Order Type Code |
| 29 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Purchase Order ID |
| 30 | `RECEIPT_COUNT` | DOUBLE |  |  | Receipt Count |
| 31 | `RECEIPT_ID` | DOUBLE | NOT NULL |  | Receipt ID : (Primary Key). |
| 32 | `RECEIPT_LINE_COUNT` | DOUBLE |  |  | Receipt Line Count |
| 33 | `RECEIVE_DT_NBR` | DOUBLE |  |  | Receive Date |
| 34 | `RECEIVE_DT_TM` | DATETIME |  |  | Receive Date and Time |
| 35 | `RECEIVE_LOCATION_CD` | DOUBLE | NOT NULL |  | Receive Location Code |
| 36 | `RECEIVE_MIN_NBR` | DOUBLE |  |  | Receive Minute |
| 37 | `REFERENCE` | VARCHAR(40) |  |  | Reference |
| 38 | `SEQUENCE` | DOUBLE |  |  | Sequence value |
| 39 | `SHIP_TO_ADDRESS_ID` | DOUBLE | NOT NULL |  | Ship to Address ID |
| 40 | `SHIP_TO_ATTN` | VARCHAR(40) |  |  | Ship to Attention |
| 41 | `STATUS_CD` | DOUBLE | NOT NULL |  | Receipt Status Code |
| 42 | `TOTAL_ORDER_PRICE` | DOUBLE |  |  | Total Order Price |
| 43 | `TOTAL_RECEIVE_PRICE` | DOUBLE |  |  | Total Receive Price |
| 44 | `TOTAL_VOUCHER_PRICE` | DOUBLE |  |  | Total Voucher Price |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 50 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 51 | `VOUCHER_COUNT` | DOUBLE |  |  | Voucher Count |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

