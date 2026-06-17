# OEN_TELOG

> Transaction message activity through the open engine.

**Description:** Transaction event log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was insertedColumn |
| 2 | `EID` | DOUBLE | NOT NULL |  | if event is from inbound or outbound interface |
| 3 | `ESTATUS` | CHAR(1) |  |  | Flag which states success or Failure |
| 4 | `EVENT_DATE` | CHAR(10) |  |  | Date the event logged. |
| 5 | `EVENT_KEY` | CHAR(25) | NOT NULL |  | Unique identifier consist of tx id and time. |
| 6 | `EVENT_TIME` | CHAR(8) |  |  | Time the event was logged. |
| 7 | `OPID` | DOUBLE | NOT NULL |  | The inbound interface, the tx came from. |
| 8 | `OTID` | CHAR(15) |  |  | original tx id. |
| 9 | `PID` | DOUBLE | NOT NULL |  | Interface id logging the event. |
| 10 | `TID` | CHAR(15) | NOT NULL |  | tx id for the current interface |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

