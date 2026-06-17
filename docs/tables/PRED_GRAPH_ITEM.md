# PRED_GRAPH_ITEM

> Stores which event sets are linked to that given graph.

**Description:** PRED GRAPH ITEM  
**Table type:** REFERENCE  
**Primary key:** `PRED_GRAPH_ITEM_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_CD` | DOUBLE | NOT NULL |  | Identifies the event code to be included in the graph. |
| 2 | `EVENT_SET_NAME` | VARCHAR(40) |  |  | Name of the event set. |
| 3 | `PRED_GRAPH_INST_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the graph sequence. |
| 4 | `PRED_GRAPH_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the pred Graph item. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRED_GRAPH_INST_ID` | [PRED_GRAPH](PRED_GRAPH.md) | `PRED_GRAPH_INST_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PRED_GRAPH_ITEM_PROP](PRED_GRAPH_ITEM_PROP.md) | `PRED_GRAPH_ITEM_ID` |

