# ORDER_ENTRY_FIELDS_HIST

> History-The table containing all the fields that may be used to capture information about an order.

**Description:** ORDER ENTRY FIELDS - hist  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_SIZE` | DOUBLE |  |  | The size of the field. |
| 2 | `ACTION_DT_TM` | DATETIME |  |  | date and time when the Action (delete/update) was taken |
| 3 | `ACTION_TAKEN_TFLG` | VARCHAR(30) |  |  | The action taken by the user (delete/update) |
| 4 | `ACTION_USER_ID` | DOUBLE |  |  | user id of the person who took the action (delete/update) |
| 5 | `ALLOW_MULTIPLE_IND` | DOUBLE |  |  | An indicator on whether the field can appear multiple times on a format. |
| 6 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog type this field may be associated with optional. |
| 7 | `CKI` | VARCHAR(30) |  |  | Cerner Knowledge Index for this order entry field |
| 8 | `CODESET` | DOUBLE |  |  | If the field is verified against a codeset - this is the codeset to use. |
| 9 | `COMMON_FLAG` | DOUBLE |  |  | Flag on whether or not to show the field in common order details. |
| 10 | `DESCRIPTION` | VARCHAR(100) |  |  | The description of the field |
| 11 | `EVENT_CD` | DOUBLE | NOT NULL |  | If 'smart defaulting' is being used - the event code for the last result to retrieve as a default. |
| 12 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | Flag used to identify the type of field it it. |
| 13 | `FSI_MAP_TO_OBX_IND` | DOUBLE |  |  | Indicates that this order_entry_field should be considered for outbound interface |
| 14 | `HELP_CONTEXT_ID` | DOUBLE | NOT NULL |  | Future. |
| 15 | `HIDE_FEMALE_IND` | DOUBLE |  |  | Indicates whether this field should be hidden for female patients. |
| 16 | `HIDE_MALE_IND` | DOUBLE |  |  | Indicates whether this field should be hidden for male patients. |
| 17 | `HIDE_MAX_AGE` | DOUBLE |  |  | The age to be older than to hide this field. |
| 18 | `HIDE_MAX_AGE_IND` | DOUBLE |  |  | whether this field should be hidden for patients older than a specified age. |
| 19 | `HIDE_MAX_AGE_UNITS_FLAG` | DOUBLE |  |  | The unit type for the max age. |
| 20 | `HIDE_MIN_AGE` | DOUBLE |  |  | The age to be younger than to hide this field. |
| 21 | `HIDE_MIN_AGE_IND` | DOUBLE |  |  | Indicates whether this field should be hidden for patients under a specified age. |
| 22 | `HIDE_MIN_AGE_UNITS_FLAG` | DOUBLE |  |  | The unit type for the minimum age. |
| 23 | `MAX_VAL` | DOUBLE |  |  | The maximum value possible for a field if it is a numeric type. |
| 24 | `MIN_VAL` | DOUBLE |  |  | The minimum value of the field if it is a numeric type. |
| 25 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | The id of the order entry field. |
| 26 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | The Cerner defined id that identifies what the field is being used for. |
| 27 | `ORDER_ENTRY_FIELDS_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 28 | `PROMPT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier for the prompt test that is located on another table. This could be a task_assay_cd. |
| 29 | `PROMPT_ENTITY_NAME` | VARCHAR(32) |  |  | The table name where the prompt test field is located - for example DISCRETE_TASK_ASSAY. This field is empty for non-prompt fields. |
| 30 | `REQUEST` | DOUBLE |  |  | Future |
| 31 | `SMART_DEFAULTING_FLAG` | DOUBLE |  |  | Flag to identify the type of defaulting this field - update or non-update ocf. |
| 32 | `SPIN_INCREMENT_CNT` | DOUBLE |  |  | For a numeric field the amount a spin control should increment by. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `VALIDATION_TYPE_FLAG` | DOUBLE |  |  | The type of validation to verify the field. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

