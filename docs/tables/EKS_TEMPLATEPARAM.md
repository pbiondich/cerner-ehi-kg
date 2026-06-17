# EKS_TEMPLATEPARAM

> This table contains definitions of parameters associated with templates. Each parameter may be set to user specified values when the associated template is placed into an expert module.

**Description:** Template parameter definition  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_TYPE` | CHAR(1) |  |  | The data type of the parameter. Character, Integer, Help, etc. |
| 2 | `DEFAULT_DATA` | VARCHAR(255) |  |  | The default data that will appear in the parameter when the associated template is placed into a module. |
| 3 | `DEPENDENCYLIST` | VARCHAR(2000) |  |  | Sometimes the list of entries returned by referential help on one parameter depends on the value(s) in other parameter(s). This field is used to store such a list of dependencies. |
| 4 | `DEPENDENCYON` | DOUBLE |  |  | Not currently used.. |
| 5 | `FORMAT_MASK` | VARCHAR(255) |  |  | The edit format mask to use for parameters based on edit boxes. |
| 6 | `HELP` | VARCHAR(2000) |  |  | The data stored in this field depends on the HELP_TYPE field. If HELP_TYPE is 0 then this field is not used if HELP_TYPE is 1 then this field contains the referential help select command if HELP_TYPE is 2 then this field contains the list of fixed choices that the user selects from |
| 7 | `HELP_TYPE` | CHAR(1) |  |  | Defines the type of help available to the user when instantiating a template within the module. 0 - no help. 1- Referential help A ccl select statement is executed and the results are available for the user to select from 2- Fixed choices list The user selects from an enumerated list of values |
| 8 | `INPUT_TYPE` | CHAR(1) |  |  | input type indicates the type of control to use in editing the parameter. The current values are : C : combo box M : multiline edit box ( Not yet available ) R : radio buttons ( Not yet available ) X : check boxes ( Not yet available ) S : single line edit box L : list box ( Not yet available ) H : single line edit box & referential help button |
| 9 | `MAX_INPUT_LENGTH` | DOUBLE |  |  | Maximum length of string that can be entered as a value of the parameter |
| 10 | `NAME_LENGTH` | DOUBLE |  |  | Length of parameter name |
| 11 | `OPTIMIZABLE_IND` | DOUBLE | NOT NULL |  | Optimizable indicator. 0 means parameter is not optimizable, 1 means parameter is optimizable. |
| 12 | `PAR_NAME` | CHAR(30) |  |  | Name of parameter |
| 13 | `PAR_NUM` | DOUBLE | NOT NULL |  | Indicates the (0-based) index of parameter in the template. |
| 14 | `POS` | DOUBLE |  |  | Indicates the character index at which this parameter begins in the template's text. |
| 15 | `RECONCILE_SCRIPT` | VARCHAR(255) |  |  | The name of the reconciliation script for the parameter. |
| 16 | `REQUIRED_FLAG` | CHAR(1) |  |  | Not currently used |
| 17 | `TEMPLATE_NAME` | CHAR(30) | NOT NULL |  | The name of the template that this parameter is associated to |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VALIDATION` | VARCHAR(2000) |  |  | Not currently used |
| 24 | `VALIDATION_TYPE` | CHAR(1) |  |  | Not currently used |
| 25 | `VERSION` | CHAR(10) | NOT NULL |  | This value is used along with the TEMPLATE_NAME to associate this parameter with the right template. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

