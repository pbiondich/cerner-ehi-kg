# LINE_ITEM_QUANTITY

> Quantity for a line item

**Description:** LINE ITEM QUANTITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_PKG_TYPE_DESC` | VARCHAR(100) |  |  | Vendors package description |
| 2 | `BASE_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to package_type |
| 3 | `BASE_PKG_TYPE_QTY` | DOUBLE |  |  | Quantity of the package type in base units |
| 4 | `BASE_PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | Package type unit of measure |
| 5 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 8 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 9 | `EXTENDED_AMOUNT` | DOUBLE |  |  | The total dollar amount ( qty X unit price ). |
| 10 | `EXTENDED_PRICE` | DOUBLE |  |  | The price multiplied by the quantity. |
| 11 | `ITEM_PRICE_ID` | DOUBLE | NOT NULL |  | Foreign key to item_price table |
| 12 | `LINE_ITEM_QTY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of quantity this row refers to |
| 13 | `PACKAGE_TYPE_DESC` | VARCHAR(100) |  |  | Package type description |
| 14 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to package type table |
| 15 | `PACKAGE_TYPE_PRICE` | DOUBLE |  |  | Price of the item |
| 16 | `PACKAGE_TYPE_QTY` | DOUBLE |  |  | The quantity of base packages contained in this package. For example, if this item comes packed individually, a box might contain multiple individual packages. |
| 17 | `PACKAGE_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | Unit of measure for this package |
| 18 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key to a table designated by parent_entity_name |
| 19 | `PARENT_ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | Defines the parent table for parent_entity_id |
| 20 | `PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | Type of price code value |
| 21 | `QTY` | DOUBLE | NOT NULL |  | Quantity value |
| 22 | `REASON_CD` | DOUBLE | NOT NULL |  | No fill reason |
| 23 | `SEL_PKG_TYPE_DESC` | VARCHAR(100) |  |  | Description of the package type that the user selected. |
| 24 | `SEL_PKG_TYPE_ID` | DOUBLE | NOT NULL |  | The internal id of the package |
| 25 | `SEL_PKG_TYPE_QTY` | DOUBLE |  |  | The quantity in base units of the package type the user selected. |
| 26 | `SEL_PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | The uom code value of the package type the user selected. |
| 27 | `TO_PKG_TYPE_DESC` | VARCHAR(100) |  |  | To Package Type Description |
| 28 | `TO_PKG_TYPE_ID` | DOUBLE | NOT NULL |  | To Package Type Id |
| 29 | `TO_PKG_TYPE_QTY` | DOUBLE |  |  | To Package Type Quantity |
| 30 | `TO_PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | To Package Type UoM Cd |
| 31 | `UNIT_TAX` | DOUBLE |  |  | Unit Tax for the Line Item |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `VEND_SHIP_DT_TM` | DATETIME |  |  | Vendor Ship Date/Time |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BASE_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

