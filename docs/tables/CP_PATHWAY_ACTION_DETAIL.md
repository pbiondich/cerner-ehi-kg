# CP_PATHWAY_ACTION_DETAIL

> Hold detailed information about actions take during an care planning workflow.

**Description:** Care Planning Action Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DETAIL_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies an action detail for the ACTION_DETAIL_ENTITY_NAME. |
| 2 | `ACTION_DETAIL_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the action detail that the user selected in the pathway/node process (ORDERS, DIAGNOSIS, NODE, etc.) |
| 3 | `ACTION_DETAIL_IDENT` | VARCHAR(255) |  |  | Optional identifier used to differentiate specific details |
| 4 | `ACTION_DETAIL_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the status for the pathway action. Active/Inerror |
| 5 | `ACTION_DETAIL_TEXT` | VARCHAR(1000) |  |  | Text display associated with an action detail |
| 6 | `CP_ACTION_DETAIL_TYPE_CD` | DOUBLE | NOT NULL |  | A code_value to identify the type of action detail |
| 7 | `CP_PATHWAY_ACTION_DETAIL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `CP_PATHWAY_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Parent row identifier on the CP_PATHWAY_ACTION table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_PATHWAY_ACTION_ID` | [CP_PATHWAY_ACTION](CP_PATHWAY_ACTION.md) | `CP_PATHWAY_ACTION_ID` |

