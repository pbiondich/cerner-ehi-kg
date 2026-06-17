# DA_BATCH_QUERY

> Contains the list of queries to be ran in the Discern Analytics 2.0 scheduler.

**Description:** Discern Analytics Batch Query  
**Table type:** REFERENCE  
**Primary key:** `DA_BATCH_QUERY_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDITIONAL_PARAMETER_TXT_ID` | DOUBLE | NOT NULL | FK→ | Additional parameters to be used for running the query |
| 3 | `ASSIGNED_DOCUMENT_NAME` | VARCHAR(100) |  |  | Name of the document to be assigned. |
| 4 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. This may be valued with the date that the row became active. |
| 5 | `CREATED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that generated this batch query. |
| 6 | `CREATED_DT_TM` | DATETIME |  |  | The date and time this batch query was created. |
| 7 | `DA_BATCH_QUERY_DESC` | VARCHAR(100) |  |  | Description of the batch query. |
| 8 | `DA_BATCH_QUERY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DA_BATCH_QUERY table. |
| 9 | `DA_BATCH_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The schedule that generates this query. |
| 10 | `DA_QUERY_ID` | DOUBLE | NOT NULL | FK→ | The query that is a part of this batch |
| 11 | `DOCUMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of document generated (such as html, pdf, postscript, etc.) |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `PROCESS_SEQ` | DOUBLE | NOT NULL |  | Sequence within the job that the batch query should be run |
| 14 | `RUNTIME_PROMPT_TXT_ID` | DOUBLE | NOT NULL | FK→ | Runtime prompts to be used for running the query. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDITIONAL_PARAMETER_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `CREATED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DA_BATCH_SCHED_ID` | [DA_BATCH_SCHED](DA_BATCH_SCHED.md) | `DA_BATCH_SCHED_ID` |
| `DA_QUERY_ID` | [DA_QUERY](DA_QUERY.md) | `DA_QUERY_ID` |
| `RUNTIME_PROMPT_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DA_BATCH_QUERY_LOG](DA_BATCH_QUERY_LOG.md) | `DA_BATCH_QUERY_ID` |

