# PATHWAY_RULE

> This table defines pathway rules. A pathway rule describe an atomic action that can be done on an object in a PowerPlan.

**Description:** Pathway Rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Enumeration that describes the action part of the rule. 1 - Include Component 2 - Exclude Component 3 - Select Order Sentence (Pharmacy Type, Comment) 4 - Ad hoc Order Component 5 - Ad hoc Outcome Component 6 - Custom IV Set |
| 2 | `ENTITY_ID` | DOUBLE | NOT NULL |  | The id of the entity that the rule will use. |
| 3 | `ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table that is referenced by the entity identification. |
| 4 | `ENTITY_UUID` | VARCHAR(255) |  |  | The string UUID of the new entity. |
| 5 | `ENTITY_VALUE` | DOUBLE | NOT NULL |  | The value that the rule will apply. |
| 6 | `PATHWAY_CUSTOMIZED_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The customized plan that this rule is associated with |
| 7 | `PATHWAY_RULE_ID` | DOUBLE | NOT NULL |  | The Primary Key of the table |
| 8 | `RULE_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence number of the row. |
| 9 | `TARGET_DESCRIPTION` | VARCHAR(500) |  |  | The target description |
| 10 | `TARGET_PARENT_UUID` | VARCHAR(255) |  |  | The target's parent UUID. This will be the sub phase component UUID if the rule is acting on a component inside a sub phase. |
| 11 | `TARGET_UUID` | VARCHAR(255) | NOT NULL |  | The target UUID that the rule is acting on. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CUSTOMIZED_PLAN_ID` | [PATHWAY_CUSTOMIZED_PLAN](PATHWAY_CUSTOMIZED_PLAN.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |

