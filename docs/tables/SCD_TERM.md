# SCD_TERM

> Activity Data, terms of the sentence.

**Description:** Hier of terms, which form sentences.  
**Table type:** ACTIVITY  
**Primary key:** `SCD_TERM_ID`  
**Columns:** 29  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | begin effective time zone |
| 7 | `CONCEPT_CKI` | VARCHAR(255) |  |  | The merging of the concept_identifier and concept_source_cd into one string column |
| 8 | `CONCEPT_IDENTIFIER` | CHAR(18) |  |  | Obsolete/no longer used. |
| 9 | `CONCEPT_SOURCE_CD` | DOUBLE | NOT NULL |  | associated concept source code |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `EVENT_ID` | DOUBLE | NOT NULL |  | event_identifier |
| 12 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL |  | This is a foreign key to prsnl which contains the id of the person that made the modification |
| 13 | `PARENT_SCD_TERM_ID` | DOUBLE | NOT NULL | FK→ | parent term id, null if this term is the start of the sentenfe. |
| 14 | `SCD_PHRASE_TYPE_ID` | DOUBLE | NOT NULL |  | link to phrase type table |
| 15 | `SCD_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | The sentence which contains this term |
| 16 | `SCD_STORY_ID` | DOUBLE | NOT NULL | FK→ | The story this term is included in. Used for retrieval performance. |
| 17 | `SCD_TERM_DATA_ID` | DOUBLE | NOT NULL |  | Term_DATA_Id, 0 if no term_data, else = SCR_TERM_ID |
| 18 | `SCD_TERM_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for this term. |
| 19 | `SCR_PHRASE_ID` | DOUBLE | NOT NULL | FK→ | Phrase Id of phrase that is associated with this term |
| 20 | `SCR_TERM_HIER_ID` | DOUBLE | NOT NULL | FK→ | Identifies node in reference canonical from which this node generated. |
| 21 | `SCR_TERM_ID` | DOUBLE | NOT NULL | FK→ | Identifies term in reference canonical from which this term was generated. |
| 22 | `SEQUENCE_NUMBER` | DOUBLE |  |  | orders all terms |
| 23 | `SUCCESSOR_TERM_ID` | DOUBLE | NOT NULL | FK→ | This field will be used as a pointer to the instance of the scd_term that succeeded this one. |
| 24 | `TRUTH_STATE_CD` | DOUBLE | NOT NULL |  | truth state code |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_SCD_TERM_ID` | [SCD_TERM](SCD_TERM.md) | `SCD_TERM_ID` |
| `SCD_SENTENCE_ID` | [SCD_SENTENCE](SCD_SENTENCE.md) | `SCD_SENTENCE_ID` |
| `SCD_STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |
| `SCR_PHRASE_ID` | [SCR_PHRASE](SCR_PHRASE.md) | `SCR_PHRASE_ID` |
| `SCR_TERM_HIER_ID` | [SCR_TERM_HIER](SCR_TERM_HIER.md) | `SCR_TERM_HIER_ID` |
| `SCR_TERM_ID` | [SCR_TERM](SCR_TERM.md) | `SCR_TERM_ID` |
| `SUCCESSOR_TERM_ID` | [SCD_TERM](SCD_TERM.md) | `SCD_TERM_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MAMMO_FIND](MAMMO_FIND.md) | `SCD_TERM_ID` |
| [SCD_TERM](SCD_TERM.md) | `PARENT_SCD_TERM_ID` |
| [SCD_TERM](SCD_TERM.md) | `SUCCESSOR_TERM_ID` |
| [SCD_TERM_DATA](SCD_TERM_DATA.md) | `SCD_TERM_DATA_ID` |

