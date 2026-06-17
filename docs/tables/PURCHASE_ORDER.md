# PURCHASE_ORDER

> Purchase orders.

**Description:** Purchase Order  
**Table type:** ACTIVITY  
**Primary key:** `PURCHASE_ORDER_ID`  
**Columns:** 54  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_DT_TM` | DATETIME |  |  | The date/Time the purchase order was acknowledged by the vendor. |
| 2 | `BILL_TO_ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | The billing address |
| 3 | `BILL_TO_ATTN` | VARCHAR(100) |  |  | Free text field to enter billing attention information |
| 4 | `BILL_TO_PSR_CD` | DOUBLE | NOT NULL |  | Bill to purchasing service resource |
| 5 | `BUYER_ID` | DOUBLE | NOT NULL |  | This denotes the buyer that is assigned to the purchase order. |
| 6 | `CLOSED_DT_TM` | DATETIME |  |  | The date/time the purchase order was closed. |
| 7 | `COMMIT_DT_TM` | DATETIME |  |  | The date and time the purchase order was committed. |
| 8 | `COMMUNICATION_DT_TM` | DATETIME |  |  | The date/time the purchase order was communicated electronically |
| 9 | `COMMUNICATION_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the communication |
| 10 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of communication utilized |
| 11 | `CONFIRMED_BY` | VARCHAR(100) |  |  | Free text field to capture who confirmed the message. |
| 12 | `CONTACT` | VARCHAR(100) |  |  | Free text field to capture contact information |
| 13 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 14 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 15 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 16 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 17 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 18 | `EXPIRATION_DT_TM` | DATETIME |  |  | Date on which a Purchase Order expires. |
| 19 | `FOB_CD` | DOUBLE | NOT NULL |  | Freight Term |
| 20 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 21 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization for which this po was created. |
| 22 | `PHASE_INVOICE_IND` | DOUBLE |  |  |  |
| 23 | `PO_NBR` | VARCHAR(40) |  |  | Purchase Order Number |
| 24 | `PO_NBR_KEY` | VARCHAR(40) | NOT NULL |  | Purchase Order Number |
| 25 | `PO_NBR_KEY_A_NLS` | VARCHAR(160) |  |  | PO_NBR_KEY_A_NLS column |
| 26 | `PO_NBR_KEY_NLS` | VARCHAR(82) |  |  | The user or system assigned purchase order number |
| 27 | `PO_RELEASE` | VARCHAR(40) |  |  |  |
| 28 | `PO_SEED_IND` | DOUBLE |  |  | Indicates where the purchase order number was generated or user defined. |
| 29 | `PO_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of purchase order created. |
| 30 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 31 | `PUR_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The purchasing profile that was used to create the po. |
| 32 | `RCV_LOCATION_CD` | DOUBLE | NOT NULL |  | The location which the po will be received. |
| 33 | `RCV_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Obsolete |
| 34 | `RECEIVE_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the receipts |
| 35 | `RECV_WORKSHEET_PRINT_DT_TM` | DATETIME |  |  | The date/time the receiving worksheet was last printed |
| 36 | `REFERENCE` | VARCHAR(40) |  |  | Free text reference field |
| 37 | `RUSH_IND` | DOUBLE | NOT NULL |  | Used to determine if the purchase order has been flagged as a rush order. |
| 38 | `SHIP_TO_ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | The address the purchase order will be shipped too |
| 39 | `SHIP_TO_ATTN` | VARCHAR(100) |  |  | Free text field to enter ship to attention information |
| 40 | `SHIP_TO_PSR_CD` | DOUBLE | NOT NULL |  | Ship to purchasing service resource |
| 41 | `SHIP_VIA_CD` | DOUBLE | NOT NULL |  | Method the purchase order will be shipped |
| 42 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the purchase order |
| 43 | `TAX_EXEMPT_IND` | DOUBLE | NOT NULL |  | Indicates whether the PO was created for a tax-exempt vendor. |
| 44 | `TEMPLATE_ID` | DOUBLE | NOT NULL |  |  |
| 45 | `TERMS_CD` | DOUBLE | NOT NULL |  | Payment Terms |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 51 | `VENDOR_ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | Vendor Address |
| 52 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 53 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to vendor_site table. |
| 54 | `VOUCHER_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the invoice voucher |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_TO_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PUR_PROFILE_ID` | [MM_PROFILE](MM_PROFILE.md) | `PROFILE_ID` |
| `RCV_PROFILE_ID` | [MM_PROFILE](MM_PROFILE.md) | `PROFILE_ID` |
| `SHIP_TO_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `VENDOR_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `VENDOR_SITE_ID` | [VENDOR_SITE](VENDOR_SITE.md) | `VENDOR_SITE_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [INVOICE](INVOICE.md) | `PURCHASE_ORDER_ID` |
| [MM_AP_LOG_LINE_HMW](MM_AP_LOG_LINE_HMW.md) | `PURCHASE_ORDER_ID` |
| [MM_PAYMENT](MM_PAYMENT.md) | `PURCHASE_ORDER_ID` |
| [MM_RECEIPT_DOC_HEADER](MM_RECEIPT_DOC_HEADER.md) | `PURCHASE_ORDER_ID` |
| [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `PURCHASE_ORDER_ID` |
| [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `PO_ID` |
| [MM_XFI_PAYMENT](MM_XFI_PAYMENT.md) | `PURCHASE_ORDER_ID` |
| [PO_BATCH_ENTRY](PO_BATCH_ENTRY.md) | `PURCHASE_ORDER_ID` |
| [PO_RECEIPT](PO_RECEIPT.md) | `PURCHASE_ORDER_ID` |

