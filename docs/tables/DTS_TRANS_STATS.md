# DTS_TRANS_STATS

> This table stores statistics associated with a transcribed document. e.g. number of characters, words, lines, pages, bytes, edit time, etc.

**Description:** dts_trans_stats table stores Dictation/Transcription productivity statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 2 | `APPLICATION_MODE_CD` | DOUBLE | NOT NULL |  | Indicates the mode of the Transcription Application such as Transcription, Correspondence, Clinical Note, Print, etc. |
| 3 | `AUTHOR_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | It serves as a foreign key to the prsnl table. It uniquely identifies the author that the statistics are related to. |
| 4 | `BYTES_CNT` | DOUBLE | NOT NULL |  | It stores the number of bytes that were a part of a current edit session. Note: The session statistics is the difference between the current and the original. |
| 5 | `CHAR_CNT` | DOUBLE | NOT NULL |  | It stores the number of characters (without spaces) of a current edit session. Note: The session statistics is the difference between the current and the original. |
| 6 | `CHAR_PER_WORD` | DOUBLE | NOT NULL |  | It stores the number of characters per word that were a part of a given edit session. |
| 7 | `CHAR_WO_CNT` | DOUBLE | NOT NULL |  | It stores the number of characters with spaces of a document. |
| 8 | `DICTATION_DT_TM` | DATETIME |  |  | It stores the Dictation Date and Time for a document |
| 9 | `DICTATION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `DOC_NAME` | VARCHAR(255) |  |  | It is the name of the document if stored in OCF and if not, it will store the path and the name of the document. |
| 11 | `DTS_TRANS_STATS_ID` | DOUBLE | NOT NULL |  | SEQUENCE:DTS_SEQ The dts_trans_stats_id serve as a unique identifier for a row in the dts_trans_stats table. |
| 12 | `EDIT_TRANS_TM` | DOUBLE | NOT NULL |  | It stores the edit time of the current edit session of a document. |
| 13 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 14 | `END_TRANS_DT_TM` | DATETIME | NOT NULL |  | It stores the date and time that the edit session was completed for a document. |
| 15 | `END_TRANS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 16 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event Cd |
| 17 | `EVENT_ID` | DOUBLE | NOT NULL |  | SEQUENCE:EVENT_SEQ It serves as a foreign key to the clinical event table. |
| 18 | `LINE_CNT` | DOUBLE | NOT NULL |  | It stores the number of lines of a current document. Note: The session statistics is the difference between the current and the original. |
| 19 | `ORIG_BYTES_CNT` | DOUBLE | NOT NULL |  | It stores number of bytes of the original document. |
| 20 | `ORIG_CHAR_CNT` | DOUBLE | NOT NULL |  | It stores the number of characters (without spaces) of the original document. |
| 21 | `ORIG_CHAR_WO_CNT` | DOUBLE | NOT NULL |  | It stores the number of characters (with spaces) of the original document. |
| 22 | `ORIG_LINE_CNT` | DOUBLE | NOT NULL |  | It stores the number of lines of the original document. |
| 23 | `ORIG_PAGE_CNT` | DOUBLE | NOT NULL |  | It stores the number of pages of the original document. |
| 24 | `ORIG_WORD_CNT` | DOUBLE | NOT NULL |  | It stores the number of words of the original document. |
| 25 | `PAGE_CNT` | DOUBLE | NOT NULL |  | It stores the number of pages of the current document. |
| 26 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | person id |
| 27 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL | FK→ | CODE SET: 8 The result_status_cd indicates the level of authenticity of the row of data. This will be AUTHENTICATED, MODIFIED, TRANSCRIBED, or IN PROGRESS. |
| 28 | `SENTENCES_PER_PARA` | DOUBLE | NOT NULL |  | It stores the number of sentences per paragraph of the document. |
| 29 | `START_TRANS_DT_TM` | DATETIME | NOT NULL |  | It stores the date and time that the edit session was started. |
| 30 | `START_TRANS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 31 | `SUBJECT_LINE` | VARCHAR(255) |  |  | It stores the subject (event_title_text) for a document |
| 32 | `TRANSACTION_TYPE_CD` | DOUBLE | NOT NULL |  | It indicates the type of document such as GENERAL, AP, OFFLINE, RAD, ORDER |
| 33 | `TRANS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE:PERSON_ONLY_SEQ It serves as a foreign key to the prsnl table. It uniquely identifies the transcriptionist responsible for the transcription productivity. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `WORDS_PER_SENTENCE` | DOUBLE | NOT NULL |  | It stores the number of words per sentence of the document. |
| 40 | `WORD_CNT` | DOUBLE | NOT NULL |  | It stores the number of words of the current document. Note: The session statistics is the difference between the current and the original. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RESULT_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRANS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

