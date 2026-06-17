# AP_OPS_EXCEPTION

> This activity table contains data used to reprocess 'Quick Verify' jobs that have failed. When the job has been processed successfully, the row is deleted.

**Description:** AP Operations Exception  
**Table type:** ACTIVITY  
**Primary key:** `ACTION_FLAG`, `PARENT_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL | PK | Indicates the type of action to be performed on the ops exception order.(-1) Held Verify, (1) Quick Verify Order, (2) Specimen Order, (3) Report Order, (4) Processing Task Order, (5) Specimen Update, (6) Report Update, (7) Processing Task Update |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `FLEX1_ID` | DOUBLE |  |  | Unique identifier to additional information required for a given action (action_flag). |
| 4 | `PARENT_ID` | DOUBLE | NOT NULL | PK | Unique identifier to the parent table which wrote the row. Table is based on the value in action_flag. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_OPS_EXCEPTION_DETAIL](AP_OPS_EXCEPTION_DETAIL.md) | `ACTION_FLAG` |
| [AP_OPS_EXCEPTION_DETAIL](AP_OPS_EXCEPTION_DETAIL.md) | `PARENT_ID` |

