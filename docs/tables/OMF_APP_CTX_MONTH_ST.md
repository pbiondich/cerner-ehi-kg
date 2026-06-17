# OMF_APP_CTX_MONTH_ST

> OMF Application Context Monthly summary table

**Description:** Monthly statistics of data stored on the application_context table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Application number from the application table. |
| 2 | `FREQUENCY` | DOUBLE |  |  | # of times successfully logged out. |
| 3 | `LOG_INS` | DOUBLE |  |  | # of times the user started the application. |
| 4 | `MINUTES` | DOUBLE |  |  | # of minutes connected. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 6 | `START_MONTH` | DATETIME | NOT NULL |  | Month when app was started. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

