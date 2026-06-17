# RC_CONT_MODEL

> Contains model definitions for continuity of flow.

**Description:** Revenue Cycle Continuity  
**Table type:** REFERENCE  
**Primary key:** `RC_CONT_MODEL_ID`  
**Columns:** 16  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DISPLAY_DATA_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The id where the position json string is stored. |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 4 | `MODEL_BEG_EFF_DT_TM` | DATETIME | NOT NULL |  | The date that the model will start to be honored in Work Flows |
| 5 | `MODEL_DRAFT_IND` | DOUBLE | NOT NULL |  | Indicates if the model is a draft or published. |
| 6 | `MODEL_END_EFF_DT_TM` | DATETIME | NOT NULL |  | The date that the model will no longer be honored in Work Flows |
| 7 | `MODEL_NAME` | VARCHAR(200) | NOT NULL |  | The name of the model, chosen by the user. |
| 8 | `MODEL_NAME_KEY` | VARCHAR(200) | NOT NULL |  | The name key for the model This will be the original model name and cannot be changed. |
| 9 | `RC_CONT_MODEL_ID` | DOUBLE | NOT NULL | PK | Uniquely generated number that identifies a single row on the rc_cont_model table. |
| 10 | `TARGETED_DAYS` | DOUBLE | NOT NULL |  | The column stores the ideal number of days in which the workflow should complete. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `WORKFLOW_TYPE_CD` | DOUBLE | NOT NULL |  | The column stores the workflow type of the model. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPLAY_DATA_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [RC_CONT_MODEL_EVENT_RELTN](RC_CONT_MODEL_EVENT_RELTN.md) | `RC_CONT_MODEL_ID` |
| [RC_CONT_MODEL_GROUP_R](RC_CONT_MODEL_GROUP_R.md) | `RC_CONT_MODEL_DRAFT_ID` |
| [RC_CONT_MODEL_RELTN](RC_CONT_MODEL_RELTN.md) | `MODEL_DRAFT_ID` |
| [RC_CONT_MODEL_RELTN](RC_CONT_MODEL_RELTN.md) | `PUBLISHED_MODEL_ID` |
| [RC_CONT_NODE](RC_CONT_NODE.md) | `RC_CONT_MODEL_ID` |
| [RC_CONT_NODE_EDGE](RC_CONT_NODE_EDGE.md) | `RC_CONT_MODEL_ID` |
| [RC_CONT_PROCESS_GROUP](RC_CONT_PROCESS_GROUP.md) | `RC_CONT_MODEL_ID` |

