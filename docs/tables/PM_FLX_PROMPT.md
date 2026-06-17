# PM_FLX_PROMPT

> Table that stores prompt information.

**Description:** PM Flex Prompt  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 46

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CODESET` | DOUBLE |  |  | Codeset value that is used for the prompt. |
| 7 | `DESCRIPTION` | VARCHAR(255) |  |  | Text description of the prompt. |
| 8 | `DISPLAY_ONLY_IND` | DOUBLE |  |  | Specifies whether the control allows the user ability to change data. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXT_OPTIONS_LONG_TEXT_REF_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: LONG_DATA_SEQ Stores the identifier of the row on the long_text_reference table containing the text associated with the options of the prompt. |
| 11 | `FIELD` | VARCHAR(255) |  |  | The table field this prompt is connected to. |
| 12 | `FORMAT` | VARCHAR(100) |  |  | Used to store the default format of the prompt if applicable. |
| 13 | `HELP_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row in the Long_Blob_Reference table containing the text associated with the prompt. |
| 14 | `HL7_DESCRIPTION` | VARCHAR(80) |  |  | Stores the description, according to HL7 definition, for the prompt. |
| 15 | `INFO_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The unique id for a field which contains the long text description for this information. |
| 16 | `LABEL` | VARCHAR(255) |  |  | Text label for the prompt. |
| 17 | `LENGTH` | DOUBLE |  |  | Length of text field. |
| 18 | `MESSAGE` | VARCHAR(255) |  |  | Used to store client site defined help comments for the prompt. |
| 19 | `OPTIONS` | VARCHAR(100) |  |  | A text string that identifies options on a individual prompt. |
| 20 | `PARENT_DATA_SOURCE_NBR` | DOUBLE |  |  | This column is for import purposes mainly. The importer can read the csv and keep track of that row it should map to. Thus allowing us to not overlay clients changes with a new import. |
| 21 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key of the parent table |
| 22 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the parent entitiy. |
| 23 | `PM_FLX_FORM_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: PM_FLX_CONVERSATION_ID_SEQ Stores the identifier of the row on the pm_flx_form table containing the reference data of the flexible form |
| 24 | `PROMPT_ID` | DOUBLE | NOT NULL |  | Unique identifier for a prompt. |
| 25 | `PROMPT_TYPE` | VARCHAR(12) |  |  | The data type of the prompt. For example, a prompt may be text, date, phone, a coded value, etc. |
| 26 | `REQUIRED_IND` | DOUBLE |  |  | Indicates whether this field is required in a conversation. |
| 27 | `RULE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ID of a long text description stored in a table. |
| 28 | `SEQUENCE` | DOUBLE |  |  | This field represents the order in which the prompt appears on the conversation. |
| 29 | `STATIC_IND` | DOUBLE |  |  | Static Indicator (Not Used) |
| 30 | `STYLE` | DOUBLE |  |  | This field is used to further define the display characteristics of a given prompt. |
| 31 | `SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The user defined code_value for the sub type |
| 32 | `SUB_TYPE_MEANING` | VARCHAR(12) |  |  | The cdf_meaning from codeset 356 for a given prompt of type user-defined. |
| 33 | `TAB` | DOUBLE |  |  | Represents the sequential tab number on which the prompt appears in the conversation. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `USER_DEFINED_IND` | DOUBLE |  |  | This indicator will tell us whether this is a 'Cerner' defined field or whether the user created this field at run time. |
| 40 | `VALUE_CD` | DOUBLE | NOT NULL |  | Code Value for the prompt. This column can be a code value from many different code sets. The "default" value of a prompt is stored in this field. It would not be tied to one single code set. |
| 41 | `VALUE_DT_TM` | DATETIME |  |  | The value of the prompt if it is a date/time type. |
| 42 | `VALUE_IND` | DOUBLE |  |  | Field that contains the default value for a prompt with value type of indicatory (short). |
| 43 | `VALUE_NBR` | DOUBLE |  |  | Field that contains the default value for a prompt with a value type of number. |
| 44 | `VALUE_STRING` | VARCHAR(255) |  |  | Field that contains the default value for a prompt with a text value. |
| 45 | `VALUE_TYPE` | VARCHAR(1) |  |  | Indicates the type of default value that is being held. |
| 46 | `VERIFY_IND` | DOUBLE |  |  | Indicates whether or not the prompt should be verified. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXT_OPTIONS_LONG_TEXT_REF_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `HELP_LONG_TEXT_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `PM_FLX_FORM_ID` | [PM_FLX_FORM](PM_FLX_FORM.md) | `PM_FLX_FORM_ID` |
| `RULE_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

