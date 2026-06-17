# MIC_EVENT_FOOTNOTE

> This table contains a record for susceptibility footnote that occurs for the orderable procedure. Each time a susceptibility footnote is added, modified or deleted a record is written to this table. Results that are corrected have the original results p

**Description:** Event table for footnotes.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARTABLE_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the susceptibility footnote is to be included on the patient reports and displayed in inquiry applications. Valid values include:0 = Not Chartable1 = Chartable |
| 2 | `EKM_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the event footnote has been generated from an expert knowledge module. Valid values include:0 = Not expert knowledge module generated1 = Expert knowledge module generated |
| 3 | `EVENT_DETAIL_SEQ` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each event detail record added to mic_event_detail table for a particular task_log_id and event_log seq combination. |
| 4 | `EVENT_LOG_SEQ` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each event record added to mic_event_log table for a particular task_log_id. |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This field identifies the long_text_id associated with the footnote text. The footnote text is stored on the long_text table. |
| 6 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value assigned to the task from the mic_task_log table thus associating the event log record with the appropriate task. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_DETAIL_SEQ` | [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `EVENT_DETAIL_SEQ` |
| `EVENT_LOG_SEQ` | [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `EVENT_LOG_SEQ` |
| `TASK_LOG_ID` | [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `TASK_LOG_ID` |

