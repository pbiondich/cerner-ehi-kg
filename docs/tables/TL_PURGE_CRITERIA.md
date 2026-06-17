# TL_PURGE_CRITERIA

> Defines the purge and retention criteria for task_activity records.

**Description:** Task List Purge Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ARCHIVE_IND` | DOUBLE |  |  | This field defines whether the qualifying task activity records should be archived before purging. |
| 3 | `ORDER_STATUS_FLAG` | DOUBLE |  |  | This field determines the order statuses that qualify a task_activity record for purge. |
| 4 | `PATIENT_STATUS_FLAG` | DOUBLE |  |  | This field determines the patient status to qualify a task activity record for purge. |
| 5 | `PURGE_ACTIVE_FLAG` | DOUBLE |  |  | This field determines whether the active status of a task activity record qualifies it of rpurge. |
| 6 | `RETENTION_DAYS` | DOUBLE |  |  | This field defines the number of days after a specified event that the task activity record should remain in the active data. |
| 7 | `TASK_STATUS_FLAG` | DOUBLE |  |  | This field determines what task statuses qualify a task activity record for purge. |
| 8 | `TASK_TYPE_CD` | DOUBLE |  |  | This field determines the task types that qualify a task activity record for purge. |
| 9 | `TL_PURGE_DESCRIPTION` | VARCHAR(100) |  |  | This field names the purge criteria entry. |
| 10 | `TL_PURGE_ID` | DOUBLE | NOT NULL |  | This field is a generated number that uniquely identifies the purge criteria record to the system. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

