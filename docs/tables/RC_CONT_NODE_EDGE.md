# RC_CONT_NODE_EDGE

> An edge defined between two nodes in a continuity of flow model.

**Description:** Revenue Cycle Continuity Node Edge  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_DATA_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores long text id for edge coordinates. |
| 2 | `FROM_RC_CONT_NODE_ID` | DOUBLE | NOT NULL | FK→ | The node from which this edge begins. |
| 3 | `RC_CONT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | The model to which this edge belongs. |
| 4 | `RC_CONT_NODE_EDGE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the rc_cont_node_edge table. |
| 5 | `TO_RC_CONT_NODE_ID` | DOUBLE | NOT NULL | FK→ | The node at which this edge terminates. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPLAY_DATA_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `FROM_RC_CONT_NODE_ID` | [RC_CONT_NODE](RC_CONT_NODE.md) | `RC_CONT_NODE_ID` |
| `RC_CONT_MODEL_ID` | [RC_CONT_MODEL](RC_CONT_MODEL.md) | `RC_CONT_MODEL_ID` |
| `TO_RC_CONT_NODE_ID` | [RC_CONT_NODE](RC_CONT_NODE.md) | `RC_CONT_NODE_ID` |

