# MIC_EVENT_DETAIL

> This table contains a record for each task and event that occurs for the orderable procedure. Eachtime a task is added, modified or deleted a record is written to this table. Results that are corrected have the original results posted to this table.

**Description:** Microbiology Event Detail  
**Table type:** ACTIVITY  
**Primary key:** `EVENT_DETAIL_SEQ`, `EVENT_LOG_SEQ`, `TASK_LOG_ID`  
**Columns:** 27  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field identifies whether or not the response has been defined as an abnormal report response.Valid values include: 0 = Normal response 1 = Abnormal response |
| 2 | `CHARTABLE_IND` | DOUBLE |  |  | This field indicates whether the task should be displayed on patient reports or be displayed in inquiry applications. Valid values include: 0 = Non-chartable 1 = Chartable |
| 3 | `DETAIL_BIOCHEM_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the detail biochemical. Detail biochemicals are defined on code set 1005. |
| 4 | `DETAIL_SUS_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value for the detail susceptibility procedure. Detail susceptibility procedures are defined on code set 1004. |
| 5 | `EVENT_DETAIL_SEQ` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each event detail record added to this table for a particular task_log_id and event_log seq combination. |
| 6 | `EVENT_LOG_SEQ` | DOUBLE | NOT NULL | PK FK→ | This field identifies a unique value for each event record added to this table for a particular task_log_id. |
| 7 | `GROUP_BIOCHEM_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the group biochemical. Group biochemicals are defined on code set 1002. |
| 8 | `MEDIA_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the specific type of media identified for this procedure. Media types are defined on code set 2051 Specimen Containers. |
| 9 | `PANEL_CD` | DOUBLE | NOT NULL |  | This field identifies the code value for the antibiotic panel. Antibiotic panels are defined on code set 1010. |
| 10 | `PANEL_MED_CD` | DOUBLE | NOT NULL |  | This field identifies the code value for the antibiotic. Antibiotic are defined on code set 1011. |
| 11 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether or not the procedure is considered positive. Microbiology procedures are considered positive when a preliminary or final report is issued that includes a positive response or organism. Valid values include: 0 = Not positive 1 = Positive |
| 12 | `PREV_EVENT_DETAIL_SEQ` | DOUBLE | NOT NULL | FK→ | Contains the event detail sequence number associated with the previous result that caused a delta checking failure on the current result. |
| 13 | `PREV_EVENT_LOG_SEQ` | DOUBLE | NOT NULL | FK→ | Contains the event log sequence number associated with the previous result that caused a delta checking failure on the current result. |
| 14 | `PREV_TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | Contains the task log identifier number associated with the previous result that caused a delta checking failure on the current result. |
| 15 | `QUANTITATION_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the quantity associated with the media and organism. Organism quantity codes are defined on code set 1022 Quantitations. |
| 16 | `REPORT_IND` | DOUBLE |  |  | This field indicates whether or not the quantity for the associated organism should be linked to the report. Only one quantity may be linked per organism. |
| 17 | `RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the biochemical or susceptibility result. Coded biochemical results are defined on code set 1027. Coded susceptibility results are defined on code sets 64 and 1025. |
| 18 | `RESULT_NUMERIC` | DOUBLE |  |  | This field identifies the susceptibility result if the detail susceptibility procedure is defined as 'numeric'. If the detail susceptibility procedure is not numeric this field will be set to '1'. |
| 19 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the result. Result statuses are defined on code set 1901. |
| 20 | `RESULT_TEXT` | VARCHAR(200) |  |  | This field identifies the result text for tasks such as free-text biochemicals, and free text comments. |
| 21 | `RESULT_UNIT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value for the units of measure associated with the numeric susceptibility result. Units of measure are defined on code set 54. |
| 22 | `TASK_LOG_ID` | DOUBLE | NOT NULL | PK FK→ | This field identifies the unique value assigned to the task from the mic_task_log table thus associating the event log record with the appropriate task. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DETAIL_SUS_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `EVENT_LOG_SEQ` | [MIC_EVENT_LOG](MIC_EVENT_LOG.md) | `EVENT_LOG_SEQ` |
| `PREV_EVENT_DETAIL_SEQ` | [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `EVENT_DETAIL_SEQ` |
| `PREV_EVENT_LOG_SEQ` | [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `EVENT_LOG_SEQ` |
| `PREV_TASK_LOG_ID` | [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `TASK_LOG_ID` |
| `TASK_LOG_ID` | [MIC_EVENT_LOG](MIC_EVENT_LOG.md) | `TASK_LOG_ID` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `PREV_EVENT_DETAIL_SEQ` |
| [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `PREV_EVENT_LOG_SEQ` |
| [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `PREV_TASK_LOG_ID` |
| [MIC_EVENT_FOOTNOTE](MIC_EVENT_FOOTNOTE.md) | `EVENT_DETAIL_SEQ` |
| [MIC_EVENT_FOOTNOTE](MIC_EVENT_FOOTNOTE.md) | `EVENT_LOG_SEQ` |
| [MIC_EVENT_FOOTNOTE](MIC_EVENT_FOOTNOTE.md) | `TASK_LOG_ID` |

