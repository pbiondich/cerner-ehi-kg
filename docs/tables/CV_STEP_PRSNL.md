# CV_STEP_PRSNL

> Stores personnel related to a step

**Description:** CV Procedure Step Personnel  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | the action_dt_tm captures the date and time that the person interacted with the step. |
| 2 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | used to keep step personnel in a specific sequence (the order in which they were entered) |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | the action_type_cd identifies which action the person performed upon the detail step. (ex. completed, started, removed) |
| 4 | `CV_STEP_ID` | DOUBLE | NOT NULL | FK→ | Cv_step_id is a foreign key to the cv_step table. it indicates which step the personnel are tied to. |
| 5 | `CV_STEP_PRSNL_ID` | DOUBLE | NOT NULL |  | The primary key for this table. |
| 6 | `STEP_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the step_prsnl_id is a foreign key to the prsnl table. it identifies the person that interacted with the step. |
| 7 | `STEP_RELATION_CD` | DOUBLE | NOT NULL |  | the step_relation_cd identifies the role that the person took when interacting with the step. (ex: tech, nurse, cardiologist, etc.) |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_STEP_ID` | [CV_STEP](CV_STEP.md) | `CV_STEP_ID` |
| `STEP_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

