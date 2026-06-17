# ONLINE_ITEM_DEFINITION

> Contains the attributes of an input control used by the form builder, including description, prompt, result type, validation information, etc.

**Description:** Online Item Definition  
**Table type:** REFERENCE  
**Primary key:** `ONLINE_ITEM_VERSION_NBR`, `TASK_ASSAY_CD`  
**Columns:** 56  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_SIZE` | DOUBLE |  |  | The accept size for the input control |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BACKCOLOR` | DOUBLE |  |  | Background color of the prompt for the input field. |
| 6 | `CATALOG_TYPE_MEANING` | VARCHAR(12) |  |  | The CDF Meaning of the catalog type that should be used when the result type is "ORC Selection". |
| 7 | `COMBINE_ALLOWED_IND` | DOUBLE |  |  | An indicator of whether or not duplicate controls should be removed when forms are combined. |
| 8 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 10 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 11 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 12 | `DECIMAL_DIGITS` | DOUBLE |  |  | The number of places past the decimal to accept for numeric result types |
| 13 | `DEF_COLUMN_HEADING` | VARCHAR(100) |  |  | The default column heading to be used in the listview of repeating forms for this input control |
| 14 | `DEF_UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | The default unit of measure to use for this input control, if applicable |
| 15 | `DESCRIPTION` | VARCHAR(100) |  |  | A description for the input control |
| 16 | `DISPLAY` | VARCHAR(100) |  |  | A textual display value for the input controlThis column is not populated by mainline Surginet applications and has been deemed OBSOLETE for that solution. It is possible, however, that other applications may use the field. |
| 17 | `DISPLAY_KEY` | VARCHAR(100) |  |  | A textual display value for the input control, in key format, used for retrieval purposes.This column is not populated by mainline Surginet applications and has been deemed OBSOLETE for that solution. It is possible, however, that other applications may use the field. |
| 18 | `FACENAME` | CHAR(50) |  |  | Font to use for the text prompt of the input field. |
| 19 | `FIELD_PROMPT` | VARCHAR(500) |  |  | The prompt to use for this input control |
| 20 | `FIELD_SIZE_FLAG` | DOUBLE |  |  | The accept size of this field, i.e. small, medium, large, memo |
| 21 | `FONTEFFECTS` | DOUBLE |  |  | Effects such as italics, bold, underline, and strike through for the prompt for the input field. |
| 22 | `FORECOLOR` | DOUBLE |  |  | Color of the text of the prompt for the input field. |
| 23 | `INCREMENT_VALUE` | DOUBLE |  |  | The increment value to use for the spin control when the result type is numeric |
| 24 | `MAX_VALUE` | DOUBLE |  |  | The maximum value to be accepted for this input control |
| 25 | `MIN_VALUE` | DOUBLE |  |  | The minimum value to be accepted for this input control |
| 26 | `MNEMONIC_TYPE_MEANING` | VARCHAR(12) |  |  | The CDF Meaning of the mnemonic type that should be used when the result type is "ORC Selection". |
| 27 | `MULTI_RESULT_ALLOWED_IND` | DOUBLE |  |  | An indicator of whether or not multiple results may be documented when this control appears on an input form |
| 28 | `ONLINE_ITEM_DEFINITION_ID` | DOUBLE | NOT NULL |  | Online Item Definition ID. This column will uniquely identify a row in the table. |
| 29 | `ONLINE_ITEM_VERSION_NBR` | DOUBLE | NOT NULL | PK | The version number associated with this input control |
| 30 | `OPTION_BORDER_IND` | DOUBLE |  |  | An indicator of whether or not a border should appear around option buttons and checkboxes |
| 31 | `OVERRIDE_CONTROL_TYPE_FLAG` | DOUBLE |  |  | An override value for the control type to be used for this input control (a default control type exists for each result type), i.e. Text Box, Combo Box, Option Buttons, etc. |
| 32 | `POINTSIZE` | DOUBLE |  |  | Size of the font of the text prompt for the input field. |
| 33 | `PROMPT_HEIGHT` | DOUBLE |  |  | Height of the text prompt for the input field. |
| 34 | `PROMPT_LOCATION_IND` | DOUBLE |  |  | Indicates where the prompt should appear; 0 = left of the control, 1= top of the control |
| 35 | `PROMPT_WIDTH` | DOUBLE |  |  | Width of the text prompt for the input field. |
| 36 | `PROVIDER_PHYS_IND` | DOUBLE |  |  | An indicator of whether or not only physicians should be displayed when the result type is "Provider" |
| 37 | `REPEAT_IND` | DOUBLE |  |  | An indicator of whether or not this is a repeating input control |
| 38 | `REQUIRED_FLAG` | DOUBLE |  |  | An indicator of whether or not this input control is required |
| 39 | `RESTRICTED_IND` | DOUBLE |  |  | An indicator of whether the user should be restricted to the list of available choices only, or allow free-text entry as well. If the control type is checkboxes or options buttons, and the restricted_ind = 0, then "Other" will be added as an option. |
| 40 | `RESULT_FIELD_NAME` | VARCHAR(30) |  |  | NOT CURRENTLY USED |
| 41 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | The result type associated with this input control, i.e. free text, date and time, inventory, provider, etc. |
| 42 | `SIGNATURE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the segment allows or requires electronic signature (0 = does not allow or require signature, 1 = allows signature, 2 = requires signature) |
| 43 | `STATIC_UNIT_IND` | DOUBLE |  |  | An indicator of whether the unit of measure is read only (value=1) or appears as a modifiable combo box (value=0) |
| 44 | `SYSTEM_DEFINED_FLAG` | DOUBLE |  |  | An indicator of the source of definition for this input control, i.e. Form Builder-defined, SurgiNet-defined, DCP-defined |
| 45 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | PK FK→ | A reference (foreign key) to the discrete_task_assay table indicating the discrete task assay for this input control. Also part of the composite primary key |
| 46 | `UNIT_MEAS_IND` | DOUBLE |  |  | An indicator of whether or not unit of measure should be display/accepted for this input control |
| 47 | `UNPROCESSED_IND` | DOUBLE |  |  | An indicator of whether or not this input control has been processed by the Version Processor |
| 48 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 49 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 50 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 51 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 52 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 53 | `VALIDATION_CODESET` | DOUBLE |  |  | The codeset to be used when validating this input control |
| 54 | `VALIDATION_FIELD` | VARCHAR(30) |  |  | The field to be used when validating this input control |
| 55 | `VALIDATION_SCRIPT` | VARCHAR(50) |  |  | The script to be used when validating this input control |
| 56 | `VALIDATION_TABLE_NAME` | VARCHAR(30) |  |  | The table to be used when validating this input control |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [GROUP_DEFINITION](GROUP_DEFINITION.md) | `ONLINE_ITEM_VERSION_NBR` |
| [GROUP_DEFINITION](GROUP_DEFINITION.md) | `TASK_ASSAY_CD` |
| [INPUT_FORM_DEFINITION](INPUT_FORM_DEFINITION.md) | `ONLINE_ITEM_VERSION_NBR` |
| [INPUT_FORM_DEFINITION](INPUT_FORM_DEFINITION.md) | `TASK_ASSAY_CD` |
| [ONLINE_ITEM_INVENTORY_CLASSES](ONLINE_ITEM_INVENTORY_CLASSES.md) | `ONLINE_ITEM_VERSION_NBR` |
| [ONLINE_ITEM_INVENTORY_CLASSES](ONLINE_ITEM_INVENTORY_CLASSES.md) | `TASK_ASSAY_CD` |

