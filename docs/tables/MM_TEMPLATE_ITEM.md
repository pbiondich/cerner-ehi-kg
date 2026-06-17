# MM_TEMPLATE_ITEM

> An item that needs to be counted in an inventory cycle.

**Description:** Supply Chain Template Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | An inventory item contained within a template. |
| 2 | `ITEM_SEQ` | DOUBLE | NOT NULL |  | The order of the item in the template. |
| 3 | `MM_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The template that an item is defined for. |
| 4 | `MM_TEMPLATE_ITEM_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_TEMPLATE_ITEM table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MM_TEMPLATE_ID` | [MM_TEMPLATE](MM_TEMPLATE.md) | `MM_TEMPLATE_ID` |

