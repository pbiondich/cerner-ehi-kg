# INVOICE

> Main invoice header table.

**Description:** INVOICE  
**Table type:** ACTIVITY  
**Primary key:** `INVOICE_ID`  
**Columns:** 41  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPROVED_DT_TM` | DATETIME |  |  | When approved/unapproved |
| 2 | `APPROVED_IND` | DOUBLE | NOT NULL |  | Indicates, invoice approved or not |
| 3 | `APPROVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_id of the person from the personnel table (prsnl) that caused the approved/unapproved the invoice. |
| 4 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was was inserted. |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 7 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 8 | `INVOICE_AMOUNT` | DOUBLE |  |  | The total money amount of the invoice entered by the user. |
| 9 | `INVOICE_DT_TM` | DATETIME |  |  | The date and time on the invoice from the vendor. |
| 10 | `INVOICE_ID` | DOUBLE | NOT NULL | PK | The system assigned unique identifier for the invoice being vouchered. |
| 11 | `INVOICE_NBR` | VARCHAR(40) |  |  | The Invoice Number provided by the vendor on the invoice document. Frequently this number is a statement date when an invoice number is not provided. |
| 12 | `INVOICE_NBR_KEY` | VARCHAR(40) |  |  | Invoice Number KEY |
| 13 | `INVOICE_NBR_KEY_A_NLS` | VARCHAR(160) |  |  | INVOICE_NBR_KEY_A_NLS column |
| 14 | `INVOICE_NBR_KEY_NLS` | VARCHAR(82) |  |  | Invoice Number KEY NLS |
| 15 | `INV_PROFILE_ID` | DOUBLE |  | FK→ | The invoice profile that the invoice was created using. |
| 16 | `LAST_INTERFACED_DT_TM` | DATETIME |  |  | The last date that the invoice was transmitted to a foreign system. |
| 17 | `LAST_TRANSMIT_DT_TM` | DATETIME |  |  | last transmit date and time |
| 18 | `MATCHED_IND` | DOUBLE |  |  | Indicates whether or not the invoice has been matched. |
| 19 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 20 | `PAID_STATUS_IND` | DOUBLE |  |  | The Paid Status Indicator may provide indication that the invoice has actually been paid when a two way accounts payable interface is present. |
| 21 | `PAYMENT_AMOUNT` | DOUBLE |  |  | The amount to be paid. |
| 22 | `PAYMENT_DT_TM` | DATETIME |  |  | The Payment Date Time may provide the date and time that the invoice was actually paid when a two way accounts payable interface is present. |
| 23 | `PAYMENT_NBR` | VARCHAR(40) |  |  | The Payment Number identifies the specific funds transfer or check number that the invoice was paid on when a two way accounts payable interface is present. |
| 24 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the purchase_order table. |
| 25 | `REMIT_ADDRESS_ID` | DOUBLE |  | FK→ | The address of the remittance site. |
| 26 | `SEQUENCE` | DOUBLE |  |  | The system assigned sequence number for this invoice. |
| 27 | `STATUS_CD` | DOUBLE | NOT NULL |  | The Status code identifies whether the invoice is open, pending or closed. Pending indicates matched but that the voucher is not assigned as auto or hand. |
| 28 | `SYSTEM_GENERATED_IND` | DOUBLE |  |  | system generated indicator |
| 29 | `TERMS_CD` | DOUBLE | NOT NULL |  | The payment terms for this invoice. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `VENDOR_CD` | DOUBLE | NOT NULL |  | The Vendor Code identifies the vendor from whom the invoice is issued. |
| 36 | `VENDOR_PO_REF` | VARCHAR(40) |  |  | A free-text field from the PO. |
| 37 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to vendor_site table. |
| 38 | `VOUCHER_DT_TM` | DATETIME |  |  | The date of the voucher. |
| 39 | `VOUCHER_EFFECTIVE_DT_TM` | DATETIME |  |  | The effective date of the voucher. |
| 40 | `VOUCHER_STATUS_CD` | DOUBLE | NOT NULL |  | The Voucher Status Code identifies the current status of the Vouchered invoice. |
| 41 | `VOUCHER_USER_ID` | DOUBLE | NOT NULL |  | The Voucher User Id indicates the User id of the person who initially added the record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPROVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `INV_PROFILE_ID` | [MM_PROFILE](MM_PROFILE.md) | `PROFILE_ID` |
| `PURCHASE_ORDER_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |
| `REMIT_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `VENDOR_SITE_ID` | [VENDOR_SITE](VENDOR_SITE.md) | `VENDOR_SITE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [INVOICE_LINE_ITEM](INVOICE_LINE_ITEM.md) | `INVOICE_ID` |
| [INVOICE_PO_RECEIPT_R](INVOICE_PO_RECEIPT_R.md) | `INVOICE_ID` |
| [MM_AP_LOG_HEADER_HMW](MM_AP_LOG_HEADER_HMW.md) | `INVOICE_ID` |

