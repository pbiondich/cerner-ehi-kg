# MIC_SUS_MED_RESULT

> This table contains the susceptibility testing activity for microbiology.

**Description:** Microbiology Medication Results  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field identifies whether or not the susceptibility result has been defined as an abnormal susceptibility response. Valid values include: 0 = Normal response 1 = Abnormal response |
| 2 | `CHARTABLE_IND` | DOUBLE |  |  | This field indicates whether the susceptibility result should be displayed on patient reports or bedisplayed in inquiry applications. Valid values include: 0 = Non-chartable 1 = Chartable |
| 3 | `COMMENT_SEQ` | DOUBLE |  |  | This field is not used at this time. |
| 4 | `COST` | CHAR(18) |  |  | This field is not used at this time. |
| 5 | `DETAIL_SUS_SEQ` | DOUBLE | NOT NULL | FK→ | The field identifies a value that uniquely identifies each susceptibility detail procedure associated with the susceptibility task. The sequence number is also used to determine the order the susceptibility detail procedures should be displayed in the result entry application and other associated applications. |
| 6 | `DOSAGE` | DOUBLE |  |  | This field is not used at this time. |
| 7 | `LOT_INFORMATION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the biochemical lot used to result the task. |
| 8 | `MEDICATION_DILUTION_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 9 | `PANEL_MEDICATION_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value for the antibiotic panel associated with the susceptibility task. Antibiotic panels are defined on code set 1010. |
| 10 | `PENDING_IND` | DOUBLE |  |  | This field identifies which antibiotic results are considered pending in the database. All pendingantibiotic results must be verified before the antibiotic panel will be considered complete. Valid values include: 0 = Not pending 1 = Pending |
| 11 | `PREV_EVENT_DETAIL_SEQ` | DOUBLE | NOT NULL |  | Event detail susceptibility of the previous result that caused a delta checking failure on the current result. From the mic_event_detail_table. |
| 12 | `PREV_EVENT_LOG_SEQ` | DOUBLE | NOT NULL |  | Event log susceptibility of the previous result that caused a delta checking failure on the current result. From the mic_event_detail_table. |
| 13 | `PREV_TASK_LOG_ID` | DOUBLE | NOT NULL |  | Task log id of the previous result that caused a delta checking failure on the current result. From the mic_event_detail_table. |
| 14 | `REQUEUE_IND` | DOUBLE |  |  | Currently used to signify that the antibiotic has a footnote. |
| 15 | `RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value for the susceptibility result. Susceptibility results are defined on code set 1025 Alpha susceptibility results and 64 Susceptibility Interpretation Results. '. If the detail susceptibility procedure is numeric this field will be set to '-1'. |
| 16 | `RESULT_NUMERIC` | DOUBLE |  |  | This field identifies the susceptibility result if the detail susceptibility procedure is defined as 'numeric'. If the detail susceptibility procedure is not numeric this field will be set to '-1'. |
| 17 | `RESULT_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the related MIC_QC_RESULT_SCHEDULE row. |
| 18 | `RESULT_SEQ` | DOUBLE | NOT NULL |  | The field identifies a value that uniquely identifies each susceptibility result for each susceptibility detail procedure. For example if there are 10 antibiotics in a panel and each antibiotic getsa dilution and interpretation result then there will be 20 result sequences, one for each result. |
| 19 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | This field identifies the code value for the units of measure associated with the numeric susceptibility result. Units of measure are defined on code set 54. |
| 20 | `ROUTE_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 21 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the susceptibility result. Result statuses are defined on codeset 1901. |
| 22 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value assigned to the susceptibility method task from the mic_task_log table thus associating the susceptibility detail procedures with the appropriate susceptibility method task. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 28 | `UPDT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DETAIL_SUS_SEQ` | [MIC_SUS_ORDER_DETAIL](MIC_SUS_ORDER_DETAIL.md) | `DETAIL_SUS_SEQ` |
| `LOT_INFORMATION_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `PANEL_MEDICATION_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `TASK_LOG_ID` | [MIC_SUS_ORDER_DETAIL](MIC_SUS_ORDER_DETAIL.md) | `TASK_LOG_ID` |

