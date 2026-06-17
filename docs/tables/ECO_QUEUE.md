# ECO_QUEUE

> This table is the work-list for the ECO server.

**Description:** Explode Continuing Orders Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE |  |  | Order action sequence which write the record. Replaced by action_sequence in eco_action_queue table. |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The action to be done on the instances (e.g. modify, cancel). Replaced by action_type_cd in eco_action_queue table. |
| 3 | `BILL_ONLY_IND` | DOUBLE |  |  | Indicates the instances should be created as bill-only. |
| 4 | `CONT_ORDER_METHOD_FLAG` | DOUBLE |  |  | Flag to define what type of continuing order the parent is.0 - Order; 1 - Task; 2 - Pharmacy |
| 5 | `ECO_FLEX_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This is a foreign key to the ECO_FLEX_SCHEDULE table. |
| 6 | `ECO_JOB_TRACKING_ID` | DOUBLE |  | FK→ | The ECO job tracking row associated to the queue row. A foreign key to the ECO_JOB_TRACKING table. |
| 7 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The effective date and time of the action to be done on the instances. Replaced by effective_dt_tm in eco_action_queue table. |
| 8 | `FREQ_UPDATED_IND` | DOUBLE |  |  | If frequency is modified we communicate it with the eco server using this indicator. Replaced by eco_action_queue table. |
| 9 | `LAST_INSTANCE_DT_TM` | DATETIME |  |  | The date and time the most recent instance was scheduled for this continuing order parent. This is where the ECO server will start its next explosion calculations. |
| 10 | `NEXT_EXPLOSION_DT_TM` | DATETIME |  |  | This is the next time that the order will qualify for explosion by the ECO server. |
| 11 | `NEXT_INSTANCE_DT_TM` | DATETIME |  |  | The next instance for the schedule will be at this time. |
| 12 | `NO_CHARGE_IND` | DOUBLE |  |  | Indicates that instances for this order should not be charged for. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL |  | The ID of the parent order and the primary key of this ECO_QUEUE table.. |
| 14 | `PROCESSING_FLAG` | DOUBLE |  |  | The eco can be flexed by different types of processing. This is where we will store which processing it picks.0 - Normal Processing; 1 - Inpatient Processing; 2 - Outpatient Processing; 3 - Outpatient Schedulable Processing |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ECO_JOB_TRACKING_ID` | [ECO_JOB_TRACKING](ECO_JOB_TRACKING.md) | `ECO_JOB_TRACKING_ID` |

