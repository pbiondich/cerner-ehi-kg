# EQUATION_COMPONENT

> Defines the component procedures to an equation and all of its attributes.

**Description:** Equation Component  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_IND` | DOUBLE |  |  | Was to be used for interpretation. (Currently not implemented) |
| 2 | `COMPONENT_FLAG` | DOUBLE |  |  | Defines the equation component type. |
| 3 | `CONSTANT_VALUE` | DOUBLE |  |  | Defines the value of a constant defined in the equation. |
| 4 | `CROSS_DRAWN_DT_TM_IND` | DOUBLE |  |  | Indicates whether the equation component may cross drawn date and time when looking up the result to be used in the equation. A value of 0 indicates the equation component will not cross drawn date and time. A value of 1 indicates the equation component may cross drawn date and time. |
| 5 | `DEFAULT_VALUE` | DOUBLE |  |  | Defines the value to use when a component result is not found and the result required flag is set to allow a default to be used. |
| 6 | `EQUATION_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific equation component. Creates a relationship to the equation table. |
| 7 | `INCLUDED_ASSAY_CD` | DOUBLE | NOT NULL |  | Defines the discrete task assay procedure to be used as a component of the equation. |
| 8 | `LOOK_TIME_DIRECTION_FLAG` | DOUBLE | NOT NULL |  | Identifies to use TIME_WINDOW_MINS and TIME WINDOW_BACK_MINUTES in an order. 0: TIME_WINDOW_BACK_MINUTES 1st and TIME_WINDOW_MINUTES 2nd 1: TIME_WINDOW_MINUTES 1st and TIME_WINDOW_BACK_MINUTES 2nd |
| 9 | `NAME` | VARCHAR(50) |  |  | Describes the component by either the procedure mnemonic or the free textname for a constant or variable. |
| 10 | `OCTAL_VALUE` | DOUBLE |  |  | Was to be used for interpretation. (Currently not implemented) |
| 11 | `RACE_IND` | DOUBLE |  |  | Was to be used for interpretation. (Currently not implemented) |
| 12 | `RESULT_REQ_FLAG` | DOUBLE |  |  | Defines whether the component is required to have a result before the equation will be processed. |
| 13 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the lowest level at which the procedure result status can be to include this component in the equation. |
| 14 | `SEQUENCE` | DOUBLE | NOT NULL |  | Defines the sequence number when multiple components are defined for an equation. |
| 15 | `SEX_IND` | DOUBLE |  |  | Was to be used for interpretation. (Currently not implemented) |
| 16 | `TIME_WINDOW_BACK_MINUTES` | DOUBLE |  |  | Defines the amount of time in minutes to look back from the collected time of the current specimen to the collected time of the previous specimen for using a result in an equation. |
| 17 | `TIME_WINDOW_MINUTES` | DOUBLE |  |  | Defines the amount of time to look across the drawn date and time to find a component that is set to cross drawn date and time. |
| 18 | `UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the unit in which this component is measured. This field is not used by PathNet, but is filled out by Power Forms. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `VARIABLE_PROMPT` | VARCHAR(50) |  |  | Stores the prompt to display for a variable to be entered at run time. (Currently not implemented) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EQUATION_ID` | [EQUATION](EQUATION.md) | `EQUATION_ID` |

