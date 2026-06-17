# DTS_TRANS_QUEUE

> This table stores the data transmitted from the Dictation System to the HNAM system.

**Description:** This table stores data transmitted from the dictation system.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(20) |  |  | Accession Number for the document to be transcribed. |
| 2 | `AUTHOR_NAME` | VARCHAR(100) |  |  | This is an identifier for an Author Name. It can be an alias name. |
| 3 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | The Contributor Source CD is used to de-alias Document Type Alias. |
| 4 | `COSIGN_NAME` | VARCHAR(100) |  |  | This is an identifier for a Cosign Name. It can be an alias name. |
| 5 | `DICTATION_DT_TM` | DATETIME |  |  | Dictation Date and Time for the document to be transcribed. |
| 6 | `DICTATION_LENGTH` | DOUBLE |  |  | Dictation Length of the document in minutes. |
| 7 | `DICTATION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 8 | `DOC_TYPE_ALIAS` | VARCHAR(255) |  |  | This is an identifier for a Document Type. It is an alias for the document type. |
| 9 | `JOB_NBR` | VARCHAR(100) |  |  | Job Number is used to populate the subject field of the document. |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL |  | Order Id for the document to be transcribed. |
| 11 | `PATIENT_INFO` | VARCHAR(200) |  |  | It can be FIN, MRN or Name for the patient to be attached to the document. |
| 12 | `QUEUE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the dts_trans_queue table. It is an internal system assigned number. |
| 13 | `TRANS_NAME` | VARCHAR(100) | NOT NULL |  | This is an identifier for a Transcriptionist's name. It can be an alias name. It is unique key in this table - only one row exist for a transcriptionist. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

