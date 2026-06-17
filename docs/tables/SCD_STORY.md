# SCD_STORY

> Contains an entry for each structured note.

**Description:** Structured Clinical Doc Story (NOTE) table  
**Table type:** ACTIVITY  
**Primary key:** `SCD_STORY_ID`  
**Columns:** 21  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | Author Id |
| 6 | `ENCOUNTER_ID` | DOUBLE | NOT NULL | FK→ | Encounter Id |
| 7 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | Indicates the UI mechanism to be used for data entry against this template. |
| 8 | `EVENT_ID` | DOUBLE | NOT NULL |  | tbd |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `SCD_STORY_ID` | DOUBLE | NOT NULL | PK | SCD Story Unique Id |
| 11 | `SCD_TERM_DATA_ID` | DOUBLE | NOT NULL |  | Used to associate term data to a document. |
| 12 | `STORY_COMPLETION_STATUS_CD` | DOUBLE | NOT NULL |  | story completion status |
| 13 | `STORY_TYPE_CD` | DOUBLE | NOT NULL |  | story type code |
| 14 | `TITLE` | VARCHAR(255) |  |  | Title for note |
| 15 | `UPDATE_LOCK_DT_TM` | DATETIME |  |  | update lock date/time |
| 16 | `UPDATE_LOCK_USER_ID` | DOUBLE | NOT NULL | FK→ | lock holder user id |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCOUNTER_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `UPDATE_LOCK_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [AP_CASE_SYNOPTIC_WS](AP_CASE_SYNOPTIC_WS.md) | `SCD_STORY_ID` |
| [RAD_REPORT](RAD_REPORT.md) | `SCD_STORY_ID` |
| [SCD_PARAGRAPH](SCD_PARAGRAPH.md) | `SCD_STORY_ID` |
| [SCD_SENTENCE](SCD_SENTENCE.md) | `SCD_STORY_ID` |
| [SCD_STORY_CONCEPT](SCD_STORY_CONCEPT.md) | `SCD_STORY_ID` |
| [SCD_STORY_ORG_RELTN](SCD_STORY_ORG_RELTN.md) | `SCD_STORY_ID` |
| [SCD_STORY_PATTERN](SCD_STORY_PATTERN.md) | `SCD_STORY_ID` |
| [SCD_TERM](SCD_TERM.md) | `SCD_STORY_ID` |
| [UCM_CASE_INTEGRATION](UCM_CASE_INTEGRATION.md) | `STORY_ID` |

