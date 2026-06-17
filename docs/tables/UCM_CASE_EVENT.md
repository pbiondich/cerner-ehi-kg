# UCM_CASE_EVENT

> This table stores events that occur to cases and case steps.

**Description:** Unified Case Management - Case Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the code to describe the type of event. |
| 2 | `RELATED_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the case step related to the ucm_case_step_id by way of event_type_cd. |
| 3 | `UCM_CASE_EVENT_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies the case event. |
| 4 | `UCM_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies the case step for this event. Note that not all events are also tied to a step. In those cases, this will be 0 |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RELATED_CASE_STEP_ID` | [UCM_CASE_STEP](UCM_CASE_STEP.md) | `UCM_CASE_STEP_ID` |
| `UCM_CASE_STEP_ID` | [UCM_CASE_STEP](UCM_CASE_STEP.md) | `UCM_CASE_STEP_ID` |

