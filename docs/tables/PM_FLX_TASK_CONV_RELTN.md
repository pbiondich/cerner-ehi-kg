# PM_FLX_TASK_CONV_RELTN

> Relationship Table between Tasks and pm_flx_conversation

**Description:** Person Management Flexible Task Conversation Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | DOUBLE |  |  | Long that relates to the conversation type. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONVERSATION_ID` | DOUBLE |  | FK→ | Conversation_Id from pm_flx_conversation table |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FLX_FORM_TYPE_CD` | DOUBLE | NOT NULL |  | This is a value that is populated when the pm_flx_form_id is populated and it refers to the type of flexible form attached to the task. |
| 10 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | Unique Identifier on Organization Table |
| 11 | `PM_FLX_FORM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the flexible form that the task and conversation are associated to. |
| 12 | `TASK` | DOUBLE |  |  | Number from the application_task table. |
| 13 | `TASK_CONV_RELTN_ID` | DOUBLE | NOT NULL |  | System Generated number that uniquely identifies each row. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONVERSATION_ID` | [PM_FLX_CONVERSATION](PM_FLX_CONVERSATION.md) | `CONVERSATION_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PM_FLX_FORM_ID` | [PM_FLX_FORM](PM_FLX_FORM.md) | `PM_FLX_FORM_ID` |

