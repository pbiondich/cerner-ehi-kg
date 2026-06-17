# PW_COMP_ACTION

> Pathway component action

**Description:** pw_comp_action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time of the action |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the person who performed the action |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Action type code |
| 4 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 5 | `ACT_PW_COMP_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway component the action is associated with |
| 6 | `COMP_STATUS_CD` | DOUBLE | NOT NULL |  | Status code of the component after the action was perfomed |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the parent entity of the pathway component.Column |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the table that the pathway component references.Column |
| 9 | `PW_COMP_ACTION_SEQ` | DOUBLE | NOT NULL |  | Sequence of the action the component |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACT_PW_COMP_ID` | [ACT_PW_COMP](ACT_PW_COMP.md) | `ACT_PW_COMP_ID` |

