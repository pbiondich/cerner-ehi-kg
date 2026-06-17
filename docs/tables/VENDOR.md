# VENDOR

> Vendors table

**Description:** Vendor  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACKNOWLEDGEMENT_IND` | DOUBLE | NOT NULL |  | Used to determine if the EDI 855 acknowledgement will create a line level comment or update the purchase order and vendor information automatically. 0 = Line level comment will be created. 1 = Purchase order and vendor information will be updated automatically. |
| 2 | `ACTIVE_DT_TM` | DATETIME |  |  | Date and time the record became active |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_TYPE_CD` | DOUBLE |  |  | Active type code value |
| 5 | `APPROVED_VENDOR_STATUS_CD` | DOUBLE |  |  | Approved vendor status code value |
| 6 | `AUTO_COMMIT_PO_IND` | DOUBLE |  |  | If true then the req-to-po process will automatically commit the purchase order. |
| 7 | `AUTO_COMMIT_RECEIPT_IND` | DOUBLE |  |  | If true then the EDI 856 (Advanced Ship Notice) process will automatically commit the receipt. |
| 8 | `BACKORDER_IND` | DOUBLE |  |  | Indicates if the vendor allows backorders |
| 9 | `CONSOLIDATE_RQSTN_IND` | DOUBLE | NOT NULL |  | Indicates whether all requisitions for a particular vendor will be grouped on a single Purchase Order or whether a Purchase Order will be generated for each requisition item. 0 - not consolidated, 1 - consolidated onto one P.O. |
| 10 | `DESCRIPTION` | VARCHAR(60) |  |  | The vendor's long description |
| 11 | `DESCRIPTION_KEY` | VARCHAR(60) |  |  | Indexed key for description field |
| 12 | `DESCRIPTION_KEY_A_NLS` | VARCHAR(240) |  |  | DESCRIPTION_KEY_A_NLS column |
| 13 | `DESCRIPTION_KEY_NLS` | VARCHAR(122) |  |  | Indexed key for description field |
| 14 | `DISPLAY` | VARCHAR(40) |  |  | Short description of vendor |
| 15 | `DISPLAY_KEY` | VARCHAR(40) |  |  | Indexed key for display field |
| 16 | `DISPLAY_KEY_A_NLS` | VARCHAR(160) |  |  | DISPLAY_KEY_A_NLS column |
| 17 | `DISPLAY_KEY_NLS` | VARCHAR(82) |  |  | Indexed key for display field - NLS support |
| 18 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 19 | `MIN_ORDER_COST` | DOUBLE |  |  | Minimum ordering cost from vendor |
| 20 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the The Output destination |
| 21 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Vendor code value |
| 22 | `TAX_EXEMPT_IND` | DOUBLE | NOT NULL |  | This indicator indicates whether the vendor is a tax exempt vendor. |
| 23 | `TAX_PAYER_NBR` | VARCHAR(50) |  |  | The tax payers number |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VENDOR_NUMBER` | DOUBLE |  |  | Vendor number |
| 30 | `VENDOR_TYPE_CD` | DOUBLE |  |  | Code for the Type of vendor |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `OUTPUT_DEST_ID` | [STATION](STATION.md) | `OUTPUT_DEST_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

