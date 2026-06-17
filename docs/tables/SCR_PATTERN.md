# SCR_PATTERN

> Patterns include "full" encounter patterns, and small fragments built to be included in other patterns.

**Description:** Contains an entry for each defined pattern.  
**Table type:** REFERENCE  
**Primary key:** `SCR_PATTERN_ID`  
**Columns:** 18  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CKI_IDENTIFIER` | VARCHAR(50) |  |  | External identifier for this pattern, used in CKI_SOURCE to form a uniqe external identifier. |
| 6 | `CKI_SOURCE` | CHAR(12) |  |  | External source for this pattern, used with CKI_IDENTIFIER to form a uniqe external identifier. |
| 7 | `DEFINITION` | VARCHAR(255) |  |  | Long Text |
| 8 | `DISPLAY` | VARCHAR(40) | NOT NULL |  | Short Text |
| 9 | `DISPLAY_KEY` | VARCHAR(40) | NOT NULL |  | Key for Display Lookup |
| 10 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | Indicates the UI mechanism to be used for data entry against this template. |
| 11 | `PATTERN_TYPE_CD` | DOUBLE | NOT NULL |  | Pattern type code |
| 12 | `REQUIRED_FIELD_ENFORCEMENT_CD` | DOUBLE | NOT NULL |  | This field will indicate how a pattern should behave if all of its required elements have not been documented. |
| 13 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | PK | Unique ID |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (10)

| From table | Column |
|------------|--------|
| [AP_CASE_SYNOPTIC_WS](AP_CASE_SYNOPTIC_WS.md) | `SCR_PATTERN_ID` |
| [ONC_WORKSHEET](ONC_WORKSHEET.md) | `SCR_PATTERN_ID` |
| [SCD_SENTENCE](SCD_SENTENCE.md) | `CANONICAL_SENTENCE_PATTERN_ID` |
| [SCD_STORY_PATTERN](SCD_STORY_PATTERN.md) | `SCR_PATTERN_ID` |
| [SCR_PARAGRAPH](SCR_PARAGRAPH.md) | `SCR_PATTERN_ID` |
| [SCR_PARAGRAPH_TYPE](SCR_PARAGRAPH_TYPE.md) | `CANONICAL_PATTERN_ID` |
| [SCR_PATTERN_CONCEPT](SCR_PATTERN_CONCEPT.md) | `SCR_PATTERN_ID` |
| [SCR_SENTENCE](SCR_SENTENCE.md) | `CANONICAL_SENTENCE_PATTERN_ID` |
| [SCR_SENTENCE](SCR_SENTENCE.md) | `SCR_PATTERN_ID` |
| [SCR_TERM_HIER](SCR_TERM_HIER.md) | `SCR_PATTERN_ID` |

