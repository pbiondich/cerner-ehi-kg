# TASK_INSTRMT_PROTCL_R

> Stores the staining protocols performed on an instrument for processing a task order.

**Description:** Task Instrument Protocol Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INSTRUMENT_PROTOCOL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the instrument protocol for this relationship. |
| 2 | `PROCESSING_TASK_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the processing task related to this relationship. |
| 3 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the sending protocol to instrument: 0 - Pending; 1 - Sent |
| 4 | `TASK_INSTRMT_PROTCL_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between the instrument protocol and the processing task. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INSTRUMENT_PROTOCOL_ID` | [INSTRUMENT_PROTOCOL](INSTRUMENT_PROTOCOL.md) | `INSTRUMENT_PROTOCOL_ID` |
| `PROCESSING_TASK_ID` | [PROCESSING_TASK](PROCESSING_TASK.md) | `PROCESSING_TASK_ID` |

