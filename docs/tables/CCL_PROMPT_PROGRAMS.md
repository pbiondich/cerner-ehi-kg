# CCL_PROMPT_PROGRAMS

> List predefined programs that return data for Discern Prompt Library controls.

**Description:** CCL PROMPT PROGRAMS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROL_CLASS_ID` | DOUBLE | NOT NULL |  | A value of 0 indicates the program is a Discern prompt form data source program, and a value of 1 indicates the program is a Discern report prompt form |
| 2 | `DESCRIPTION` | VARCHAR(128) |  |  | Tool tip description for the program. |
| 3 | `DISPLAY` | VARCHAR(128) |  |  | User viewable name of the program. |
| 4 | `GROUP_NO` | DOUBLE | NOT NULL |  | CCL program group access code. |
| 5 | `PROGRAM_NAME` | VARCHAR(128) | NOT NULL |  | CCL program object name. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

