# MM_OMF_ITEMLOC

> This table is exclusively used for ProCure's PowerVision reports.

**Description:** This is a summary table of ITEM_CONTROL_INFO,ACQUIREMENT_INFO, QUANTITY_REQUIRE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 54

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABC_CLASS_CD` | DOUBLE | NOT NULL |  | Item Classification (A, B, C) Code |
| 2 | `ACC_STOCKOUT_FREQ_CD` | DOUBLE | NOT NULL |  | The acceptable stockout frequency which is allowed at this location |
| 3 | `ACQUIRE_UPDT_CNT` | DOUBLE |  |  | The date that acquirement information on this table has been updated. |
| 4 | `AVERAGE_DAILY_USAGE` | DOUBLE |  |  | Average daily usage of the item in the location. |
| 5 | `AVERAGE_LEAD_TIME` | DOUBLE |  |  | The average lead time the vendor requires |
| 6 | `AVERAGE_LEAD_TIME_UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure that applies to the average lead time |
| 7 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | The charge type that applies to the item |
| 8 | `CONSIGNMENT_IND` | DOUBLE |  |  | Indicates whether or not it is a consignment item |
| 9 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code |
| 10 | `COUNTBACK_FLAG` | DOUBLE | NOT NULL |  | Flag used to determine if this item/location requires a physical count once the item has been removed. 0 - no count is required; 1 - Blind counting; 2 - Confirm count |
| 11 | `COUNT_CYCLE_CD` | DOUBLE | NOT NULL |  | The type of cycle counting required for the item |
| 12 | `ECONOMIC_ORDER_QTY` | DOUBLE |  |  | The economic order quantity for the item at this location |
| 13 | `FILL_LOCATION_CD` | DOUBLE | NOT NULL |  | The fill location for the item |
| 14 | `FIXED_ORDER_QTY` | DOUBLE | NOT NULL |  | Replenishment quantity will be created in increments of the fixed order quantity. |
| 15 | `INSTANCE_IND` | DOUBLE |  |  | The indicator to reflect if this is an instance |
| 16 | `ITEM_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 17 | `I_CTRL_UPDT_CNT` | DOUBLE |  |  | The number of times the Item Control information has been updated |
| 18 | `LAST_SYSCALC_DT_TM` | DATETIME |  |  | The last date/time the system calculated item-location information. |
| 19 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location code |
| 20 | `LOCATION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of location |
| 21 | `LOCATOR_QTY` | DOUBLE | NOT NULL |  | The quantity that can be stored in an individual locator. |
| 22 | `LOCATOR_TYPE_CD` | DOUBLE | NOT NULL |  | The type of locator where the item is being stored. |
| 23 | `LOCK_IND` | DOUBLE | NOT NULL |  | Indicator used to determine if the item can be removed from the location. This only applies to RxStation locations. |
| 24 | `LOT_TRACKING_LEVEL_CD` | DOUBLE | NOT NULL |  | The level of lot tracking for the item |
| 25 | `MAXIMUM_LEVEL` | DOUBLE |  |  | Maximum Level of the item that should in the lacation |
| 26 | `MAX_DAYS_ADU` | DOUBLE |  |  | Maximum number of days that the average daily usage is based upon |
| 27 | `MINIMUM_LEVEL` | DOUBLE |  |  | Minimum level of the item that should be in the location |
| 28 | `MIN_DAYS_ADU` | DOUBLE |  |  | Minimum number of days that the average daily usage is based upon |
| 29 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization for the location |
| 30 | `PRIMARY_VENDOR_CD` | DOUBLE | NOT NULL |  | The primary reorder vendor |
| 31 | `PRIMARY_VENDOR_ITEM_ID` | DOUBLE | NOT NULL |  | The primary reorder vendor item |
| 32 | `PRODUCT_ORIGIN_CD` | DOUBLE | NOT NULL |  | The code value for the origin of the product |
| 33 | `QTY_REQ_UPDT_CNT` | DOUBLE |  |  | The number of times the quantity requirement information has been updated |
| 34 | `REORDER_METHOD_CD` | DOUBLE | NOT NULL |  | The reorder method being utilized. |
| 35 | `REORDER_PACKAGE_TYPE_DESC` | VARCHAR(100) |  |  | The reorder package type description |
| 36 | `REORDER_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL |  | The primary key for the reorder package type ID |
| 37 | `REORDER_POINT` | DOUBLE |  |  | The quantity when the item will be reordered |
| 38 | `REORDER_TYPE_CD` | DOUBLE | NOT NULL |  | The reorder type being utilized |
| 39 | `SAFETY_STOCK_QTY` | DOUBLE |  |  | The quantity of safety stock defined for the item at this location |
| 40 | `SEASONAL_ITEM_IND` | DOUBLE |  |  | Indicator used to determine if the item is considered seasonal |
| 41 | `STOCK_PACKAGE_TYPE_DESC` | VARCHAR(100) |  |  | The description of the stock package type |
| 42 | `STOCK_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL |  | StoThe foreign key for the stock package type ID |
| 43 | `STOCK_TYPE_IND` | DOUBLE |  |  | The indicator that reflects whether the item is tracked perpetually at this location |
| 44 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The item's sub account code value |
| 45 | `SYSCALC_ABC_CLASS_IND` | DOUBLE |  |  | Indicator to determine if the ABC classification will be calculated by the system. |
| 46 | `SYSCALC_PAR_LEVEL_IND` | DOUBLE |  |  | Indicator to determine if the PAR level will be calculated by the system |
| 47 | `SYSCALC_REORDER_POINT_IND` | DOUBLE |  |  | Indicator to determine if the reorder point will be calculated by the system |
| 48 | `SYSCALC_SAFETY_STOCK_IND` | DOUBLE |  |  | Indicator to determine if the safety stock will be calculated by the system |
| 49 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 50 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 51 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 52 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 53 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 54 | `VIEW_TYPE_CD` | DOUBLE | NOT NULL |  | The location view type |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

