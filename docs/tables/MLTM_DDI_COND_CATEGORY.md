# MLTM_DDI_COND_CATEGORY

> The child condition (represented by child_cond_ddi_id) is a member within the corresponding parent condition (represented by parent_cond_ddi_id). For example, condition "Felty's Syndrome" is a child of "Rheumatoid Arthritis", which is a child of "Collagen Vascular Disease", which in turn is a child of "Autoimmune Disorder". Interaction text blocks that are associated with a parent condition automatically apply to all children conditions nested below the parent level.

**Description:** Describe the relationship, if any, between the conditions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COND_DDI_ID` | DOUBLE | NOT NULL | FK→ | The child condition (represented by child_condition_id) is a member within the corresponding parent condition (represented by parent_condition_id). |
| 2 | `PARENT_COND_DDI_ID` | DOUBLE | NOT NULL | FK→ | The child condition (represented by child_condition_id) is a member within the corresponding parent condition (represented by parent_condition_id). |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_COND_DDI_ID` | [MLTM_DDI_DESCRIPTION](MLTM_DDI_DESCRIPTION.md) | `DDI_ID` |
| `PARENT_COND_DDI_ID` | [MLTM_DDI_DESCRIPTION](MLTM_DDI_DESCRIPTION.md) | `DDI_ID` |

