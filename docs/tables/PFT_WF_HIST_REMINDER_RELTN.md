# PFT_WF_HIST_REMINDER_RELTN

> Stores information about a work item escalation/reminder.

**Description:** ProFit Work Flow History Reminder Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | The time the reminder was enqueued. |
| 2 | `DUE_DT_TM` | DATETIME | NOT NULL |  | The time that the reminder is intended to be sent out. |
| 3 | `PFT_QUEUE_ITEM_WF_HIST_ID` | DOUBLE | NOT NULL | FK→ | References the pft_queue_item_wf_hist row that is/was active when the reminder was sent. |
| 4 | `PFT_WF_HIST_REMINDER_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information about a work item escalation/reminder |
| 5 | `PFT_WF_ISSUE_CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | References the pft_wf_issue_criteria that defines the reminder options for the work item (at the time this reminder was sent) |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who received the reminder, or 0 if the reminder hasn't been sent yet. |
| 7 | `RECIPIENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The recipient of the reminder, which indicates who the reminder will be sent to relative to the work item. |
| 8 | `REMINDER_TYPE_FLAG` | DOUBLE | NOT NULL |  | The method of sending the reminder (via Discern Notify or a work item). |
| 9 | `SENT_DT_TM` | DATETIME |  |  | The time the reminder was sent out, or null if it hasn't been sent yet. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `WORKFLOW_STATE_FLAG` | DOUBLE | NOT NULL |  | The state of the work item that the reminder is sent out on (assessment, resolution, review). 0 - Assessment; 1 - Resolution; 2 - Review; 3 - Manual |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_QUEUE_ITEM_WF_HIST_ID` | [PFT_QUEUE_ITEM_WF_HIST](PFT_QUEUE_ITEM_WF_HIST.md) | `PFT_QUEUE_ITEM_WF_HIST_ID` |
| `PFT_WF_ISSUE_CRITERIA_ID` | [PFT_WF_ISSUE_CRITERIA](PFT_WF_ISSUE_CRITERIA.md) | `PFT_WF_ISSUE_CRITERIA_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

