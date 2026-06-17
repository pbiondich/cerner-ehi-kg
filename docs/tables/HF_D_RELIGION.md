# HF_D_RELIGION

> Dimension table of the list of religions

**Description:** HF_D_RELIGION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RELIGION_CODE` | VARCHAR(10) |  |  | The PHINVADs concept code for religion. |
| 2 | `RELIGION_DESC` | VARCHAR(120) |  |  | The description of the person's religion. |
| 3 | `RELIGION_ID` | DOUBLE |  |  | PRIMARY KEY |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

