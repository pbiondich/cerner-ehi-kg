# SI_SPINE_AUDIT

> This table will store all Spine SOAP messages from si.soap_audit queue

**Description:** SI_SPINE_AUDIT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGE_SIZE` | DOUBLE |  |  | size of message as stored on this table |
| 2 | `MESSAGE_TEXT` | LONGTEXT |  |  | message that was sent/received |
| 3 | `MSG_IDENT` | VARCHAR(100) |  |  | message identifier from message body |
| 4 | `MSG_TRIG_ACTION_TEXT` | VARCHAR(100) |  |  | this is the message trigger |
| 5 | `SI_SPINE_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SI_SPINE_AUDIT table |
| 6 | `TRN_CONV_IDENT` | VARCHAR(100) |  |  | this is a unique identifier for conversation between two parties. the party initiating a conversation determines the value of the conversationid element that shall be reflected in all messages pertaining to that conversation. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

