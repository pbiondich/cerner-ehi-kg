# LOT_NUMBER_INFO

> Holds an item's lot number(s)

**Description:** LOT NUMBER INFO  
**Table type:** REFERENCE  
**Primary key:** `LOT_NUMBER_ID`  
**Columns:** 19  
**Referenced by:** 19 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_EXP_DT_TM` | DATETIME |  |  | Expiration Date as determined at place of origin. |
| 2 | `ABS_EXP_TZ` | DOUBLE |  |  | Time zone associated with the ABS_EXP_DT_TM column. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `EXP_DT_TM` | DATETIME |  |  | The date/time an item will expire. |
| 8 | `ITEM_ID` | DOUBLE | NOT NULL |  | The unique id for the item master. |
| 9 | `LOT_NUMBER` | CHAR(40) |  |  | Character description of the lot number as defined by the manufacturer of the lot. |
| 10 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK | Primary key. |
| 11 | `LOT_NUMBER_TXT` | VARCHAR(40) | NOT NULL |  | The lot number converted to all uppercase. |
| 12 | `MANF_DT_TM` | DATETIME |  |  | Date and time an item in the lot was manufactured. |
| 13 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | Manufacturer for the item. |
| 14 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Primary Key from the MED_PRODUCT table. Represents the medication product associated to the lot. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |

## Referenced by (19)

| From table | Column |
|------------|--------|
| [ALIQUOTTED_PRIMER_KIT](ALIQUOTTED_PRIMER_KIT.md) | `LOT_NUMBER_ID` |
| [BLOT_BATCH](BLOT_BATCH.md) | `LOT_NUMBER_ID` |
| [HLA_AB_SCREEN_BATCH](HLA_AB_SCREEN_BATCH.md) | `LOT_NUMBER_ID` |
| [HLA_AB_SCREEN_TRAY_MAP](HLA_AB_SCREEN_TRAY_MAP.md) | `LOT_NUMBER_ID` |
| [HLA_TYP_TRAY_MAP](HLA_TYP_TRAY_MAP.md) | `LOT_NUMBER_ID` |
| [HLA_XM_TRAY_MAP](HLA_XM_TRAY_MAP.md) | `LOT_NUMBER_ID` |
| [HLA_XM_TRAY_WELL](HLA_XM_TRAY_WELL.md) | `LOT_NUMBER_ID` |
| [LOT_NUMBER_LOCATION_INFO](LOT_NUMBER_LOCATION_INFO.md) | `LOT_NUMBER_ID` |
| [MM_INSTANCE](MM_INSTANCE.md) | `LOT_NUMBER_ID` |
| [MM_LOT_RELTN](MM_LOT_RELTN.md) | `LOT_NUMBER_ID` |
| [MM_LOT_RELTN](MM_LOT_RELTN.md) | `PARENT_LOT_NUMBER_ID` |
| [MM_RECEIPT_DOC_LOT](MM_RECEIPT_DOC_LOT.md) | `LOT_NUMBER_ID` |
| [MM_SUPPLY_CABINET](MM_SUPPLY_CABINET.md) | `LOT_NUMBER_ID` |
| [MM_TRANS_IDENTIFIER_RELTN](MM_TRANS_IDENTIFIER_RELTN.md) | `LOT_NUMBER_ID` |
| [MM_XFI_ASN_LOT](MM_XFI_ASN_LOT.md) | `LOT_NUMBER_ID` |
| [MM_XFI_QOH](MM_XFI_QOH.md) | `LOT_NUMBER_ID` |
| [MM_XFI_REQ_FILL_LOT](MM_XFI_REQ_FILL_LOT.md) | `LOT_NUMBER_ID` |
| [MOLECULAR_BLOT](MOLECULAR_BLOT.md) | `LOT_NUMBER_ID` |
| [SN_PICKLIST_ITEM_DETAIL](SN_PICKLIST_ITEM_DETAIL.md) | `LOT_NUMBER_ID` |

