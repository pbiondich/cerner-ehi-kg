# MIC_QC_COND_SCHEDULE

> This reference table contains a record for each microbiology QC conditional schedule.

**Description:** Micro Quality Control Conditional Schedule  
**Table type:** REFERENCE  
**Primary key:** `COND_SCHEDULE_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COND_SCHEDULE_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value that identifies the QC conditional schedule. |
| 6 | `COND_SCHEDULE_NAME` | VARCHAR(40) | NOT NULL |  | This field contains the unique name for the QC conditional schedule. |
| 7 | `COND_SCHEDULE_NAME_KEY` | VARCHAR(40) | NOT NULL |  | This field is the same as the cond_schedule_name field, only converted to uppercase. |
| 8 | `COND_SCHEDULE_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | COND_SCHEDULE_NAME_KEY_A_NLS column |
| 9 | `COND_SCHEDULE_NAME_KEY_NLS` | VARCHAR(82) | NOT NULL |  | This field is the cond_schedule_name_key with the length doubled and 2 added, for the purpose of sorting non-English. |
| 10 | `PREACTIVE_IND` | DOUBLE | NOT NULL |  | This field indicates whether a conditional schedule can be used only with pre-active lots. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_QC_NODE](MIC_QC_NODE.md) | `COND_SCHEDULE_ID` |
| [MIC_QC_TASK_DETAIL](MIC_QC_TASK_DETAIL.md) | `ACTIVE_COND_SCHEDULE_ID` |
| [MIC_QC_TASK_DETAIL](MIC_QC_TASK_DETAIL.md) | `PREACTIVE_COND_SCHEDULE_ID` |

