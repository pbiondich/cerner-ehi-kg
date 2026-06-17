# MM_XFI_ASN_HEADER

> Table used to store incoming Advance Ship Notice interface header transactions. Data is moved from this table to PO_RECEIPT.

**Description:** MM XFI ASN HEADER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASN_DT_TM` | DATETIME |  |  | The date of notice. |
| 2 | `ASN_NBR` | VARCHAR(40) |  |  | The number assigned to this ASN. |
| 3 | `BATCH_PROCESSED_DT_TM` | DATETIME |  |  | The date and time the record was processed. |
| 4 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 6 | `CREATE_ID` | DOUBLE |  | FK→ | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 7 | `END_TRANS_ID` | DOUBLE | NOT NULL |  | The ending transaction identifier for this ASN. For internal use only. |
| 8 | `ERROR_EMAIL` | VARCHAR(100) |  |  | The email address to notify in case an error occurs. |
| 9 | `INVOICE_NBR_TXT` | VARCHAR(40) |  |  | Stores the vendor invoice number from EDI 856 |
| 10 | `JOB_EXECUTION_ID` | DOUBLE |  | FK→ | The job execution that processed this record. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `LOGIC_DETERMINE_FLAG` | DOUBLE |  |  | Indicates what logic to apply to resolve the PO line item. |
| 13 | `PACKING_LIST_NBR` | VARCHAR(40) |  |  | The Packing List Number assigned by the vendor. |
| 14 | `PO_NBR` | VARCHAR(40) |  |  | PO Number |
| 15 | `PROCESS_FLAG` | DOUBLE |  |  | Process flag |
| 16 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Foreign key to the purchase order table. |
| 17 | `SHIPMENT_DT_TM` | DATETIME |  |  | The date that the package will be shipped. |
| 18 | `SHIP_FROM_ADDR` | VARCHAR(300) |  |  | vendor address wher the item is shipped from. |
| 19 | `SHIP_FROM_NAME` | VARCHAR(60) |  |  | Vendor name, where the item is shipped from. |
| 20 | `SHIP_TO_ADDR` | VARCHAR(300) |  |  | Address of the facility to which the item is shipped |
| 21 | `SHIP_TO_NAME` | VARCHAR(60) |  |  | Facility to which the item is shipped; |
| 22 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 23 | `TRANSACTION_STATEMENT_IND` | DOUBLE |  |  | This column is to denote that the vendor has acceptance against the comment. 1 = the vendor agrees to the comment made. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `VENDOR` | VARCHAR(100) |  |  | The vendor name or number. |
| 30 | `VENDOR_CD` | DOUBLE | NOT NULL |  | The codevalue assigned to this vendor. |
| 31 | `VENDOR_COMMENT_TXT` | VARCHAR(300) |  |  | Records the vendor instructions that is made for the purchse order; |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `JOB_EXECUTION_ID` | [JOB_EXECUTION](JOB_EXECUTION.md) | `JOB_EXECUTION_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

