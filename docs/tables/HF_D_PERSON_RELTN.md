# HF_D_PERSON_RELTN

> This is the HealthFacts dimension table that contains standard values for person relationships

**Description:** HF_D_PERSON_RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERSON_RELTN_DESC` | VARCHAR(60) |  |  | A description of the type of relationship between two people |
| 2 | `PERSON_RELTN_DISPLAY` | VARCHAR(40) |  |  | A short display value for the type of relationship between two people |
| 3 | `PERSON_RELTN_ID` | DOUBLE | NOT NULL |  | Primary key to the table. |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

