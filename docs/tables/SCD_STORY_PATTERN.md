# SCD_STORY_PATTERN

> Activty Data, Pattern/Story relation table.

**Description:** Identifies the patterns that were used to to construct the story.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PATTERN_TYPE_CD` | DOUBLE | NOT NULL |  | SCR Pattern Type |
| 2 | `SCD_STORY_ID` | DOUBLE | NOT NULL | FK→ | Unique Story Id |
| 3 | `SCR_PARAGRAPH_TYPE_ID` | DOUBLE | NOT NULL |  | Unique id to paragraph type |
| 4 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | A pattern that was used to construct the story. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCD_STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |
| `SCR_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |

