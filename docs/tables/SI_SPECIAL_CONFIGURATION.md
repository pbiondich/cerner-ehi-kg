# SI_SPECIAL_CONFIGURATION

> This table stores the definitions of the SI_Manager Special Configurations.

**Description:** System Integration Special Configurations  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_TYPE_DISPLAY_TXT` | VARCHAR(200) | NOT NULL |  | This extension works in conjunction with the "Alias Type List" extension. In certain cases, the value in the "Alias Type List" extension will not make sense to the user and a different display is needed. This is the format of the field. " ;" The ";" is a delimiter between displayed values. It isn't necessary to populate this extension, but if it is to be used then for each value in the "Alias Type List" there must be a corresponding value in this extension. |
| 2 | `ALIAS_TYPE_LIST_TXT` | VARCHAR(200) | NOT NULL |  | This extension stores available options for alias type meanings, if multiple options are possible. This is the format of the field. " ;" The ";" is a delimiter between stored values. Remember that the extension field is 100 characters in length; steps should be taken to ensure that this length is met, otherwise other options will have to be used. |
| 3 | `CATEGORY_TXT` | VARCHAR(40) | NOT NULL |  | This is the category for which the related value falls under. For example: Orders, Results, Person/Encounter processing. |
| 4 | `CODE_SET` | DOUBLE | NOT NULL |  | Special Configuration's Code Set |
| 5 | `CONFIGURATION_CD` | DOUBLE | NOT NULL |  | Special Configurations Code Value |
| 6 | `CONFIGURATION_CDF_TXT` | VARCHAR(12) | NOT NULL |  | the CDF_Meaning related to the Code Value used to define this record |
| 7 | `DEF_MEANING_TXT` | VARCHAR(20) | NOT NULL |  | Certain values require a specified Alias Meaning be set when the code value is activated. This extension stores the expected default Alias Meaning. |
| 8 | `FIELD_TXT` | VARCHAR(25) | NOT NULL |  | This extension serves multiple purposes. It defines any special processing related to the given code value, for example "ProFit" and the ZM2 code values. It also defines the type of alias required by the related code value Alias Text (If multiple Aliases are possible), Receiving App, and Sending App. Possible values include "Alias Text", "Receiving App", "Sending App", or a pre-defined text that the code has been setup to recognize. |
| 9 | `QUESTION_TXT` | VARCHAR(300) | NOT NULL |  | This extension holds the question/description of the code value that an alias needs to be set for. |
| 10 | `SECTION_TXT` | VARCHAR(40) | NOT NULL |  | This is the section for which the related value falls under. The related code value does not require a section to be set if the Category extension is sufficient for placement in the hierarchy. |
| 11 | `SERVER_VERSION_TXT` | VARCHAR(20) | NOT NULL |  | Indicates which version of the ESI Server is being used. Possible values are "New," "Old," and "Both." |
| 12 | `SI_SPECIAL_CONFIGURATION_ID` | DOUBLE | NOT NULL |  | Unique Identifier |
| 13 | `SORT_SEQUENCE` | DOUBLE | NOT NULL |  | Sort Order for the position of the configuration in the display. |
| 14 | `SUBSECTION_TXT` | VARCHAR(40) | NOT NULL |  | This is the sub-section for which the related value falls under. The related code value does not require a sub-section if either the Section extension was not populated or the Category/Section relationship is sufficient for placement in the hierarchy. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `USE_OPTION_TABLE_IND` | DOUBLE | NOT NULL |  | If the value of this extension is "1", then the code should query the SI_SPECIAL_CONFIG_OPTIONS table for the configured values for the given code value. See the SI_SPECIAL_CONFIG_OPTIONS section for details on this new table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

