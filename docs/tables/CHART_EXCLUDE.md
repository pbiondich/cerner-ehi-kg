# CHART_EXCLUDE

> This table a temporary table to hold disqualified encounters in distr.

**Description:** CHART EXCLUDE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL |  | This is the distribution_id of encounter/distribution being excluded from qualifying encounters. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

