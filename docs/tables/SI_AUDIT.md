# SI_AUDIT

> Contains a log of all transactions sent and received.

**Description:** SI Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ERROR_CD` | DOUBLE | NOT NULL |  | This is the error code of the current transaction. it can indicate a specific error in a given system. |
| 2 | `ERROR_TEXT` | VARCHAR(500) | NOT NULL |  | This is the text provided for the given error code. |
| 3 | `MSG_CREATION_DT_TM` | DATETIME | NOT NULL |  | Date and time the message was created. |
| 4 | `MSG_IDENT` | VARCHAR(250) | NOT NULL |  | This is the unique identifier for the given message (alpha-numeric) |
| 5 | `MSG_TRIG_ACTION_TXT` | VARCHAR(250) | NOT NULL |  | This is the message trigger |
| 6 | `MSG_TYPE_TXT` | VARCHAR(250) | NOT NULL |  | This is the message type |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This is the identifier of the table referenced by parent_entity_name |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This is the name of the parent table referenced |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for the person |
| 10 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | this is the value of the unique primary identifier of the cqm queue table. it is an internal system assigned number and storing it in this table to support not_slot_cancel resend functionality. |
| 11 | `RECV_APP_IDENT` | VARCHAR(250) | NOT NULL |  | This is the identifier of the receiving application |
| 12 | `RECV_FAC_IDENT` | VARCHAR(250) |  |  | This is the identifier of the receiving facility |
| 13 | `REFER_TO_MSG_IDENT` | VARCHAR(250) | NOT NULL |  | This is the unique identifier of a message referred to by the current message |
| 14 | `RETAIN_UNTIL_DT_TM` | DATETIME |  |  | This field contains the DATE/TIME value that indicates retention period of the rows before purging. |
| 15 | `SEND_APP_IDENT` | VARCHAR(250) | NOT NULL |  | This is the identifier of the sending application. |
| 16 | `SEND_FAC_IDENT` | VARCHAR(250) |  |  | This is the identifier of the sending facility |
| 17 | `SI_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique row identifier for each audit event |
| 18 | `STATUS_CD` | DOUBLE | NOT NULL |  | This is the status code of the current transaction. It can indicate an application success or failure in a given system. |
| 19 | `SYS_DIRECTION_CD` | DOUBLE | NOT NULL |  | This is the direction or usage of the contributor system. This will differentiate between inbound and outbound transactions. |
| 20 | `TRN_CONV_IDENT` | VARCHAR(250) |  |  | This is a unique identifier for conversation between two parties. The Party initiating a conversation determines the value of the ConversationId element that SHALL be reflected in all messages pertaining to that conversation. |
| 21 | `TRN_MSG_IDENT` | VARCHAR(250) |  |  | This is a unique identifier for ebxml message |
| 22 | `TRN_REF_TO_MSG_IDENT` | VARCHAR(250) |  |  | RefToMessageId element contains the MessageId of the message whose delivery is being reported. This is always the message id from the previous message. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUEUE_ID` | [CQM_FSIESO_QUE](CQM_FSIESO_QUE.md) | `QUEUE_ID` |

