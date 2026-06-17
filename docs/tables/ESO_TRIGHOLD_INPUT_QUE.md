# ESO_TRIGHOLD_INPUT_QUE

> Acts as an input queue for the trigger hold server. Populated by HNAUSER. Logs information about each trigger that is enqueued on the eso_trighold_que table.

**Description:** ESO Trigger Hold Input Que  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ERROR_TEXT` | VARCHAR(500) |  |  | Error text reported by the script if a trigger combine failed |
| 2 | `ESO_TRIGHOLD_INPUT_QUE_ID` | DOUBLE | NOT NULL |  | Defines a unique ID for each trigger's input que info |
| 3 | `ESO_TRIGHOLD_QUE_ID` | DOUBLE | NOT NULL |  | Defines a unique ID for each trigger enqueued on the eso_trighold_que table. |
| 4 | `MESSAGE` | LONGBLOB |  |  | Compressed message |
| 5 | `MESSAGE_LEN` | DOUBLE |  |  | Message lengthColumn |
| 6 | `PRIMARY_ENTITY_ID` | DOUBLE | NOT NULL |  | Value of the first identifier used for matching triggers of this class |
| 7 | `TRIGGER_HELD_IND` | DOUBLE | NOT NULL |  | Trigger held indicatorColumn |
| 8 | `TRIGGER_PROC_FLAG` | DOUBLE |  |  | Trigger process status flag 1 = Trigger Received 2 = Trigger on hold 3 = Trigger sent to CQM |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

