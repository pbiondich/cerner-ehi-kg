# ONLINE_ITEM_INVENTORY_CLASSES

> Contains the Online Item inventory class for the online items for the inventory type controls

**Description:** the Online Item inventory class for the online items for the inventory control  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 3 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 4 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The created date and timeColumn |
| 6 | `CREATE_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 8 | `ITEM_CLASS_NODE_ID` | DOUBLE |  |  | The item class nodes of the items that the control needs to display |
| 9 | `ONLINE_ITEM_DEFINITION_ID` | DOUBLE | NOT NULL |  | Foreign Key value from the ONLINE_ITEM_DEFINITION table. |
| 10 | `ONLINE_ITEM_VERSION_NBR` | DOUBLE |  | FK→ | The online item version numberColumn |
| 11 | `TASK_ASSAY_CD` | DOUBLE |  | FK→ | A reference (foreign key) to the discrete_task_assay table indicating the discrete task assay for this input control. Also part of the composite primary key |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ONLINE_ITEM_VERSION_NBR` | [ONLINE_ITEM_DEFINITION](ONLINE_ITEM_DEFINITION.md) | `ONLINE_ITEM_VERSION_NBR` |
| `TASK_ASSAY_CD` | [ONLINE_ITEM_DEFINITION](ONLINE_ITEM_DEFINITION.md) | `TASK_ASSAY_CD` |

