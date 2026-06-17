# MM_XFI_ITEMLOC

> Interface Item Location table. Data is moved from this table to these tables: ITEM_CONTROL_INFO, AQUIREMENT_INFO, QUANTITY_REQUIREMENTS, STORED_AT

**Description:** Interface Item Location  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 80

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABC_CLASS` | CHAR(1) |  |  | The ABC classification for this item at this location. |
| 2 | `ABC_CLASS_CD` | DOUBLE | NOT NULL |  | The ABC classification for this item at this location. |
| 3 | `ACC_STOCKOUT_FREQ` | DOUBLE |  |  | The acceptable stockout frequency which is allowed at this location |
| 4 | `ACTION_FLAG` | DOUBLE |  |  | Action flag for the action |
| 5 | `AVG_DAILY_USAGE` | DOUBLE |  |  | The average quantity utilized for the item/location |
| 6 | `AVG_LEAD_TIME` | DOUBLE |  |  | The average number of days it takes the vendor to ship the item |
| 7 | `AVG_WEEKS_ORDER_QTY` | DOUBLE |  |  | %Avearge% |
| 8 | `BATCH_REF` | VARCHAR(100) |  |  | The batch reference for the upload |
| 9 | `CONSIGNMENT_IND` | DOUBLE |  |  | Indicator utilized to depict if the item is stored as consignment at the location |
| 10 | `CONTRIBUTOR` | VARCHAR(40) |  |  | Foreign contributor can be the foreign system name if being used as an interface |
| 11 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | The foreign contributor for the item/location upload. |
| 12 | `COST_CENTER` | VARCHAR(40) |  |  | The cost center associated with the item. |
| 13 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The cost center associated with the item. |
| 14 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted |
| 16 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert of the row in the table. |
| 17 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 18 | `ECONOMIC_ORDER_QTY` | DOUBLE |  |  | The economic order quantity for the item at this location |
| 19 | `FILL_LOCATION_CD` | DOUBLE | NOT NULL |  | The location where the item will be replenished (filled) from. |
| 20 | `FILL_LOCATION_NAME` | VARCHAR(100) |  |  | The name of the location where the item will be replenished (filled) from. |
| 21 | `FIXED_ORDER_QTY` | DOUBLE | NOT NULL |  | %Replemish |
| 22 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item |
| 23 | `ITEM_IDENTIFIER` | VARCHAR(255) |  |  | Identifier used to resolve to an item in millennium |
| 24 | `ITEM_IDENTIFIER_TYPE` | VARCHAR(40) |  |  | The type of identifier being resolved too |
| 25 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Item Identifier Type CD |
| 26 | `LOCATION` | VARCHAR(100) |  |  | Location where the item exists. |
| 27 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location the item is being assigned |
| 28 | `LOCATOR_QTY` | DOUBLE | NOT NULL |  | The quantity that can be stored in an individual locator. |
| 29 | `LOCATOR_TYPE` | VARCHAR(40) | NOT NULL |  | Free text description of the type of locator where the item is being stored. |
| 30 | `LOCATOR_TYPE_CD` | DOUBLE | NOT NULL |  | The type of locator where the item is being stored. |
| 31 | `LOCK_IND` | DOUBLE | NOT NULL |  | Indicator used to determine if the item can be removed from the location. this only applies to RxStation locations. |
| 32 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 33 | `LOT_TRACKING_LEVEL` | VARCHAR(40) |  |  | The level at which lots are tracked at this location. |
| 34 | `LOT_TRACKING_LEVEL_CD` | DOUBLE | NOT NULL |  | The level at which lots are tracked at this location. |
| 35 | `MAX_DAYS_ADU` | DOUBLE |  |  | Maximum number of days that the average daily usage is based upon |
| 36 | `MAX_LEVEL` | DOUBLE |  |  | Maximum quantity of the item at the location |
| 37 | `MIN_DAYS_ADU` | DOUBLE |  |  | Minimum number of days that the average daily usage is based upon |
| 38 | `MIN_LEVEL` | DOUBLE |  |  | minimum quantity of the item at the location |
| 39 | `ORGANIZATION` | VARCHAR(100) |  |  | The organization for the location |
| 40 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 41 | `PRIMARY_VENDOR` | VARCHAR(100) |  |  | The vendor that this item is usually ordered from. |
| 42 | `PRIMARY_VENDOR_CD` | DOUBLE | NOT NULL |  | The vendor that this item is usually ordered from. |
| 43 | `PRIMARY_VENDOR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Primary vendor item that will be used to order the item |
| 44 | `PRIMARY_VENDOR_ITEM_TXT` | VARCHAR(255) | NOT NULL |  | Primary vendor catalog number for a location that will be used to order the item (text representation of number) |
| 45 | `PROCESS_FLAG` | DOUBLE |  |  | The process flag will reflect the status of the upload record |
| 46 | `PRODUCT_ORIGIN` | VARCHAR(40) |  |  | The free text description of the origin of the product |
| 47 | `PRODUCT_ORIGIN_CD` | DOUBLE | NOT NULL |  | The code value for the origin of the product |
| 48 | `RECALC_METHOD` | VARCHAR(40) |  |  | Method used to calculate reorder quantities |
| 49 | `RECALC_METHOD_CD` | DOUBLE | NOT NULL |  | Method used to calculate reorder quantities |
| 50 | `REORDER_PKG_TYPE_CONV` | DOUBLE |  |  | The reorder package type pack factor |
| 51 | `REORDER_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The primary key for the reorder package type ID |
| 52 | `REORDER_PKG_TYPE_UOM` | VARCHAR(40) |  |  | The free text for the reorder package type unit of measure |
| 53 | `REORDER_PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | The code value for the reorder package type unit of measure |
| 54 | `REORDER_POINT` | DOUBLE |  |  | Quantity when the item will qualify to be reordered |
| 55 | `REPLENISHMENT_TYPE` | VARCHAR(40) |  |  | The free text for the method of replenishment used for this item/location |
| 56 | `REPLENISHMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the method of replenishment used for this item/location |
| 57 | `SAFETY_STOCK_QTY` | DOUBLE |  |  | The quantity of safety stock defined for the item at this location |
| 58 | `SEASONAL_ITEM_IND` | DOUBLE |  |  | Indicator used to determine if the item is considered seasonal |
| 59 | `SEGMENT_IDENTIFIER` | VARCHAR(10) |  |  | The segment identifier of the upload |
| 60 | `SEGMENT_VERSION` | VARCHAR(10) |  |  | The segment version of the upload |
| 61 | `STOCK_PKG_TYPE_CONV` | DOUBLE |  |  | The stock package type pack factor |
| 62 | `STOCK_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The package type in which this item is stocked. |
| 63 | `STOCK_PKG_TYPE_UOM` | VARCHAR(40) |  |  | Free text of the items stock package type |
| 64 | `STOCK_PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | The item's stock package type code value |
| 65 | `STOCK_TYPE_IND` | DOUBLE |  |  | Indicates the stock type for an item. |
| 66 | `SUB_ACCOUNT` | VARCHAR(40) |  |  | Free text of the items sub account |
| 67 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The item's sub account code value |
| 68 | `SYSCALC_ABC_IND` | DOUBLE |  |  | Indicator to determine if the ABC classification will be calculated by the system. |
| 69 | `SYSCALC_EOQ_IND` | DOUBLE |  |  | Indicator to determine if the economic order quantity will be calculated by the system |
| 70 | `SYSCALC_PARLEVEL_IND` | DOUBLE |  |  | Indicator to determine if the PAR level will be calculated by the system |
| 71 | `SYSCALC_REORDER_POINT_IND` | DOUBLE |  |  | Indicator to determine if the reorder point will be calculated by the system |
| 72 | `SYSCALC_SAFETY_STOCK_IND` | DOUBLE |  |  | Indicator to determine if the safety stock will be calculated by the system |
| 73 | `TRACK_INSTANCE_IND` | DOUBLE |  |  | Indicates whether or not this location tracks instances of the item. Stored permanently in ITEM_CONTROL_INFO.INSTANCE_IND. |
| 74 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 75 | `UPDATE_RULE_FLAG` | DOUBLE |  |  | The flag used to determine updating rules |
| 76 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 77 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 78 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 79 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 80 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRIMARY_VENDOR_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `REORDER_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `STOCK_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

