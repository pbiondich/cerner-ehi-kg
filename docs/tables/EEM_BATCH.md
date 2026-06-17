# EEM_BATCH

> EEM_BATCH tracks each batch job submitted

**Description:** EEM batch  
**Table type:** ACTIVITY  
**Primary key:** `EEM_BATCH_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EEM_BATCH_ID` | DOUBLE | NOT NULL | PK | eem batch identifier |
| 2 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of a health plan for the health_plan table |
| 3 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | payer identifier |
| 4 | `SUBMIT_DT_TM` | DATETIME | NOT NULL |  | The date and time for which the bill record is submitted to a payer. |
| 5 | `TRANSACTION_CD` | DOUBLE | NOT NULL |  | transaction code |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EEM_BATCH_JOB](EEM_BATCH_JOB.md) | `EEM_BATCH_ID` |
| [EEM_TRANSACTION](EEM_TRANSACTION.md) | `EEM_BATCH_ID` |

