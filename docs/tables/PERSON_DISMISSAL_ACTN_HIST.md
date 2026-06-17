# PERSON_DISMISSAL_ACTN_HIST

> Used for tracking history of changes to the person_dismissal rows.

**Description:** Person Dismissal Action History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of action taken on the dismissal. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have changed. |
| 7 | `NOTIFY_DT_TM` | DATETIME |  |  | The date and time the patient was notified of their impending dismissal via the notification action type. |
| 8 | `PERSON_DISMISSAL_ACTN_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a history row related to the person_dismissal_actn table. |
| 9 | `PERSON_DISMISSAL_ACTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the person dismissal action to which this history row is related. |
| 10 | `PERSON_DISMISSAL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the person dismissal to which this history row is related. |
| 11 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 12 | `REASON_CD` | DOUBLE | NOT NULL |  | The reason for the patient being dismissed at the time of the action. |
| 13 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 14 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

