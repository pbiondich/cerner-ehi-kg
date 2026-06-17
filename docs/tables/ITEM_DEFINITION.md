# ITEM_DEFINITION

> Parent table for all Inventory, Vendor, and Manufacturer items.

**Description:** ITEM DEFINITION  
**Table type:** REFERENCE  
**Primary key:** `ITEM_ID`  
**Columns:** 48  
**Referenced by:** 78 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPROVED_IND` | DOUBLE |  |  | Indicates that this item has been approved for use. |
| 6 | `BASE_ISSUE_FACTOR` | DOUBLE | NOT NULL |  | The factor in which an item's issue quantity can be broken down in. For example: A tablet is what aspirin is tracked by, but they can dispense it in half tablets. Therefor the base issue factor will be 1/2. |
| 7 | `BATCH_QTY` | DOUBLE |  |  | The quantity that is manufactured / assembled each time. |
| 8 | `CHARGEABLE_IND` | DOUBLE | NOT NULL |  | Indicates whether the item is chargeable or not. |
| 9 | `COMPONENT_FILL_RETURN_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to use component fill/return hierarchy. Used to indicate that the components are decremented from a different location than where the pack was filled/decremented from. |
| 10 | `COMPONENT_IND` | DOUBLE |  |  | Indicates whether or not this item contains components. |
| 11 | `COMPONENT_TRANS_IND` | DOUBLE | NOT NULL |  | Indicates whether or not a component generates an inventory transaction. Indicates that the components are decremented independently from the parent/pack level. |
| 12 | `COMPONENT_USAGE_IND` | DOUBLE |  |  | Defines whether or not usage is captured for each component in a pack/set. |
| 13 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was created. |
| 15 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that created the row in the table. |
| 16 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that created the row. |
| 17 | `IMPLANT_TYPE_CD` | DOUBLE | NOT NULL |  | If this item is an implant, indicates the type of implant. |
| 18 | `ITEM_ID` | DOUBLE | NOT NULL | PK | Primary key. |
| 19 | `ITEM_LEVEL_FLAG` | DOUBLE | NOT NULL |  | This flag indicates the item type, specifically for med def items. |
| 20 | `ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | Codevalue for the type of item (ITEM_MASTER, ITEM_EQP,...). |
| 21 | `LATEX_IND` | DOUBLE |  |  | Indicator which specifies whether the item is latex or not. |
| 22 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 23 | `LOT_TRACKING_IND` | DOUBLE | NOT NULL |  | Indicates if the item quantity is tracked at lot level. |
| 24 | `MAX_TEMP_AMT` | DOUBLE | NOT NULL |  | The maximum temperature at which this item should be stored. |
| 25 | `MIN_TEMP_AMT` | DOUBLE | NOT NULL |  | The minimum temperature at which this item should be stored. |
| 26 | `MULTI_LOT_TRANSFER_IND` | DOUBLE | NOT NULL |  | Indicates if the a transfer is for one lot or multiple lots. 0 - single lot, 1 - multiple lots |
| 27 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 28 | `PHA_TYPE_FLAG` | DOUBLE | NOT NULL |  | This flag indicates the pharmacy item type: inpatient, retail or shared. |
| 29 | `PRE_EXP_DATE_PERIOD_NBR` | DOUBLE | NOT NULL |  | When to alert the user that the product should be used before expiring. |
| 30 | `PRE_EXP_DATE_UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure associated to PRE_EXP_DATE_PERIOD_NBR. |
| 31 | `QUICKADD_IND` | DOUBLE |  |  | Indicates that this item was added through the QuickAdd function. |
| 32 | `REUSABLE_IND` | DOUBLE |  |  | Indicates whether or not this item is reusable. |
| 33 | `SHELF_LIFE` | DOUBLE |  |  | Indicates the shelf life for this item. |
| 34 | `SHELF_LIFE_UOM_CD` | DOUBLE | NOT NULL |  | The units of measure for the shelf life. |
| 35 | `SUBSTITUTION_IND` | DOUBLE |  |  | Indicator which specifies whether the item is under substitution. |
| 36 | `SUPPRESS_AUTO_FILL_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to suppress automated fill on Case Pick list. Used to prevent the components from being filled prematurely. |
| 37 | `TEMP_UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure the temperature columns represent. |
| 38 | `UDI_EXP_DATE_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by expiration date |
| 39 | `UDI_LOT_NBR_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by lot number |
| 40 | `UDI_MFR_DATE_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by manufacturer date |
| 41 | `UDI_SERIAL_NBR_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by serial number |
| 42 | `UNIQUE_FIELD` | VARCHAR(400) |  |  | Unique field which will hold the Item Nbr, Description, and Vendor/Manufacturer concatenated together for merging purposes. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_PRICE_SCHED_PRICE_IND` | DOUBLE | NOT NULL |  | Denotes whether the price schedule price needs to be update for this item. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (78)

| From table | Column |
|------------|--------|
| [ACQUIREMENT_INFO](ACQUIREMENT_INFO.md) | `ITEM_ID` |
| [CE_INVENTORY_RESULT](CE_INVENTORY_RESULT.md) | `ITEM_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `ITEM_ID` |
| [IMPLANT_HISTORY](IMPLANT_HISTORY.md) | `IMPLANT_ITEM_ID` |
| [ITEM_CLASS_NODE_R](ITEM_CLASS_NODE_R.md) | `ITEM_ID` |
| [ITEM_COMPONENT](ITEM_COMPONENT.md) | `COMPONENT_ID` |
| [ITEM_COMPONENT](ITEM_COMPONENT.md) | `ITEM_ID` |
| [ITEM_CONTROL_INFO](ITEM_CONTROL_INFO.md) | `ITEM_ID` |
| [ITEM_INSTANCE](ITEM_INSTANCE.md) | `ITEM_ID` |
| [ITEM_ITEM_XREF](ITEM_ITEM_XREF.md) | `CHILD_ITEM_ID` |
| [ITEM_ITEM_XREF](ITEM_ITEM_XREF.md) | `PARENT_ITEM_ID` |
| [ITEM_LOCATION_COST](ITEM_LOCATION_COST.md) | `ITEM_ID` |
| [ITEM_ORG_RELTN](ITEM_ORG_RELTN.md) | `ITEM_ID` |
| [LOCATOR_ROLLUP](LOCATOR_ROLLUP.md) | `ITEM_ID` |
| [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `INV_MASTER_ID` |
| [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `PARENT_ITEM_ID` |
| [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `PRIMARY_MANF_ITEM_ID` |
| [MED_DISPENSE](MED_DISPENSE.md) | `ITEM_ID` |
| [MED_INGRED_SET](MED_INGRED_SET.md) | `CHILD_ITEM_ID` |
| [MED_INGRED_SET](MED_INGRED_SET.md) | `PARENT_ITEM_ID` |
| [MM_APPROVAL_LOG](MM_APPROVAL_LOG.md) | `ITEM_ID` |
| [MM_AP_LOG_LINE_HMW](MM_AP_LOG_LINE_HMW.md) | `ITEM_ID` |
| [MM_CS_PATIENT_PRICE](MM_CS_PATIENT_PRICE.md) | `ITEM_ID` |
| [MM_INSTANCE](MM_INSTANCE.md) | `ITEM_ID` |
| [MM_ITEM_ORG_COST_HIST](MM_ITEM_ORG_COST_HIST.md) | `ITEM_ID` |
| [MM_ITEM_REPL](MM_ITEM_REPL.md) | `ITEM_ID` |
| [MM_ITEM_REPL](MM_ITEM_REPL.md) | `REPL_ITEM_ID` |
| [MM_OMF_ITEM_MASTER](MM_OMF_ITEM_MASTER.md) | `ITEM_MASTER_ID` |
| [MM_REQ_FILL_ROUTE](MM_REQ_FILL_ROUTE.md) | `ITEM_ID` |
| [MM_SUPPLY_CABINET](MM_SUPPLY_CABINET.md) | `ITEM_ID` |
| [MM_SUPPLY_CABINET](MM_SUPPLY_CABINET.md) | `MFR_ITEM_ID` |
| [MM_TEMPLATE_ITEM](MM_TEMPLATE_ITEM.md) | `ITEM_ID` |
| [MM_XFI_COST](MM_XFI_COST.md) | `ITEM_ID` |
| [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `ITEM_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `ITEM_MASTER_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `MFR_ITEM_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `VENDOR_ITEM_ID` |
| [MM_XFI_ITEMLOC](MM_XFI_ITEMLOC.md) | `ITEM_ID` |
| [MM_XFI_ITEMLOC](MM_XFI_ITEMLOC.md) | `PRIMARY_VENDOR_ITEM_ID` |
| [MM_XFI_ITEM_REPL](MM_XFI_ITEM_REPL.md) | `ITEM_ID` |
| [MM_XFI_ITEM_REPL](MM_XFI_ITEM_REPL.md) | `REPL_ITEM_ID` |
| [MM_XFI_LOCATOR](MM_XFI_LOCATOR.md) | `ITEM_ID` |
| [MM_XFI_MFR_ITEM](MM_XFI_MFR_ITEM.md) | `ITEM_ID` |
| [MM_XFI_MFR_ITEM](MM_XFI_MFR_ITEM.md) | `MFR_ITEM_ID` |
| [ORDER_CATALOG_ITEM_R](ORDER_CATALOG_ITEM_R.md) | `ITEM_ID` |
| [ORDER_PRODUCT](ORDER_PRODUCT.md) | `ITEM_ID` |
| [PACKAGE_TYPE](PACKAGE_TYPE.md) | `ITEM_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `ITEM_ID` |
| [PHYS_COUNT_SHEET_ITEM](PHYS_COUNT_SHEET_ITEM.md) | `ITEM_ID` |
| [PREF_CARD_PICK_LIST](PREF_CARD_PICK_LIST.md) | `ITEM_ID` |
| [PROD_DISPENSE_HX](PROD_DISPENSE_HX.md) | `ITEM_ID` |
| [PROD_DISPENSE_HX](PROD_DISPENSE_HX.md) | `MANF_ITEM_ID` |
| [QUANTITY_ON_HAND](QUANTITY_ON_HAND.md) | `ITEM_ID` |
| [RXS_ACTIVITY_INDEX](RXS_ACTIVITY_INDEX.md) | `ITEM_ID` |
| [RXS_ALERT](RXS_ALERT.md) | `INV_ITEM_ID` |
| [RXS_EXTENDED_COUNT_PROP](RXS_EXTENDED_COUNT_PROP.md) | `ITEM_ID` |
| [RXS_FOREIGN_DEVICE_ALERT](RXS_FOREIGN_DEVICE_ALERT.md) | `INV_ITEM_ID` |
| [RXS_GROUP_ITEM_RELTN](RXS_GROUP_ITEM_RELTN.md) | `ITEM_ID` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `INV_ITEM_ID` |
| [RXS_LAST_LOCATOR_ACTIVITY](RXS_LAST_LOCATOR_ACTIVITY.md) | `ITEM_ID` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `INV_ITEM_ID` |
| [RX_ADMIN_PROD_DISPENSE_HX](RX_ADMIN_PROD_DISPENSE_HX.md) | `ITEM_ID` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `INV_ITEM_ID` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `ITEM_ID` |
| [RX_WS_FAC_ITEM_RELTN](RX_WS_FAC_ITEM_RELTN.md) | `ITEM_ID` |
| [RX_WS_FAC_RELTN](RX_WS_FAC_RELTN.md) | `PARENT_ITEM_ID` |
| [SCH_PEND_SURG_ITEM](SCH_PEND_SURG_ITEM.md) | `ITEM_ID` |
| [SCH_RESOURCE](SCH_RESOURCE.md) | `ITEM_ID` |
| [SN_PICKLIST_ITEM](SN_PICKLIST_ITEM.md) | `ITEM_ID` |
| [SN_PICKLIST_ITEM](SN_PICKLIST_ITEM.md) | `REPLACES_ITEM_ID` |
| [SN_PICKLIST_ITEM_REPL](SN_PICKLIST_ITEM_REPL.md) | `ITEM_ID` |
| [SN_PICKLIST_ITEM_REPL](SN_PICKLIST_ITEM_REPL.md) | `REPLACED_WITH_ITEM_ID` |
| [SN_PREF_CARD_EXCEPT_ADD](SN_PREF_CARD_EXCEPT_ADD.md) | `ITEM_ID` |
| [SN_PREF_CARD_EXCEPT_REMOVE](SN_PREF_CARD_EXCEPT_REMOVE.md) | `ITEM_ID` |
| [SN_PREF_CARD_ITEM](SN_PREF_CARD_ITEM.md) | `ITEM_ID` |
| [STANDARDIZED_PHA_DOSE](STANDARDIZED_PHA_DOSE.md) | `ITEM_ID` |
| [STORED_AT](STORED_AT.md) | `ITEM_ID` |
| [TEMPLATE_NONFORMULARY](TEMPLATE_NONFORMULARY.md) | `SHELL_ITEM_ID` |

