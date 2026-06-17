# QC_STEP_STATUS

> Table used by autoverification to hold the QC Schedule steps status information. This table will indicate the last step's QC that has been completed for a specific service resource and assay combonation.

**Description:** Quality Control Schedule Step Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CURRENT_RESULTS_NBR` | DOUBLE | NOT NULL |  | The current number of results performed since this step was complete. |
| 2 | `INTERVAL_MIN` | DOUBLE | NOT NULL |  | This value indicates how long this step is valid. This value is set for each step in QC Scheduler. |
| 3 | `QC_STEP_STATUS_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the status information for a specific QC schedule step. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Unique code value to indicate the service resource for which this step's QC has been completed. |
| 5 | `STEP_COMPLETE_DT_TM` | DATETIME | NOT NULL |  | Value to hold the date and time this step's QC was completed. This will be the verified date and time of the last QC result entered, which caused this step's QC to be complete. |
| 6 | `STEP_EXPIRE_DT_TM` | DATETIME |  |  | The date and time this step expires. Written initially as the step_complete_dt_tm + verify_minutes_nbr and then updated to the current date and time when the verify_results_nbr matches the current_results_nbr. |
| 7 | `STEP_NBR` | DOUBLE | NOT NULL |  | The step number for which the QC is complete. |
| 8 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Unique code value to indicate the procedure for which QC has been completed for the step. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VERIFY_MINUTES_NBR` | DOUBLE | NOT NULL |  | The number of minutes that results can continue to be verified. |
| 15 | `VERIFY_RESULTS_NBR` | DOUBLE | NOT NULL |  | The number of results that can be verified. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

