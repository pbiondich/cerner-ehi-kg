# CNT_POWERFORM

> POWERFORM

**Description:** CNT POWERFORM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNT_PF_KEY_ID` | DOUBLE | NOT NULL | FK→ | `Sequence generated ID - FK from CNT_PF_KEY2 |
| 3 | `CNT_POWERFORM_ID` | DOUBLE | NOT NULL |  | each form has a unique reference id that is used to identify the form. each version of the form is identified by a unique instance id. |
| 4 | `DONE_CHARTING_IND` | DOUBLE | NOT NULL |  | Done charting indicator |
| 5 | `ENFORCE_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether to make the user enter all required fields before they are allowed to save. Without this option users can chart forms missing required fields, tasks associated with the results will be in an "in progress" status. |
| 6 | `FORM_EVENT_CD` | DOUBLE | NOT NULL |  | event_cd associated with this form to be used for various purposes. currently is not used |
| 7 | `FORM_EVENT_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 8 | `FORM_EVENT_SET_NAME` | VARCHAR(100) |  |  | Specify an Event Set that is associated with this form to enable charting to print results |
| 9 | `FORM_FLAG` | DOUBLE | NOT NULL |  | 1 - do not allow any charting unless all required fields are filled out.2 - show form in a maximized state0 - not defined |
| 10 | `FORM_HEIGHT` | DOUBLE | NOT NULL |  | Height the form should be sized |
| 11 | `FORM_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for PowerForm |
| 12 | `FORM_WIDTH` | DOUBLE | NOT NULL |  | Width the form should be sized |
| 13 | `TEXT_RENDITION_EVENT_CD` | DOUBLE | NOT NULL |  | event code associated with the text rendered from the form. |
| 14 | `TEXT_RENDITION_EVENT_CDUID` | VARCHAR(100) |  |  | unique identifier value from the CNT_CODE_VALUE_KEY table (code_value_uid) |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_PF_KEY_ID` | [CNT_PF_KEY2](CNT_PF_KEY2.md) | `CNT_PF_KEY_ID` |

