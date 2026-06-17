# SI_OEN_WORK_POOL

> Defines work pools used to execute processing steps.

**Description:** Open Engine Work Pool  
**Table type:** REFERENCE  
**Primary key:** `SI_OEN_WORK_POOL_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CORE_POOL_SIZE` | DOUBLE |  |  | The initial number of threads in the work pool |
| 2 | `KEEP_ALIVE_SECONDS` | DOUBLE |  |  | The amount of time, in seconds, to keep idle threads alive in the work pool |
| 3 | `MAX_POOL_SIZE` | DOUBLE |  |  | The maximum number of threads in the work pool |
| 4 | `QUEUE_CAPACITY` | DOUBLE |  |  | The maximum depth of the task queue for backlogged tasks waiting to be executed by the work pool |
| 5 | `SI_OEN_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | ID that identifies the comserver the workpool is used in |
| 6 | `SI_OEN_WORK_POOL_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WORK_POOL_NAME` | VARCHAR(100) | NOT NULL |  | The name of the work pool |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_OEN_CONTEXT_ID` | [SI_OEN_CONTEXT](SI_OEN_CONTEXT.md) | `SI_OEN_CONTEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_OEN_SUBSCRIPTION_STEP_R](SI_OEN_SUBSCRIPTION_STEP_R.md) | `SI_OEN_WORK_POOL_ID` |

