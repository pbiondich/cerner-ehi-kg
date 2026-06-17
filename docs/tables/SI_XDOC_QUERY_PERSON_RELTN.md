# SI_XDOC_QUERY_PERSON_RELTN

> This table stores the dates and statuses of queries to registries or gateways in attempts to query for documents.

**Description:** System Integration External Document Query Person Relationship  
**Table type:** ACTIVITY  
**Primary key:** `SI_XDOC_QUERY_PERSON_RELTN_ID`  
**Columns:** 21  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_MESSAGE_LOG table where the record contains information from the acknowledgement of the primary message. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `INTERNAL_MESSAGE_IDENT` | VARCHAR(60) | NOT NULL |  | ** OBSOLETE - this column is no longer used - replaced by usage of the SI_MESSAGE_LOG_ID field. |
| 4 | `MESSAGE_SEQUENCE` | DOUBLE | NOT NULL |  | ** OBSOLETE - this column is no longer used - replaced by usage of the SI_MESSAGE_LOG_ID field. |
| 5 | `MESSAGE_TYPE` | VARCHAR(100) |  |  | This will be the type of message sent for this query, Find Documents, Pix Query are just examples of what can be called. |
| 6 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization used to initiate the query. |
| 7 | `PARENT_QUERY_PRSN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Any row that ha this populated is a Child row to the primary query relationship. These will be spawned because of multiple messages that may be transmitted because of the initial query. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person being whose documents are being queried for. Foreign key to Person table. |
| 9 | `QUERY_FROM_DT_TM` | DATETIME |  |  | This is the date that the query is requesting documents from. |
| 10 | `QUERY_START_DT_TM` | DATETIME | NOT NULL |  | The date that the document query was initiated |
| 11 | `QUERY_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the querying, Queried, Success, Failure |
| 12 | `QUERY_STOP_DT_TM` | DATETIME | NOT NULL |  | The date that the document query was completed |
| 13 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CQM_OENINTERFACE_QUE table for the query that has been enqueued to a CQM listener, such as Open Engine. |
| 14 | `SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_MESSAGE_LOG table where the record contains the information related to the primary message |
| 15 | `SI_XDOC_QUERY_PERSON_RELTN_ID` | DOUBLE | NOT NULL | PK | The primary key of the table. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `USER_ID` | DOUBLE | NOT NULL | FK→ | The user that initiated the query. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACK_SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PARENT_QUERY_PRSN_RELTN_ID` | [SI_XDOC_QUERY_PERSON_RELTN](SI_XDOC_QUERY_PERSON_RELTN.md) | `SI_XDOC_QUERY_PERSON_RELTN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |
| `USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SI_EXT_REGISTRY_RESPONSE](SI_EXT_REGISTRY_RESPONSE.md) | `SI_XDOC_QUERY_PERSON_RELTN_ID` |
| [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `SI_XDOC_QUERY_PERSON_RELTN_ID` |
| [SI_XDOC_QUERY_PERSON_RELTN](SI_XDOC_QUERY_PERSON_RELTN.md) | `PARENT_QUERY_PRSN_RELTN_ID` |

