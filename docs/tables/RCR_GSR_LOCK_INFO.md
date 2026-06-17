# RCR_GSR_LOCK_INFO

> This table provides a locking mechanism for the Gold Standard ETL job.

**Description:** Revenue Cycle Reporting - Gold Standard Reporting Lock Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DIMENSION_INDEX` | DOUBLE | NOT NULL |  | This is an index for an internal structure that tracks the available dimensions. |
| 3 | `LOCK_DT_TM` | DATETIME |  |  | Used to Store the Lock date and time, when the lock was acquired. |
| 4 | `LOCK_IND` | DOUBLE | NOT NULL |  | Indicator to determine if the lock is active. 1 indicates that the lock is active. |
| 5 | `LOCK_NAME` | VARCHAR(255) | NOT NULL |  | Used to store the name of the lock on the process. |
| 6 | `RCR_GSR_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RCR_GSR_CONTEXT table. |
| 7 | `RCR_GSR_LOCK_INFO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single rown on the RCR_GSR_LOCK_INFO table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCR_GSR_CONTEXT_ID` | [RCR_GSR_CONTEXT](RCR_GSR_CONTEXT.md) | `RCR_GSR_CONTEXT_ID` |

