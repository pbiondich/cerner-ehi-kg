# QUANTITY_ON_HAND

> Stores quantity on hand for an item at a location.

**Description:** QUANTITY ON HAND  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_APPLCTX` | DOUBLE | NOT NULL |  | The registered (assigned) application number for the process that updated the row. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVE_STATUS_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that updated the row. |
| 7 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The registered (assigned) application number for the process that created the row. |
| 8 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 9 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 10 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 11 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location |
| 13 | `LOCATOR_CD` | DOUBLE | NOT NULL |  | Locator |
| 14 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to package type table. |
| 15 | `QOH_TYPE_CD` | DOUBLE | NOT NULL |  | The type of quantity. |
| 16 | `QTY` | DOUBLE | NOT NULL |  | The item quantity. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

