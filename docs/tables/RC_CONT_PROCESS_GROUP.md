# RC_CONT_PROCESS_GROUP

> Data that is common to all processes representing an instance of a continuous workflow model.

**Description:** Revenue Cycle Continuity Process Group  
**Table type:** ACTIVITY  
**Primary key:** `RC_CONT_PROCESS_GROUP_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PAUSE_IND` | DOUBLE | NOT NULL |  | Indicates whether this particular group is paused or not. |
| 5 | `PFT_EVENT_OCCUR_LOG_ID` | DOUBLE | NOT NULL | FK→ | The id of the event occurrence that is unique to this model instance. |
| 6 | `PROCESS_CNT` | DOUBLE | NOT NULL |  | The column stores the value of the number of work items that a model has and updates the value of the counter accordingly (decrements if pbm rules don't qualify)and checks for other child nodes and increments/decrements accordingly |
| 7 | `RC_CONT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Stores the link to the table which stores workflow model reference data. |
| 8 | `RC_CONT_PROCESS_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RC_CONT_PROCESS_GROUP table. |
| 9 | `STATUS_CD` | DOUBLE | NOT NULL |  | Contains the status of the model instance. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_EVENT_OCCUR_LOG_ID` | [PFT_EVENT_OCCUR_LOG](PFT_EVENT_OCCUR_LOG.md) | `PFT_EVENT_OCCUR_LOG_ID` |
| `RC_CONT_MODEL_ID` | [RC_CONT_MODEL](RC_CONT_MODEL.md) | `RC_CONT_MODEL_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PFT_ENCNTR](PFT_ENCNTR.md) | `RC_CONT_PROCESS_GROUP_ID` |
| [RC_CONT_PROCESS](RC_CONT_PROCESS.md) | `RC_CONT_PROCESS_GROUP_ID` |
| [RC_CONT_PROCESS_GRP_PAUSE](RC_CONT_PROCESS_GRP_PAUSE.md) | `RC_CONT_PROCESS_GROUP_ID` |
| [RC_CONT_PROCESS_HIST](RC_CONT_PROCESS_HIST.md) | `RC_CONT_PROCESS_GROUP_ID` |

