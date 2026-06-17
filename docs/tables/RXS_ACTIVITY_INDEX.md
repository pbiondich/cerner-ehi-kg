# RXS_ACTIVITY_INDEX

> A table that stores RxStation specific activities related to medication dispense and pharmacy stocking workflows.

**Description:** RxStation Activity Index  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | The date and time the activity was performed. |
| 2 | `CLUSTER_CD` | DOUBLE | NOT NULL | FK→ | This is the cluster (grouping) that the RxStation device belongs to. |
| 3 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a dispensing event. Foreign key from the DISPENSE_HX table. |
| 4 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the pharmacy formulary item. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Identifies an RxStation device. |
| 6 | `LOCATOR_CD` | DOUBLE | NOT NULL | FK→ | The lowest level of the location hierarchy for which the item will be placed. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the personnel who performed the activity. |
| 8 | `RXS_ACTIVITY_INDEX_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_ACTIVITY_INDEX table. |
| 9 | `RXS_LOCATION_TASK_ID` | DOUBLE | NOT NULL | FK→ | The task that this activity row pertains to. |
| 10 | `TASK_TYPE_CD` | DOUBLE | NOT NULL |  | The type of task - for example: replenish, load, unload. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLUSTER_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATOR_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RXS_LOCATION_TASK_ID` | [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_LOCATION_TASK_ID` |

