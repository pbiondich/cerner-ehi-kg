# SA_TODO_FLUID

> Surginet Anesthesia To Do Fluid

**Description:** SA To Do Fluid  
**Table type:** ACTIVITY  
**Primary key:** `SA_TODO_FLUID_ID`  
**Columns:** 33  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_AMOUNT` | DOUBLE |  |  | The bag volume of the fluid to be given |
| 6 | `ADMIN_RATE_CD` | DOUBLE | NOT NULL |  | The unit of measure for the rate the fluid is to be given |
| 7 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | The route the fluid is to be given |
| 8 | `ADMIN_SITE_CD` | DOUBLE | NOT NULL |  | The site the fluid is to be given |
| 9 | `AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure of the amount of the fluid to be given |
| 10 | `COMPLETE_DT_TM` | DATETIME |  |  | The date/time the todo item was completed |
| 11 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates whether the todo item has been completed |
| 12 | `EVENT_CD` | DOUBLE | NOT NULL |  | The Event Cd for the fluid item |
| 13 | `FLUID_ADMIN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Fluid Admin Type Flag: 0 not defined; 1 Bolus; 2 Infusion |
| 14 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item id for the fluid |
| 15 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the long text identifier |
| 16 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The med product id for the fluid |
| 17 | `PREV_TODO_FLUID_ID` | DOUBLE | NOT NULL | FK→ | The previous version of the todo fluid item |
| 18 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The provider who added the item to the todo list. |
| 19 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The instance of a macro that added the item to the todo list. |
| 20 | `SA_TODO_FLUID_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for this record |
| 21 | `SA_TODO_LIST_ID` | DOUBLE | NOT NULL | FK→ | The ToDo list record this item belongs to |
| 22 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task assay code |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `VOLUME_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of volume |
| 29 | `VOLUME_RATE_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of Volume Rate |
| 30 | `VOLUME_RATE_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time field of Volume Rate |
| 31 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for dosage in WBD |
| 32 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time in WBD |
| 33 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for weight in WBD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `PREV_TODO_FLUID_ID` | [SA_TODO_FLUID](SA_TODO_FLUID.md) | `SA_TODO_FLUID_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_TODO_LIST_ID` | [SA_TODO_LIST](SA_TODO_LIST.md) | `SA_TODO_LIST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_TODO_FLUID](SA_TODO_FLUID.md) | `PREV_TODO_FLUID_ID` |
| [SA_TODO_FLUID_ITEM](SA_TODO_FLUID_ITEM.md) | `SA_TODO_FLUID_ID` |

