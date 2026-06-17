# PATHWAY_REVIEW

> Contains review information for PowerPlan phases (pathway).

**Description:** PATHWAY_REVIEW  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the PowerPlan phase to which the pathway review belongs. |
| 3 | `PATHWAY_REVIEW_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PATHWAY_REVIEW table. |
| 4 | `PW_ACTION_SEQ` | DOUBLE | NOT NULL |  | The pathway action sequence for the PowerPlan phase that created the review. |
| 5 | `REVIEW_STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the review. |
| 6 | `REVIEW_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of the review. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |

