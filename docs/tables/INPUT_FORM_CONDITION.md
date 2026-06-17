# INPUT_FORM_CONDITION

> Defines conditions for input_form_reference forms; when evaluated these conditions can trigger behaviors from input_form_behavior

**Description:** Input_Form_Condition  
**Table type:** REFERENCE  
**Primary key:** `CONDITION_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPARISON_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Compared to the value in the trigger control to determine if behavior(s) should be executed |
| 2 | `COMPARISON_PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the table from which Comparison_Parent_Entity_ID comes |
| 3 | `COMPARISON_TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The field/input control whose value will be evaluated to determine if any behavior(s) should be executed. |
| 4 | `COMPARISON_TEXT` | VARCHAR(255) |  |  | Compared to the value in the trigger control to determine if behavior(s) should be executed |
| 5 | `CONDITION_ID` | DOUBLE | NOT NULL | PK | Unique identifier for this row. PK |
| 6 | `CONDITION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Logical operation that will be used to compare the value in the trigger to the comparison control/value/text.0 - Equal To; 1 - Not Equal To; 2 - Any Value; 3 - Less Than; 4 - Greater Than; 5 - Greater Than/Equal To; 6 - Less Than/Equal To |
| 7 | `INPUT_FORM_CD` | DOUBLE | NOT NULL |  | The code of the parent form from Input_Form_Reference. |
| 8 | `TRIGGER_TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The field/input control whose value will be evaluated to determine if any behavior(s) should be executed. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INPUT_FORM_BEHAVIOR](INPUT_FORM_BEHAVIOR.md) | `CONDITION_ID` |

