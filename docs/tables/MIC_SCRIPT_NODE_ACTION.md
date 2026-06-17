# MIC_SCRIPT_NODE_ACTION

> This reference table contains actions that will be taken when the defined results are entered for the parent biochemical (MIC_SCRIPT_NODE).

**Description:** Microbiology Script Node Action  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code that uniquely identifies the 'biochemical node action'. |
| 2 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field is used to identify the type of action. Valid actions include: ordering microbiology task, displaying a message box, and adding a free-text comment. |
| 3 | `DISPLAY_ORDER` | DOUBLE | NOT NULL |  | This field is used to determine the order in which the actions are taken. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for a message box and free-text comment action. |
| 5 | `NODE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the parent MIC_SCRIPT_NODE row. |
| 6 | `TASK_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code to a microbiology task. Valid 'action' tasks include: susceptibilities, reports, automated identifications, and organism name changes. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `NODE_ID` | [MIC_SCRIPT_NODE](MIC_SCRIPT_NODE.md) | `NODE_ID` |

