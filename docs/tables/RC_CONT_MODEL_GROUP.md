# RC_CONT_MODEL_GROUP

> A group of prioritized workflow models.

**Description:** Revenue Cycle - Continuity Model Group  
**Table type:** REFERENCE  
**Primary key:** `RC_CONT_MODEL_GROUP_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this record was created. |
| 3 | `EVENT_CD` | DOUBLE | NOT NULL |  | The column stores the event code for the starting event for the models in the group. |
| 4 | `MODEL_GROUP_NAME` | VARCHAR(200) | NOT NULL |  | Contains the name of the group. |
| 5 | `MODEL_GROUP_NAME_KEY` | VARCHAR(200) | NOT NULL |  | The unique key of a given model group name. |
| 6 | `RC_CONT_MODEL_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the rc_cont_model_group table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_CONT_MODEL_GROUP_R](RC_CONT_MODEL_GROUP_R.md) | `RC_CONT_MODEL_GROUP_ID` |

