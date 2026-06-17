# OEN_TXLOG

> Log of all tx's going through open engine interfaces.

**Description:** Open engine Transaction log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was insertedColumn |
| 2 | `EVENTID` | CHAR(4) |  |  | if the tx is from inbound or outbound interface. |
| 3 | `GROUP_NAME` | VARCHAR(40) |  |  | Group NameColumn |
| 4 | `INTERFACEID` | CHAR(5) |  |  | The interface id from which the tx came |
| 5 | `MESSAGE_NAME` | VARCHAR(40) |  |  | Message NameColumn |
| 6 | `MSGID` | CHAR(15) |  |  | Actual message id |
| 7 | `MSG_DATE` | CHAR(10) |  |  | The date when Tx was logged |
| 8 | `MSG_LEN` | DOUBLE |  |  | Message Length |
| 9 | `MSG_SIZE` | CHAR(5) |  |  | The size of the tx message |
| 10 | `MSG_TEXT` | LONGTEXT |  |  | The actual tx message |
| 11 | `MSG_TIME` | CHAR(8) |  |  | The time message was logged |
| 12 | `PART_NO` | CHAR(4) |  |  | Future |
| 13 | `PART_SIZE` | CHAR(5) |  |  | Future |
| 14 | `RECEIVING_SYSTEM` | VARCHAR(40) |  |  | Receiving SystemColumn |
| 15 | `SENDING_SYSTEM` | VARCHAR(40) |  |  | Sending SystemColumn |
| 16 | `SEQ_NO` | CHAR(10) |  |  | Future |
| 17 | `TX_KEY` | CHAR(27) | NOT NULL |  | Unique identifier of the table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

