# OE_FORMAT_FIELDS_HIST

> History-Table stores all the fields that will be placed on an order entry format.

**Description:** Order Entry Format Fields - hist  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_FLAG` | DOUBLE |  |  | Flag describes whether the field is accepted or not and how. 0 - Required - 1 - Optional - 2 - No Display - 3 - Display Only |
| 2 | `ACTION_DT_TM` | DATETIME |  |  | date and time when the Action (delete/update) was taken |
| 3 | `ACTION_TAKEN_TFLG` | VARCHAR(30) |  |  | The action taken by the user (delete/update) |
| 4 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of action to associate this field to the format with. |
| 5 | `ACTION_USER_ID` | DOUBLE |  |  | user id of the person who took the action (delete/update) |
| 6 | `CARRY_FWD_PLAN_IND` | DOUBLE | NOT NULL |  | Indicates whether to bring forward the value of this field from one order to the next for PowerPlans. The ""field"" is the front end format field which in relation to this table is the entire row of this table. A good example would be a Dose field. 1 - Carry Forward - 0- Do not Carry Forward |
| 7 | `CLIN_LINE_IND` | DOUBLE |  |  | An indicator on whether to show this field on the clinical display line. |
| 8 | `CLIN_LINE_LABEL` | VARCHAR(25) |  |  | The label to be shown with the field value on the clinical line. |
| 9 | `CLIN_SUFFIX_IND` | DOUBLE |  |  | An indicator on whether to show the clinical line label as a suffix to the field value. |
| 10 | `CORE_IND` | DOUBLE |  |  | A core field will require the eco server to re-explode orders |
| 11 | `DEFAULT_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier for the default value - if the default value is coded. This field will be empty (zero) for non-coded defaults. |
| 12 | `DEFAULT_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table that the coded default value is from. This field will be empty for non-coded defaults. |
| 13 | `DEFAULT_VALUE` | VARCHAR(100) |  |  | The default value to be used for this field. |
| 14 | `DEF_PREV_ORDER_IND` | DOUBLE |  |  | An indicator on whether to bring forward the value of this field from one order to the next. |
| 15 | `DEPT_LINE_IND` | DOUBLE |  |  | An indicator on whether to show this field on the department display line. |
| 16 | `DEPT_LINE_LABEL` | VARCHAR(25) |  |  | The label to show with the field value on the department display line. |
| 17 | `DEPT_SUFFIX_IND` | DOUBLE |  |  | An indicator on whether to show the department line label as a suffix to the field value. |
| 18 | `DISP_DEPT_YES_NO_FLAG` | DOUBLE |  |  | A flag on whether to show all positive and negative responses to a YES/NO field on the dept displayline. 0 - Display Yes/No - 1 - Display Yes - 2 - Display No |
| 19 | `DISP_YES_NO_FLAG` | DOUBLE |  |  | A flag on whether to show the positive/negative responses to a YES/NO field on the clinical displayline. 0 - Display Yes/No 1 - Display Yes - 2 - Display No. |
| 20 | `EPILOG_METHOD` | DOUBLE |  |  | For future use. |
| 21 | `FIELD_SEQ` | DOUBLE |  |  | A sequence number identifying the order of all the fields that have been grouped together using thegroup sequence. |
| 22 | `FILTER_PARAMS` | VARCHAR(255) |  |  | Filter parameters order detail list boxes. |
| 23 | `GROUP_SEQ` | DOUBLE |  |  | A sequence number used to identify the ordering of fields on the format. |
| 24 | `INPUT_MASK` | VARCHAR(50) |  |  | For future use |
| 25 | `LABEL_TEXT` | VARCHAR(200) |  |  | The label that should be displayed for this field. |
| 26 | `LOCK_ON_MODIFY_FLAG` | DOUBLE | NOT NULL |  | Indicates if a detail is to be locked for a modify action. A 0 indicates that the detail is not locked and the accept_flag will be honored. 0 - Not locked - 1 - Locked. |
| 27 | `MAX_NBR_OCCUR` | DOUBLE |  |  | The maximum number of times this field can appear on the format. |
| 28 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | The id of the field. |
| 29 | `OE_FORMAT_FIELDS_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 30 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | The id of the format. |
| 31 | `PROLOG_METHOD` | DOUBLE |  |  | For future use. |
| 32 | `REQUIRE_COSIGN_IND` | DOUBLE |  |  | An indicator on whether this field - should cause the cosign logic to be checked. |
| 33 | `REQUIRE_REVIEW_IND` | DOUBLE |  |  | Requires a nurse to review an order placed. Keeps an order in a Pending Review status. |
| 34 | `REQUIRE_VERIFY_IND` | DOUBLE |  |  | Requires Pharmacist to verify an order. In On Hold status until it is verified. |
| 35 | `STATUS_LINE` | VARCHAR(200) |  |  | A display line of information about the field. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `VALUE_REQUIRED_IND` | DOUBLE |  |  | An indicator on whether the field has to have a value entered. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

