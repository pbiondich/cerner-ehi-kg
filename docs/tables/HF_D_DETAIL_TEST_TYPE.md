# HF_D_DETAIL_TEST_TYPE

> This is the HealthFacts dimension table that contains standard values for susceptibility detail test types

**Description:** HF_D_DETAIL_TEST_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_TEST_TYPE_DESC` | VARCHAR(60) |  |  | The description for the susceptibility detail test type. This tells if the susceptibility test was a Blood, CSF, or Urine type test |
| 2 | `DETAIL_TEST_TYPE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a detail test type |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

