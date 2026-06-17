# RXS_LOC_ENCNTR_INVENTORY

> Stores the inventory for a patient's encounter-specific bin.

**Description:** RxStation Location Encounter Inventory  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item on this encounter that is in this location. |
| 2 | `ITEM_QTY` | DOUBLE | NOT NULL |  | The quantity of the item in this location. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order this item is associated with. |
| 4 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The package type for this item. |
| 5 | `RXS_LOCATOR_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Indicates the location and encounter that this item is supplied for. |
| 6 | `RXS_LOC_ENCNTR_INVENTORY_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_LOC_ENCNTR_INVENTORY table. |
| 7 | `TNF_ID` | DOUBLE | NOT NULL |  | The template non-formulary key that is associated with this location and encounter. A type of product that does not relate to a real medication. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `RXS_LOCATOR_ENCNTR_ID` | [RXS_LOCATOR_ENCNTR](RXS_LOCATOR_ENCNTR.md) | `RXS_LOCATOR_ENCNTR_ID` |

