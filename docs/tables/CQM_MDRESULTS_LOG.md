# CQM_MDRESULTS_LOG

> This CQM log table presents debugging and logging information associated with the MDI Results application.

**Description:** MDI Results CQM Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the CQM contributor configuration table. It is an internal system assigned number. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 3 | `LISTENER_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the CQM listener configuration table. It is an internal system assigned number. |
| 4 | `LOG_ERROR_LOCATION` | VARCHAR(80) |  |  | The code module that generated the error message in this row. |
| 5 | `LOG_ERROR_TEXT` | VARCHAR(132) |  |  | The error text message. |
| 6 | `LOG_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the CQM log table. It is an internal system assigned number. |
| 7 | `PARAM_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the CQM queue parameters table. It is an internal system assigned number. |
| 8 | `PROCESS_STATUS_FLAG` | DOUBLE |  |  | The current trigger explosion state for this transaction row. |
| 9 | `PROCESS_STATUS_TEXT` | VARCHAR(132) |  |  | Descriptive text string associated to the processing status flag. |
| 10 | `QUEUE_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the CQM queue table. It is an internal system assigned number. |
| 11 | `REGISTRY_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the CQM listener registry table. It is an internal system assigned number. |
| 12 | `TRIGGER_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the CQM listener trigger table. It is an internal system assigned number. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUEUE_ID` | [CQM_MDRESULTS_QUE](CQM_MDRESULTS_QUE.md) | `QUEUE_ID` |
| `TRIGGER_ID` | [CQM_MDRESULTS_TR_1](CQM_MDRESULTS_TR_1.md) | `TRIGGER_ID` |

