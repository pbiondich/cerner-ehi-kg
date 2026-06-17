# QC_SCHEDULE

> This table is used by QCScheduler.dll as the top level table for setting up the QC Schedule for autoverification.

**Description:** Quality Control Schedule  
**Table type:** ACTIVITY  
**Primary key:** `QC_SCHEDULE_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `ENFORCE_VERIFIED_RESULTS_IND` | DOUBLE | NOT NULL |  | Indicator to show whether or not all results are subject to quality control schedule restriction before results can be verified. |
| 5 | `LOOK_BACK_LIMIT` | DOUBLE | NOT NULL |  | (Currently not implemented) |
| 6 | `MULTI_CONTROL_LIMIT` | DOUBLE | NOT NULL |  | Defines the maximum time period in which the user must run all of the controls under a single step. (Step Group Time Limit) |
| 7 | `QC_SCHEDULE_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific QC schedule for a given instrument. |
| 8 | `REMINDER_MINUTES_NBR` | DOUBLE | NOT NULL |  | A number of minutes before quality control is going to expire and when the user will be notified. |
| 9 | `REMINDER_RESULTS_NBR` | DOUBLE | NOT NULL |  | A number of results that remain before quality control is going to expire and when the user will be notified. |
| 10 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific service resource (i.e. instrument) to which the QC schedule applies. |
| 11 | `START_DT_TM` | DATETIME |  |  | Defines the time used to indicate when the QC cycle is to start each day. The date portion of the field is not used. |
| 12 | `START_IN_OUT_FLAG` | DOUBLE |  |  | (Currently not implemented) |
| 13 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | (Currently not implemented) |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [QC_SCHEDULE_STEP](QC_SCHEDULE_STEP.md) | `QC_SCHEDULE_ID` |

