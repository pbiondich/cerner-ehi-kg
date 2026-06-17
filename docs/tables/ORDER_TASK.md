# ORDER_TASK

> Table that contains the tasks that can be done in relation to an order.

**Description:** ORDER TASK  
**Table type:** REFERENCE  
**Primary key:** `REFERENCE_TASK_ID`  
**Columns:** 31  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLPOSITIONCHART_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be charted by any position. |
| 3 | `APP_OBJECT_NAME` | VARCHAR(255) |  |  | For MRNet: To determine what app needs to execute in order to complete the task |
| 4 | `CAPTURE_BILL_INFO_IND` | DOUBLE |  |  | Should charting applications prompt for additional billing information when the task is charted |
| 5 | `CERNERTASK_FLAG` | DOUBLE |  |  | A flag that will identify a certain number of Cerner defined tasks not to be changed by the user. |
| 6 | `CHART_NOT_CMPLT_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be charted as not complete. |
| 7 | `DCP_FORMS_REF_ID` | DOUBLE | NOT NULL |  | This is a unique identifier for the charting form. |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code that will be used for charting the specified task. |
| 9 | `GRACE_PERIOD_MINS` | DOUBLE | NOT NULL |  | Used to calculate the time window during which to update the task. |
| 10 | `IGNORE_REQ_IND` | DOUBLE |  |  | An indicator that identifies whether the required fields will be ignored when the task is invoked from ad hoc charting. |
| 11 | `OVERDUE_MIN` | DOUBLE |  |  | The number of minutes used to define when a task is considered overdue. |
| 12 | `OVERDUE_UNITS` | DOUBLE |  |  | Identifies whether or not overdue value is in terms of minutes or hours |
| 13 | `PROCESS_LOCATION_CD` | DOUBLE | NOT NULL |  | Location of where the task is being performed |
| 14 | `QUICK_CHART_DONE_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be quick charted as done. |
| 15 | `QUICK_CHART_IND` | DOUBLE |  |  | Identifies whether or not the specified task can be quick charted (future functionality) |
| 16 | `QUICK_CHART_NOTDONE_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be quick charted as not done. |
| 17 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | PK | A unique, generated number that is used to identify this task. |
| 18 | `RESCHEDULE_TIME` | DOUBLE |  |  | The number of hours a task can be rescheduled |
| 19 | `RETAIN_TIME` | DOUBLE |  |  | The number of min/hours/weeks that is used to determined if a task is overdue and whether the task should be included on the task list. |
| 20 | `RETAIN_UNITS` | DOUBLE |  |  | The unit that determines if minutes, hours, or weeks are being used in reference to the retain_timefield. (values are 1 - 4) |
| 21 | `TASK_ACTIVITY_CD` | DOUBLE | NOT NULL |  | The type of activity that can be placed upon an order (i.e. chart, review, sign, etc.) |
| 22 | `TASK_DESCRIPTION` | VARCHAR(100) |  |  | The description of the task. |
| 23 | `TASK_DESCRIPTION_KEY` | VARCHAR(100) |  |  | The description of the task in uppercase used to access the table. |
| 24 | `TASK_DESCRIPTION_KEY_A_NLS` | VARCHAR(400) |  |  | TASK_DESCRIPTION_KEY_A_NLS column |
| 25 | `TASK_DESCRIPTION_KEY_NLS` | VARCHAR(202) |  |  | international key field |
| 26 | `TASK_TYPE_CD` | DOUBLE | NOT NULL |  | The task_type_cd, from the task type codeset, that is defined for this task. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (12)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP](ACT_PW_COMP.md) | `REFERENCE_TASK_ID` |
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `REFERENCE_TASK_ID` |
| [ORDER_TASK_POSITION_XREF](ORDER_TASK_POSITION_XREF.md) | `REFERENCE_TASK_ID` |
| [ORDER_TASK_RESPONSE](ORDER_TASK_RESPONSE.md) | `REFERENCE_TASK_ID` |
| [ORDER_TASK_RESPONSE](ORDER_TASK_RESPONSE.md) | `RESPONSE_TASK_ID` |
| [ORDER_TASK_XREF](ORDER_TASK_XREF.md) | `REFERENCE_TASK_ID` |
| [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `REFERENCE_TASK_ID` |
| [OUTCOME_CATALOG](OUTCOME_CATALOG.md) | `REFERENCE_TASK_ID` |
| [PATHWAY_COMP](PATHWAY_COMP.md) | `REFERENCE_TASK_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `REFERENCE_TASK_ID` |
| [TASK_CHARTING_AGENT_R](TASK_CHARTING_AGENT_R.md) | `REFERENCE_TASK_ID` |
| [TASK_DISCRETE_R](TASK_DISCRETE_R.md) | `REFERENCE_TASK_ID` |

