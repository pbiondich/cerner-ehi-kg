# MIC_SCRIPT_NODE

> This reference table contains biochemical tasks and their relationships to other biochemical tasks in order to defined pathways for a script.

**Description:** Microbiology Script Node  
**Table type:** REFERENCE  
**Primary key:** `NODE_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIOCHEMICAL_TASK_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the biochemical task, both group and detail biochemicals are valid. A biochemical task can only exist once within a pathway of a script. |
| 2 | `NODE_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the 'biochemical step' and its associated parameters. This value is used to join to the MIC_SCRIPT_NODE_* tables. |
| 3 | `PARENT_NODE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the parent MIC_SCRIPT_NODE row. This field defines relationships to biochemical nodes within a script pathway. |
| 4 | `SCRIPT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the parent MIC_SCRIPT table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_NODE_ID` | [MIC_SCRIPT_NODE](MIC_SCRIPT_NODE.md) | `NODE_ID` |
| `SCRIPT_ID` | [MIC_SCRIPT](MIC_SCRIPT.md) | `SCRIPT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_SCRIPT_NODE](MIC_SCRIPT_NODE.md) | `PARENT_NODE_ID` |
| [MIC_SCRIPT_NODE_ACTION](MIC_SCRIPT_NODE_ACTION.md) | `NODE_ID` |
| [MIC_SCRIPT_NODE_RESULT](MIC_SCRIPT_NODE_RESULT.md) | `NODE_ID` |

