# DOC_TRANSCRIPTION_QUEUE

> List dictated documentations that are ready for transcription

**Description:** Documentation Transcription Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | Identifies the provider who is the author of the documentation. |
| 2 | `DOCUMENTATION_TYPE_CD` | DOUBLE | NOT NULL |  | The documentation type represented by event cd. |
| 3 | `DOC_TRANSCRIPTION_QUEUE_ID` | DOUBLE | NOT NULL |  | Identifies the queue uniquely. Primary Key |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient encounter this documentation belongs to. Can be 0. |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifies a Unique Event set from the CLINICAL EVENT table which is associated to the documentation type code |
| 6 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Indicates the Facility of the patient. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient this documentation belongs to |
| 8 | `PRIORITY_IND` | DOUBLE | NOT NULL |  | Indicates if the documentation is marked as priority item. |
| 9 | `PURGE_IND` | DOUBLE | NOT NULL |  | Indicates that this documentation has been transcribed and is ready to be purged. |
| 10 | `TOTAL_DICTATION_LENGTH` | DOUBLE | NOT NULL |  | Indicated a total length of the dictation for the entire document in minutes. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

