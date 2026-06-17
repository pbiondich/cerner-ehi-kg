# SI_XDOC_METADATA

> This table stores the metadata returned by document queries and holds the status of the possible retrieve.

**Description:** System Integration Document Metadata  
**Table type:** ACTIVITY  
**Primary key:** `SI_XDOC_METADATA_ID`  
**Columns:** 80  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AVAILABILITY_STATUS` | VARCHAR(40) | NOT NULL |  | an XDS Document shall have one of two availability statuses: Approved - available for patient care; Deprecated - obsolete |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CLASS_CD` | DOUBLE | NOT NULL |  | Specifies the particular kind of document (e.g. Prescription, Discharge Summary, Report). |
| 8 | `CLASS_CODE_DISPLAY_NAME` | VARCHAR(256) |  |  | The name to be displayed for communicating to a human the meaning of the classCode |
| 9 | `CLASS_CODE_TXT` | VARCHAR(100) |  |  | The literal value from the message of the class code associated with the document metadata. |
| 10 | `COMMENTS_ID` | DOUBLE | NOT NULL | FK→ | Free form text comments associated with the Document. The comments will be written on the long_text table. |
| 11 | `CONTENT_TYPE` | VARCHAR(255) |  |  | The content type of the document as it is stored in CAMM |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `CREATION_DT_TM` | DATETIME |  |  | Date and Time the author created the document in the source system |
| 14 | `DOC_ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the document in terms of the relationship with the database. Values include New or Processed. |
| 15 | `DOC_EVENT_ID` | DOUBLE | NOT NULL |  | The Event ID of the child document that this record is related to. - this value is from EVENT_ID in CLINICAL_EVENT. |
| 16 | `DOC_FORMAT_CD` | DOUBLE | NOT NULL |  | Allows a potential consumer to know how to render the specific media file format of the document and corresponds to the equivalent MIME type of the document as it was stored in CAMM. |
| 17 | `DOC_QUERIED_DT_TM` | DATETIME | NOT NULL |  | The date that the Document was queried. |
| 18 | `DOC_RETR_ACK_SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_MESSAGE_LOG table for the audited transport protocol message containing the acknowledgement after it is received inbound. |
| 19 | `DOC_RETR_COMPLETE_DT_TM` | DATETIME | NOT NULL |  | The date and time of when the retrieve of the related document finished. |
| 20 | `DOC_RETR_ERR_CODE` | VARCHAR(40) |  |  | A textual error code that represents an error in retrieval if any has occurred. |
| 21 | `DOC_RETR_ERR_TEXT` | VARCHAR(255) |  |  | The error text that was returned to the system if any errors had occurred during the retrieval. |
| 22 | `DOC_RETR_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CQM_OENINTERFACE_QUE table for an enqueued retrieval request. |
| 23 | `DOC_RETR_SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_MESSAGE_LOG table for the audited transport protocol message containing a retrieval request after it is sent outbound. |
| 24 | `DOC_RETR_START_DT_TM` | DATETIME | NOT NULL |  | The date and time of when the retrieve of the related document started. |
| 25 | `DOC_RETR_STATUS_CD` | DOUBLE | NOT NULL |  | Retrieval status of the document. Values include Queried, Completed, Retrieved, Parsed, Purged, Direct, and various Failures. (code set 4002660) |
| 26 | `DOC_TITLE` | VARCHAR(255) |  |  | Title of the document |
| 27 | `DOC_VALID_IND` | DOUBLE | NOT NULL |  | Indicates whether the retrieved document has been successfully validated against the XDOC_HASH, XDOC_SIZE (when available) and/or successfully passed an XML well-formedness check, or any other methods of validation relevant to the document type. |
| 28 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 29 | `FORMAT_CD` | DOUBLE | NOT NULL |  | Along with typeCode, should provide sufficient information to allow potential consumer to know if it will be able to process the document. Shall be sufficiently specific to ensure processing/display by identifying a document encoding, structure and template (e.g. for HITSP CCD, the fact that it complies with a CDA schema, a template, and choice of content-specific style sheet. |
| 30 | `FORMAT_CODE_TXT` | VARCHAR(100) |  |  | The literal value from the message of the format code associated with the document metadata. |
| 31 | `FORMAT_DISPLAY_NAME` | VARCHAR(256) |  |  | Raw text from the message related to the Format Code |
| 32 | `HEALTHCARE_FACILITY_TYPE_CD` | DOUBLE | NOT NULL |  | Represents the type of organizational setting of the clinical encounter during which the documented act occurred. Alias From: HCFACTYPCODE |
| 33 | `HEALTHCARE_FAC_TYPE_DISP_NAME` | VARCHAR(256) |  |  | Raw text from the message related to the healthcare facility type code. |
| 34 | `HEALTHCARE_FAC_TYPE_TXT` | VARCHAR(100) |  |  | The literal value from the message of the healthcare facility type associated with the document metadata. |
| 35 | `HOME_COMMUNITY_IDENT` | VARCHAR(100) |  |  | The Community shared by the creator of the document and the registry that the document was sent to. |
| 36 | `INSTANCE_IND` | DOUBLE | NOT NULL |  | Indicates whether the record is a document instance. |
| 37 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | Human language of character data in the document. As identified by the IETF RFC 3066. Code Set 36 |
| 38 | `LAST_INSTANCE_XDOC_METADATA_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_XDOC_METADATA record that identifies the last successfully retrieved document instance |
| 39 | `LEGAL_AUTH_NAME_FIRST` | VARCHAR(100) |  |  | First name of the person who signed as the legal authenticator. |
| 40 | `LEGAL_AUTH_NAME_FULL_FRMT` | VARCHAR(255) |  |  | Represents a participant who has legally authenticated the document within the authorInstitution. |
| 41 | `LEGAL_AUTH_NAME_LAST` | VARCHAR(100) |  |  | Last name of the person who signed as the legal authenticator. |
| 42 | `LEGAL_AUTH_NAME_MIDDLE` | VARCHAR(100) |  |  | Middle name of the person who signed as the legal authenticator. |
| 43 | `LEGAL_AUTH_NAME_PREFIX` | VARCHAR(50) |  |  | Prefix of the person who signed as the legal authenticator. |
| 44 | `LEGAL_AUTH_NAME_SUFFIX` | VARCHAR(50) |  |  | Suffix of the person who signed as the legal authenticator. |
| 45 | `MDOC_EVENT_ID` | DOUBLE | NOT NULL |  | The Event ID of the Parent document that this record is related to.this value is from EVENT_ID in CLINICAL_EVENT. |
| 46 | `MEDIA_OBJECT_IDENTIFIER` | VARCHAR(64) |  |  | Identifier of the document object if stored in the multimedia storage. |
| 47 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE |  |  | Version of the identified document object in the multimedia storage. |
| 48 | `MIME_TYPE` | VARCHAR(40) |  |  | MIME type of the document in the Repository |
| 49 | `NEW_REPOSITORY_UNIQUE_IDENT` | VARCHAR(100) |  |  | An optional new repository unique id that identifies the repository where the document instance was stored after generation. |
| 50 | `NEW_SOURCE_DOC_UNIQUE_IDENT` | VARCHAR(100) |  |  | A new source document unique id that identifies a new document instance. |
| 51 | `OBJECT_TYPE_DISPLAY` | VARCHAR(60) |  |  | The human-readable representation of the corresponding object_type_txt column for this record. |
| 52 | `OBJECT_TYPE_TEXT` | VARCHAR(60) |  |  | Describes the type of document received in terms of: on-demand, delayed generation, initial generation |
| 53 | `PARENT_DOCUMENT_IDENT` | VARCHAR(100) |  |  | The identifier of the parentDocument entry that represents the source of a document replacement, addendum, transformation, or signs relationship |
| 54 | `PARENT_DOCUMENT_RELTN` | VARCHAR(100) |  |  | Type of relationship that the document has with the parentDocument: Replace, addendum, transformation, or signs |
| 55 | `PARENT_DOC_EVENT_ID` | DOUBLE | NOT NULL |  | The parent event ID that will be passed down from the parent document in terms of appends and replacement documents. |
| 56 | `PARENT_MDOC_EVENT_ID` | DOUBLE | NOT NULL |  | The parent MDOC to be carried through the life cycle of the series of events created by document generation |
| 57 | `PARENT_SI_XDOC_METADATA_ID` | DOUBLE | NOT NULL | FK→ | The related document metadata record. |
| 58 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the queried document. |
| 59 | `PRACTICE_SETTING_CD` | DOUBLE | NOT NULL |  | Specifies the clinical specialty where the act that resulted in the document was performed. Alias From: PRACSETCODE |
| 60 | `PRACTICE_SETTING_DISPLAY_NAME` | VARCHAR(256) |  |  | Raw text from the message related to the Practice Setting Code. |
| 61 | `PRACTICE_SETTING_TXT` | VARCHAR(100) |  |  | The literal value from the message of the practice setting associated with the document metadata. |
| 62 | `REPOSITORY_UNIQUE_IDENT` | VARCHAR(100) | NOT NULL |  | An OID that is used to uniquely define the repository |
| 63 | `REPO_DOCUMENT_UNIQUE_IDENT` | VARCHAR(100) | NOT NULL |  | The Identifier known by the registry and repository to uniquely indentify the related document. |
| 64 | `SERVICE_START_DT_TM` | DATETIME | NOT NULL |  | Represents the start time the service being documented took place (clinically significant). |
| 65 | `SERVICE_STOP_DT_TM` | DATETIME | NOT NULL |  | Represents the stop time the service being documented took place (clinically significant) |
| 66 | `SI_XDOC_METADATA_ID` | DOUBLE | NOT NULL | PK | The primary key to the document metadata table. |
| 67 | `SI_XDOC_QUERY_PERSON_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to query relationship to track which query was responsible for this document. |
| 68 | `SOURCE_DOC_UNIQUE_IDENT` | VARCHAR(100) |  |  | Globally unique identifier assigned by the document creator to this document. May be used in the body of other XDS Documents to reference this document. Structure and format shall be consistent with the specification corresponding to the format attribute (e.g., DICOM 64 character numeric UID, HL7 CDA root^extension |
| 69 | `SOURCE_PATIENT_IDENT` | VARCHAR(255) |  |  | Represents the subject of care medical record identifier in the local MPI. It shall contain 2 parts: Authority Domain Id and an Id in the above domain. |
| 70 | `TRANSPORT_METHOD` | VARCHAR(20) |  |  | The transport used to retrieve the document. |
| 71 | `TYPE_CD` | DOUBLE | NOT NULL |  | Specifies the precise kind of document (e.g. Pulmonary History and Physical, Discharge Summary, Ultrasound Report). |
| 72 | `TYPE_CODE_DISPLAY_NAME` | VARCHAR(256) |  |  | Raw Text from the message related to the Type Code. |
| 73 | `TYPE_CODE_TXT` | VARCHAR(100) |  |  | The literal value from the message of the type code associated with the document metadata. |
| 74 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 75 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 76 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 77 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 78 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 79 | `XDOC_HASH` | VARCHAR(256) |  |  | Hash key of the XDS Document itself. |
| 80 | `XDOC_SIZE` | DOUBLE | NOT NULL |  | Size in bytes of the byte stream that was provided in the Register and Provide Transaction and stored by the XDS Document Repository. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENTS_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DOC_RETR_ACK_SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |
| `DOC_RETR_QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `DOC_RETR_SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |
| `LAST_INSTANCE_XDOC_METADATA_ID` | [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `SI_XDOC_METADATA_ID` |
| `PARENT_SI_XDOC_METADATA_ID` | [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `SI_XDOC_METADATA_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SI_XDOC_QUERY_PERSON_RELTN_ID` | [SI_XDOC_QUERY_PERSON_RELTN](SI_XDOC_QUERY_PERSON_RELTN.md) | `SI_XDOC_QUERY_PERSON_RELTN_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SI_XDOC_AUTHOR](SI_XDOC_AUTHOR.md) | `SI_XDOC_METADATA_ID` |
| [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `LAST_INSTANCE_XDOC_METADATA_ID` |
| [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `PARENT_SI_XDOC_METADATA_ID` |
| [SI_XDOC_METADATA_INFO](SI_XDOC_METADATA_INFO.md) | `SI_XDOC_METADATA_ID` |

