# PM_FLX_RULE_LIB

> Library of interfield rules used by person management.

**Description:** Person Management Flexible Rule Library  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATEGORY` | VARCHAR(60) |  |  | Classification of a rule. |
| 3 | `DESCRIPTION` | VARCHAR(255) |  |  | Text description of the rule library. |
| 4 | `FIELD` | VARCHAR(255) |  |  | Field in a table associated with a rule library. |
| 5 | `OPTIONS` | VARCHAR(255) |  |  | A text string that identifies options on a library rule. |
| 6 | `REVISION` | VARCHAR(20) |  |  | The particular revision that a rule was added to this library. |
| 7 | `RULE_LIB_ID` | DOUBLE | NOT NULL |  | Unique identifier of a rule library. |
| 8 | `RULE_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | ID where long text description is stored.. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

