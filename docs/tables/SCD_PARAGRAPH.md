# SCD_PARAGRAPH

> Activity Data, paragrah table.

**Description:** Contains an entry for each paragraph of each note.  
**Table type:** ACTIVITY  
**Primary key:** `SCD_PARAGRAPH_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | event_identifier |
| 2 | `PARAGRAPH_CLASS_CD` | DOUBLE | NOT NULL |  | Identifiers behavior of a paragraph |
| 3 | `SCD_PARAGRAPH_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for this paragraph |
| 4 | `SCD_STORY_ID` | DOUBLE | NOT NULL | FK→ | The story of which this paragraph is part of. |
| 5 | `SCD_TERM_DATA_ID` | DOUBLE | NOT NULL |  | scd term data identifier |
| 6 | `SCR_PARAGRAPH_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique Identifier for this table |
| 7 | `SEQUENCE_NUMBER` | DOUBLE |  |  | Sequence of this paragraph amongst all other paragraphs |
| 8 | `TRUTH_STATE_CD` | DOUBLE | NOT NULL |  | State of the paragraph term |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCD_STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |
| `SCR_PARAGRAPH_TYPE_ID` | [SCR_PARAGRAPH_TYPE](SCR_PARAGRAPH_TYPE.md) | `SCR_PARAGRAPH_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCD_SENTENCE](SCD_SENTENCE.md) | `SCD_PARAGRAPH_ID` |

