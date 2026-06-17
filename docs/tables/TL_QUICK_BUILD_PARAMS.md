# TL_QUICK_BUILD_PARAMS

> Holds the values when quick build functionality is executed.

**Description:** TL QUICK BUILD PARAMS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | The activity_type_cd from the activity type codeset.Column |
| 3 | `ALLPOSITIONCHART_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be charted by any position.Column |
| 4 | `ANCILLARY_SYNONYM_IND` | DOUBLE |  |  | An indicator that identifies whether the task will be built with the ancillary synonym. |
| 5 | `BUILD_EVENT_CD_IND` | DOUBLE |  |  | Identifies whether or not to build an event cdColumn |
| 6 | `BUILD_INPUT_FORM_IND` | DOUBLE |  |  | Defines whether a new input form template should be automatically generated. |
| 7 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog_type_cd from the catalog type codeset.Column |
| 8 | `CHART_NOT_CMPLT_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be charted as not complete.Column |
| 9 | `DCP_SYNONYM_IND` | DOUBLE |  |  | An indicator that identifies whether the task will be built with the dcp synonym. |
| 10 | `INPUT_FORM_CD` | DOUBLE |  |  | The input (charting) form to be associated with the tasks built. |
| 11 | `OVERDUE_MIN` | DOUBLE |  |  | The number of minutes used to define when a task is considered overdue.Column |
| 12 | `OVERDUE_UNITS` | DOUBLE |  |  | Identifies whether the overdue value is in minutes or hours |
| 13 | `PRIMARY_SYNONYM_IND` | DOUBLE |  |  | An indicator that identifies whether the task will be built with the primary synonym. |
| 14 | `QUICK_CHART_DONE_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be quick charted as done.Column |
| 15 | `QUICK_CHART_IND` | DOUBLE |  |  | Identifies whether or not the specified task can be quick charted (future functionality) |
| 16 | `QUICK_CHART_NOTDONE_IND` | DOUBLE |  |  | An indicator that identifies whether this task can be quick charted as not done.Column |
| 17 | `RESCHEDULE_TIME` | DOUBLE |  |  | The number of hours that a task can be rescheduled. |
| 18 | `RETAIN_TIME` | DOUBLE |  |  | The number of minutes/hours/days/weeks that is used to determine if a task is overdue and whether the task should be included on the task list. |
| 19 | `RETAIN_UNITS` | DOUBLE |  |  | The unit that determines if minutes, hours, days, or weeks are being used in reference to the retain_time field. (values are 1 - 4) |
| 20 | `TASK_TYPE_CD` | DOUBLE |  |  | The task_type_cd, from the task type codeset, that is defined for this task. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

