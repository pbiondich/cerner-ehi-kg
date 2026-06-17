# CE_GROUPING_QUEUE

> Queue of person_ids with clinical event rows that need to processed for groupings.

**Description:** Clinical Event Grouping Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CE_GROUPING_QUEUE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CE_GROUPING_QUEUE table. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | This is the original date and time the row was created. |
| 7 | `ERROR_MESSAGE_TXT` | VARCHAR(1500) |  |  | The last error message received when this row was processed. |
| 8 | `PERSON_ID` | DOUBLE |  | FK→ | The ID of the patient who needs their events checked for grouping. |
| 9 | `PROCESS_DT_TM` | DATETIME |  |  | The date and time when this row was last processed. |
| 10 | `QUEUE_STATUS_TFLG` | VARCHAR(20) |  |  | Status of item in the queue. Values: skip, failure, success, pending |
| 11 | `REMAINING_RETRY_CNT` | DOUBLE |  |  | The number of times this row can be processed by grouping procedures. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

