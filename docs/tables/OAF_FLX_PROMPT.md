# OAF_FLX_PROMPT

> This table contains all the prompts used to make a profile

**Description:** prompts  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CODESET` | DOUBLE |  |  | Code Set |
| 7 | `DESCRIPTION` | VARCHAR(100) |  |  | This is the description of prompt that is displayed in the front end |
| 8 | `DISPLAY_ONLY_IND` | DOUBLE |  |  | Display only indicator |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `FIELD` | VARCHAR(255) |  |  | Field displays the data mapping of the prompt |
| 11 | `FORMAT` | VARCHAR(100) |  |  | Formatting to apply to this column. |
| 12 | `HL7_DESCRIPTION` | VARCHAR(80) |  |  | HL7_Description |
| 13 | `INFO_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | key to long text table for documents and attachments |
| 14 | `LABEL` | VARCHAR(255) |  |  | The displayed text of the prompt |
| 15 | `LENGTH` | DOUBLE |  |  | Length |
| 16 | `MESSAGE` | VARCHAR(255) |  |  | Message |
| 17 | `OPTIONS` | VARCHAR(100) |  |  | Options |
| 18 | `PARENT_DATA_SOURCE_NBR` | DOUBLE |  |  | This column is for import purpose mainly. The importer can read the csv and keep track of that row it should map to.Thus allowing us to not overlay clients changes with a new import. |
| 19 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent id |
| 20 | `PARENT_ENTITY_NAME` | CHAR(32) |  |  | Parent name |
| 21 | `PROMPT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the oaf_flx_prompt table. It is an internal system assigned number. |
| 22 | `PROMPT_TYPE` | CHAR(12) |  |  | Prompt_type indicates the type of prompt. (text, number etc.) |
| 23 | `REQUIRED_IND` | DOUBLE |  |  | Required_id |
| 24 | `RULE_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Long_text_id |
| 25 | `SEQUENCE` | DOUBLE |  |  | Sequence of the prompts |
| 26 | `STATIC_IND` | DOUBLE |  |  | Static_id |
| 27 | `STYLE` | DOUBLE |  |  | Style |
| 28 | `SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Esi user defined code_value |
| 29 | `TAB` | DOUBLE |  |  | Tab |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 35 | `USER_DEFINED_IND` | DOUBLE |  |  | User_defined_ind |
| 36 | `VALUE_CD` | DOUBLE | NOT NULL |  | Code value |
| 37 | `VALUE_DT_TM` | DATETIME |  |  | Date/time of the value |
| 38 | `VALUE_IND` | DOUBLE |  |  | Value_ind |
| 39 | `VALUE_NBR` | DOUBLE |  |  | Value_nbr |
| 40 | `VALUE_STRING` | VARCHAR(255) |  |  | Value String |
| 41 | `VALUE_TYPE` | CHAR(1) |  |  | Value_type |
| 42 | `VERIFY_IND` | DOUBLE |  |  | Verify_ind |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

