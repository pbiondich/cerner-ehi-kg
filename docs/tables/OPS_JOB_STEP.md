# OPS_JOB_STEP

> The operations job step table stores information about a step and its default parameter values. A step relates one to one with a request defined in Application Registration. The parameters are Output_Dist, Message, and Batch_Selection.

**Description:** Operations Job Step  
**Table type:** REFERENCE  
**Primary key:** `OPS_JOB_STEP_ID`  
**Columns:** 24  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_SELECTION` | VARCHAR(2000) |  |  | The default parameter value for batch selection. |
| 6 | `BATCH_SELECTION_IND` | DOUBLE |  |  | Indicates if this step has a batch selection parameter or not. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `MESSAGE` | VARCHAR(100) |  |  | The default parameter value for batch selection. |
| 10 | `OPS_DATE_IND` | DOUBLE |  |  | Indicates if this step has an operations date parameter or not. |
| 11 | `OPS_JOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_JOB. Indicates which job this step belongs to. |
| 12 | `OPS_JOB_STEP_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a step record. |
| 13 | `OUTPUT_DIST` | VARCHAR(100) |  |  | The default parameter value for batch selection. |
| 14 | `OUTPUT_DIST_IND` | DOUBLE |  |  | Indicates if this step has an output distribution parameter or not. |
| 15 | `REQUEST_NUMBER` | DOUBLE |  |  | The request number of the request assigned to the step. |
| 16 | `SEVERITY_IND` | DOUBLE |  |  | Indicates if the OpsExec server will stop processing the job if this step returns an error or if it will continue with the next step. |
| 17 | `STEP_NAME` | VARCHAR(100) |  |  | The name of the request assigned to the step. |
| 18 | `STEP_NUMBER` | DOUBLE |  |  | Number to order the sequence of steps within a job. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `Z_IND` | DOUBLE |  |  | Indicates if no data is returned form the request should be translated as an error or success. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS_JOB_ID` | [OPS_JOB](OPS_JOB.md) | `OPS_JOB_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [OPS_JOB_VERIFY](OPS_JOB_VERIFY.md) | `D_STEP_ID` |
| [OPS_JOB_VERIFY](OPS_JOB_VERIFY.md) | `T_STEP_ID` |
| [OPS_SCHEDULE_JOB_STEP](OPS_SCHEDULE_JOB_STEP.md) | `OPS_JOB_STEP_ID` |
| [OPS_SCHEDULE_PARAM](OPS_SCHEDULE_PARAM.md) | `OPS_JOB_STEP_ID` |

