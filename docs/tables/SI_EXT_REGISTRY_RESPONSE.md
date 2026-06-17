# SI_EXT_REGISTRY_RESPONSE

> This table stores a response received from a external registry, needed for future processing

**Description:** System Integration External Registry Response  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONSOLIDATION_STATUS_CD` | DOUBLE | NOT NULL |  | CODE SET:4002659 Status of the document in terms of the relationship with the database. Values include New, Reviewed, or Imported |
| 2 | `CONTENT_TYPE` | VARCHAR(32) |  |  | The content type of the document as it is stored in CAMM |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `IMPORTED_DT_TM` | DATETIME |  |  | The date and time the consolidated data from the response was imported into a patient's chart. |
| 5 | `MEDIA_OBJECT_IDENTIFIER` | VARCHAR(64) | NOT NULL |  | Identifier of the response message object if stored in the multimedia storage. |
| 6 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE | NOT NULL |  | The version of the identified response message object in the multimedia storage. |
| 7 | `MIME_TYPE` | VARCHAR(100) |  |  | The MIME type of the response message. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the queried registry response. |
| 9 | `RESPONSE_DT_TM` | DATETIME | NOT NULL |  | The date and time when the row was added, correlating to the actual response date and time. |
| 10 | `SI_EXT_REGISTRY_RESPONSE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `SI_XDOC_QUERY_PERSON_RELTN_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:SI_DOCUMENT_SEQ Foreign key to query relationship to track which query was responsible for this registry response. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SI_XDOC_QUERY_PERSON_RELTN_ID` | [SI_XDOC_QUERY_PERSON_RELTN](SI_XDOC_QUERY_PERSON_RELTN.md) | `SI_XDOC_QUERY_PERSON_RELTN_ID` |

