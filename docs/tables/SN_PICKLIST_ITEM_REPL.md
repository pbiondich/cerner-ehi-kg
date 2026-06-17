# SN_PICKLIST_ITEM_REPL

> Stores the number of times an item has been replaced and whether preference cards have been updated based on a certain threshold

**Description:** Surginet Picklist Item Replacement  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ITEM_ID` | DOUBLE |  | FK→ | The item that was replaced |
| 2 | `LAST_REPLACEMENT_DT_TM` | DATETIME |  |  | The last time this item was replaced by the replacement item |
| 3 | `PROCESSED_FLAG` | DOUBLE |  |  | Whether the preference card has been updated to reflect this replacement. 0 = Row has not been processed 1 = Row is being processed 2 = Row has been processed; |
| 4 | `REPLACED_WITH_ITEM_ID` | DOUBLE |  | FK→ | The item that replaced the original item |
| 5 | `REPLACEMENT_CNT` | DOUBLE |  |  | The number of times this item was replaced by the replacement item |
| 6 | `SN_PICKLIST_ITEM_REPL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `SURG_AREA_CD` | DOUBLE |  |  | Surgical area this replacement was applied in |
| 8 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `REPLACED_WITH_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

