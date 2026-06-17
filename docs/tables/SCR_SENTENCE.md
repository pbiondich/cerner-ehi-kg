# SCR_SENTENCE

> Contains an entry for each high-level selection within a paragraph.

**Description:** Identifies the sentences within a given pattern.  
**Table type:** REFERENCE  
**Primary key:** `SCR_SENTENCE_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CANONICAL_SENTENCE_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | Sentences of the pattern |
| 2 | `DEFAULT_CD` | DOUBLE | NOT NULL |  | default code |
| 3 | `RECOMMENDED_CD` | DOUBLE | NOT NULL |  | recommneded code |
| 4 | `SCR_PARAGRAPH_TYPE_ID` | DOUBLE | NOT NULL |  | paragraph type id |
| 5 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | Pattern Id |
| 6 | `SCR_SENTENCE_ID` | DOUBLE | NOT NULL | PK | Unique Identifier (PK) |
| 7 | `SENTENCE_CLASS_CD` | DOUBLE | NOT NULL |  | sentence class |
| 8 | `SENTENCE_TOPIC_CD` | DOUBLE | NOT NULL |  | Sentence topic code |
| 9 | `SEQUENCE_NUMBER` | DOUBLE |  |  | sequence number |
| 10 | `TEXT_FORMAT_RULE_CD` | DOUBLE | NOT NULL |  | text format rule code |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CANONICAL_SENTENCE_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |
| `SCR_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ONC_NOMEN_TERM_RELTN](ONC_NOMEN_TERM_RELTN.md) | `SCR_SENTENCE_ID` |
| [SCR_TERM_HIER](SCR_TERM_HIER.md) | `SCR_SENTENCE_ID` |

