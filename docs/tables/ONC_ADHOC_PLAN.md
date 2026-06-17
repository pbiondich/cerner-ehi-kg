# ONC_ADHOC_PLAN

> Activity data identifying chemotherapy treatment times for an oncology patient.

**Description:** Ad Hoc Oncology Treatment Plan  
**Table type:** ACTIVITY  
**Primary key:** `ONC_ADHOC_PLAN_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | End date for the plan |
| 2 | `ONC_ADHOC_PLAN_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person to whom the plan is associated |
| 4 | `PLAN_NAME` | VARCHAR(100) | NOT NULL |  | Caption for the plan |
| 5 | `START_DT_TM` | DATETIME |  |  | Start date for the plan |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ONC_ADHOC_PHASE](ONC_ADHOC_PHASE.md) | `ONC_ADHOC_PLAN_ID` |

