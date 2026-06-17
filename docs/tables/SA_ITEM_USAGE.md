# SA_ITEM_USAGE

> Contains records that document the quantities used, returned, wasted for items used on an anesthesia record Based on how many items they used during a case. Estimate 1:1 with SA_ITEM. 522,000

**Description:** SA Item Usage  
**Table type:** ACTIVITY  
**Primary key:** `SA_ITEM_USAGE_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHARGE_QTY` | DOUBLE | NOT NULL |  | The number of items that should be charged. |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long_text record that contains the comment for the item usage |
| 7 | `PREVIOUS_ITEM_USAGE_ID` | DOUBLE | NOT NULL | FK→ | The id to the usage record before the record was changed. If 0, this is the original unchanged record |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who documented the quantities, if 0, added by a macro |
| 9 | `RETURNED_QTY` | DOUBLE |  |  | The number of this item that was returned in the anesthesia record |
| 10 | `SA_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The SA_ITEM record id that this usage record is documenting |
| 11 | `SA_ITEM_USAGE_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the item usage record |
| 12 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | Ties to the macro that added the usage to the anesthesia record, if 0, added by user |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `USAGE_DT_TM` | DATETIME |  |  | The date/time the item usage occurred |
| 19 | `USED_QTY` | DOUBLE |  |  | The number of this item that was used in the anesthesia record |
| 20 | `WASTED_QTY` | DOUBLE |  |  | The number of this item that was wasted in the anesthesia record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREVIOUS_ITEM_USAGE_ID` | [SA_ITEM_USAGE](SA_ITEM_USAGE.md) | `SA_ITEM_USAGE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_ITEM_ID` | [SA_ITEM](SA_ITEM.md) | `SA_ITEM_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SA_ACTION](SA_ACTION.md) | `SA_ITEM_USAGE_ID` |
| [SA_ACTION_ITEM](SA_ACTION_ITEM.md) | `SA_ITEM_USAGE_ID` |
| [SA_ITEM_USAGE](SA_ITEM_USAGE.md) | `PREVIOUS_ITEM_USAGE_ID` |

