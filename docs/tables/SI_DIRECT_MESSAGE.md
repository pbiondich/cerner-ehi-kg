# SI_DIRECT_MESSAGE

> Audit of Direct messages coming into and sending out of Millennium.

**Description:** System Integration Direct Message  
**Table type:** ACTIVITY  
**Primary key:** `SI_DIRECT_MESSAGE_ID`  
**Columns:** 28  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier for the application data model this message is linked to |
| 2 | `APPLICATION_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the table the application_entity_id is from. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was created. |
| 4 | `DIRECTION_TXT` | VARCHAR(10) |  |  | The direction of the direct message in relation to the Millennium Domain |
| 5 | `IN_REPLY_TO_IDENT` | VARCHAR(100) |  |  | The identifier of the message this message is replying to. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The logical domain that the message belongs to. |
| 7 | `MEDIA_OBJECT_IDENTIFIER` | VARCHAR(64) |  |  | The CareAware Multimedia identifier for the full MIME message. |
| 8 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE |  |  | The version of the message in CAMM. |
| 9 | `MESSAGE_IDENT` | VARCHAR(100) |  |  | Message identifier in the Direct message |
| 10 | `MESSAGE_SIZE` | DOUBLE |  |  | The size of the message |
| 11 | `MESSAGE_TYPE_TXT` | VARCHAR(20) |  |  | The type of message. For example: Reply, Forward, BounceBack, etc. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The patient id associated to the message. This only applies to outbound messages |
| 13 | `PROCESS_TIME_SECS` | DOUBLE | NOT NULL |  | The time it took to process the message in seconds. |
| 14 | `RECEIVED_DT_TM` | DATETIME |  |  | The date and time the message was received |
| 15 | `REQUESTER_ID` | DOUBLE | NOT NULL | FK→ | The user that requested the direct message be sent. This may or may not be the same as the sender_entity_id. |
| 16 | `SENDER_ADDRESS` | VARCHAR(100) | NOT NULL |  | Email address of the sender of the message |
| 17 | `SENDER_ENTITY_ID` | DOUBLE | NOT NULL |  | The Millennium id associated to the sender's email address. Only applies to outbound messages |
| 18 | `SENDER_ENTITY_NAME` | VARCHAR(30) |  |  | The Millennium table that the sender entity id comes from. |
| 19 | `SENT_DT_TM` | DATETIME | NOT NULL |  | The date and time the message was sent |
| 20 | `SI_DIRECT_MESSAGE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 21 | `STATUS_TXT` | VARCHAR(20) |  |  | The current status of the message. It may be update by delivery notifications |
| 22 | `SUBJECT_TXT` | VARCHAR(255) |  |  | Subject line of the message |
| 23 | `TRANSPORT_METHOD` | VARCHAR(20) | NOT NULL |  | The method of transport for the Direct Message and its attachments. Possible values include DIRECT_SMTP, DIRECT_XDM, and DIRECT_XDR |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REQUESTER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_DIRECT_ATTACHMENT](SI_DIRECT_ATTACHMENT.md) | `SI_DIRECT_MESSAGE_ID` |
| [SI_DIRECT_RECIPIENT](SI_DIRECT_RECIPIENT.md) | `SI_DIRECT_MESSAGE_ID` |

