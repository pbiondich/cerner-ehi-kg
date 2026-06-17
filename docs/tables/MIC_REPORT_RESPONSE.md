# MIC_REPORT_RESPONSE

> This table contains all coded and freetext responses associated with a microbiology report task.

**Description:** Microbiology Report Responses  
**Table type:** ACTIVITY  
**Primary key:** `RESPONSE_SEQ`, `TASK_LOG_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field identifies whether or not the response has been defined as an abnormal report response.Valid values include: 0 = Normal response 1 = Abnormal response |
| 2 | `COMMENT_SEQ` | DOUBLE |  |  | This field is not used at this time. |
| 3 | `GROUP_RESPONSE_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the group response code used to enter the responses for this report task. Group responses are defined on code set 1019. |
| 4 | `GROUP_RESPONSE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the group response entered for the report task. This could be used to join to the MIC_GROUP_RESPONSE table. |
| 5 | `NBR_OF_EPI` | DOUBLE |  |  | This field is not used at this time. |
| 6 | `NBR_OF_WBC` | DOUBLE |  |  | This field is not used at this time. |
| 7 | `NEW_PHRASE_IND` | DOUBLE |  |  | This field identifies if the response code for this record should be displayed on a new line for patient reports and in inquiry applications. Valid values include: 0 = Response displays on current line. 1 = Response displays on new line. |
| 8 | `ORG_TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field is used to correlate multiple responses to one task_log_id on the mic_task_log table. |
| 9 | `POSITIVE_IND` | DOUBLE |  |  | This field identifies whether or not the response has been defined as a positive report response. Valid values include: 0 = negative response 1= positive response |
| 10 | `REQUEUE_IND` | DOUBLE |  |  | Not currently used |
| 11 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the detail report responses. Report responses are defined on code set 1022. |
| 12 | `RESPONSE_CLASS_FLAG` | DOUBLE |  |  | This field identifies the type of response used in issuing the report. |
| 13 | `RESPONSE_DISPLAY_ORDER` | DOUBLE |  |  | This field a value that determines the order in which the responses should be displayed on patient reports and in various applications. |
| 14 | `RESPONSE_SEQ` | DOUBLE | NOT NULL | PK | The field contains a value that uniquely identifies each report response. This value will allow multiples of the same report response to be uniquely identified. |
| 15 | `RESPONSE_TEXT` | VARCHAR(200) |  |  | This field identifies free text information associated with the report task. |
| 16 | `RESPONSE_TYPE_FLAG` | DOUBLE |  |  | Denotes type of response. |
| 17 | `TASK_LOG_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the unique value assigned to the report task from the mic_task_log table thus associating the report responses with the appropriate report task. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORG_TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_CORRELATION_FOOTNOTE](MIC_CORRELATION_FOOTNOTE.md) | `RESPONSE_SEQ` |
| [MIC_CORRELATION_FOOTNOTE](MIC_CORRELATION_FOOTNOTE.md) | `TASK_LOG_ID` |

