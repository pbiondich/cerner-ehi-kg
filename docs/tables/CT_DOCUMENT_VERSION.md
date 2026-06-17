# CT_DOCUMENT_VERSION

> Contains the version information of documents

**Description:** CT DOCUMENT VERSION  
**Table type:** REFERENCE  
**Primary key:** `CT_DOCUMENT_VERSION_ID`  
**Columns:** 18  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | Begin Effective Date and Time |
| 3 | `CT_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | The document to which this version belongs |
| 4 | `CT_DOCUMENT_VERSION_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ct_document_version table. It is an internal system assigned number. |
| 5 | `DISPLAY_IND` | DOUBLE | NOT NULL |  | Indicates whether a document can be displayed outside the document manager or consenting process. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FILE_NAME` | VARCHAR(255) | NOT NULL |  | File name of the document |
| 8 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the long_blob table. It is an internal system assigned number. |
| 9 | `PREV_CT_DOCUMENT_VERSION_ID` | DOUBLE | NOT NULL | FK→ | The original value of ct_document_version_id used for grouping the related versions. Required for type2 versioning. |
| 10 | `PRINT_WITH_CONSENT_IND` | DOUBLE | NOT NULL |  | Indicates whether the document will be prompted to be printed when the consent is release for a patient. |
| 11 | `REVISION_ID` | DOUBLE | NOT NULL | FK→ | The revision_id , in case this document is associated with a revision |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VERSION_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | Textual description of the version |
| 18 | `VERSION_NBR` | DOUBLE | NOT NULL |  | The number of the version |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_DOCUMENT_ID` | [CT_DOCUMENT](CT_DOCUMENT.md) | `CT_DOCUMENT_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `PREV_CT_DOCUMENT_VERSION_ID` | [CT_DOCUMENT_VERSION](CT_DOCUMENT_VERSION.md) | `CT_DOCUMENT_VERSION_ID` |
| `REVISION_ID` | [REVISION](REVISION.md) | `REVISION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CT_DOCUMENT_BLOB](CT_DOCUMENT_BLOB.md) | `CT_DOCUMENT_VERSION_ID` |
| [CT_DOCUMENT_VERSION](CT_DOCUMENT_VERSION.md) | `PREV_CT_DOCUMENT_VERSION_ID` |
| [PT_CONSENT](PT_CONSENT.md) | `CT_DOCUMENT_VERSION_ID` |

