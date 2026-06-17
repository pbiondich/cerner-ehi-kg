# EEM_JOB

> This table defines pending jobs that need to be processed at a later time

**Description:** EEM job  
**Table type:** ACTIVITY  
**Primary key:** `EEM_JOB_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 2 | `EEM_JOB_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. |
| 3 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is only used by transactions that are tied to a health plan when the health plan is known before submitting the transaction. It is a unique identifier from the health_plan table. |
| 4 | `JOB_STATE_CD` | DOUBLE | NOT NULL |  | The job state is used to track where a job is in its life cycle. Jobs are created for transactions that are to be processed at a later time. A job is created in a pending state and may move to the other states as it is processed. |
| 5 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | This is only used by transactions sent to a payer. A payer is known as a carrier organization. It is a unique identifier from the organization table. |
| 6 | `TEMPLATE_INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Unique identifier for the transaction template |
| 7 | `TRANSACTION_CD` | DOUBLE | NOT NULL |  | The transaction code is used to define the type of transaction for which the job was created. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EEM_BATCH_JOB](EEM_BATCH_JOB.md) | `EEM_JOB_ID` |
| [EEM_TRANSACTION](EEM_TRANSACTION.md) | `EEM_JOB_ID` |

