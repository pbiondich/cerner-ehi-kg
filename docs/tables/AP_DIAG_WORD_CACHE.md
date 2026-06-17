# AP_DIAG_WORD_CACHE

> This table is used as a data store for the automatic (and interactive) diagnostic coder's diagnostic word cache. This table will be read upon startup and any time the source_vocabulary_cd changes to populate the server's internal cache.

**Description:** AP Diagnostic Coding Word Cache  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CACHE_RANKING` | DOUBLE | NOT NULL |  | This column is used to store the ranking of the word within the server's cache the last time the server was shutdown. |
| 2 | `DIAGNOSTIC_WORD` | VARCHAR(255) | NOT NULL |  | This column is used to store the diagnostic words. Each word corresponds to a word from Anatomic Pathology report text. |
| 3 | `LAST_CACHE_IND` | DOUBLE | NOT NULL |  | This column is used as an indication that the corresponding diagnostic word needs to be loaded when the automatic diagnostic coder starts up. |
| 4 | `SNGLR_DIAGNOSTIC_WORD` | VARCHAR(255) | NOT NULL |  | This column is used to store the singular form of the diagnostic word if one was found. |
| 5 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | This column is used to store the source vocabulary code for which the diagnostic word is associated. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WORD_FREQUENCY` | DOUBLE | NOT NULL |  | This column is used to keep track of how many times the word has occurred while automatically coding AP report text. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

