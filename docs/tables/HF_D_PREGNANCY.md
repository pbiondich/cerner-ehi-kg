# HF_D_PREGNANCY

> HEALTH FACT PREGNANCY DIMENSION

**Description:** HF_D_PREGNANCY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PREGNANCY_DESC` | VARCHAR(60) |  |  | DESCRIPTION |
| 2 | `PREGNANCY_ID` | DOUBLE |  |  | UNIQUE IDENTIFIER FOR A PREGNANCY DIMENSION ROW |
| 3 | `PREGNANCY_SNOMED` | VARCHAR(20) |  |  | The Health Data assigned SNOMED code if applicable for the pregnancy |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user who performed action on this record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

