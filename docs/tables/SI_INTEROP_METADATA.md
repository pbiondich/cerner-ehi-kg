# SI_INTEROP_METADATA

> System Integration Advanced Interop Metadata

**Description:** SI INTEROP METADATA  
**Table type:** ACTIVITY  
**Primary key:** `SI_INTEROP_METADATA_ID`  
**Columns:** 38  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CATEGORY_TXT` | VARCHAR(100) |  |  | The category that the document belongs to. |
| 7 | `CLIENT_IDENT` | VARCHAR(100) | NOT NULL |  | The identifier of the client who last updated the document. |
| 8 | `CONFIDENTIALITY_TXT` | VARCHAR(100) | NOT NULL |  | The value which indicates the confidentiality of the document. |
| 9 | `DOC_ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | CODE SET:4002659; Status of the document in terms of the relationship with the database. Values include New or Processed. |
| 10 | `DOC_EVENT_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:CLINICAL_EVENT_SEQ; The Event ID of the child document that this record is related to. - this value is from EVENT_ID in CLINICAL_EVENT. |
| 11 | `DOC_FORMAT_CD` | DOUBLE | NOT NULL |  | CODE SET:23; Allows a potential consumer to know how to render the specific media file format of the document and corresponds to the equivalent MIME type of the document as it was stored in CAMM. |
| 12 | `DOC_REF_STATUS_CD` | DOUBLE | NOT NULL |  | document reference status code value |
| 13 | `DOC_TITLE` | VARCHAR(100) |  |  | Title of the document. |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:ENCOUNTER_ONLY_SEQ; The primary encounter for the document. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `EVENT_CD` | DOUBLE | NOT NULL |  | CODE SET:72; Specifies the precise kind of document (e.g. Pulmonary History and Physical, Discharge Summary, Ultrasound Report). |
| 17 | `FORMAT_CD` | DOUBLE | NOT NULL |  | CODE SET:4002390; Along with typeCode, should provide sufficient information to allow potential consumer to know if it will be able to process the document. Shall be sufficiently specific to ensure processing/display by identifying a document encoding, structure and template (e.g. for HITSP CCD, the fact that it complies with a CDA schema, a template, and choice of content-specific style sheet. |
| 18 | `INSTANCE_IND` | DOUBLE |  |  | Indicates whether the record is a document instance. |
| 19 | `LGL_AUTHENT_NAME_FULL_FRMT` | VARCHAR(255) |  |  | legal authenticator full name formatted |
| 20 | `LGL_AUTHENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | PRSNL ID of the authenticator |
| 21 | `MEDIA_OBJECT_IDENTIFIER` | VARCHAR(100) |  |  | Identifier of the document object if stored in the multimedia storage. |
| 22 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE |  |  | Version of the identified document object in the multimedia storage. |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:PERSON_ONLY_SEQ; The person related to the document. |
| 24 | `ROOT_METADATA_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:SI_DOCUMENT_SEQ; The ID of the oldest version of the document in this table. |
| 25 | `SERVICE_START_DT_TM` | DATETIME |  |  | Represents the start time the service being documented took place (clinically significant). |
| 26 | `SERVICE_START_TZ` | DOUBLE | NOT NULL |  | The time zone in which the service start date time was captured. |
| 27 | `SERVICE_STOP_DT_TM` | DATETIME |  |  | date and time service was stopped |
| 28 | `SERVICE_STOP_TZ` | DOUBLE | NOT NULL |  | The time zone in which the service stop date time was captured. |
| 29 | `SI_INTEROP_METADATA_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 30 | `UPDATE_DT_TM` | DATETIME |  |  | Date and time when the attachment (document) has been updated. |
| 31 | `UPDATE_TZ` | DOUBLE | NOT NULL |  | The time zone in which the update date time was captured. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `VERIFIED_DT_TM` | DATETIME |  |  | Date and time the document was verified. |
| 38 | `VERIFIED_TZ` | DOUBLE | NOT NULL |  | The time zone in which the verified date time was captured. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LGL_AUTHENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ROOT_METADATA_ID` | [SI_INTEROP_METADATA](SI_INTEROP_METADATA.md) | `SI_INTEROP_METADATA_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_INTEROP_AUTHOR](SI_INTEROP_AUTHOR.md) | `SI_INTEROP_METADATA_ID` |
| [SI_INTEROP_METADATA](SI_INTEROP_METADATA.md) | `ROOT_METADATA_ID` |

