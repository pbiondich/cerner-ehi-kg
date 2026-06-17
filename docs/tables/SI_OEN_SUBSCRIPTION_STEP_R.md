# SI_OEN_SUBSCRIPTION_STEP_R

> Defines the relationship and sequence of steps to the subscriptions that they are used in.

**Description:** Open engine Subscription Step relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SI_OEN_STEP_ID` | DOUBLE | NOT NULL | FK→ | ID of the step related to the subscription |
| 2 | `SI_OEN_SUBSCRIPTION_ID` | DOUBLE | NOT NULL | FK→ | ID of the subscription related to the step |
| 3 | `SI_OEN_SUBSCRIPTION_STEP_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `SI_OEN_WORK_POOL_ID` | DOUBLE |  | FK→ | The work thread pool that will be used to execute the step. If not populated, the step will be executed in the caller thread. |
| 5 | `STEP_SEQUENCE` | DOUBLE |  |  | The execution sequence of the step |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_OEN_STEP_ID` | [SI_OEN_STEP](SI_OEN_STEP.md) | `SI_OEN_STEP_ID` |
| `SI_OEN_SUBSCRIPTION_ID` | [SI_OEN_SUBSCRIPTION](SI_OEN_SUBSCRIPTION.md) | `SI_OEN_SUBSCRIPTION_ID` |
| `SI_OEN_WORK_POOL_ID` | [SI_OEN_WORK_POOL](SI_OEN_WORK_POOL.md) | `SI_OEN_WORK_POOL_ID` |

