# CDI_FORM_CRITERIA

> A row in this table represents criteria which is part of a rule for when a CPDI interactive form may be required.

**Description:** CDI Form Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_FORM_CRITERIA_ID` | DOUBLE | NOT NULL |  | Unique row identifier for the CDI Form Criteria table. It is internally generated. |
| 2 | `CDI_FORM_RULE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the cdi_form_rule table. Identifies the rule the criteria is associated with. |
| 3 | `COMPARISON_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of comparison to perform. 0 - equals, 1 - less than, 2 - greater than, 3 - not equal, 4 - less than or equal, 5 - greater than or equal |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `VALUE_CD` | DOUBLE |  |  | The code value to compare against. Code set will vary. |
| 10 | `VALUE_DT_TM` | DATETIME |  |  | Date/time value to compare against. |
| 11 | `VALUE_NBR` | DOUBLE |  |  | Numeric value to compare against. |
| 12 | `VALUE_TEXT` | VARCHAR(30) |  |  | Text value to compare against. |
| 13 | `VARIABLE_CD` | DOUBLE | NOT NULL |  | Identifies the variable (encounter data, etc.) that this criteria is evaluated against. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_FORM_RULE_ID` | [CDI_FORM_RULE](CDI_FORM_RULE.md) | `CDI_FORM_RULE_ID` |

