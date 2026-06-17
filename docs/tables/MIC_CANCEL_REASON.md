# MIC_CANCEL_REASON

> This table contains information regarding canceled microbiology tasks.

**Description:** Microbiology Cancellation Reason  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of code cancelation reason assigned to this task. Cancel reasons are defined on code set 1309. |
| 2 | `CREDIT_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the task being cancelled is to be credited for any charges that have already been incurred. Valid values include: 0 = Not credited 1= Credited |
| 3 | `DETAIL_SEQ` | DOUBLE | NOT NULL |  | This field when used with the task_log_id to query the mic_sus_order_detail table will identify thedetail susceptibility components that were cancelled. |
| 4 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value assigned to the task from the mic_task_log table thus identifying the task being cancelled. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

