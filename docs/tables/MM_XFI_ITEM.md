# MM_XFI_ITEM

> Intermediate inbound interface table for importing an item. Data is moved from this table to the following tables: ITEM_DEFINITION, ITEM_MASTER,OBJECT_IDENTIFIER, IDENTIFIER, OBJECT_IDENTIFIER_INDEX

**Description:** MM XFI ITEM  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 133  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Action flag for the type of action to take |
| 2 | `ACTIVATE_ITEM_IND` | DOUBLE |  |  | Indicator used to determine if the item should be reactivated if it is currently inactive. 0 = Do not reactivate, 1= reactivate item |
| 3 | `ADDITIONAL_AMOUNT_ACTION_FLAG` | DOUBLE | NOT NULL |  | This flag indicates whether to create, update, or delete the additional amount of an item. |
| 4 | `ADDITIONAL_AMOUNT_TYPE` | VARCHAR(40) | NOT NULL |  | Contains the display, description or CDF_Meaning for additional amount_type_cd |
| 5 | `ADDITIONAL_AMOUNT_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for additional amount |
| 6 | `BASE_PKG_CONV` | DOUBLE |  |  | Base Package Qty. It is always assumed to be "1". |
| 7 | `BASE_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The primary key for the base package type. |
| 8 | `BASE_PKG_UOM` | VARCHAR(40) |  |  | The unit-of-measure for the base package type. |
| 9 | `BASE_PKG_UOM_CD` | DOUBLE | NOT NULL |  | The code value for the base pkg type unit-of-measure. |
| 10 | `BATCH_GROUP_ID` | DOUBLE |  | FK→ | Grouper TRANSACTION_ID for a set of MM_XFI_ITEM rows in order to perform batch processing on a subset of rows. |
| 11 | `BATCH_REF` | VARCHAR(100) |  |  | This is a user defined field; allows a reference number/string to be passed in as part of an interface. |
| 12 | `CHARGEABLE_IND` | DOUBLE | NOT NULL |  | Indicates whether the item is chargeable or not. |
| 13 | `CHARGE_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | The category of the charge for the item. This identifier would be utilized by the charge services team on the price schedule setup to charge the item. |
| 14 | `CHARGE_NUMBER_TXT` | VARCHAR(40) | NOT NULL |  | Additional identifier for the item. Used by the charge services team on the price schedule setup. |
| 15 | `CLASS_INSTANCE_CD` | DOUBLE | NOT NULL |  | The code value for this particular instance of a classification. |
| 16 | `CLASS_INSTANCE_MEAN` | VARCHAR(50) | NOT NULL |  | The Type of Class Instance and stores the cdf_meaning value of class. |
| 17 | `CLASS_NODE_DESC` | VARCHAR(100) | NOT NULL |  | The description of the Class. |
| 18 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | The class node for this item |
| 19 | `CLASS_RELTN_ACTION_FLAG` | DOUBLE | NOT NULL |  | Stores the type of relation between class and item.0 - No relation Action; 1 - Create class relation; 3 - Update class relation; 5 - Delete class relation |
| 20 | `COMPONENT_IND` | DOUBLE |  |  | Indicates whether or not this item contains components. From ITEM_DEFINITION |
| 21 | `CONTRIBUTOR` | VARCHAR(40) |  |  | This indicates the Contributor Source to be used for code value aliasing. |
| 22 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | The code value for the contributor that was passed in. |
| 23 | `COST_CENTER` | VARCHAR(40) |  |  | Cost center value |
| 24 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The Code Value of the cost center associated with the item. |
| 25 | `COUNTABLE_IND` | DOUBLE |  |  | Countable Indicator. |
| 26 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 27 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted |
| 28 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 29 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 30 | `CRITICAL_IND` | DOUBLE |  |  | Indicates if this item is critical in order for a procedure to be performed. From ITEM_MASTER |
| 31 | `EQUIPMENT_IND` | DOUBLE |  |  | Indicates if this item is a piece of equipment. |
| 32 | `EXTERNAL_REF_IDENT` | VARCHAR(15) |  |  | Stores the external ERP's batch identification; |
| 33 | `FDA_REPORTABLE_IND` | DOUBLE |  |  | Indicates this item is reportable to the FDA. From ITEM_MASTER |
| 34 | `IMPLANT_TYPE_CD` | DOUBLE | NOT NULL |  | If this item is an implant, indicates the type of implant. |
| 35 | `IMPLANT_TYPE_TXT` | VARCHAR(100) |  |  | If this item is an implant, contains the textual description of the implant type. |
| 36 | `ITEM_ALIAS` | VARCHAR(40) |  |  | The name the item is known by outside of Millennium. |
| 37 | `ITEM_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Item Alias Identifier. |
| 38 | `ITEM_CLINICAL_DESC` | VARCHAR(255) |  |  | The clinical description for the item |
| 39 | `ITEM_CLINICAL_DESC_ID` | DOUBLE | NOT NULL | FK→ | Reference to the IDENTIFIER table where the clinical description of the item is stored. |
| 40 | `ITEM_DESC` | VARCHAR(255) |  |  | Item Description Identifier. |
| 41 | `ITEM_DESC_ID` | DOUBLE | NOT NULL | FK→ | %Descritio |
| 42 | `ITEM_IDENTIFIER` | VARCHAR(255) |  |  | A string value that will be resolved to an Item in Millennium. |
| 43 | `ITEM_IDENTIFIER_TYPE` | VARCHAR(40) |  |  | This is a string that will be converted to a corresponding code value. For example, if "Item Number" is entered, then item_identifier_type_cd will be resolved to a code value with CDF meaning = "Item Number". |
| 44 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Item Identifier Type CD. |
| 45 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Item Master ID. |
| 46 | `ITEM_NBR` | VARCHAR(255) |  |  | Item Number Identifier. |
| 47 | `ITEM_NBR_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Item Number. |
| 48 | `ITEM_ORG_RELTN_FLAG` | DOUBLE | NOT NULL |  | Identifies the action necessary for relating the item to an organization. |
| 49 | `ITEM_SHORT_DESC` | VARCHAR(255) |  |  | Item Short Description Identifier. |
| 50 | `ITEM_SHORT_DESC_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Item Short Description. |
| 51 | `LATEX_IND` | DOUBLE |  |  | Indicator which specifies whether the item is latex or not. |
| 52 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 53 | `LOT_TRACKING_IND` | DOUBLE | NOT NULL |  | Indicates if the item quantity is tracked at lot level. |
| 54 | `MAX_TEMP_AMT_TXT` | VARCHAR(50) | NOT NULL |  | %tempratur |
| 55 | `MFR` | VARCHAR(60) |  |  | Manufacturer Name |
| 56 | `MFR_CD` | DOUBLE | NOT NULL |  | The manufacturer of the item. From the MANUFACTURER_ITEM table. |
| 57 | `MFR_ITEM_BRAND_NAME` | VARCHAR(255) |  |  | Manufacturer Item Brand Name Identifier. |
| 58 | `MFR_ITEM_BRAND_NAME_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Manufacturer Item Brand Name. |
| 59 | `MFR_ITEM_DESC` | VARCHAR(255) |  |  | Manufacturer Item Description Identifier. |
| 60 | `MFR_ITEM_DESC_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Manufacturer Item Description Identifier. |
| 61 | `MFR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Manufacturer Item ID. |
| 62 | `MFR_ITEM_NBR` | VARCHAR(40) |  |  | Manufacturer Item Number Identifier. |
| 63 | `MFR_ITEM_NBR_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Manufacturer Item Number Identifier. |
| 64 | `MFR_ITEM_TRADE_NAME` | VARCHAR(255) |  |  | Manufacturer Item Trade Name Identifier. |
| 65 | `MFR_ITEM_TRADE_NAME_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Manufacturer Item Trade Name Identifier. |
| 66 | `MIN_TEMP_AMT_TXT` | VARCHAR(50) | NOT NULL |  | %tempratur |
| 67 | `MULTI_LOT_TRANSFER_IND` | DOUBLE | NOT NULL |  | Indicates if the a transfer is for one lot or multiple lots. 0 - single lot, 1 - multiple lots |
| 68 | `ORGANIZATION` | VARCHAR(100) | NOT NULL |  | Free text organization name |
| 69 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization associated to the price. |
| 70 | `PKG_TYPE_ACTION_FLAG` | DOUBLE |  |  | Package Action Flag. Defaults to 2. |
| 71 | `PKG_TYPE_CONV` | DOUBLE |  |  | Package Type Qty. |
| 72 | `PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The primary key for the Package Type |
| 73 | `PKG_TYPE_UOM` | VARCHAR(40) |  |  | The unit-of-measure for the Package Type. |
| 74 | `PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | The code value for the package type unit-of-measure. |
| 75 | `PRE_EXP_DATE_PERIOD_NBR` | DOUBLE | NOT NULL |  | When to alert the user that the product should be used before expiring. |
| 76 | `PRE_EXP_DATE_UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure associated to PRE_EXP_DATE_PERIOD_NBR. |
| 77 | `PRE_EXP_DATE_UOM_TXT` | VARCHAR(40) |  |  | Text value of unit of measure. |
| 78 | `PRICE` | DOUBLE |  |  | Price for the Vendor Item package type. |
| 79 | `PRICE_CONTRACT_DESC` | VARCHAR(100) |  |  | A free text description field that may be used to describe the associated contract. From ITEM_PRICE |
| 80 | `PRICE_EFF_DT_TM` | DATETIME |  |  | Date & Time when that Price will be Effective . |
| 81 | `PRICE_EXP_DT_TM` | DATETIME |  |  | Date & Time when that Price will be Expired. |
| 82 | `PRICE_ID` | DOUBLE | NOT NULL | FK→ | The primary key for the price.. |
| 83 | `PRICE_RULE_FLAG` | DOUBLE |  |  | Price Rule Flag value |
| 84 | `PRICE_TYPE` | VARCHAR(40) |  |  | Price Type value. |
| 85 | `PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | Price Type Code Value. |
| 86 | `PROCESS_FLAG` | DOUBLE |  |  | Defines the state of the row in the upload process. |
| 87 | `QUICKADD_IND` | DOUBLE |  |  | % proces % |
| 88 | `RELATION_ACTION_FLAG` | DOUBLE |  |  | Used to create/delete the relationship between item master and its vendor and manufacturer item. |
| 89 | `REPLACEMENT_UPN` | VARCHAR(40) |  |  | Replacement UPN Identifier. |
| 90 | `REPLACEMENT_UPN_ID` | DOUBLE | NOT NULL | FK→ | %Replacmen |
| 91 | `REUSABLE_IND` | DOUBLE |  |  | Indicates if this item is reusable or disposable. |
| 92 | `SAFETY_CHECK_IND` | DOUBLE |  |  | Does this item require a safety check prior to use? Yes/No |
| 93 | `SCHEDUABLE_IND` | DOUBLE |  |  | Indicates that this item can be scheduled as a resource from the scheduling application. |
| 94 | `SEGMENT_IDENTIFIER` | VARCHAR(10) |  |  | Indicates the upload type (item upload, item location upload, etc.) |
| 95 | `SEGMENT_VERSION` | VARCHAR(10) |  |  | The version of the upload. |
| 96 | `SHELF_LIFE` | DOUBLE |  |  | Shelf Life of an Item. |
| 97 | `SHELF_LIFE_UOM` | VARCHAR(40) |  |  | The unit of measure for the shelf life. |
| 98 | `SHELF_LIFE_UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure code value for the Shelf Life. |
| 99 | `STERILIZATION_REQUIRED_IND` | DOUBLE |  |  | Indicates if this item needs sterilization prior to use. From ITEM_MASTER. |
| 100 | `STORAGE_REQUIREMENT` | VARCHAR(40) |  |  | Describes how to store an item. From code set 11020. |
| 101 | `STORAGE_REQUIREMENT_CD` | DOUBLE | NOT NULL |  | The code value for the Storage Requirement. |
| 102 | `SUBSTITUTION_IND` | DOUBLE |  |  | Indicator which specifies whether the item is under substitution. |
| 103 | `SUB_ACCOUNT` | VARCHAR(40) |  |  | Identifies, along with cost_center, which department in the organization is incurring the expense. |
| 104 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The number of the sub account. |
| 105 | `TAX_VALUE` | DOUBLE | NOT NULL |  | The percent or amount value for the tax |
| 106 | `TAX_VALUE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the tax value is a percentage or fixed amount |
| 107 | `TEMP_UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure the temperature columns represent. |
| 108 | `TEMP_UOM_TXT` | VARCHAR(100) |  |  | The unit of measure the temperature columns represent. |
| 109 | `TRACK_COMPONENT_USAGE_IND` | DOUBLE |  |  | Defines whether or not usage is captured for each component in a pack/set. From ITEM_DEFINITION |
| 110 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Unique,generated number that identifies a single row on the MM_XFI_ITEM table. |
| 111 | `UDI_EXP_DATE_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by expiration date |
| 112 | `UDI_LOT_NBR_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by lot number |
| 113 | `UDI_MFR_DATE_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by manufacturer date |
| 114 | `UDI_SERIAL_NBR_IND` | DOUBLE | NOT NULL |  | Indicates whether the UDI is tracked by serial number |
| 115 | `UPDATE_RULE_FLAG` | DOUBLE |  |  | Update Rule Flag. (For Future Use) |
| 116 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 117 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 118 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 119 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 120 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 121 | `UPN` | VARCHAR(40) |  |  | UPN Identifier. |
| 122 | `UPN_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the UPN. |
| 123 | `UPN_SALABLE_BY_DIST_IND` | DOUBLE |  |  | Indicates whether or not this UPN specific item & package is salable by the vendor. From IDENTIFIER |
| 124 | `UPN_SALABLE_BY_MFR_IND` | DOUBLE |  |  | Indicates whether or not this UPN specific item & package is salable by the manufacturer. From IDENTIFIER |
| 125 | `USAGE_UOM_CD` | DOUBLE | NOT NULL |  | Holds CD value for the usage unit of measurement text. |
| 126 | `USAGE_UOM_TXT` | VARCHAR(250) |  |  | Holds the usage unit of measurement text |
| 127 | `VENDOR` | VARCHAR(60) |  |  | Name of the vendor for this item. |
| 128 | `VENDOR_CD` | DOUBLE | NOT NULL |  | The code value for the Vendor. |
| 129 | `VENDOR_ITEM_DESC` | VARCHAR(255) |  |  | Vendor Item Description Identifier. |
| 130 | `VENDOR_ITEM_DESC_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Vendor Item Description. |
| 131 | `VENDOR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key for the Vendor Item |
| 132 | `VENDOR_ITEM_NBR` | VARCHAR(40) |  |  | Vendor Item Number Identifier. |
| 133 | `VENDOR_ITEM_NBR_ID` | DOUBLE | NOT NULL | FK→ | Identifier ID for the Vendor Item Number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BASE_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `BATCH_GROUP_ID` | [MM_XFI_ITEM](MM_XFI_ITEM.md) | `TRANSACTION_ID` |
| `CHARGE_NUMBER_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `ITEM_ALIAS_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `ITEM_CLINICAL_DESC_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `ITEM_DESC_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `ITEM_MASTER_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `ITEM_NBR_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `ITEM_SHORT_DESC_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `MFR_ITEM_BRAND_NAME_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `MFR_ITEM_DESC_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `MFR_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MFR_ITEM_NBR_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `MFR_ITEM_TRADE_NAME_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PRICE_ID` | [ITEM_PRICE](ITEM_PRICE.md) | `ITEM_PRICE_ID` |
| `REPLACEMENT_UPN_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `UPN_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `VENDOR_ITEM_DESC_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `VENDOR_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `VENDOR_ITEM_NBR_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `BATCH_GROUP_ID` |
| [MM_XFI_ITEM_BATCH](MM_XFI_ITEM_BATCH.md) | `BATCH_GROUP_ID` |

