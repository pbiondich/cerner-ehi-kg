# SI_MESSAGE_LOG

> This table is used to store inbound and outbound interface messages for auditing and troubleshooting purposes

**Description:** Si_message_log  
**Table type:** ACTIVITY  
**Primary key:** `SI_MESSAGE_LOG_ID`  
**Columns:** 17  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_SEQUENCE` | DOUBLE | NOT NULL |  | ACK SEQUENCE column |
| 2 | `APPLICATION_NAME` | VARCHAR(50) |  |  | The name of the interface application that logged the message. |
| 3 | `COMPRESSING_IND` | DOUBLE | NOT NULL |  | Indicates whether message body has been compressed |
| 4 | `ENDPOINT_URI` | VARCHAR(255) |  |  | Free-text endpoint URI that is associated with the message. |
| 5 | `INTERFACEID` | DOUBLE | NOT NULL |  | Identifier of interface inserting message. Value from OEN_PROCINFO |
| 6 | `INTERNAL_MESSAGE_IDENT` | VARCHAR(40) | NOT NULL |  | System generated message identifier |
| 7 | `MESSAGE_DIRECTION_FLAG` | DOUBLE | NOT NULL |  | Direction of message in relation to the interface inserting row. 0 - not set 1 - Inbound message 2 - Outbound message |
| 8 | `MESSAGE_IDENT` | VARCHAR(40) | NOT NULL |  | Message identifier from message body |
| 9 | `MESSAGE_SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of message in conversation |
| 10 | `MESSAGE_SIZE` | DOUBLE | NOT NULL |  | Size of message as stored on this table |
| 11 | `MESSAGE_TEXT` | LONGBLOB |  |  | Message that was sent/received |
| 12 | `SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (10)

| From table | Column |
|------------|--------|
| [DQR_DOCUMENT_ACTION](DQR_DOCUMENT_ACTION.md) | `SI_MESSAGE_LOG_ID` |
| [SI_ERROR_RELTN](SI_ERROR_RELTN.md) | `SI_MESSAGE_LOG_ID` |
| [SI_HAAD_TRANSACTION](SI_HAAD_TRANSACTION.md) | `SUBMIT_MSGLOG_ID` |
| [SI_HAAD_TRANSACTION](SI_HAAD_TRANSACTION.md) | `SUBMIT_RESP_MSGLOG_ID` |
| [SI_REPO_REG_RELTN](SI_REPO_REG_RELTN.md) | `ACK_SI_MESSAGE_LOG_ID` |
| [SI_REPO_REG_RELTN](SI_REPO_REG_RELTN.md) | `SI_MESSAGE_LOG_ID` |
| [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `DOC_RETR_ACK_SI_MESSAGE_LOG_ID` |
| [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `DOC_RETR_SI_MESSAGE_LOG_ID` |
| [SI_XDOC_QUERY_PERSON_RELTN](SI_XDOC_QUERY_PERSON_RELTN.md) | `ACK_SI_MESSAGE_LOG_ID` |
| [SI_XDOC_QUERY_PERSON_RELTN](SI_XDOC_QUERY_PERSON_RELTN.md) | `SI_MESSAGE_LOG_ID` |

