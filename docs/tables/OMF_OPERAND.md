# OMF_OPERAND

> Holds operands between items in one line of a rule.

**Description:** OMF OPERAND  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONDITION_LEVEL` | DOUBLE |  |  | No longer used. |
| 2 | `MODE_CD` | DOUBLE | NOT NULL |  | The code_value for the rule mode (only used in Infection Control. Examples: susceptibilities, antibiotics, and general lab results). Code set 14199. |
| 3 | `MODE_LEVEL` | DOUBLE |  |  | No longer used. |
| 4 | `MODE_SEQ` | DOUBLE | NOT NULL |  | Determines what order to display lines on the rule builder grid. Also used with omf_mode_operand table to determine what operand goes between mode sequences. |
| 5 | `OPERAND` | VARCHAR(20) |  |  | '=' or '!=' - Determines whether we are excluding or including the value being tested. |
| 6 | `OPERAND_SEQ` | DOUBLE | NOT NULL |  | Used when a string field on this table exceeds 255 characters. |
| 7 | `RULE_ID` | DOUBLE | NOT NULL |  | Unique rule_id from the omf_rules table. |
| 8 | `VALUE1` | VARCHAR(100) |  |  | Database value of a qualifiers (on left side of operand). |
| 9 | `VALUE2` | VARCHAR(100) |  |  | Database value of a qualifiers (on right side of operand). Can be more than one of these per 'VALUE1'. |
| 10 | `VALUE2_SEQ` | DOUBLE | NOT NULL |  | Used if more than one 'VALUE2' per 'VALUE1'. |
| 11 | `VALUE_SEQ` | DOUBLE | NOT NULL |  | Sequence of qualifiers per mode sequence. |
| 12 | `VIS_VALUE1` | VARCHAR(255) |  |  | On screen value of VALUE1. |
| 13 | `VIS_VALUE2` | VARCHAR(255) |  |  | On screen value of VALUE2. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

