# OMF_IN_OUT_DAYS

> Store active days for rules which use in by/out by calculations

**Description:** Store active days for rules which use in by/out by calculations.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DAY_OF_WEEK` | DOUBLE | NOT NULL |  | Day of week the rule is active for. 0=Sunday;...6=Saturday |
| 2 | `EVENT_NUM` | DOUBLE | NOT NULL |  | Event number such as 'ORDER', 'COMPLETE', 'DRAWN', etc. |
| 3 | `RULE_ID` | DOUBLE | NOT NULL |  | Rule id these days belong to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

