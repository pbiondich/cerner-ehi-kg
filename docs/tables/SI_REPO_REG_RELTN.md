# SI_REPO_REG_RELTN

> Relates registered document information with repository information.

**Description:** System Integration Repository Registry Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_MESSAGE_LOG table for the audited transport protocol message containing the acknowledgement after it is received inbound. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `DOCUMENT_ENTRY_UUID` | VARCHAR(50) |  |  | XDSDocumentEntry entryUUID |
| 4 | `ENDPOINT_URL` | VARCHAR(255) |  |  | The endpoint URL that is the target of a document registration or the source of a document retrieval. |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the LONG_TEXT table |
| 6 | `MESSAGE_TYPE` | VARCHAR(100) |  |  | Type of document registration message sent to/received from a repository. Valid values are ProvideAndRegister, Register, RegisterOnDemand, Retrieve, and RetrieveOnDemand |
| 7 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CQM_OENINTERFACE_QUE table for the document that has been enqueued to Open Engine. |
| 8 | `REQUEST_STATUS_FLAG` | DOUBLE | NOT NULL |  | The Status of the request to registry from the related repository. |
| 9 | `SI_DOCUMENT_INFO_ID` | DOUBLE | NOT NULL | FK→ | FK value from table SI_DOCUMENT_INFO |
| 10 | `SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_MESSAGE_LOG table for the audited transport protocol message containing the document submission after it is sent outbound. |
| 11 | `SI_REPO_REG_RELTN_ID` | DOUBLE | NOT NULL |  | Primary Key to the SI_Repo_Reg_Reltn table. |
| 12 | `SUBMISSION_ENTRY_UUID` | VARCHAR(50) |  |  | XDSSubmissionSet entryUUID |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACK_SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `SI_DOCUMENT_INFO_ID` | [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `SI_DOCUMENT_INFO_ID` |
| `SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |

