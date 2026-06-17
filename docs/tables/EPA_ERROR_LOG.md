# EPA_ERROR_LOG

> Stores partial failures that may occur during epa workflows

**Description:** Electronic Prior Authorization Errors  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DISMISS_IND` | DOUBLE | NOT NULL |  | Whether this error has been dismissed by the provider or not. |
| 3 | `EPA_ERROR_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `EPA_ERROR_NOTE_ID` | DOUBLE | NOT NULL | FK→ | This value comes from the LONG_TEXT id from the EPA_LONG_TEXT table |
| 5 | `EPA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The EPA_RECORD id from the EPA_RECORD table |
| 6 | `FAILURE_IND_BIT` | DOUBLE | NOT NULL |  | A bitmask representing the failure(s) that occurred. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `WORKFLOW_FLAG` | DOUBLE | NOT NULL |  | Workflow where the error occurred.1 PA_UNKNOWN2 PA_INITIATION_REQUEST3 PA_INITIATION_RESPONSE4 PA_REQUEST5 PA_RESPONSE6 PA_CANCEL_REQUEST7 PA_CANCEL_RESPONSE8 PA_CHANGE_RESPONSE |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EPA_ERROR_NOTE_ID` | [EPA_LONG_TEXT](EPA_LONG_TEXT.md) | `EPA_LONG_TEXT_ID` |
| `EPA_RECORD_ID` | [EPA_RECORD](EPA_RECORD.md) | `EPA_RECORD_ID` |

