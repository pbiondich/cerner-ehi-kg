# HF_D_EVENT_SOURCE

> HF_D_EVENT_SOURCE table

**Description:** HF_D_EVENT_SOURCE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_SOURCE_DESC` | VARCHAR(60) |  |  | The description for the event source |
| 2 | `EVENT_SOURCE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines an event source |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

