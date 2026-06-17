# GROUP_REFERENCE

> Contains the attributes of an input group, including the description, repeating indicator, etc.

**Description:** Group Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 3 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 4 | `BACKCOLOR` | DOUBLE |  |  | Color behind the text for the group frame. |
| 5 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 8 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 9 | `DESCRIPTION` | VARCHAR(100) |  |  | A description of the input group |
| 10 | `DISPLAY` | VARCHAR(50) |  |  | A display of the input group.This column is not populated by mainline Surginet applications and has been deemed OBSOLETE for that solution. It is possible, however, that other applications may use the field. |
| 11 | `DISPLAY_KEY` | VARCHAR(50) |  |  | The display for this input group, in key format -- used for retrieval purposes.This column is not populated by mainline Surginet applications and has been deemed OBSOLETE for that solution. It is possible, however, that other applications may use the field. |
| 12 | `FACENAME` | VARCHAR(50) |  |  | Font used for the font of the text of the group frame. |
| 13 | `FONTEFFECTS` | DOUBLE |  |  | Look of text of the group frame such as italic, bold, underline, and strike through. |
| 14 | `FORECOLOR` | DOUBLE |  |  | Color of the text for the group frame. |
| 15 | `GROUP_CD` | DOUBLE | NOT NULL |  | Identifies an input group used by the Form Builder |
| 16 | `GROUP_REFERENCE_ID` | DOUBLE | NOT NULL |  | Group Reference ID. This column will uniquely identify a row in this table. Can be treated like a PK. |
| 17 | `GROUP_VERSION_NBR` | DOUBLE | NOT NULL |  | A part of the composite primary key, identifying the version number for the input group. |
| 18 | `PART_PROCESS_IND` | DOUBLE |  |  | An indicator of whether or not the version processor is currently running but not yet complete. |
| 19 | `POINTSIZE` | DOUBLE |  |  | Size of the font for the text for the group frame. |
| 20 | `PROMPT_HEIGHT` | DOUBLE |  |  | Height of the text for the group frame. |
| 21 | `PROMPT_WIDTH` | DOUBLE |  |  | Width of the text for the group frame. |
| 22 | `REPEAT_IND` | DOUBLE |  |  | An indicator of whether or not the input group is repeating |
| 23 | `SYSTEM_DEFINED_FLAG` | DOUBLE |  |  | An indicator of the source of definition for this input group, i.e. Form Builder-defined, SurgiNet-defined, DCP-defined. |
| 24 | `UNPROCESS_IND` | DOUBLE |  |  | An indicator of whether or not this input group has been processed by the Version Processor. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

