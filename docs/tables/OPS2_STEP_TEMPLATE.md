# OPS2_STEP_TEMPLATE

> Template available to create a step

**Description:** Operations Step Template  
**Table type:** REFERENCE  
**Primary key:** `OPS2_STEP_TEMPLATE_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BATCH_SELECTION_TXT` | VARCHAR(2000) |  |  | User input parameters for the request 'batch selection' field. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ERROR_IF_EMPTY_IND` | DOUBLE | NOT NULL |  | Indicates if no data is returned from the request, should the step be reported as a success or error. |
| 6 | `OPERATOR_MSG_TXT` | VARCHAR(100) | NOT NULL |  | A message to be communicated to the 'operator'. |
| 7 | `OPS2_JOB_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_JOB_TEMPLATE. Indicates to which job template this step template belongs. |
| 8 | `OPS2_STEP_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the OPS2_STEP_TEMPLATE table. |
| 9 | `ORIG_OPS2_STEP_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the step templates. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 10 | `OUTPUT_DISTRIBUTION_TXT` | VARCHAR(100) |  |  | User input parameters for the request 'output distribution' field. |
| 11 | `REQUEST_NAME` | VARCHAR(100) | NOT NULL |  | The request name that this step executes. |
| 12 | `REQUEST_NBR` | DOUBLE | NOT NULL |  | The request number that this step executes. |
| 13 | `STEP_SEQ` | DOUBLE | NOT NULL |  | Number to order the sequence of steps within a job. |
| 14 | `STOP_JOB_ON_ERROR_IND` | DOUBLE | NOT NULL |  | Indicates if the entire job should stop further executing if this step fails (STOP_JOB_ON_ERROR_IND = 1) or continue executing (STOP_JOB_ON_ERROR_IND = 0). |
| 15 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The time zone context to be provided when executing the request of the step. This is often used by reporting solutions to provide the context in which date and time values should be formated. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS2_JOB_TEMPLATE_ID` | [OPS2_JOB_TEMPLATE](OPS2_JOB_TEMPLATE.md) | `OPS2_JOB_TEMPLATE_ID` |
| `ORIG_OPS2_STEP_TEMPLATE_ID` | [OPS2_STEP_TEMPLATE](OPS2_STEP_TEMPLATE.md) | `OPS2_STEP_TEMPLATE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OPS2_STEP](OPS2_STEP.md) | `OPS2_STEP_TEMPLATE_ID` |
| [OPS2_STEP_TEMPLATE](OPS2_STEP_TEMPLATE.md) | `ORIG_OPS2_STEP_TEMPLATE_ID` |

