# VENDOR_SITE

> Vendor customer account

**Description:** VENDOR SITE  
**Table type:** REFERENCE  
**Primary key:** `VENDOR_SITE_ID`  
**Columns:** 26  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_NUMBER` | VARCHAR(40) | NOT NULL |  | Account number |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ASN_IND` | DOUBLE | NOT NULL |  | Enables the user to identify whethere a vendor site supports ASN or not. |
| 7 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 8 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 9 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 10 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 11 | `DESCRIPTION` | VARCHAR(200) |  |  | Description of account |
| 12 | `FREIGHT_TERMS_CD` | DOUBLE | NOT NULL |  | Freight Terms |
| 13 | `PAYMENT_TERMS_CD` | DOUBLE | NOT NULL |  | Payment terms |
| 14 | `PO_PRINT_FORMAT_CD` | DOUBLE | NOT NULL |  | Purchase Order printing format |
| 15 | `PO_TRANSMIT_TYPE_CD` | DOUBLE | NOT NULL |  | PO Transmission type |
| 16 | `RCV_PROFILE_ID` | DOUBLE |  | FK→ | The receiving profile for the vendor site. |
| 17 | `SECONDARY_VENDOR_SITE_ID` | DOUBLE |  | FK→ | This field has foreign key relation with vendor_site_id from the self table. Alternate vendor site for the same vendor. |
| 18 | `SHIP_VIA_CD` | DOUBLE | NOT NULL |  | Ship Via |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 25 | `VENDOR_PRICE_SCHEDULE_ID` | DOUBLE | NOT NULL |  | Foreign key to price schedule |
| 26 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCV_PROFILE_ID` | [MM_PROFILE](MM_PROFILE.md) | `PROFILE_ID` |
| `SECONDARY_VENDOR_SITE_ID` | [VENDOR_SITE](VENDOR_SITE.md) | `VENDOR_SITE_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [ACQUIREMENT_INFO](ACQUIREMENT_INFO.md) | `VENDOR_SITE_ID` |
| [INVOICE](INVOICE.md) | `VENDOR_SITE_ID` |
| [PO_BATCH](PO_BATCH.md) | `VENDOR_SITE_ID` |
| [PURCHASE_ORDER](PURCHASE_ORDER.md) | `VENDOR_SITE_ID` |
| [VENDOR_SITE](VENDOR_SITE.md) | `SECONDARY_VENDOR_SITE_ID` |
| [VENDOR_SITE_RESUB_REASON](VENDOR_SITE_RESUB_REASON.md) | `VENDOR_SITE_ID` |

