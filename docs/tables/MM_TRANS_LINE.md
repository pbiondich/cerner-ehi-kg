# MM_TRANS_LINE

> MM Trans Line Table

**Description:** MM Transaction Line  
**Table type:** ACTIVITY  
**Primary key:** `MM_TRANS_LINE_ID`  
**Columns:** 127  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_FROM_PKG_TYPE_ID` | DOUBLE | NOT NULL |  | ACTUAL PACKAGE TYPE passed for FROM LOCATION. column |
| 2 | `ACTUAL_FROM_QTY_UNIT_COST` | DOUBLE |  |  | ACTUAL UNIT COST for the PACKAGE TYPE passed for FROM LOCATION. column |
| 3 | `ACTUAL_FROM_TRANS_QTY` | DOUBLE |  |  | ACTUAL QUANTITY of packages passed for FROM LOCATION. column |
| 4 | `ACTUAL_TO_PKG_TYPE_ID` | DOUBLE | NOT NULL |  | ACTUAL PACKAGE TYPE passed for TO LOCATION. column |
| 5 | `ACTUAL_TO_TRANS_QTY` | DOUBLE |  |  | ACTUAL QUANTITY of packages passed for TO LOCATION. column |
| 6 | `BASE_PKG_DESC` | VARCHAR(100) |  |  | Description of base package type column |
| 7 | `BASE_PKG_QTY` | DOUBLE |  |  | Base package type quantity column |
| 8 | `BASE_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to package type column |
| 9 | `BASE_PKG_UOM_CD` | DOUBLE | NOT NULL |  | Base package type unit of measure code value column |
| 10 | `BASE_PKG_UOM_DESC` | VARCHAR(60) |  |  | Base package type unit of measure description column |
| 11 | `BASE_PKG_UOM_DISP` | VARCHAR(40) |  |  | Base package type unit of measure display column |
| 12 | `BASE_QTY` | DOUBLE |  |  | The transaction quantity expressed in base units column |
| 13 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | batch identifier value column |
| 14 | `BATCH_SUBMIT_DT_TM` | DATETIME |  |  | identifies the date and time that the batch was submitted to FSI column |
| 15 | `BILL_ONLY_IND` | DOUBLE |  |  | Bill Only Indicator column |
| 16 | `CONSIGN_IND` | DOUBLE |  |  | If 1, then the item is consigned either at from location or to location. column |
| 17 | `CONSIGN_PROCESS_FLAG` | DOUBLE |  |  | If 1, then it means that the line is already been processed and an extract is already been created for that transaction line. For now, we are NOT USING this flag. column |
| 18 | `CONTROL_NBR` | VARCHAR(40) |  |  | The items control number column |
| 19 | `COST_OVERRIDE_IND` | DOUBLE |  |  | If 1, the user manually entered a cost instead of accepting the default. column |
| 20 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row column |
| 21 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. column |
| 22 | `CREATE_ID` | DOUBLE | NOT NULL |  | User id of person which created this row column |
| 23 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row column |
| 24 | `DB_AVG_COST` | DOUBLE |  |  | The difference between old average cost and new average cost. column |
| 25 | `DB_LAST_COST` | DOUBLE |  |  | The difference between old last cost and new last cost. column |
| 26 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. column |
| 27 | `FROM_AVERAGE_COST_NEW` | DOUBLE |  |  | The new average cost for the "from" location column |
| 28 | `FROM_AVERAGE_COST_OLD` | DOUBLE |  |  | The old average cost for the "from" location column |
| 29 | `FROM_LAST_COST_NEW` | DOUBLE |  |  | The from locations new last-cost column |
| 30 | `FROM_LAST_COST_OLD` | DOUBLE |  |  | The from locations old last-cost column |
| 31 | `FROM_LOCATION_CD` | DOUBLE | NOT NULL |  | The From location"s code value column |
| 32 | `FROM_LOCATION_DESC` | VARCHAR(60) |  |  | The From locations description column |
| 33 | `FROM_LOCATION_DISP` | VARCHAR(40) |  |  | The From locations display column |
| 34 | `FROM_LOCATOR_CD` | DOUBLE | NOT NULL |  | locator column |
| 35 | `FROM_LOCATOR_DESC` | VARCHAR(60) |  |  | locator description column |
| 36 | `FROM_LOCATOR_DISP` | CHAR(40) |  |  | Locator Display column |
| 37 | `FROM_PKG_DESC` | VARCHAR(100) |  |  | The From locations package description column |
| 38 | `FROM_PKG_QTY` | DOUBLE |  |  | Quantity of the From Package Type. column |
| 39 | `FROM_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | ID value of the From Package Type column |
| 40 | `FROM_PKG_UOM_CD` | DOUBLE | NOT NULL |  | From package type unit of measure code value column |
| 41 | `FROM_PKG_UOM_DESC` | VARCHAR(60) |  |  | From package type unit of measure description column |
| 42 | `FROM_PKG_UOM_DISP` | VARCHAR(40) |  |  | From package type unit of measure display column |
| 43 | `FROM_QOH_NEW` | DOUBLE |  |  | New Quantity of Hand at From Location column |
| 44 | `FROM_QOH_OLD` | DOUBLE |  |  | Old Quantity of Hand at From Location column |
| 45 | `FROM_QOH_TYPE_CD` | DOUBLE | NOT NULL |  | Quantity of Hand Type Code Value at From Location column |
| 46 | `FROM_QOH_TYPE_DESC` | VARCHAR(60) |  |  | Quantity of Hand Type Description at From Location column |
| 47 | `FROM_QOH_TYPE_DISP` | VARCHAR(40) |  |  | Quantity of Hand Type Display at From Location column |
| 48 | `FROM_QTY_UNIT_COST` | DOUBLE |  |  | Each unit cost of the From Qty. column |
| 49 | `FROM_TRANS_QTY` | DOUBLE |  |  | From Transaction Quantity column |
| 50 | `HOLD_IND` | DOUBLE |  |  | Hold Indicator column |
| 51 | `IMPACT_USAGE_IND` | DOUBLE |  |  | Impact Usage Indicator column |
| 52 | `INIT_DISP_TRANS_LINE_ID` | DOUBLE | NOT NULL | FK→ | In POU workflow, if the user does a return or waste transaction against a dispensed item, this column will store the transaction id of initial dispensed row |
| 53 | `ITEM_DESC` | VARCHAR(255) |  |  | Item Description column |
| 54 | `ITEM_DESC_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item Description column |
| 55 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item column |
| 56 | `ITEM_NBR` | VARCHAR(255) |  |  | Item Number column |
| 57 | `ITEM_NBR_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item Number column |
| 58 | `ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | Item Type Code Value column |
| 59 | `ITEM_TYPE_DESC` | VARCHAR(60) |  |  | Item Type Description column |
| 60 | `ITEM_TYPE_DISP` | VARCHAR(40) |  |  | Item Type Display column |
| 61 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the line_item table. column |
| 62 | `LOT_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier from the tables that appear in column parent_entity_name. |
| 63 | `LOT_PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The uppercase name of the table to which this row is related. |
| 64 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | In POU workflow, if the user dispenses an item, this field will hold the manufacturer cd of the dispensed item. |
| 65 | `MFR_CATALOG_NBR_ID` | DOUBLE | NOT NULL | FK→ | To store identifier_id of dispensed manufacturer catalog number. |
| 66 | `MFR_CATALOG_NBR_TXT` | VARCHAR(200) |  |  | In POU workflow, if the user dispenses an item, this field will hold the manufacturer catalog number of the dispensed item. |
| 67 | `MISC_CODE` | VARCHAR(40) |  |  | Misc. Code column |
| 68 | `MM_PROJECT_NBR_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | The project for this transaction line. |
| 69 | `MM_TRANS_LINE_ID` | DOUBLE | NOT NULL | PK | Transaction Line ID column |
| 70 | `OFFSET_LOCATION_CD` | DOUBLE | NOT NULL |  | This location, if specified, will be used to determine the offsetting cost center and subaccount for the specified transaction. |
| 71 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the person table. column |
| 72 | `PCB_AVG_COST` | DOUBLE |  |  | The percent change between old average cost and new average cost. column |
| 73 | `PCB_LAST_COST` | DOUBLE |  |  | The percent change between old last cost and new last cost. column |
| 74 | `PERFORMING_LOC_CD` | DOUBLE | NOT NULL | FK→ | In POU workflow, the user can dispense an item from a fill location to a performing location. This column is used to record the performing location to which the supply item is supplied to. |
| 75 | `PO_LINE_NBR` | DOUBLE |  |  | PO Line Number column |
| 76 | `PRICE_CHANGED_QTY` | DOUBLE |  |  | Price Changed Quantity. column |
| 77 | `PRICE_COST_NEW` | DOUBLE |  |  | New Price Cost. column |
| 78 | `PRICE_COST_OLD` | DOUBLE |  |  | Old Price Cost. column |
| 79 | `PRICE_ORIGINAL_TRANS_DT_TM` | DATETIME |  |  | Price Original Transaction Date. column |
| 80 | `PRICE_ORIGINAL_TRANS_ID` | DOUBLE | NOT NULL | FK→ | x column |
| 81 | `PRICE_PO_ID` | DOUBLE | NOT NULL |  | x column |
| 82 | `PRICE_PO_NBR` | VARCHAR(40) |  |  | x column |
| 83 | `PRICE_VENDOR_CD` | DOUBLE | NOT NULL |  | Price Vendor Code Value column |
| 84 | `PRICE_VENDOR_DESC` | VARCHAR(60) |  |  | Price Vendor Description column |
| 85 | `PRICE_VENDOR_DISP` | VARCHAR(40) |  |  | Price Vendor Display column |
| 86 | `PROJECT_CODE_CD` | DOUBLE | NOT NULL |  | Project Code Value column |
| 87 | `PROJECT_CODE_DESC` | VARCHAR(60) |  |  | Project Code Description column |
| 88 | `PROJECT_CODE_DISP` | VARCHAR(40) |  |  | Project Code Display column |
| 89 | `QOH_FLAG` | DOUBLE | NOT NULL |  | This flag will determine which solution is updating the quantity on hand record. column |
| 90 | `REASON_CD` | DOUBLE | NOT NULL |  | Reason Code Value column |
| 91 | `REASON_DESC` | VARCHAR(60) |  |  | Reason Description column |
| 92 | `REASON_DISP` | VARCHAR(40) |  |  | Reason Display column |
| 93 | `RECEIPT_LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to receipt_line_item table column |
| 94 | `REQ_LINE_NBR` | DOUBLE |  |  | Requisition Line Number column |
| 95 | `SCANNED_ITEM_BARCODE` | VARCHAR(255) |  |  | Barcode text that is scanned to identify the item. |
| 96 | `TO_AVERAGE_COST_NEW` | DOUBLE |  |  | New To Average Cost column |
| 97 | `TO_AVERAGE_COST_OLD` | DOUBLE |  |  | Old To Average Cost column |
| 98 | `TO_LAST_COST_NEW` | DOUBLE |  |  | New To Last Cost column |
| 99 | `TO_LAST_COST_OLD` | DOUBLE |  |  | Old To Last Cost column |
| 100 | `TO_LOCATION_CD` | DOUBLE | NOT NULL |  | To Location Code Value column |
| 101 | `TO_LOCATION_DESC` | VARCHAR(60) |  |  | To Location Code Description column |
| 102 | `TO_LOCATION_DISP` | VARCHAR(40) |  |  | To Location Code Display column |
| 103 | `TO_LOCATOR_CD` | DOUBLE | NOT NULL |  | To Locator Code Value column |
| 104 | `TO_LOCATOR_DESC` | VARCHAR(60) |  |  | To Locator Description column |
| 105 | `TO_LOCATOR_DISP` | VARCHAR(40) |  |  | To Locator Display column |
| 106 | `TO_PKG_DESC` | VARCHAR(100) |  |  | To Package Type Description column |
| 107 | `TO_PKG_QTY` | DOUBLE |  |  | To Package Type Quantity column |
| 108 | `TO_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | To Package Type ID column |
| 109 | `TO_PKG_UOM_CD` | DOUBLE | NOT NULL |  | To package type unit of measure code value column |
| 110 | `TO_PKG_UOM_DESC` | VARCHAR(60) |  |  | To package type unit of measure description column |
| 111 | `TO_PKG_UOM_DISP` | VARCHAR(40) |  |  | To package type unit of measure display column |
| 112 | `TO_QOH_NEW` | DOUBLE |  |  | New Quantity of Hand at To Location column |
| 113 | `TO_QOH_OLD` | DOUBLE |  |  | Old Quantity of Hand at To Location column |
| 114 | `TO_QOH_TYPE_CD` | DOUBLE | NOT NULL |  | Quantity of Hand Type Code Value at To Location column |
| 115 | `TO_QOH_TYPE_DESC` | VARCHAR(60) |  |  | Quantity of Hand Type Description at To Location column |
| 116 | `TO_QOH_TYPE_DISP` | VARCHAR(40) |  |  | Quantity of Hand Type Display at To Location column |
| 117 | `TO_QTY_UNIT_COST` | DOUBLE |  |  | Each unit cost of theTo Qty. column |
| 118 | `TO_TRANS_QTY` | DOUBLE |  |  | To Transaction Quantity column |
| 119 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | ID value of the Transaction column |
| 120 | `TRANSFER_FLAG` | DOUBLE | NOT NULL |  | Used to determine whether an average cost is calculated at the fill location. |
| 121 | `TRANS_PARENT_TRANS_ID` | DOUBLE | NOT NULL |  | Transaction Id column |
| 122 | `TRANS_STATUS_CD` | DOUBLE | NOT NULL |  | Code which specifies the status of the transaction. column |
| 123 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 124 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 125 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 126 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 127 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BASE_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `BATCH_ID` | [SI_BATCH](SI_BATCH.md) | `BATCH_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FROM_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `INIT_DISP_TRANS_LINE_ID` | [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MM_TRANS_LINE_ID` |
| `ITEM_DESC_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `ITEM_NBR_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |
| `MFR_CATALOG_NBR_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `MM_PROJECT_NBR_TRACKING_ID` | [MM_PROJECT_NBR_TRACKING](MM_PROJECT_NBR_TRACKING.md) | `MM_PROJECT_NBR_TRACKING_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERFORMING_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PRICE_ORIGINAL_TRANS_ID` | [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MM_TRANS_LINE_ID` |
| `RECEIPT_LINE_ITEM_ID` | [RECEIPT_LINE_ITEM](RECEIPT_LINE_ITEM.md) | `RECEIPT_LINE_ITEM_ID` |
| `TO_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [MM_INSTANCE_TRANS_LINE_R](MM_INSTANCE_TRANS_LINE_R.md) | `MM_TRANS_LINE_ID` |
| [MM_TRANS_ERROR_LOG](MM_TRANS_ERROR_LOG.md) | `MM_TRANS_LINE_ID` |
| [MM_TRANS_GL](MM_TRANS_GL.md) | `MM_TRANS_LINE_ID` |
| [MM_TRANS_IDENTIFIER_RELTN](MM_TRANS_IDENTIFIER_RELTN.md) | `MM_TRANS_LINE_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `INIT_DISP_TRANS_LINE_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `PRICE_ORIGINAL_TRANS_ID` |

