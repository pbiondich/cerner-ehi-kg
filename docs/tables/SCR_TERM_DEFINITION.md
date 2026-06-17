# SCR_TERM_DEFINITION

> Used for further details on how to collect and store data associated with the term.

**Description:** For specialized terms. Most terms will not have a data definition  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEF_TEXT` | VARCHAR(255) |  |  | Term Data Definition Text |
| 2 | `FKEY_ENTITY_NAME` | VARCHAR(32) |  |  | fkey_entity_name |
| 3 | `FKEY_ID` | DOUBLE | NOT NULL |  | fkey_id |
| 4 | `SCR_TERM_DEF_ID` | DOUBLE | NOT NULL | FK→ | ScrTermId from ScrTermTable |
| 5 | `SCR_TERM_DEF_KEY` | VARCHAR(255) |  |  | term definition key |
| 6 | `SCR_TERM_DEF_TYPE_CD` | DOUBLE | NOT NULL |  | term type |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCR_TERM_DEF_ID` | [SCR_TERM](SCR_TERM.md) | `SCR_TERM_ID` |

