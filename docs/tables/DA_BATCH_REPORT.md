# DA_BATCH_REPORT

> Contains report schedule information for reports scheduled in Discern Analytics 2.0.

**Description:** Discern Analytics Batch Report  
**Table type:** REFERENCE  
**Primary key:** `DA_BATCH_REPORT_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDITIONAL_PARAMETER_TXT_ID` | DOUBLE | NOT NULL | FK→ | Additional parameters to be used for running the report |
| 3 | `ASSIGNED_DOCUMENT_NAME` | VARCHAR(100) |  |  | Name of the document to be assigned. |
| 4 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | Date and time batch report is effective. |
| 5 | `CREATED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel that added the report to be scheduled. |
| 6 | `CREATED_DT_TM` | DATETIME |  |  | Date and time this batch report was created. |
| 7 | `DA_BATCH_REPORT_DESC` | VARCHAR(100) |  |  | Description of the batch report. |
| 8 | `DA_BATCH_REPORT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DA_BATCH_REPORT table. |
| 9 | `DA_BATCH_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The schedule that generates this report. |
| 10 | `DA_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the report that is to be run. |
| 11 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | Type of document to be produced |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `PROCESS_SEQ` | DOUBLE | NOT NULL |  | Sequence within the job that the batch report should be run |
| 14 | `REPORT_PARAMETER_TXT_ID` | DOUBLE | NOT NULL | FK→ | Report parameters to be used for running the report |
| 15 | `RUNTIME_PROMPT_TXT_ID` | DOUBLE | NOT NULL | FK→ | Runtime prompts to be used for running the report. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDITIONAL_PARAMETER_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `CREATED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DA_BATCH_SCHED_ID` | [DA_BATCH_SCHED](DA_BATCH_SCHED.md) | `DA_BATCH_SCHED_ID` |
| `DA_REPORT_ID` | [DA_REPORT](DA_REPORT.md) | `DA_REPORT_ID` |
| `REPORT_PARAMETER_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `RUNTIME_PROMPT_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DA_BATCH_REPORT_LOG](DA_BATCH_REPORT_LOG.md) | `DA_BATCH_REPORT_ID` |

