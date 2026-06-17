# HF_OTH_HS_R_TEST_RULES

> A work table for processing test rules.

**Description:** HF_OTH_HS_R_TEST_RULES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `OUTBOUND_HSS_ID` | DOUBLE | NOT NULL |  | The unique identifier of the organization that this result will be reported to. |
| 3 | `TEST_DETAIL_ID` | DOUBLE | NOT NULL |  | A unique identifier that joins to HF_OTH_HS_R_TEST_DETAIL for this look back rule. Each combination of In and Out tests needs a unique test_detail_id. |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

