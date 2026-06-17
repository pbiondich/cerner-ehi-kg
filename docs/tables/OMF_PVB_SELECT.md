# OMF_PVB_SELECT

> Select statement used to generate the result set for a scheduled PowerVision view.

**Description:** Select statement used to generate the result set for a scheduled PowerVision vie  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL |  | Result set this select statement is for. |
| 2 | `SELECT_STMT` | VARCHAR(255) |  |  | CCL select statement. |
| 3 | `SEL_SEQ` | DOUBLE | NOT NULL |  | Ordering sequence. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

