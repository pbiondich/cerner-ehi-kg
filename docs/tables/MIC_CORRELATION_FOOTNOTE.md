# MIC_CORRELATION_FOOTNOTE

> This activity table contains all correlation warnings and/or actions that have occured on the specified report. This table is directly tied to the MIC_REPORT_RESPONSE table.

**Description:** Microbiology Correlation Footnote  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CORR_TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field is used to correlate report footnotes to the previous report. |
| 2 | `FAILURE_REASON_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code assigned to the type of failure the correlation rule is checking. |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the long_text_id associated with the correlation footnote. The footnote text will be stored on the long_text table in an already formatted form so applications can pull this formatted text to display. |
| 4 | `NEW_IND` | DOUBLE | NOT NULL |  | Indicates whether the footnote is newly added or added onto a previous version of the report. |
| 5 | `ORG_TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field is used to correlate report footnotes to linked organism responses in the mic_report_responses table. |
| 6 | `RESPONSE_SEQ` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to the report response from the mic_report_response table thus associating the footnote with the appropriate report response. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field contains the unique value assigned to the correlation footnote which along with the TASK_LOG_ID and RESPONSE_SEQ make up the unique key for this table. The sequence is also the footnote number in a chart view. |
| 8 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to the report task from the mic_report_response table thus associating the footnote with the appropriate report task. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WARNING_IND` | DOUBLE | NOT NULL |  | This field contains a value indicating that the correlation check issued a warning or appended a footnote to the end of the report. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CORR_TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORG_TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |
| `RESPONSE_SEQ` | [MIC_REPORT_RESPONSE](MIC_REPORT_RESPONSE.md) | `RESPONSE_SEQ` |
| `TASK_LOG_ID` | [MIC_REPORT_RESPONSE](MIC_REPORT_RESPONSE.md) | `TASK_LOG_ID` |

