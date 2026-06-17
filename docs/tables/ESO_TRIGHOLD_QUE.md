# ESO_TRIGHOLD_QUE

> Stores outbound triggers before they reach the CQM server. Will combine selected triggers to reduce outbound volume.

**Description:** ESO Trigger Hold Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS` | VARCHAR(15) | NOT NULL |  | The trigger's CQM class |
| 2 | `ESO_TRIGHOLD_QUE_ID` | DOUBLE | NOT NULL |  | Defines a unique ID for each trigger on the queue |
| 3 | `MESSAGE` | LONGBLOB |  |  | Compressed messageColumn |
| 4 | `MESSAGE_LEN` | DOUBLE |  |  | Message lengthColumn |
| 5 | `QUE_INSERT_DT_TM` | DATETIME | NOT NULL |  | Date/time trigger was inserted into queue |
| 6 | `TRIG_IDENTIFIER_COMP` | VARCHAR(100) | NOT NULL |  | Trigger identifier composite string |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

