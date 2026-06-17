# PRED_GRAPH_ITEM_PROP

> Stores the additional attributes about the event set which is the part of the given graph. For example whether that event set values will be plotted as line or not. Whether it will have secondary axis..

**Description:** Pred Graph Item Prop  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PRED_GRAPH_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the pred Graph item. |
| 2 | `PRED_GRAPH_ITEM_PROP_ID` | DOUBLE | NOT NULL |  | Specifies the entities that a graph can be linked to. |
| 3 | `PROP_NAME` | VARCHAR(100) | NOT NULL |  | Specifies the entity associated with a graph. |
| 4 | `PROP_VALUE` | VARCHAR(255) | NOT NULL |  | Specifies the unique identifier of the entity associated with a graph. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRED_GRAPH_ITEM_ID` | [PRED_GRAPH_ITEM](PRED_GRAPH_ITEM.md) | `PRED_GRAPH_ITEM_ID` |

