# RCR_UPDATE_REGISTRY

> This table contains data related to Revenue Cycle analytics clean up and update scripts.

**Description:** Revenue Cycle - Update Registry  
**Table type:** ACTIVITY  
**Primary key:** `RCR_UPDATE_REGISTRY_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_SCRIPT_NAME` | VARCHAR(40) |  |  | Column stores the name of the Audit script associated with a particular cleanup. |
| 2 | `COMPLETED_DT_TM` | DATETIME |  |  | Stores the successful completion date time of the execution script. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | Date and time the row was added. |
| 4 | `EXECUTION_SCRIPT_NAME` | VARCHAR(40) | NOT NULL |  | Name of the cleanup Script. Update script/execution script. |
| 5 | `LOCK_IND` | DOUBLE | NOT NULL |  | Indicates whether the script attached to the execution can be run toghether with another execution script or it has to be run stand alone. |
| 6 | `PROCESS_BY_SLICE_IND` | DOUBLE | NOT NULL |  | Indicates whether we need to process the execution scripts in a batch or single mode. |
| 7 | `QUALIFIED_CNT` | DOUBLE | NOT NULL |  | Number of rows which qualified in the qualification script. |
| 8 | `QUAL_BEGIN_DT_TM` | DATETIME |  |  | Stores the begin date from the input prompt. |
| 9 | `QUAL_END_DT_TM` | DATETIME |  |  | Stores the end date from the input prompt. |
| 10 | `QUAL_SCRIPT_NAME` | VARCHAR(40) | NOT NULL |  | Name of the qualification script which qualifies a list of ids for the cleanup script to clean up. |
| 11 | `RCR_UPDATE_REGISTRY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RCR_UPDATE_REGISTRY table. |
| 12 | `RECOMMENDED_RANGE_MTHS` | DOUBLE | NOT NULL |  | Recommended number of months that the update script can be run. |
| 13 | `SLC_SIZE_CNT` | DOUBLE | NOT NULL |  | Indicates the maximum size of the slice. |
| 14 | `START_DT_TM` | DATETIME |  |  | Stores the date and time the execution script was started. |
| 15 | `SUMMARY_IND` | DOUBLE | NOT NULL |  | Indicates whether the summarization is required or not. |
| 16 | `UPDATE_REQUEST_IDENT` | VARCHAR(40) | NOT NULL |  | The CR number to identify the clean up. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCR_UPDATE_QUAL](RCR_UPDATE_QUAL.md) | `RCR_UPDATE_REGISTRY_ID` |

