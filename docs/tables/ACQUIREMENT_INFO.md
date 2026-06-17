# ACQUIREMENT_INFO

> Item / Location relationship that defines how you acquire an item.

**Description:** ACQUIREMENT INFO  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AVERAGE_LEAD_TIME` | DOUBLE |  |  | The average time it takes a vendor to deliver goods. |
| 2 | `AVERAGE_LEAD_TIME_UOM_CD` | DOUBLE | NOT NULL |  | Average Lead Time Unit of Measure |
| 3 | `CONSIGNMENT_IND` | DOUBLE |  |  | Consignment indicator |
| 4 | `ECONOMIC_ORDER_QTY` | DOUBLE |  |  | The quantity that is economically feasible to reorder from the vendor. |
| 5 | `FILL_LOCATION_CD` | DOUBLE | NOT NULL |  | The location that the item is replenished from. |
| 6 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Primary Key |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `PRIMARY_VENDOR_CD` | DOUBLE | NOT NULL |  | The vendor that this item is usually ordered from. |
| 9 | `PRIMARY_VENDOR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The primary vendor's item that is reordered. |
| 10 | `PRODUCT_ORIGIN_CD` | DOUBLE | NOT NULL |  | x |
| 11 | `REORDER_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The package type that is usually reordered from the vendor. |
| 12 | `SYSCALC_EOQ_IND` | DOUBLE |  |  | x |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the vendor site |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PRIMARY_VENDOR_ITEM_ID` | [VENDOR_ITEM](VENDOR_ITEM.md) | `ITEM_ID` |
| `REORDER_PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `VENDOR_SITE_ID` | [VENDOR_SITE](VENDOR_SITE.md) | `VENDOR_SITE_ID` |

