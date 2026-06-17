# SI_DIRECT_ATTACHMENT

> Audit of file attached to each direct message either sent or received.

**Description:** System Integration Direct Message Attachment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARCHIVE_FILE_NAME` | VARCHAR(100) |  |  | The name of the archive file that the attachment was stored in within the message. |
| 2 | `ATTACHMENT_NAME` | VARCHAR(100) | NOT NULL |  | The name of the attachment. |
| 3 | `ATTACHMENT_SIZE` | DOUBLE | NOT NULL |  | The size of the attachment. |
| 4 | `CONTENT_TYPE_TXT` | VARCHAR(20) |  |  | The CareAware Multimedia content type used for storing the attachment. |
| 5 | `MEDIA_OBJECT_IDENT` | VARCHAR(64) |  |  | The CareAware Multimedia identifier of the attachment. |
| 6 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE | NOT NULL |  | The version of the attachmen in CareAware Multimedia. |
| 7 | `MIME_TYPE_TXT` | VARCHAR(100) |  |  | The MIME content type of the attachment |
| 8 | `SI_DIRECT_ATTACHMENT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `SI_DIRECT_MESSAGE_ID` | DOUBLE | NOT NULL | FK→ | Identifier to link the attachment to the si_direct_message table |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_DIRECT_MESSAGE_ID` | [SI_DIRECT_MESSAGE](SI_DIRECT_MESSAGE.md) | `SI_DIRECT_MESSAGE_ID` |

