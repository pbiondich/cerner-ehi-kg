# SURG_REQ_PLAN_R

> Links a powerplan to a surgical request

**Description:** Surgical Request Plan Reference  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The pathway catalog related to this surgical request plan |
| 3 | `PATHWAY_CUSTOMIZED_PLAN_ID` | DOUBLE | NOT NULL | FK→ | PATHWAY CUSTOMIZED PLAN ID is used to store the favorite ID of the powerplan |
| 4 | `REQUESTED_PLAN_COUNT` | DOUBLE | NOT NULL |  | REQUESTED PLAN COUNT |
| 5 | `SURG_REQ_ID` | DOUBLE | NOT NULL | FK→ | The surgical request related to this surgical request plan |
| 6 | `SURG_REQ_PLAN_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PATHWAY_CUSTOMIZED_PLAN_ID` | [PATHWAY_CUSTOMIZED_PLAN](PATHWAY_CUSTOMIZED_PLAN.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |
| `SURG_REQ_ID` | [SURG_REQ](SURG_REQ.md) | `SURG_REQ_ID` |

