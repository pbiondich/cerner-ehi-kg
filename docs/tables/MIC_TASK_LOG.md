# MIC_TASK_LOG

> This table contains task level activity associated with a microbiology orderable procedure. Tasks refer to organism observations, biochemical, reports and susceptibilities associated with the orderable procedure.

**Description:** Microbiology Task Log  
**Table type:** ACTIVITY  
**Primary key:** `TASK_LOG_ID`  
**Columns:** 38  
**Referenced by:** 14 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field indicates whether the report task included a coded response that is defined as abnormal. Valid values include: 0 = Normal 1 = Abnormal |
| 2 | `ACTION_DT_TM` | DATETIME |  |  | Identifies the date and time the task was last updated. |
| 3 | `ACTION_TECH_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user that last updated the task. |
| 4 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 6 | `CHARTABLE_IND` | DOUBLE |  |  | This field indicates whether the task should be displayed on patient reports or be displayed in inquiry applications. Valid values include: 0 = Non-chartable 1 = Chartable |
| 7 | `COMMENT_IND` | DOUBLE |  |  | This field is not used at this time. |
| 8 | `CORRECTED_IND` | DOUBLE |  |  | This field is not used at this time. |
| 9 | `CRITICAL_IND` | DOUBLE | NOT NULL |  | When user checks the critical indicator in micdbtools, we want to hold the user selection value in another field/column so that if user uncheck the critical indicator checkbox in micdbtool, we can have the check history for that field. |
| 10 | `EVENT_HISTORY_FLAG` | DOUBLE | NOT NULL |  | This field identifies the amount of history that has been kept for a given task. 0 - No or partial history has been kept for this task; 1 - All history has been kept for this task |
| 11 | `EXPEDITE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 12 | `EXTERNAL_DEVICE_IND` | DOUBLE |  |  | Indicates whether the task has been issued by an external device or issued from millennium applications Valid values include: 0=Millennium Applications, 1 = External Device. |
| 13 | `INSTR_ID_NBR` | VARCHAR(20) |  |  | This field identifies the identification number assigned to the susceptibility task for use in identifying specimens performed on an automated susceptibility analyzer. |
| 14 | `INSTR_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field identifies the instrument where the susceptibility task is to be performed. This field will be left blank for susceptibilities not performed on an automated instrument. |
| 15 | `INSTR_RESULT_IDENT` | VARCHAR(50) |  |  | Identification number assigned to results (e.g. organism observations) uploaded from automated microbiology instruments. |
| 16 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This field identifies the long_text_id associated with the report task. The report text is now going to be stored on the long_text table in an already formatted form so applications such as inquiry can pull this formatted text to display. Free-text comments issued within result entry are also written to this field. |
| 17 | `OBSERVATION` | VARCHAR(100) |  |  | This field is not used at this time. |
| 18 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 19 | `ORGANISM_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the organism associated with the task. Organism observations, biochemical, ID's and susceptibility tasks are associated with an organism. |
| 20 | `ORGANISM_QUAL` | DOUBLE |  |  | This field identifies a sequence number for each organism code_value entered. For example, if there are two GPC organisms identified for this procedure the first GPC organism would have an organism qualifier of '01' and the second GPC organism would have a qualifier of '02'. |
| 21 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether the report task included a coded response that is defined as positive. Valid values include: 0 = Negative 1 = Positive |
| 22 | `Q_SCORE` | DOUBLE |  |  | This field is not used at this time. |
| 23 | `REQUEUE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 24 | `TASK_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the task. This code value can come from several code sets depending on the type of task entered. Task related code sets include: 65 = Susceptibility Methods 1000 = Reports 1002 = Group Biochemicals 1005 = Detail Biochemicals 1019 = Group Report Responses 1021 = Organisms |
| 25 | `TASK_CLASS_FLAG` | DOUBLE |  |  | This field identifies a value that determines the class associated with the task entered. Tasks are grouped into classes as a means of categorizing the tasks into logical groupings such as reports, biochemicals, etc. Task classes are used to flex how the applications react to particular types of tasks. For most queries the task_type_flag field would be a better field to select. |
| 26 | `TASK_DISPLAY_ORDER` | DOUBLE |  |  | This field includes a numeric value that uniquely identifies the display order of the tasks associated with the orderable procedure. Tasks for a procedure are displayed in numerical order according to the task display order in applications such as Microbiology Result Entry. |
| 27 | `TASK_DT_TM` | DATETIME |  |  | This field identifies the date and time the task was entered. |
| 28 | `TASK_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the service_resource where the orderable procedure was routed at the time the task was entered. Service resource code_values come from code set 221 Service Resource. |
| 29 | `TASK_LOG_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value assigned to the specific task associated with the orderable procedure. |
| 30 | `TASK_QUAL` | DOUBLE |  |  | This field includes a numeric value that uniquely identifies multiple occurrences of the same task_cd. For example if there are multiple preliminary reports on a procedure this number identifies each preliminary report uniquely. The first preliminary report would have a task_qual of 01 and the subsequent occurrences would have the qualifier assigned in sequential order, i.e., 02, 03, 04. |
| 31 | `TASK_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the current status of the task. The status code_value is from code set 1901 Result Status. |
| 32 | `TASK_TECH_ID` | DOUBLE | NOT NULL |  | This field identifies the ID of the person performing a specific task. The task_tech_id corresponds to the person_id on the prsnl table, which identifies the user. |
| 33 | `TASK_TYPE_FLAG` | DOUBLE |  |  | This field identifies a value that determines the task type associated with the task entered. The task type further categorizes similar tasks within each task class. For example the task class biochemicals has two task type associated: (3)Group Biochemicals and (4)Detail Biochemicals |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_TECH_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORGANISM_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `TASK_LOCATION_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (14)

| From table | Column |
|------------|--------|
| [CONTAINER](CONTAINER.md) | `TASK_LOG_ID` |
| [CONTAINER_EVENT](CONTAINER_EVENT.md) | `TASK_LOG_ID` |
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `TASK_LOG_ID` |
| [MIC_BIOCHEMICAL_TEST_RESULT](MIC_BIOCHEMICAL_TEST_RESULT.md) | `TASK_LOG_ID` |
| [MIC_CANCEL_REASON](MIC_CANCEL_REASON.md) | `TASK_LOG_ID` |
| [MIC_CORRELATION_FOOTNOTE](MIC_CORRELATION_FOOTNOTE.md) | `CORR_TASK_LOG_ID` |
| [MIC_CORRELATION_FOOTNOTE](MIC_CORRELATION_FOOTNOTE.md) | `ORG_TASK_LOG_ID` |
| [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `TASK_LOG_ID` |
| [MIC_EVENT_LOG](MIC_EVENT_LOG.md) | `TASK_LOG_ID` |
| [MIC_ORGANISM_ID](MIC_ORGANISM_ID.md) | `TASK_LOG_ID` |
| [MIC_ORGANISM_OBSERVATION](MIC_ORGANISM_OBSERVATION.md) | `TASK_LOG_ID` |
| [MIC_REPORT_RESPONSE](MIC_REPORT_RESPONSE.md) | `ORG_TASK_LOG_ID` |
| [MIC_REPORT_RESPONSE](MIC_REPORT_RESPONSE.md) | `TASK_LOG_ID` |
| [MIC_SUS_ORDER_DETAIL](MIC_SUS_ORDER_DETAIL.md) | `TASK_LOG_ID` |

