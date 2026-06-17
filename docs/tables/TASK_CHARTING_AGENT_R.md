# TASK_CHARTING_AGENT_R

> The table is used to store the relationship between reference tasks and their associated charting agents.

**Description:** Reference task and task charting agent relationship.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARTING_AGENT_CD` | DOUBLE | NOT NULL |  | Code value represents the different types of charting agents. For example, PowerForms, PowerNotes, APACHE. Component such as Task List may use this value to decide which charting agent to load when a task is charted. code set 255090 |
| 2 | `CHARTING_AGENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The numeric value to identify which form or template to be used for a given charting agent when a task is charted. This field is used when the form or template has a unique numeric identifier. It should be used in conjunction with charting_agent_entity_name. |
| 3 | `CHARTING_AGENT_ENTITY_NAME` | VARCHAR(255) |  |  | The table name where the charting agent id is located. For example, "DCP_FORMS_REF". This field is used when the form or template has a unique numeric identifier; otherwise, it should be empty. It should be used in conjunction with charting_agent_entity_id. |
| 4 | `CHARTING_AGENT_IDENTIFIER` | VARCHAR(255) |  |  | The reference string to identify which form or template to be used for a given charting agent when a task is charted. This field is used when the form or template does not have a unique numeric identifier. |
| 5 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | ID of the reference task to which the charting agent is associated with. |
| 6 | `TASK_CHARTING_AGENT_R_ID` | DOUBLE | NOT NULL |  | Unique identifier. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |

