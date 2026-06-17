# MM_AP_LOG_HEADER_HMW

> AP Log Header

**Description:** AP Log Header  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPANY_CODE` | VARCHAR(20) |  |  | Company Code or Number |
| 2 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 3 | `CREATE_NAME` | VARCHAR(100) |  |  | Create Name |
| 4 | `FREIGHT_AMT` | DOUBLE |  |  | Freight Amount |
| 5 | `GROSS_AMT` | DOUBLE |  |  | Gross Amount |
| 6 | `HEADER_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 7 | `INVOICE_DT_TM` | DATETIME |  |  | Invoice Date |
| 8 | `INVOICE_ID` | DOUBLE | NOT NULL | FK→ | Invoice ID |
| 9 | `INVOICE_NBR` | VARCHAR(40) |  |  | Invoice Number |
| 10 | `LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID |
| 12 | `PAYMENT_TERMS` | VARCHAR(60) |  |  | Payment Terms |
| 13 | `PAYMENT_TERMS_CD` | DOUBLE | NOT NULL |  | Payment Terms |
| 14 | `RAW_VOUCHER_HEADER` | VARCHAR(200) |  |  | The actual text written out to the file. |
| 15 | `SALES_TAX_AMT` | DOUBLE |  |  | Sales Tax Amount |
| 16 | `TOTAL_VOUCHER_LINES` | DOUBLE |  |  | Total Voucher Lines |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VENDOR` | VARCHAR(40) |  |  | Vendor |
| 23 | `VENDOR_ALIAS` | VARCHAR(20) |  |  | Vendor Alias |
| 24 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | `INVOICE_ID` |
| `LOG_ID` | [MM_AP_LOG_HMW](MM_AP_LOG_HMW.md) | `LOG_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

