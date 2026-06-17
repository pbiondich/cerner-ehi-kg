# DRR_PROCESS_PLAN_HIST

> Activity table to store history DRR planned action of selected persons.

**Description:** DRR_PROCESS_PLAN_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY` | DOUBLE | NOT NULL |  | order in which the process should run; multiple steps run in group in parallel |
| 2 | `DRR_PROCESS_PLAN_HIST_ID` | DOUBLE | NOT NULL |  | primary key use sequence DRR_SEQ. |
| 3 | `DRR_PROCESS_PLAN_ID` | DOUBLE | NOT NULL |  | FK to drr_process_plan. |
| 4 | `DRR_PROCESS_QUEUE_ID` | DOUBLE | NOT NULL |  | FK to drr_process_queue. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL |  | person_id to run the process for. |
| 6 | `PRIMARY_PERSON_ID` | DOUBLE |  |  | root person_id in case the person_id was added for a combine tree. |
| 7 | `RELATED_ID_REASON` | VARCHAR(100) |  |  | reason related id is included for this action (e.g. combine, free text person. Etc) |
| 8 | `RETRY_COUNT` | DOUBLE |  |  | number of retries |
| 9 | `STATUS` | VARCHAR(50) |  |  | like QUEUED/IN PROCESS/ERROR/DELETE use code_set |
| 10 | `STATUS_DETAILS` | VARCHAR(4000) |  |  | details of latest error; error messages might be in log tables |
| 11 | `STATUS_DT_TM` | DATETIME |  |  | date when the status change occurred |
| 12 | `TASK` | VARCHAR(50) | NOT NULL |  | Type of call to make core proc, external script, external service, etc |
| 13 | `TASK_DETAIL` | VARCHAR(2000) | NOT NULL |  | Detail information about the task: script name, transaction id, etc. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

