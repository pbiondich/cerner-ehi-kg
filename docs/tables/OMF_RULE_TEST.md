# OMF_RULE_TEST

> Stores conditions and values for tests to be run against existing TAT rules in the OMF Turnaround Tool.

**Description:** Stores conditions and values for tests to be run against existing TAT rules.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERSON_ID` | DOUBLE | NOT NULL |  | The person that created the rule test scenario. |
| 2 | `REFERENCE_NUM` | DOUBLE | NOT NULL |  | Number that indicates the condition against which the value will be evaluated against. |
| 3 | `VALUE` | VARCHAR(255) |  |  | The value that will be compared against the condition value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

