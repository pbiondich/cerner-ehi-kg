# FLEX_FORM

> Used to store the client created flex forms.

**Description:** FLEX FORM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | DOUBLE |  |  | This is an integer that is assigned to the form to tell the engine what this forms actual 'action' will be. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DESCRIPTION` | VARCHAR(255) |  |  | This is the caption of the form or name of it. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FLEX_DATA_SOURCE_ID` | DOUBLE |  |  | This id is stamped by the form builder so we can tell if what data source a given form belongs to. |
| 10 | `FLEX_FORM_ID` | DOUBLE | NOT NULL |  | This is a sequence that is assigned to each form as needed. |
| 11 | `FUNCTION` | DOUBLE |  |  | This is used by the engine and is selectable in the Flex Tool to tell us which function a particular form fulfills. |
| 12 | `HEIGHT` | DOUBLE |  |  | This is the value in twips of the forms height. |
| 13 | `ICON_INDEX` | DOUBLE |  |  | This is the icon_index of the particular form. No longer used. |
| 14 | `LONG_TEXT_ID` | DOUBLE |  |  | This is a id that tells us which icon we have stored for this form. |
| 15 | `PRODUCT` | DOUBLE |  |  | This column will allow us to differentiate between different product groups and their data. |
| 16 | `TASK` | DOUBLE |  |  | This is a number that coincides with a task number that we can use for security reasons to lock out a given user. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WIDTH` | DOUBLE |  |  | This is the value in twips of the width of the flex form. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

