# MM_TEMPLATE

> Generic header information about a group of items that will need to be counted during an inventory.

**Description:** Supply Chain Template  
**Table type:** REFERENCE  
**Primary key:** `MM_TEMPLATE_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADU_OP_FLAG` | DOUBLE | NOT NULL |  | The criteria to use on ADU quantity when retrieving an item. |
| 2 | `ADU_QTY` | DOUBLE | NOT NULL |  | The threshold ADU to be retrieved. |
| 3 | `CYCLE_CNT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of cycle count (random/reorder/custom). |
| 4 | `ITEM_DISTRIBUTION_FLAG` | DOUBLE | NOT NULL |  | Method used to distribute items into logical sheets. |
| 5 | `ITEM_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The related template that contains a list of items. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location this template was created for. |
| 7 | `LOOKBACK_DAYS` | DOUBLE | NOT NULL |  | Number of days the system should look back to determine whether the item has been counted in past X days. Based off the number of days defined in this column, system would determine whether the items needs to be counted or not.. |
| 8 | `MAX_ITEM_QTY` | DOUBLE | NOT NULL |  | Maximum number of items to be included in this count. |
| 9 | `MM_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the MM_TEMPLATE table. |
| 10 | `SHEET_QTY` | DOUBLE | NOT NULL |  | If item_distribution_flag = 2, this will determine the number of logical sheets created. |
| 11 | `TEMPLATE_NAME` | VARCHAR(255) | NOT NULL |  | The name of the inventory template. |
| 12 | `TEMPLATE_NAME_KEY` | VARCHAR(255) | NOT NULL |  | The alphanumeric uppercase value of template name. |
| 13 | `TEMPLATE_NAME_KEY_A_NLS` | VARCHAR(1020) |  |  | TEMPLATE_NAME_KEY_A_NLS column |
| 14 | `TEMPLATE_NAME_KEY_NLS` | VARCHAR(512) | NOT NULL |  | The NLS value associated with the column template_name_key. |
| 15 | `TEMPLATE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of template that this row contains information about. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_TEMPLATE_ID` | [MM_TEMPLATE](MM_TEMPLATE.md) | `MM_TEMPLATE_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MM_CYCLE_CNT_FILTER](MM_CYCLE_CNT_FILTER.md) | `MM_TEMPLATE_ID` |
| [MM_TEMPLATE](MM_TEMPLATE.md) | `ITEM_TEMPLATE_ID` |
| [MM_TEMPLATE_ITEM](MM_TEMPLATE_ITEM.md) | `MM_TEMPLATE_ID` |

