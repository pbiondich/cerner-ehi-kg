# SESSION_LOG

> The Session_Log table provides detailed information about the session transmission.

**Description:** Session Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGE_CD` | DOUBLE | NOT NULL |  | A series of unique message codes that represents different transmission status data. I.e. Message Code 0 = Normal Transmission. |
| 2 | `MESSAGE_TEXT` | VARCHAR(200) |  |  | Text that defines the session messages.Column |
| 3 | `QUALIFIER` | DOUBLE | NOT NULL |  | This is needed in case the same session is being retransmitted. |
| 4 | `SESSION_NUM` | DOUBLE | NOT NULL |  | Sequential number assigned at time of transmission. |
| 5 | `SESS_DT_TM` | DATETIME |  |  | The date and time that a specific session was created. This date and time is the time the report or group of reports is selected for transmission by the communications port. |
| 6 | `SESS_LEVEL` | DOUBLE |  |  | Determines at what log level this message will display.Column |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

