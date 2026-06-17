# RX_PERSON_OWE

> This table will store information about the person owe values related to dispensing.

**Description:** RX Person Owe  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel identifier of the user that created and/or modified the owe. If the value is 0, it means it was created by the system. Otherwise, the it contains the personnel identifier from the person table. |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Action that was performed to create this row. For example - create, cancel, resolve, etc. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `DISPENSE_FROM_CD` | DOUBLE | NOT NULL | FK→ | Identifies the pharmacy location that is needed for the owed stock. |
| 5 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | This field links the person_owe_id record to the dispensing event record. This will enable users to track the owe to the original dispense. |
| 6 | `INGRED_SEQ` | DOUBLE | NOT NULL |  | Identifies the sequence of the ingredients on the order. |
| 7 | `INVENTORY_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Inventory location that owes the person. |
| 8 | `INV_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the inventory item which qoh(quantity on hand) is tracked, in place of the formulation, including active ingredient, strength and dosage form. |
| 9 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | This column represents the item to which this owe is associated. |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field represents the order to which the owe is associated. |
| 11 | `OWE_ACTION_SEQ` | DOUBLE | NOT NULL |  | Indicates the number of times this owe (per dispense hx id) has been modified. When the owe is created, it will be 1. |
| 12 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the package associated to the item for which this owe was created. |
| 13 | `PERSON_OWE_DOSES_CNT` | DOUBLE |  |  | This value will indicate how many doses the person is owed. It is manually assigned. |
| 14 | `PERSON_OWE_QTY` | DOUBLE |  |  | This column contains the value of the person_owe_doses * QPD(Quantity Per Dose). |
| 15 | `RESOLVED_DHX_ID` | DOUBLE | NOT NULL | FK→ | Represents the dispensed History resolved person owe or reconciled what was person owe. |
| 16 | `RX_PERSON_OWE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a person owe related to dispensing. |
| 17 | `SYS_PERSON_OWE_QTY` | DOUBLE |  |  | Amount of owe quantity that the system calculates without user interaction. |
| 18 | `SYS_PRSN_OWE_DOSES_CNT` | DOUBLE |  |  | Contains the amount of owe doses that the system calculated without user interaction. |
| 19 | `TNF_ID` | DOUBLE | NOT NULL |  | Identifier of the template non-formulary item. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_FROM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `INVENTORY_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `INV_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `RESOLVED_DHX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |

