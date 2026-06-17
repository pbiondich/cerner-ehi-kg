# DRR_PROCESS_PLAN

> Activity table to store DRR planned action of selected persons.

**Description:** DRR_PROCESS_PLAN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRR_PROCESS_PLAN_ID` | DOUBLE | NOT NULL |  | primary key use sequence DRR_SEQ. |
| 2 | `DRR_PROCESS_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | FK to drr_process_queue. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL |  | person_id to run the process for. |
| 4 | `PRIMARY_PERSON_ID` | DOUBLE |  |  | non-combined-way person_id in case the person_id was added for a combine tree. |
| 5 | `RELATED_ID_REASON` | VARCHAR(100) |  |  | reason related id is included for this action (e.g. combine, free text person. Etc) |
| 6 | `RETRY_COUNT` | DOUBLE |  |  | number of retries |
| 7 | `STATUS` | VARCHAR(50) |  |  | like QUEUED/IN PROCESS/ERROR/DELETE use code_set |
| 8 | `STATUS_DETAILS` | VARCHAR(2000) |  |  | details of latest error; error messages might be in log tables |
| 9 | `STATUS_DT_TM` | DATETIME |  |  | date when the status change occurred |
| 10 | `TASK` | VARCHAR(50) | NOT NULL |  | Type of call to make core proc, external script, external service, etc |
| 11 | `TASK_DETAIL` | VARCHAR(2000) | NOT NULL |  | Detail information about the task: script name, transaction id, etc |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRR_PROCESS_QUEUE_ID` | [DRR_PROCESS_QUEUE](DRR_PROCESS_QUEUE.md) | `DRR_PROCESS_QUEUE_ID` |

