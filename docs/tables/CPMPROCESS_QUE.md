# CPMPROCESS_QUE

> When the Process Server encounters errors processing requests, the request data is written to this table. Then, one or more cpmprocess_error records are written that point to each row on this table.

**Description:** Process Server Request Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGE` | LONGBLOB |  |  | This contains the error information. |
| 2 | `MESSAGE_SIZE` | DOUBLE |  |  | This is the size of the error message. |
| 3 | `NEXT_QUE_ID` | DOUBLE | NOT NULL |  | This is the unique queue error ID in the table that followed this one. |
| 4 | `QUE_ID` | DOUBLE | NOT NULL |  | This is the unique ID in this table for this error. |
| 5 | `QUE_SEQ` | DOUBLE |  |  | This is the current position in the table waiting for recovery. |
| 6 | `REQUEST_NUMBER` | DOUBLE |  |  | This is the name of the step whose process was getting service when the error occurred. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

