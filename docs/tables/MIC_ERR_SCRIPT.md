# MIC_ERR_SCRIPT

> ERROR TABLE FOR FORMAT SCRIPTS.

**Description:** MIC ERR SCRIPT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NAME` | VARCHAR(100) |  |  | NAME OF THE APPLICATION THAT ERRORED OUT. |
| 2 | `DATA_ID` | DOUBLE | NOT NULL |  | Unique number to identify the groups of records that will be stored on the mic_err_data_r table. |
| 3 | `LOCATION` | VARCHAR(40) |  |  | iDENTIFIER IN SCRIPT WHERE IT ERRORED OUT. |
| 4 | `LOGICAL_IND` | DOUBLE | NOT NULL |  | INDICATOR TO DETERMINE IF THE ERROR IS A LOGICAL ERROR OR A CCL ERROR. |
| 5 | `MESSAGE` | VARCHAR(255) |  |  | The error that occurred. |
| 6 | `SCRIPT_NAME` | VARCHAR(30) | NOT NULL |  | NAME OF THE SCRIPT WHERE THE ERROR OCCURED. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `USER_NAME` | VARCHAR(100) |  |  | THE NAME OF THE USER. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

