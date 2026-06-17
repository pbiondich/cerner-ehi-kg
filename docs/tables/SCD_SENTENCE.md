# SCD_SENTENCE

> Activty Data, Sentence

**Description:** Contains an entry for each sentence.  
**Table type:** ACTIVITY  
**Primary key:** `SCD_SENTENCE_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHOR_PERSNL_ID` | DOUBLE | NOT NULL | FK→ | Author Unique Id |
| 6 | `CANONICAL_SENTENCE_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | scr_pattern_id |
| 7 | `CAN_SENT_PAT_CKI_IDENTIFIER` | VARCHAR(50) |  |  | canonical sentence pattern cki identifier |
| 8 | `CAN_SENT_PAT_CKI_SOURCE` | CHAR(12) |  |  | canonical sentence pattern cki identifier |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | event_identifier |
| 10 | `SCD_PARAGRAPH_ID` | DOUBLE | NOT NULL | FK→ | Identifies the paragraph which contains this sentence. |
| 11 | `SCD_SENTENCE_ID` | DOUBLE | NOT NULL | PK | Unique Sentence Id |
| 12 | `SCD_STORY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the story which contains this sentence. |
| 13 | `SCR_TERM_HIER_ID` | DOUBLE | NOT NULL | FK→ | The entry in the reference hier which corresponds to the first saved term in the sentence. |
| 14 | `SENTENCE_CLASS_CD` | DOUBLE | NOT NULL |  | Categorizes sentences with similar behavior and organization |
| 15 | `SENTENCE_TOPIC_CD` | DOUBLE | NOT NULL |  | Topic of sentence, for grouping, text generation |
| 16 | `SEQUENCE_NUMBER` | DOUBLE |  |  | The sequence number of this sentence within the paragraph. |
| 17 | `TEXT_FORMAT_RULE_CD` | DOUBLE | NOT NULL |  | Text format rule code |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_PERSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CANONICAL_SENTENCE_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |
| `SCD_PARAGRAPH_ID` | [SCD_PARAGRAPH](SCD_PARAGRAPH.md) | `SCD_PARAGRAPH_ID` |
| `SCD_STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |
| `SCR_TERM_HIER_ID` | [SCR_TERM_HIER](SCR_TERM_HIER.md) | `SCR_TERM_HIER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCD_TERM](SCD_TERM.md) | `SCD_SENTENCE_ID` |

