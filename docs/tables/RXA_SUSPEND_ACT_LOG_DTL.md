# RXA_SUSPEND_ACT_LOG_DTL

> Stores the failure reasons that occur when a suspended order moves to various stages.

**Description:** Outpatient Pharmacy Suspend Activity Log Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DTL_CD` | DOUBLE | NOT NULL |  | The code value (Code set 4296005) representing the activity detail of the suspended order within the current stage during the suspend order workflow. This can be 0, when there is no additional detail for the current stage. |
| 2 | `ACT_DTL_DT_TM` | DATETIME |  |  | The date/time at which each activity detail row was added or modified. |
| 3 | `DTL_SEQ` | DOUBLE | NOT NULL |  | A number that identifies the sequence of failure details recorded during a suspend activity for a stage. |
| 4 | `REASON_TXT` | VARCHAR(250) |  |  | To document the detail/reason that is not mapped to detail code value in the refill workqueue batch detail status codeset (code set 4296005) |
| 5 | `RXA_SUSPEND_ACT_LOG_DTL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RXA_SUSPEND_ACT_LOG_DTL table. |
| 6 | `RXA_SUSPEND_ACT_LOG_ID` | DOUBLE | NOT NULL | FK→ | The activity taken on a suspended order. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RXA_SUSPEND_ACT_LOG_ID` | [RXA_SUSPEND_ACT_LOG](RXA_SUSPEND_ACT_LOG.md) | `RXA_SUSPEND_ACT_LOG_ID` |

