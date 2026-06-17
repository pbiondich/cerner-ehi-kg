# EHI_PLAN

> Contains predefined EHI tasks for each request

**Description:** EHI PLAN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EHI_EXTRACT_SIZE_BYTES` | DOUBLE |  |  | The size of the extract file in bytes |
| 2 | `EHI_PLAN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY - Unique generated number that identifies a single row |
| 3 | `EHI_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Request from EHI_QUEUE table. |
| 4 | `PLAN_END_TS` | DATETIME(6) |  |  | The time that the task ended |
| 5 | `PLAN_NAME` | VARCHAR(50) | NOT NULL |  | Plan name for the task |
| 6 | `PLAN_START_TS` | DATETIME(6) |  |  | The time that the task started |
| 7 | `PLAN_STATUS_DETAIL_TXT` | VARCHAR(4000) |  |  | Detailed description of the status |
| 8 | `PLAN_STATUS_TFLG` | VARCHAR(16) |  |  | Current status of the plan |
| 9 | `PLAN_STATUS_TS` | DATETIME(6) |  |  | Date and time that the status was updated |
| 10 | `RETRY_CNT` | DOUBLE |  |  | The number of times the plan has been tried |
| 11 | `STATUS_DETAIL_EXT_CLOB` | LONGTEXT |  |  | Extended space for detail description of the status |
| 12 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EHI_QUEUE_ID` | [EHI_QUEUE](EHI_QUEUE.md) | `EHI_QUEUE_ID` |

