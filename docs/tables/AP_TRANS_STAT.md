# AP_TRANS_STAT

> This activity table contains entries for all transcription events if a site chooses to record transcription activity. This captures the number of characters and words that are added to a report in each transcription event.

**Description:** AP TRANS STAT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AP_TRANS_STAT_ID` | DOUBLE | NOT NULL |  | This field uniquely defines a row included on the AP_TRANS_STAT table. This field represents a specific transcription event. |
| 2 | `CASE_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the case type code value associated with the transcription event. |
| 3 | `NBR_CHARACTERS` | DOUBLE |  |  | This field contains the total number of additional characters that were added during this transcription event. |
| 4 | `NBR_WORDS` | DOUBLE |  |  | This field contains the total number of additional words that were added during this transcription event. |
| 5 | `PATHOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | This field contains the id of the responsible pathologist for the case corresponding to this transcription event. |
| 6 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique report to which this transcription event is associated. |
| 7 | `TRANSCRIBED_DT_TM` | DATETIME |  |  | The field contains the date and time at which this transcription event occurred. |
| 8 | `TRANSCRIPTIONIST_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique id of the individual who transcribed this particular transcription event. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REPORT_ID` | [CASE_REPORT](CASE_REPORT.md) | `REPORT_ID` |
| `TRANSCRIPTIONIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

