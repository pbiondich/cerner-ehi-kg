# PATHWAY_CUSTOMIZED_PLAN

> This table defines a set of pathway rules that can be used to alter a catalog PowerPlan when it is being added.

**Description:** Pathway Customized Plan  
**Table type:** REFERENCE  
**Primary key:** `PATHWAY_CUSTOMIZED_PLAN_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the customized plan was created |
| 3 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The pathway catalog id of the plan that this customized plan is based on. |
| 4 | `PATHWAY_CUSTOMIZED_PLAN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `PLAN_NAME` | VARCHAR(100) | NOT NULL |  | The name of the customized plan. |
| 6 | `PLAN_NAME_KEY` | VARCHAR(100) | NOT NULL |  | The name key field used to search the table for entries. |
| 7 | `PLAN_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_KEY field for national language support |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that owns this customized plan. |
| 9 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the customized plan. 0 - No Restriction. 1 - In Review - The customized plan has been marked as needing review. 2 - Restricted - The customized plan is restricted and it should not be used, but it should still be visible. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PATHWAY](PATHWAY.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |
| [PATHWAY_CUSTOMIZED_NOTIFY](PATHWAY_CUSTOMIZED_NOTIFY.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |
| [PATHWAY_RULE](PATHWAY_RULE.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |
| [SURG_REQ_PLAN_R](SURG_REQ_PLAN_R.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |

