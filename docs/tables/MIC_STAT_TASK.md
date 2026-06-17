# MIC_STAT_TASK

> This summary table is comprised of records extracted from the MIC_TASK_LOG table. This information is utilized by the Microbiology Statistical Reporting package.

**Description:** Microbiology Statistical Task  
**Table type:** ACTIVITY  
**Primary key:** `TASK_LOG_ID`  
**Columns:** 32  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field indicates whether the report task included a coded response that is defined as abnormal. Valid values include: 0 = Normal 1 = Abnormal |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `CORRELATION_IND` | DOUBLE |  |  | This field indicates whether the correlation has occurred on a report task. Valid values include: 0 = No correlation 1 = Correlation |
| 4 | `DISPLAY_ORDER` | DOUBLE | NOT NULL |  | This field contains a numeric value that uniquely identifies the display order of the tasks associated with the orderable procedure. |
| 5 | `DUP_ORGANISM_IND` | DOUBLE |  |  | This field indicates whether an 'organism' task is considered to be a duplicate organism. The setting of the field is based on susceptibility duplicate checking rules. |
| 6 | `EVENT_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the result event to which this task is associated. This could be used to join to the CLINICAL_EVENT table. |
| 7 | `FREETEXT_RESULT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for a report or a free text comment. |
| 8 | `INSTR_ID_NBR` | VARCHAR(20) |  |  | This field identifies the identification number assigned to the susceptibility task for use in identifying specimens performed on an automated susceptibility analyzer. |
| 9 | `MOST_RECENT_REPORT_IND` | DOUBLE |  |  | This field indicates whether a report task is the most recent report issued. |
| 10 | `ORDER_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the task was ordered. Used to gather date information from the OMF_DATE table. |
| 11 | `ORDER_DT_TM` | DATETIME |  |  | This field contains the date and time at which the task was ordered. |
| 12 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the order to which this task is associated. This could be used to join to the MIC_STAT_ORDER table. |
| 13 | `ORDER_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the task was ordered. Used to get time information from the OMF_TIME table. |
| 14 | `ORDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom ordered the task. This could be used to join to the PRSNL table. |
| 15 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the organism associated with the task. Organism observations, biochemical, ID's and susceptibility tasks are associated with an organism. |
| 16 | `ORGANISM_QUAL` | DOUBLE | NOT NULL |  | This field identifies a sequence number for each organism code_value entered. For example, if there are two GPC organisms identified for this procedure the first GPC organism would have an organism qualifier of "01" and the second GPC organism would have a qualifier of "02". |
| 17 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether the report task included a coded response that is defined as positive. Valid values include: 0 = Negative 1 = Positive |
| 18 | `RESULT_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the task was last updated. Used to gather date information from the OMF_DATE table. |
| 19 | `RESULT_DT_TM` | DATETIME |  |  | This field contains the date and time at which the task was last updated. |
| 20 | `RESULT_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the task was last updated. Used to get time information from the OMF_TIME table. |
| 21 | `RESULT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom last updated the task. This could be used to join to the PRSNL table. |
| 22 | `TASK_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the task. This code value can come from several code sets depending on the type of task entered. Task related code sets include: 65 = Susceptibility Methods 1000 = Reports 1002 = Group Biochemicals 1005 = Detail Biochemicals 1019 = Group Report Responses 1021 = Organisms |
| 23 | `TASK_CLASS_FLAG` | DOUBLE |  |  | This field identifies a value that determines the class associated with the task entered. Tasks are grouped into classes as a means of categorizing the tasks into logical groupings such as reports, biochemicals, etc. |
| 24 | `TASK_LOG_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value assigned to the specific task associated with the orderable procedure. |
| 25 | `TASK_QUAL` | DOUBLE | NOT NULL |  | This field contains a numeric value that uniquely identifies multiple occurrences of the same TASK_CD. For example if there are multiple preliminary reports on a procedure this number identifies each preliminary report uniquely. The first preliminary report would have a TASK_QUAL value of 01 and the subsequent occurrences would have the qualifier assigned in sequential order, i.e., 02, 03, 04. |
| 26 | `TASK_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the current status of the task. |
| 27 | `TASK_TYPE_FLAG` | DOUBLE |  |  | This field identifies a value that determines the task type associated with the task entered. The task type further categorizes similar tasks within each task class. For example the task class biochemicals has two task type associated: (3)Group Biochemicals and (4)Detail Biochemicals. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FREETEXT_RESULT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [MIC_STAT_ORDER](MIC_STAT_ORDER.md) | `ORDER_ID` |
| `ORDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESULT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [MIC_STAT_BIOCHEMICAL](MIC_STAT_BIOCHEMICAL.md) | `TASK_LOG_ID` |
| [MIC_STAT_FOOTNOTE](MIC_STAT_FOOTNOTE.md) | `TASK_LOG_ID` |
| [MIC_STAT_ORGANISM_ID](MIC_STAT_ORGANISM_ID.md) | `TASK_LOG_ID` |
| [MIC_STAT_ORG_OBSERVATION](MIC_STAT_ORG_OBSERVATION.md) | `TASK_LOG_ID` |
| [MIC_STAT_REPORT_RESPONSE](MIC_STAT_REPORT_RESPONSE.md) | `ORG_TASK_LOG_ID` |
| [MIC_STAT_REPORT_RESPONSE](MIC_STAT_REPORT_RESPONSE.md) | `TASK_LOG_ID` |
| [MIC_STAT_SUSCEPTIBILITY](MIC_STAT_SUSCEPTIBILITY.md) | `TASK_LOG_ID` |

