# SCRATCHPAD_ITEM_LABEL

> Contains the labels associated to a scratchpad item.

**Description:** Scratchpad Item Label  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DELETE_IND` | DOUBLE | NOT NULL |  | Indicates if the scratchpad item label row has been deleted. |
| 3 | `ITEM_SEQ` | DOUBLE | NOT NULL |  | The scratchpad item sequence. Identifies the order in which labels were added to this table. |
| 4 | `LABEL_NAME` | VARCHAR(100) | NOT NULL |  | The string label associated to a scratchpad item. The label can be used to provide information about a scratchpad item. |
| 5 | `SCRATCHPAD_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The scratchpad item identifier to which this label is associated. |
| 6 | `SCRATCHPAD_ITEM_LABEL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the scratchpad_item_label table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCRATCHPAD_ITEM_ID` | [SCRATCHPAD_ITEM](SCRATCHPAD_ITEM.md) | `SCRATCHPAD_ITEM_ID` |

