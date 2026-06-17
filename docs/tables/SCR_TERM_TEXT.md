# SCR_TERM_TEXT

> The text used to generate text from the term. Can be in many different languages.

**Description:** Contains the text associated with the term.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFINITION` | VARCHAR(255) |  |  | Long Text |
| 2 | `DISPLAY` | VARCHAR(255) | NOT NULL |  | Short Name |
| 3 | `EXTERNAL_REFERENCE_INFO` | VARCHAR(255) |  |  | External text info |
| 4 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | language code |
| 5 | `SCR_TERM_ID` | DOUBLE | NOT NULL | FK→ | Term Identifier |
| 6 | `TEXT_FORMAT_RULE_CD` | DOUBLE | NOT NULL |  | Text format rule code |
| 7 | `TEXT_NEGATION_RULE_CD` | DOUBLE | NOT NULL |  | text negation rule code |
| 8 | `TEXT_REPRESENTATION` | VARCHAR(255) |  |  | text representation |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCR_TERM_ID` | [SCR_TERM](SCR_TERM.md) | `SCR_TERM_ID` |

