# CCL_PROMPT_DEFINITIONS

> Defines the prompts for a CCL program that has had a prompt library control defined.

**Description:** CCL Prompt Definitions  
**Table type:** REFERENCE  
**Primary key:** `PROMPT_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROL` | DOUBLE |  |  | Numerical identifier of the form's control assigned by discern PromptLib. |
| 2 | `DEFAULT_VALUE` | VARCHAR(100) |  |  | Control defined textual representation of the default value. |
| 3 | `DESCRIPTION` | VARCHAR(100) |  |  | User defined status bar help text. |
| 4 | `DISPLAY` | VARCHAR(100) |  |  | User defined label text for the control and the command line display text. |
| 5 | `EXCLUDE_IND` | DOUBLE |  |  | Flag to exclude this prompt from the CCL command line execute statement. |
| 6 | `GROUP_NO` | DOUBLE |  |  | CCL group access number. |
| 7 | `HEIGHT` | DOUBLE |  |  | User definable height (in dialog units) of the control. |
| 8 | `POSITION` | DOUBLE |  |  | Prompt's order in the executable. 0 to n-1 where n is the total number of prompts. |
| 9 | `PROGRAM_NAME` | VARCHAR(128) | NOT NULL |  | CCL program object name this form is attached to. |
| 10 | `PROMPT_ID` | DOUBLE | NOT NULL | PK | CCL program unique, system assigned prompt identifier. |
| 11 | `PROMPT_NAME` | VARCHAR(30) | NOT NULL |  | Unique user defined identifier for the prompt |
| 12 | `RESULT_TYPE_IND` | DOUBLE |  |  | Command line format indicator. 0=quoted string, 3=expression. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `WIDTH` | DOUBLE |  |  | User definable width (in dialog units) of the control. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CCL_PROMPT_PROPERTIES](CCL_PROMPT_PROPERTIES.md) | `PROMPT_ID` |

