# MIC_EVENT_LOG

> This table contains a record for each task and event that occurs for the orderable procedure. Eachtime a task is added, modified or deleted a record is written to this table.

**Description:** Microbiology Event Log  
**Table type:** ACTIVITY  
**Primary key:** `EVENT_LOG_SEQ`, `TASK_LOG_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | Indicates whether the event in the row is abnormal. |
| 2 | `CHARTABLE_IND` | DOUBLE |  |  | Indicates whether the event in the row should be printed on a patient chart. |
| 3 | `EVENT_DT_TM` | DATETIME |  |  | This field identifies the date and time the event log record was written. |
| 4 | `EVENT_LOG_FLAG` | DOUBLE | NOT NULL |  | Flag for the mic_event_log table that specifies special characteristics of the given row. |
| 5 | `EVENT_LOG_SEQ` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each event record added to this table for a particular task_log_id. |
| 6 | `EVENT_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the task at the time the event log record was written. Result statuses are defined on code set 1901. |
| 7 | `EVENT_TECH_ID` | DOUBLE | NOT NULL |  | This field identifies the ID of the person working with the task when the event log record is written. The event_tech_id corresponds to the person_id on the prsnl table, which identifies the user. |
| 8 | `EXTERNAL_DEVICE_IND` | DOUBLE |  |  | Indicates whether the task has been issued by an external device or issued from millennium applications. Valid values include: 0=Millennium Applications, 1=External Device. |
| 9 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the long_text_id associated with the report task as it existed at a given event date and time. The report text is stored on the long_text table in formatted form for retrieval and display on management reports and inquiries. |
| 10 | `ORGANISM_CD` | DOUBLE | NOT NULL | FK→ | The Organism code is the code set value that identifies the organism associated with the event in the row. |
| 11 | `ORGANISM_SEQ` | DOUBLE | NOT NULL |  | This field identifies a sequence number for each organism code_value entered. For example, if there are two gpc organisms identified for this procedure the first gpc organism would have an organism seq of 01 the second would have 02. |
| 12 | `POSITIVE_IND` | DOUBLE |  |  | Indicates whether the catalog code is considered positive. |
| 13 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The code value of the service resource code associated with the event. |
| 14 | `TASK_LOG_ID` | DOUBLE | NOT NULL | PK FK→ | This field identifies the unique value assigned to the task from the mic_task_log table thus associating the event log record with the appropriate task. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORGANISM_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `EVENT_LOG_SEQ` |
| [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `TASK_LOG_ID` |

