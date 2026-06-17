# OMF_RULE_TIME_BLK

> Defines effective time intervals for a turnaround time rule. The time intervals are based on a clinical event.

**Description:** Defines effective time intervals for a turnaround time rule.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DAY_OF_WEEK` | DOUBLE | NOT NULL |  | The effective day(s) of the week for the given turnaround time rule. |
| 2 | `RULE_ID` | DOUBLE | NOT NULL |  | The unique identification number for a turnaround time rule. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

