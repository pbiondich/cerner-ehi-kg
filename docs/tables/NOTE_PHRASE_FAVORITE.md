# NOTE_PHRASE_FAVORITE

> Contains favorites (very similar to bookmarks) that point to most frequently used auto text template shortcuts.

**Description:** Note Phrase Favorite  
**Table type:** ACTIVITY  
**Primary key:** `NOTE_PHRASE_FAVORITE_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTEXT_URN` | VARCHAR(100) | NOT NULL |  | URN of a context where favorite is saved, ; like "cerner:documentation:ckeditor: " |
| 6 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | The order the favorites are displayed to the user |
| 7 | `LABEL_TXT` | VARCHAR(50) |  |  | Text label of a bookmark (only for non-leaf nodes aka folders) |
| 8 | `NOTE_PHRASE_FAVORITE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the NOTE_PHRASE_FAVORITE table. |
| 9 | `NOTE_PHRASE_ID` | DOUBLE | NOT NULL | FK→ | Pointer to the favorite entry. |
| 10 | `PARENT_NOTE_PHRASE_FAVORITE_ID` | DOUBLE | NOT NULL | FK→ | The parent of this favorite. If different than the primary key value, denotes a folder level. |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who set up this favorite. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_PHRASE_ID` | [NOTE_PHRASE](NOTE_PHRASE.md) | `NOTE_PHRASE_ID` |
| `PARENT_NOTE_PHRASE_FAVORITE_ID` | [NOTE_PHRASE_FAVORITE](NOTE_PHRASE_FAVORITE.md) | `NOTE_PHRASE_FAVORITE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [NOTE_PHRASE_FAVORITE](NOTE_PHRASE_FAVORITE.md) | `PARENT_NOTE_PHRASE_FAVORITE_ID` |

