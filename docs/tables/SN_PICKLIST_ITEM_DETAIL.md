# SN_PICKLIST_ITEM_DETAIL

> Unique Instance of a given item on a surgical picklist

**Description:** Surginet Picklist Item Detail  
**Table type:** ACTIVITY  
**Primary key:** `SN_PICKLIST_ITEM_DETAIL_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEVICE_IDENTIFIER_TXT` | VARCHAR(255) |  |  | The device identifier of the instance of the item |
| 2 | `DONATION_IDENT` | VARCHAR(255) |  |  | The donation Identified of the instance of the item |
| 3 | `EXPIRATION_DT_TM` | DATETIME |  |  | the date of expiration of the instance of the item |
| 4 | `LOT_NBR_TXT` | VARCHAR(255) |  |  | The lot number of the instance of the item |
| 5 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | If the item contains a lot numner, the identifier of the lot number for this instance of the item |
| 6 | `MANF_CATALOG_NBR_TXT` | VARCHAR(255) |  |  | The catalog number of the manufacturers item |
| 7 | `MANF_CD` | DOUBLE | NOT NULL |  | The manufacturer of the instance of the item |
| 8 | `MANUFACTURE_DT_TM` | DATETIME |  |  | The date of manufacture of the instance of the item |
| 9 | `MM_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | The instance identifier contains a serial numner, the instance identifier for this instance of the item |
| 10 | `PARENT_PICKLIST_ITEM_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | PARENT DETAIL ID |
| 11 | `SERIAL_NBR_TXT` | VARCHAR(255) |  |  | The serial Number of the instance of the item |
| 12 | `SN_PICKLIST_ITEM_DETAIL_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 13 | `SN_PICKLIST_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item on the picklist that this detail is defining. |
| 14 | `UDI_HRF_TXT` | VARCHAR(255) |  |  | The Human readable (formatted) version of the barcode of the instance of the item |
| 15 | `UDI_MRF_TXT` | VARCHAR(255) |  |  | The machine readable (raw) version of the barcode of the instance of the item; |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `MM_INSTANCE_ID` | [MM_INSTANCE](MM_INSTANCE.md) | `MM_INSTANCE_ID` |
| `PARENT_PICKLIST_ITEM_DETAIL_ID` | [SN_PICKLIST_ITEM_DETAIL](SN_PICKLIST_ITEM_DETAIL.md) | `SN_PICKLIST_ITEM_DETAIL_ID` |
| `SN_PICKLIST_ITEM_ID` | [SN_PICKLIST_ITEM](SN_PICKLIST_ITEM.md) | `SN_PICKLIST_ITEM_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SN_PICKLIST_FILL](SN_PICKLIST_FILL.md) | `SN_PICKLIST_ITEM_DETAIL_ID` |
| [SN_PICKLIST_ITEM_DETAIL](SN_PICKLIST_ITEM_DETAIL.md) | `PARENT_PICKLIST_ITEM_DETAIL_ID` |
| [SN_PICKLIST_RETURN](SN_PICKLIST_RETURN.md) | `SN_PICKLIST_ITEM_DETAIL_ID` |
| [SN_PICKLIST_USE](SN_PICKLIST_USE.md) | `SN_PICKLIST_ITEM_DETAIL_ID` |
| [SN_PICKLIST_WASTE](SN_PICKLIST_WASTE.md) | `SN_PICKLIST_ITEM_DETAIL_ID` |

