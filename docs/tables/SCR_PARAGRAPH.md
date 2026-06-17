# SCR_PARAGRAPH

> This table is essentially a many-to-many relation table, exclusively for connecting patterns to paragraph types

**Description:** Identifies the paragraphs contained within a given pattern.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SCR_PARAGRAPH_ID` | DOUBLE | NOT NULL |  | SCR paragraph identifier |
| 2 | `SCR_PARAGRAPH_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the paragraph belonging to the pattern |
| 3 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | Identifies a pattern |
| 4 | `SEQUENCE_NUMBER` | DOUBLE |  |  | Orders paragraphs within the pattern |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCR_PARAGRAPH_TYPE_ID` | [SCR_PARAGRAPH_TYPE](SCR_PARAGRAPH_TYPE.md) | `SCR_PARAGRAPH_TYPE_ID` |
| `SCR_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |

