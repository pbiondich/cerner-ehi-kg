# OMF_MODE_OPERAND

> Holds operands between a rules modes such as for Infection Control - 'Demographics' AND ('Micro' OR 'Lab' OR 'Susceptibiliities')

**Description:** Holds operands between a rules modes.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODE1_CD` | DOUBLE | NOT NULL |  | Mode_cd of first mode. |
| 2 | `MODE2_CD` | DOUBLE | NOT NULL |  | Mode code of second mode. |
| 3 | `OPERAND` | VARCHAR(20) |  |  | Operand to use between mode rule parts such as 'AND' or 'OR'. |
| 4 | `RULE_ID` | DOUBLE | NOT NULL |  | Unique rule_id from the omf_rules table. |
| 5 | `VIS_MODE_CD1` | VARCHAR(255) |  |  | No longer used. |
| 6 | `VIS_MODE_CD2` | VARCHAR(255) |  |  | No longer used. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

