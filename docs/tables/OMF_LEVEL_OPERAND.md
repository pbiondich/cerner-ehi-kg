# OMF_LEVEL_OPERAND

> Holds operands between lines of rules.

**Description:** OMF LEVEL OPERAND  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODE_CD` | DOUBLE | NOT NULL |  | The code_value for the rule mode (only used in Infection Control. Examples: susceptibilities, antibiotics, and general lab results). Code set 14199. |
| 2 | `MODE_SEQ1` | DOUBLE | NOT NULL |  | One line of the rule for a mode. |
| 3 | `MODE_SEQ2` | DOUBLE | NOT NULL |  | Second line of the rule for a mode. |
| 4 | `OPERAND` | VARCHAR(20) |  |  | Operand to put between rule lines. |
| 5 | `RULE_ID` | DOUBLE | NOT NULL |  | Rule identifier from the omf_rules table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

