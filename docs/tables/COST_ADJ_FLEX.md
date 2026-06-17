# COST_ADJ_FLEX

> Allows markups/discounts to be flexed by multiple entity types (e.g. Item Class, Bill Item)

**Description:** Cost Adjustment Flex  
**Table type:** REFERENCE  
**Primary key:** `COST_ADJ_FLEX_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COST_ADJ_FLEX_ID` | DOUBLE | NOT NULL | PK | Cost Adjustment Flex ID - Primary Key |
| 2 | `COST_ADJ_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Cost Adjustment Schedule ID - Foreign Key |
| 3 | `MIN_CHARGE_AMT` | DOUBLE |  |  | Defines the minimum charge amount |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Entity ID |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Name of the parent entity table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COST_ADJ_SCHED_ID` | [COST_ADJ_SCHED](COST_ADJ_SCHED.md) | `COST_ADJ_SCHED_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [COST_ADJ](COST_ADJ.md) | `COST_ADJ_FLEX_ID` |

