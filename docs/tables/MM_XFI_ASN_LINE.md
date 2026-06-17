# MM_XFI_ASN_LINE

> Table used to store incoming Advance Ship Notice interface line transactions. Data is moved from this table to RECEIPT_LINE_ITEM and LINE_ITEM_QUANTITY.

**Description:** MM XFI ASN LINE  
**Table type:** ACTIVITY  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 30  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASN_COMMENT` | VARCHAR(255) |  |  | The Vendor's comments |
| 2 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 3 | `ITEM_MASTER_DESC` | VARCHAR(255) |  |  | Stores the item description that the vendor passes from EDI. |
| 4 | `ITEM_MASTER_NBR` | VARCHAR(40) |  |  | The clients Item Master number. |
| 5 | `LINE_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign key to the line_item table. |
| 6 | `LINE_NBR` | DOUBLE |  |  | The Purchase Order line number. |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `MFR` | VARCHAR(100) |  |  | The manufacturer of the product. |
| 9 | `MFR_ADDR` | VARCHAR(300) |  |  | Stores the address of the manufacturer who has manufactured the supply item. |
| 10 | `MFR_CD` | DOUBLE |  |  | Stores the manufacturer cd for the given manufacturer |
| 11 | `MFR_ITEM_NBR` | VARCHAR(40) |  |  | The manufacturers catalog number. |
| 12 | `NDC_TXT` | VARCHAR(255) |  |  | Stores the NDC that is passed from the third party vendor.; |
| 13 | `PACK_FACTOR` | DOUBLE |  |  | The ordered/shipped packaging pack factor. |
| 14 | `PROCESS_FLAG` | DOUBLE |  |  | Process flag |
| 15 | `QTY_ORDERED` | DOUBLE |  |  | The ordered quantity. |
| 16 | `QTY_SHIPPED` | DOUBLE |  |  | The shipped quantity. |
| 17 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 18 | `TRANS_HEADER_ID` | DOUBLE | NOT NULL |  | Foreign key to mm_xfi_asn_header. |
| 19 | `UOM` | VARCHAR(100) |  |  | The ordered/shipped unit of measure. |
| 20 | `UOM_CD` | DOUBLE | NOT NULL |  | The Unit of Measure |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPN` | VARCHAR(40) |  |  | The products UPN. |
| 27 | `UPN_TXT` | VARCHAR(255) |  |  | Stores the text version of the UPN that is passed from the third party vendor.; |
| 28 | `VENDOR_ITEM_NBR` | VARCHAR(40) |  |  | The vendors catalog number. |
| 29 | `VENDOR_PACK_FACTOR` | DOUBLE |  |  | Stores the pack factor that the vendor has passed from the EDI specification file |
| 30 | `VENDOR_UOM` | VARCHAR(100) |  |  | Stores the UOM that the vendor has passed from the EDI specification file |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_XFI_ASN_LOT](MM_XFI_ASN_LOT.md) | `TRANS_LINE_ID` |

