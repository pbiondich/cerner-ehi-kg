# SCRATCHPAD_ITEM

> Contains scratchpad items associated to a patient/user/concept centric scratchpad session.

**Description:** Scratchpad Item  
**Table type:** ACTIVITY  
**Primary key:** `SCRATCHPAD_ITEM_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ITEM_CONCEPT_NAME` | VARCHAR(100) |  |  | The concept used to identify the scratchpad item. For example, if the item is an order, the item_concept could be something like ""ORDER"" with a corresponding item_concept_id with the order_id. |
| 3 | `ITEM_CONCEPT_VALUE` | DOUBLE |  |  | The numeric concept identifier used to identify the scratchpad item. For example, if the item is an order, the item_concept could be something like ""ORDER"" with a corresponding item_concept_id with the order_id. |
| 4 | `LAST_ITEM_SEQ` | DOUBLE | NOT NULL |  | The last scratchpad item sequence. Used to identify the latest sequence used to add either label or component information. |
| 5 | `SCRATCHPAD_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the scratchpad_item table. |
| 6 | `SCRATCHPAD_SESSION_ID` | DOUBLE | NOT NULL | FK→ | The scratchpad session identifier to which this item is associated. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERSION_NBR` | DOUBLE | NOT NULL |  | The scratchpad item version. This is used to ensure modifications made to a scratchpad item are performed against the latest version of the scratchpad item. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCRATCHPAD_SESSION_ID` | [SCRATCHPAD_SESSION](SCRATCHPAD_SESSION.md) | `SCRATCHPAD_SESSION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SCRATCHPAD_ITEM_COMPONENT](SCRATCHPAD_ITEM_COMPONENT.md) | `SCRATCHPAD_ITEM_ID` |
| [SCRATCHPAD_ITEM_LABEL](SCRATCHPAD_ITEM_LABEL.md) | `SCRATCHPAD_ITEM_ID` |

