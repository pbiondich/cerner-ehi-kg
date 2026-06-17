# DRR_PROCESS_QUEUE_HIST

> History table to store all transactions for selected persons on the DRR_PROCESS_QUEUE table. Activity table.

**Description:** DRR_PROCESS_QUEUE_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | original time the row was inserted |
| 2 | `DRR_PROCESS_QUEUE_HIST_ID` | DOUBLE | NOT NULL |  | primary key use sequence DRR_SEQ. |
| 3 | `DRR_PROCESS_QUEUE_ID` | DOUBLE | NOT NULL |  | FK to drr_process_queue. |
| 4 | `DRR_SERVICE_IDENT` | DOUBLE | NOT NULL |  | used by the drr queue service to -reserve- items to work on |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL |  | person to restrict/delete/etc. |
| 6 | `PROCESS_NAME` | VARCHAR(50) | NOT NULL |  | e.g. RESTRICT DELETE_RESTRICT UNRESTRICT DELETE. use code_set |
| 7 | `REASON` | VARCHAR(50) |  |  | comment made by data controller |
| 8 | `REASON_PRSNL_ID` | DOUBLE |  |  | person/data controller which put person on the queue. |
| 9 | `STATUS` | VARCHAR(50) |  |  | like QUEUED/IN PROCESS/ERROR/DELETE use code_set |
| 10 | `STATUS_DETAILS` | VARCHAR(4000) |  |  | details of latest error; error messages might be in log tables |
| 11 | `STATUS_DT_TM` | DATETIME |  |  | date when the status change occurred |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

