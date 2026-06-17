# HF_OTH_HS_RUN

> Work table that is used during HealthSentry loads.

**Description:** HF_OTH_HS_RUN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_DT_TM` | DATETIME |  |  | The begin date and time of the period being processed. |
| 3 | `END_DT_TM` | DATETIME |  |  | The end date and time of the period being processed. |
| 4 | `HF_RUN_GROUP_ID` | DOUBLE | NOT NULL |  | The identifier of the group of runs. |
| 5 | `HF_RUN_KEY` | DOUBLE | NOT NULL |  | Unique identifier of the Informatic run. |
| 6 | `MNEMONIC` | VARCHAR(40) |  |  | The mnemonic of the client run logged. |
| 7 | `PROCESS_RANGE_END_DT_TM` | DATETIME |  |  | The end date of the processing range. |
| 8 | `PROCESS_RANGE_START_DT_TM` | DATETIME |  |  | The start date of the processing range. |
| 9 | `RUN_ID` | DOUBLE | NOT NULL |  | The Run Identifier. |
| 10 | `RUN_TYPE_FLG` | DOUBLE |  |  | A numeric code indicating what type of workflow is or was running at the time of this processing. The codes are: 1=w_HF_Reference_Load, 2=w_HS_Cln_EDW, 3=w_DM_HealthSentry, 4=w_HF_DM_i2b2, 5=w_HF_DM_Critical_Outcomes, 6=w_CERN_DM, 10=w_HF_Blended_View, 11=w_DH_DM, 12=w_HF_CRN or =UNKNOWN_WORKFLOW |
| 11 | `STATUS_FLG` | DOUBLE |  |  | The current or last status of this run. The codes are: 1=COMPLETE, 2=DISABLED, 3=FAILED, 4=STOPPED, 5=ABORTED, 6=IN PROCESS, 15=TERMINATED or =MISSING. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

