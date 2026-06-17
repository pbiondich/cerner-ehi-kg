# PM_SCH_PREFERENCES

> Search preferences.

**Description:** Search preferences.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Application number. |
| 2 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 3 | `PREFERENCES` | VARCHAR(200) |  |  | Preferences. |
| 4 | `STYLE_FLAG` | DOUBLE | NOT NULL |  | Style. |
| 5 | `TASK_NUMBER` | DOUBLE | NOT NULL |  | The task_number of the application that created the transaction row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

