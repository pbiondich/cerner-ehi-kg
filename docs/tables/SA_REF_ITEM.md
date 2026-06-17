# SA_REF_ITEM

> Contains records that define all of the items that can be used within the anesthesia applications. Size - Based on the # of inventory items they want to define. Estimate 100 rows.

**Description:** SA Reference Item  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_ITEM_ID`  
**Columns:** 12  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Id of the materials management item FK from ITEM_MASTER |
| 6 | `REF_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of reference this item is built for (I.e Anesthesia (0), CVNet (1) |
| 7 | `SA_REF_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique value to the anesthesia item record |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [SA_ITEM](SA_ITEM.md) | `SA_REF_ITEM_ID` |
| [SA_REF_CAT_ITEM](SA_REF_CAT_ITEM.md) | `SA_REF_ITEM_ID` |
| [SA_REF_EXCLUDE_ITEM](SA_REF_EXCLUDE_ITEM.md) | `SA_REF_ITEM_ID` |
| [SA_REF_MACRO_ACTION](SA_REF_MACRO_ACTION.md) | `SA_REF_ITEM_ID` |
| [SA_REF_REQUIRED_ITEM](SA_REF_REQUIRED_ITEM.md) | `SA_REF_ITEM_ID` |
| [SA_TODO_ACTION](SA_TODO_ACTION.md) | `SA_REF_ITEM_ID` |
| [SA_TODO_ACTION_ITEM](SA_TODO_ACTION_ITEM.md) | `SA_REF_ITEM_ID` |

