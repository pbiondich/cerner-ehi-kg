# OMF_APP_CTX_DAY_ST

> Holds daily statistics of information going into the application_context table.

**Description:** OMF Application Context Day summary table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Number of the application which was run. |
| 2 | `FREQUENCY` | DOUBLE |  |  | Number of times logged out successfully. |
| 3 | `LOG_INS` | DOUBLE |  |  | # of times the application was started by the user. |
| 4 | `MINUTES` | DOUBLE |  |  | # of minutes connect for the day. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 6 | `START_DAY` | DATETIME | NOT NULL |  | Day on which the app originally connected. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

