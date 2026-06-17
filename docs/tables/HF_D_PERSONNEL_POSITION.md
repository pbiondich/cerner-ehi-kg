# HF_D_PERSONNEL_POSITION

> HF_D_PERSONNEL_POSITION table

**Description:** HF_D_PERSONNEL_POSITION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERSONNEL_POSITION_DESC` | VARCHAR(60) |  |  | The description for the personnel position. |
| 2 | `PERSONNEL_POSITION_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely defines a personnel position record |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, MANUAL should be entered. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

