# CNT_EQUATION_COMPONENT

> CONTENT EQUATION COMPONENTS

**Description:** CNT EQUATION COMPONENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_IND` | DOUBLE | NOT NULL |  | was to be used for interpretation. (currently not implemented) |
| 2 | `CNT_EQUATION_COMPONENT_ID` | DOUBLE | NOT NULL |  | Sequence generated ID |
| 3 | `CNT_EQUATION_ID` | DOUBLE | NOT NULL | FK→ | FK to CNT_EQUATION |
| 4 | `COMPONENT_FLAG` | DOUBLE | NOT NULL |  | FLAG_VALUE:DESCRIPTION:DEFINITION 1.00:Procedure:Denotes the row as defining a procedure. 2.00:Variable:(not currently implemented) 3.00:Constant:Denotes the row as defining a constant. |
| 5 | `COMPONENT_NAME` | VARCHAR(50) |  |  | describes the component by either the procedure mnemonic or the free textname for a constant or variable. |
| 6 | `COMPONENT_SEQUENCE` | DOUBLE | NOT NULL |  | defines the sequence number when multiple components are defined for an equation. |
| 7 | `CONSTANT_VALUE` | DOUBLE |  |  | defines the value of a constant defined in the equation. |
| 8 | `CROSS_DRAWN_DT_TM_IND` | DOUBLE | NOT NULL |  | indicates whether the equation component may cross drawn date and time when looking up the result to be used in the equation. a value of 0 indicates the equation component will not cross drawn date and time. a value of 1 indicates the equation component may cross drawn date and time. |
| 9 | `DEFAULT_VALUE` | DOUBLE |  |  | defines the value to use when a component result is not found and the result required flag is set to allow a default to be used. |
| 10 | `EQUATION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for EQUATION |
| 11 | `INCLUDED_ASSAY_CD` | DOUBLE | NOT NULL |  | a unique code value that identifies a specific discrete task assay. |
| 12 | `INCLUDED_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 13 | `LOOK_TIME_DIRECTION_FLAG` | DOUBLE | NOT NULL |  | FLAG_VALUE:DESCRIPTION:DEFINITION 0.00:TIME WINDOW BACK MINUTES:TIME_WINDOW_BACK_MINUTES 1st and TIME_WINDOW_MINUTES 2nd 1.00:TIME WINDOW MINUTES:TIME_WINDOW_MINUTES 1st and TIME_WINDOW_BACK_MINUTES 2nd |
| 14 | `OCTAL_VALUE` | DOUBLE |  |  | was to be used for interpretation. (currently not implemented) |
| 15 | `RACE_IND` | DOUBLE | NOT NULL |  | was to be used for interpretation. (currently not implemented) |
| 16 | `RESULT_REQ_FLAG` | DOUBLE | NOT NULL |  | FLAG_VALUE:DESCRIPTION:DEFINITION 0.00:Not Required:Result not required and default value may be used. 1.00:Required:Result required for equation to evaluate. |
| 17 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Code Set: 1901 a unique code value that identifies the lowest level at which the procedure result status can be to include this component in the equation. |
| 18 | `RESULT_STATUS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Result Status Code Value |
| 19 | `SEX_IND` | DOUBLE | NOT NULL |  | was to be used for interpretation. (currently not implemented) |
| 20 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Universal identifier for the task assay |
| 21 | `TIME_WINDOW_BACK_MINUTES` | DOUBLE |  |  | defines the amount of time in minutes to look back from the collected time of the current specimen to the collected time of the previous specimen for using a result in an equation. |
| 22 | `TIME_WINDOW_MINUTES` | DOUBLE |  |  | defines the amount of time to look across the drawn date and time to find a component that is set to cross drawn date and time. |
| 23 | `UNITS_CD` | DOUBLE | NOT NULL |  | Code Set: 54 a unique code value that identifies the unit in which this component is measured. this field is not used by pathnet, but is filled out by power forms. |
| 24 | `UNITS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Units Code Value |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `VARIABLE_PROMPT` | VARCHAR(50) |  |  | stores the prompt to display for a variable to be entered at run time. (currently not implemented) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_EQUATION_ID` | [CNT_EQUATION](CNT_EQUATION.md) | `CNT_EQUATION_ID` |

