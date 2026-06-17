# MM_RECEIPT_DOC_LINE

> An EDI 856 transaction can contain the receipt information of multiple PO lines, this table will store the item details of each line. ;

**Description:** Receipt Documen Line  
**Table type:** ACTIVITY  
**Primary key:** `MM_RECEIPT_DOC_LINE_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ITEM_MASTER_DESC` | VARCHAR(255) |  |  | Stores the item description that the vendor passes from EDI. |
| 2 | `ITEM_MASTER_NBR_TXT` | VARCHAR(255) |  |  | Stores item number for T3 documentation purpose. |
| 3 | `LINE_ITEM_ID` | DOUBLE |  | FK→ | FK reference to the line_item table. |
| 4 | `MFR_ADDR` | VARCHAR(300) |  |  | Stores the address of the manufacturer who has manufactured the supply item. |
| 5 | `MFR_CD` | DOUBLE |  |  | The manufacturer of the item. From the MANUFACTURER_ITEM table. |
| 6 | `MFR_NAME` | VARCHAR(100) |  |  | The manufacturer of the item. |
| 7 | `MM_RECEIPT_DOC_HEADER_ID` | DOUBLE |  | FK→ | The header that this line is a part of. |
| 8 | `MM_RECEIPT_DOC_LINE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_RECEIPT_DOC_LINE table. |
| 9 | `PACK_FACTOR_NBR` | DOUBLE |  |  | FK reference to the line_item table. |
| 10 | `SHIPPED_QTY` | DOUBLE |  |  | The quantity of the item on this line that was shipped. |
| 11 | `UOM_CD` | DOUBLE |  |  | The Unit of Measure for this item. |
| 12 | `UOM_DESC` | VARCHAR(100) |  |  | UOM description for the T3 documentation purpose. |
| 13 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VENDOR_ITEM_NBR_TXT` | VARCHAR(40) |  |  | Stores vendor catalog for T3 documentation purpose. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |
| `MM_RECEIPT_DOC_HEADER_ID` | [MM_RECEIPT_DOC_HEADER](MM_RECEIPT_DOC_HEADER.md) | `MM_RECEIPT_DOC_HEADER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_RECEIPT_DOC_LOT](MM_RECEIPT_DOC_LOT.md) | `MM_RECEIPT_DOC_LINE_ID` |

