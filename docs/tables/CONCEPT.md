# CONCEPT

> The Concept table contains one row for each unique meaning or idea. A concept code has no intrinsic meaning. Its purpose is to link alternative names and views of the same concept together and to identify useful relationships between different concepts.

**Description:** Concept  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CKI` | VARCHAR(255) | NOT NULL |  | The CKID is composed of a source and an identifier. If the source cannot uniquely define an identifier, then the source will include a domain. These elements will always determine uniqueness whether created at Cerner, a third party content developer, or on a client site. Wherever possible we will use industry standard vocabularies to create this unique external identifier. |
| 7 | `CONCEPT_IDENTIFIER` | VARCHAR(242) | NOT NULL |  | A unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a concept. All Cerner assigned concept identifiers are created from the CONCEPT_SEQ. The sequence number is formatted to an 8-byte number padded |
| 8 | `CONCEPT_NAME` | VARCHAR(255) |  |  | The name of the concept, or idea, generally defaulted as the preferred string of the preferred term. |
| 9 | `CONCEPT_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents the external source that owns the concept_identifier. |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 11 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 12 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | The review status of the concept. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

