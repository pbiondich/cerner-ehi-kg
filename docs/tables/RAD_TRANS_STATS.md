# RAD_TRANS_STATS

> The rad_trans_stats table stores transcription productivity statistics at the report level.

**Description:** Radiology Transcription Statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHAR_CNT` | DOUBLE |  |  | The char_cnt column stores the number of characters that were a part of a given reports edit session. |
| 2 | `LAST_TRANS_DT_TM` | DATETIME |  |  | The last_trans_dt_tm column stores the date and time that the reports edit session was completed. |
| 3 | `LAST_TRANS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `LINE_CNT` | DOUBLE |  |  | The line_cnt column stores the number of lines that were a part of a given reports edit session. |
| 5 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The rad_report_id column serves as a foreign key to the rad_report table. It uniquely identifies the report that the transcription statistics are related to. |
| 6 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence along with the rad_report_id column serve as a unique identifier for a row on the rad_trans_stats table. |
| 7 | `TRANS_PRSNL_ID` | DOUBLE |  | FK→ | The trans_prsnl_id serves as a foreign key to the prsnl table. It uniquely identifies the transcriptionist responsible for the transcription productivity. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `WORD_CNT` | DOUBLE |  |  | The word_cnt column stores the number of words that were a part of a given reports edit session. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |
| `TRANS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

