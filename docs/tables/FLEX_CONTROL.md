# FLEX_CONTROL

> In addition to the Flex Tool, the engine also reads this table for the Flexible Regisrtation.

**Description:** This table is used by Flex to store controls.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BACKCOLOR` | DOUBLE |  |  | This hold a Visual Basic backcolor to describe the backcolor of the control. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CODESET` | DOUBLE |  |  | Codeset. |
| 8 | `DESCRIPTION` | VARCHAR(255) |  |  | This is a description of the control. |
| 9 | `DISPLAY_ONLY_IND` | DOUBLE |  |  | This indicator tells the Engine whether or not this control is display only. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FIELD` | VARCHAR(255) |  |  | This is and actual v500 database field that can and will be used to add update and delete to the database. |
| 12 | `FLEX_CONTROL_ID` | DOUBLE | NOT NULL |  | Sequence to the actual control. |
| 13 | `FONT_BOLD_IND` | DOUBLE |  |  | This indicates whether the given font is bold or not. |
| 14 | `FONT_ITALIC_IND` | DOUBLE |  |  | This indicates whether the given font is italic or not. |
| 15 | `FONT_NAME` | VARCHAR(100) |  |  | The Win32 font name chosen for the given control. |
| 16 | `FONT_SIZE` | DOUBLE |  |  | The Win32 font size chosen for the given control. |
| 17 | `FORECOLOR` | DOUBLE |  |  | The fore color of the given control, it may or may not effect the color of the text. |
| 18 | `HEIGHT` | DOUBLE |  |  | The height of the control given in twips. |
| 19 | `LABEL` | VARCHAR(255) |  |  | The Label for the control. |
| 20 | `LABEL_PSN` | DOUBLE |  |  | The position of the label. |
| 21 | `LEFT` | DOUBLE |  |  | Left value for the control given in twips. |
| 22 | `LONG_TEXT_ID` | DOUBLE |  |  | The long_text_id for the control., Used to tie it to a script |
| 23 | `PARENT_ENTITY_ID` | DOUBLE |  |  | The parent entity id of the control. |
| 24 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The parent name of the control. |
| 25 | `REQUIRED_IND` | DOUBLE |  |  | This tells the engine whether or not a user must enter something in this field. |
| 26 | `TABORDER` | DOUBLE |  |  | The taborder of the given control. |
| 27 | `TOP` | DOUBLE |  |  | The top value in twips for the given control. |
| 28 | `TYPE` | VARCHAR(12) |  |  | This is a string telling us what kind of control we are dealing with. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 34 | `USER_DEFINED_IND` | DOUBLE |  |  | This indicator will tell us whether this is a 'Cerner' defined field or whether the user created this field at run time. |
| 35 | `WIDTH` | DOUBLE |  |  | This is the value of the width of the given control in twips. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

