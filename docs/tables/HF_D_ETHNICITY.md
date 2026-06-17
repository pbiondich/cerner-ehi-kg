# HF_D_ETHNICITY

> Dimension table for ethnicity, a religious, national, racial, or cultural group of persons.

**Description:** HF_D_ETHNICITY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ETHNICITY_DESC` | VARCHAR(60) |  |  | The description of the religious, national, racial, or cultural group of the person. |
| 2 | `ETHNICITY_ID` | DOUBLE |  |  | The Health Data identifier that is unique to the table for ethnicity. |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

