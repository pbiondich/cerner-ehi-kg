# RC_CONT_NODE

> A single node in a continuity of flow model.

**Description:** Revenue Cycle Coninuity Node  
**Table type:** REFERENCE  
**Primary key:** `RC_CONT_NODE_ID`  
**Columns:** 11  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_DATA_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The id where the position json string is stored. |
| 2 | `NODE_DISPLAY_NAME` | VARCHAR(100) | NOT NULL |  | The display name for the node. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the entity to which this process is associated. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the entity to which this process is associated. |
| 5 | `RC_CONT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the model to which this node belongs. |
| 6 | `RC_CONT_NODE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the rc_cont_node table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPLAY_DATA_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `RC_CONT_MODEL_ID` | [RC_CONT_MODEL](RC_CONT_MODEL.md) | `RC_CONT_MODEL_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RC_CONT_NODE_EDGE](RC_CONT_NODE_EDGE.md) | `FROM_RC_CONT_NODE_ID` |
| [RC_CONT_NODE_EDGE](RC_CONT_NODE_EDGE.md) | `TO_RC_CONT_NODE_ID` |
| [RC_CONT_PROCESS](RC_CONT_PROCESS.md) | `RC_CONT_CURRENT_NODE_ID` |
| [RC_CONT_PROCESS_HIST](RC_CONT_PROCESS_HIST.md) | `RC_CONT_NODE_ID` |

