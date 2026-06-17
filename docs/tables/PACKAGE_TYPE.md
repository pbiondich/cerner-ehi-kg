# PACKAGE_TYPE

> Contains package types that an item comes in.

**Description:** Package Type  
**Table type:** REFERENCE  
**Primary key:** `PACKAGE_TYPE_ID`  
**Columns:** 15  
**Referenced by:** 35 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BASE_PACKAGE_TYPE_IND` | DOUBLE |  |  | Indicates this is the base package for an item. |
| 6 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of this package type. |
| 7 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to item_definition table. |
| 8 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the package type table. It is an internal system assigned number. |
| 9 | `QTY` | DOUBLE |  |  | The quantity of base package types contained in this package. |
| 10 | `UOM_CD` | DOUBLE | NOT NULL |  | The Unit of Measure for this package type. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

## Referenced by (35)

| From table | Column |
|------------|--------|
| [ACQUIREMENT_INFO](ACQUIREMENT_INFO.md) | `REORDER_PACKAGE_TYPE_ID` |
| [IDENTIFIER](IDENTIFIER.md) | `PACKAGE_TYPE_ID` |
| [ITEM_COMPONENT](ITEM_COMPONENT.md) | `PACKAGE_TYPE_ID` |
| [ITEM_CONTROL_INFO](ITEM_CONTROL_INFO.md) | `STOCK_PACKAGE_TYPE_ID` |
| [ITEM_PRICE](ITEM_PRICE.md) | `PACKAGE_TYPE_ID` |
| [ITEM_PRICE_HIST](ITEM_PRICE_HIST.md) | `PACKAGE_TYPE_ID` |
| [LINE_ITEM_QUANTITY](LINE_ITEM_QUANTITY.md) | `BASE_PKG_TYPE_ID` |
| [LINE_ITEM_QUANTITY](LINE_ITEM_QUANTITY.md) | `PACKAGE_TYPE_ID` |
| [LOCATOR_ROLLUP](LOCATOR_ROLLUP.md) | `PACKAGE_TYPE_ID` |
| [LOT_NUMBER_LOCATION_INFO](LOT_NUMBER_LOCATION_INFO.md) | `PACKAGE_TYPE_ID` |
| [MED_DISPENSE](MED_DISPENSE.md) | `PACKAGE_TYPE_ID` |
| [MED_INGRED_SET](MED_INGRED_SET.md) | `CHILD_PKG_TYPE_ID` |
| [MED_PRODUCT](MED_PRODUCT.md) | `INNER_PKG_TYPE_ID` |
| [MED_PRODUCT](MED_PRODUCT.md) | `OUTER_PKG_TYPE_ID` |
| [MM_APPROVAL_LOG](MM_APPROVAL_LOG.md) | `PACKAGE_TYPE_ID` |
| [MM_ITEM_ORG_COST_HIST](MM_ITEM_ORG_COST_HIST.md) | `PACKAGE_TYPE_ID` |
| [MM_LOT_RELTN](MM_LOT_RELTN.md) | `PACKAGE_TYPE_ID` |
| [MM_OMF_ITEM_MASTER](MM_OMF_ITEM_MASTER.md) | `BASE_PKG_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `BASE_PKG_TYPE_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `FROM_PKG_TYPE_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `TO_PKG_TYPE_ID` |
| [MM_XFI_COST](MM_XFI_COST.md) | `PKG_TYPE_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `BASE_PKG_TYPE_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `PKG_TYPE_ID` |
| [MM_XFI_ITEMLOC](MM_XFI_ITEMLOC.md) | `REORDER_PKG_TYPE_ID` |
| [MM_XFI_ITEMLOC](MM_XFI_ITEMLOC.md) | `STOCK_PKG_TYPE_ID` |
| [MM_XFI_LOCATOR](MM_XFI_LOCATOR.md) | `PKG_TYPE_ID` |
| [PHYS_COUNT_SHEET_ITEM](PHYS_COUNT_SHEET_ITEM.md) | `PACKAGE_TYPE_ID` |
| [PROD_DISPENSE_HX](PROD_DISPENSE_HX.md) | `PACKAGE_TYPE_ID` |
| [QUANTITY_ON_HAND](QUANTITY_ON_HAND.md) | `PACKAGE_TYPE_ID` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `PACKAGE_TYPE_ID` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `PACKAGE_TYPE_ID` |
| [RXS_LOC_ENCNTR_INVENTORY](RXS_LOC_ENCNTR_INVENTORY.md) | `PACKAGE_TYPE_ID` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `PACKAGE_TYPE_ID` |
| [STORED_AT](STORED_AT.md) | `PACKAGE_TYPE_ID` |

