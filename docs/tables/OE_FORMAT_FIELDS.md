# OE_FORMAT_FIELDS

> Table stores all the fields that will be placed on an order entry format.

**Description:** Order Entry Format Fields  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_FLAG` | DOUBLE |  |  | Flag describes whether the field is accepted or not and how. 0 - Required, 1 - Optional, 2 - No Display, 3 - Display Only |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The type of action to associate this field to the format with. |
| 3 | `CARRY_FWD_PLAN_IND` | DOUBLE | NOT NULL |  | Indicates whether to bring forward the value of this field from one order to the next for PowerPlans. The "field" is the front end format field which in relation to this table is the entire row of this table. A good example would be a Dose field. 1 - Carry Forward, 0- Do not Carry Forward |
| 4 | `CLIN_LINE_IND` | DOUBLE |  |  | An indicator on whether to show this field on the clinical display line. |
| 5 | `CLIN_LINE_LABEL` | VARCHAR(25) |  |  | The label to be shown with the field value on the clinical line. |
| 6 | `CLIN_SUFFIX_IND` | DOUBLE |  |  | An indicator on whether to show the clinical line label as a suffix to the field value. |
| 7 | `CORE_IND` | DOUBLE |  |  | A core field will require the eco server to re-explode orders |
| 8 | `DEFAULT_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier for the default value, if the default value is coded. This field will be empty (zero) for non-coded defaults. |
| 9 | `DEFAULT_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table that the coded default value is from. This field will be empty for non-coded defaults. |
| 10 | `DEFAULT_VALUE` | VARCHAR(100) |  |  | The default value to be used for this field. |
| 11 | `DEF_PREV_ORDER_IND` | DOUBLE |  |  | An indicator on whether to bring forward the value of this field from one order to the next. |
| 12 | `DEPT_LINE_IND` | DOUBLE |  |  | An indicator on whether to show this field on the department display line. |
| 13 | `DEPT_LINE_LABEL` | VARCHAR(25) |  |  | The label to show with the field value on the department display line. |
| 14 | `DEPT_SUFFIX_IND` | DOUBLE |  |  | An indicator on whether to show the department line label as a suffix to the field value. |
| 15 | `DISP_DEPT_YES_NO_FLAG` | DOUBLE |  |  | A flag on whether to show all positive and negative responses to a YES/NO field on the dept displayline. 0 - Display Yes/No, 1 - Display Yes, 2 - Display No |
| 16 | `DISP_YES_NO_FLAG` | DOUBLE |  |  | A flag on whether to show the positive/negative responses to a YES/NO field on the clinical displayline. 0 - Display Yes/No, 1 - Display Yes, 2 - Display No. |
| 17 | `EPILOG_METHOD` | DOUBLE |  |  | For future use. |
| 18 | `FIELD_SEQ` | DOUBLE |  |  | A sequence number identifying the order of all the fields that have been grouped together using thegroup sequence. |
| 19 | `FILTER_PARAMS` | VARCHAR(255) |  |  | Filter parameters order detail list boxes. |
| 20 | `GROUP_SEQ` | DOUBLE |  |  | A sequence number used to identify the ordering of fields on the format. |
| 21 | `INPUT_MASK` | VARCHAR(50) |  |  | For future use |
| 22 | `LABEL_TEXT` | VARCHAR(200) |  |  | The label that should be displayed for this field. |
| 23 | `LOCK_ON_MODIFY_FLAG` | DOUBLE | NOT NULL |  | Indicates if a detail is to be locked for a modify action. A 0 indicates that the detail is not locked and the accept_flag will be honored. 0 - Not locked, 1 - Locked. |
| 24 | `MAX_NBR_OCCUR` | DOUBLE |  |  | The maximum number of times this field can appear on the format. |
| 25 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | The id of the field. |
| 26 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The id of the format. |
| 27 | `PROLOG_METHOD` | DOUBLE |  |  | For future use. |
| 28 | `REQUIRE_COSIGN_IND` | DOUBLE |  |  | An indicator on whether this field, if changed, should cause the cosign logic to be checked. |
| 29 | `REQUIRE_REVIEW_IND` | DOUBLE |  |  | Requires a nurse to review an order placed. Keeps an order in a Pending Review status. |
| 30 | `REQUIRE_VERIFY_IND` | DOUBLE |  |  | Requires Pharmacist to verify an order. In On Hold status until it is verified. |
| 31 | `STATUS_LINE` | VARCHAR(200) |  |  | A display line of information about the field. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 37 | `VALUE_REQUIRED_IND` | DOUBLE |  |  | An indicator on whether the field has to have a value entered. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_TYPE_CD` | [ORDER_ENTRY_FORMAT](ORDER_ENTRY_FORMAT.md) | `ACTION_TYPE_CD` |
| `OE_FORMAT_ID` | [ORDER_ENTRY_FORMAT](ORDER_ENTRY_FORMAT.md) | `OE_FORMAT_ID` |

