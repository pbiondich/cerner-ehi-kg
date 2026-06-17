# SI_DOCUMENT_RECIPIENT_RELTN

> This table stores the relationship between documents and their recipients along with the status of any email communication.

**Description:** SI_DOCUMENT_RECIPIENT_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BOUNCE_BACK_IND` | DOUBLE | NOT NULL |  | When valued, our system was sent an indicator that this document was unable to be delivered to the given recipient. |
| 2 | `MESSAGE_IDENT` | VARCHAR(255) |  |  | The message identifier generated at the time that the document was delievered to the recipient. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key relationships from the tables defined by the parent entity name |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of parent entities that can relate to the document (CE_EVENT_PRSNL, CONTRIBUTOR_SYSTEM, CR_OUTPUT_DESTINATION, CR_REPORT_REQUEST, DEVICE, EMAIL_INFO, PRSNL) |
| 5 | `RECIPIENT_TYPE` | VARCHAR(32) | NOT NULL |  | The type of medium used to send the document to the given recipient. This will include: EMAIL, PRINT, FAX, FILE, CONTRIBUTOR_SYSTEM, DEVICE, MULTI, PUBLISH |
| 6 | `SI_DOCUMENT_INFO_ID` | DOUBLE | NOT NULL | FK→ | Foreign key relationship to the si_document_info table. |
| 7 | `SI_DOCUMENT_RECIPIENT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number - Primary Key |
| 8 | `SUBMISSION_DT_TM` | DATETIME | NOT NULL |  | The date that the given document was sent to the given recipient |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_DOCUMENT_INFO_ID` | [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `SI_DOCUMENT_INFO_ID` |

