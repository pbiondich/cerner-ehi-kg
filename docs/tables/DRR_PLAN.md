# DRR_PLAN

> Reference table to store high level planned actions for DRR process.

**Description:** DRR_PLAN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRR_PLAN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY. |
| 2 | `DRR_PLAN_URN` | VARCHAR(200) | NOT NULL |  | globally unique identifier to allow for easy updating for tasks e.g. urn:cerner:drr:restrict:ext:srvdir: |
| 3 | `PROCESS_NAME` | VARCHAR(50) | NOT NULL |  | e.g. RESTRICT DELETE_RESTRICT UNRESTRICT DELETE. use code_set |
| 4 | `TASK` | VARCHAR(50) | NOT NULL |  | Type of call : core proc, external script, external service, etc |
| 5 | `TASK_DETAIL` | VARCHAR(2000) | NOT NULL |  | Detail information about the task: script name, transaction id, etc. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

