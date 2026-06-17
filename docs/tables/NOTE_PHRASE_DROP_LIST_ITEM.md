# NOTE_PHRASE_DROP_LIST_ITEM

> Individual items in a note phrase drop list.

**Description:** Note Phrase Drop List Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Tells whether this is the default item in a drop list. |
| 2 | `ITEM_DISPLAY_TXT` | VARCHAR(255) | NOT NULL |  | The display for the drop list item. For example, in a drop list for severity you might have the following three displays: mild, moderate, severe. |
| 3 | `ITEM_SEQ` | DOUBLE | NOT NULL |  | Determines the order in which this item appears in a drop list. |
| 4 | `NOTE_PHRASE_DROP_LIST_ID` | DOUBLE | NOT NULL | FK→ | Tells which auto text drop list this item belongs to. |
| 5 | `NOTE_PHRASE_DROP_LIST_ITEM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the NOTE_PHRASE_DROP_LIST_ITEM table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_PHRASE_DROP_LIST_ID` | [NOTE_PHRASE_DROP_LIST](NOTE_PHRASE_DROP_LIST.md) | `NOTE_PHRASE_DROP_LIST_ID` |

