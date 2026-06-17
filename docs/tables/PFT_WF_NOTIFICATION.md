# PFT_WF_NOTIFICATION

> This reference table stores all the application that needs to be notified for a given process model, when work item is identified or transitions to a different state.

**Description:** ProFit Workflow Norification  
**Table type:** REFERENCE  
**Primary key:** `PFT_WF_NOTIFICATION_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSESSMENT_IND` | DOUBLE | NOT NULL |  | Indicates if the notification needs to be sent to an application if the work item is in the assessment state. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LISTENER_IDENT` | VARCHAR(250) | NOT NULL |  | Identifier for the listener that will be notified about the work item into and out of state. |
| 6 | `PFT_WF_NOTIFICATION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a ProFit Workflow Notification |
| 7 | `PFT_WF_PROCESS_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related workflow process model. |
| 8 | `PREV_PFT_WF_NOTIFICATION_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the ProFit Workflow Notification information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `RESOLUTION_IND` | DOUBLE | NOT NULL |  | Indicates if the notification needs to be sent to an application if the work item is in a resolution state. |
| 10 | `REVIEW_IND` | DOUBLE | NOT NULL |  | Indicates if the notification needs to be sent to an application if the work item is in a review state. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_WF_PROCESS_MODEL_ID` | [PFT_WF_PROCESS_MODEL](PFT_WF_PROCESS_MODEL.md) | `PFT_WF_PROCESS_MODEL_ID` |
| `PREV_PFT_WF_NOTIFICATION_ID` | [PFT_WF_NOTIFICATION](PFT_WF_NOTIFICATION.md) | `PFT_WF_NOTIFICATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_WF_NOTIFICATION](PFT_WF_NOTIFICATION.md) | `PREV_PFT_WF_NOTIFICATION_ID` |

