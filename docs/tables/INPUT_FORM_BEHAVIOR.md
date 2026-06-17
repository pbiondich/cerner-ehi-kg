# INPUT_FORM_BEHAVIOR

> Defines behaviors for input_form_reference forms

**Description:** Input_Form_Behavior  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEHAVIOR_ID` | DOUBLE | NOT NULL |  | Unique identifier for this row. PK |
| 2 | `CONDITION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from Input_Form_Condition, the condition that triggers this behavior |
| 3 | `EFFECTED_FORM_CD` | DOUBLE | NOT NULL |  | The input_form_reference form that will be effected by this behavior |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONDITION_ID` | [INPUT_FORM_CONDITION](INPUT_FORM_CONDITION.md) | `CONDITION_ID` |

