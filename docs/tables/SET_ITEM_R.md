# SET_ITEM_R

> IV and Order Set relationship table.

**Description:** SET ITEM R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT1_ID` | DOUBLE | NOT NULL |  | Long text id for IV set s Comment 1. |
| 2 | `COMMENT1_TYPE` | DOUBLE |  |  | Type for IV set's Comment 1. |
| 3 | `COMMENT2_ID` | DOUBLE | NOT NULL |  | Long text id for IV set's Comment 2. |
| 4 | `COMMENT2_TYPE` | DOUBLE |  |  | Type for IV set's Comment 2. |
| 5 | `COMMENT_ID` | DOUBLE | NOT NULL |  | Not in use. |
| 6 | `COMPONENT_ITEM_ID` | DOUBLE | NOT NULL |  | Key to medication_definition item for this component. |
| 7 | `COMPONENT_SEQUENCE` | DOUBLE | NOT NULL |  | Order this item should appear in the orderor set. |
| 8 | `DEFAULT_ACTION_CD` | DOUBLE | NOT NULL | FK→ | Default action for this order (only applies to Order sets.) |
| 9 | `OE_FORMAT_FLAG` | DOUBLE |  |  | Default screen format that indicates if order is med, continuous, intermittent, or no default specified. |
| 10 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL |  | order sentence for this IV set component |
| 11 | `SET_ITEM_ID` | DOUBLE | NOT NULL |  | Item ID that identifies the set. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFAULT_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

