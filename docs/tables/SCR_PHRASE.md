# SCR_PHRASE

> This table contains Phrases. A Phrase is made of concatenated concept ckis of the term's hierarchy

**Description:** Contains the concept cki hierarchy of a term.  
**Table type:** REFERENCE  
**Primary key:** `SCR_PHRASE_ID`  
**Columns:** 3  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PHRASE_STRING` | VARCHAR(2000) |  |  | contains the concatenated concept ckis of the term's hierarchy. |
| 2 | `PHRASE_STRING_INDEX` | VARCHAR(255) | NOT NULL |  | phrase_string_index |
| 3 | `SCR_PHRASE_ID` | DOUBLE | NOT NULL | PK | primary key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCD_TERM](SCD_TERM.md) | `SCR_PHRASE_ID` |

