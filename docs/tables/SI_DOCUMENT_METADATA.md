# SI_DOCUMENT_METADATA

> This table keeps track of the most recent version of documents, with keys to more specific document tables, and can be used for filtering documents.

**Description:** System Integration Document Metadata  
**Table type:** ACTIVITY  
**Primary key:** `SI_DOCUMENT_METADATA_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CLIENT_IDENT` | VARCHAR(100) | NOT NULL |  | The identifier of the client who last updated the document. |
| 7 | `CUR_DOC_ENTITY_ID` | DOUBLE | NOT NULL |  | The CURRENT OR NEWEST tracked version of a document's metadata from table identified in DOC_ENTITY_NAME |
| 8 | `DOC_ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | CODE SET:4002659; Status of the importing and staging of the document. |
| 9 | `DOC_ENTITY_NAME` | VARCHAR(30) |  |  | Parent Entity Name of the table from which the ID vaues come from for ROOT_DOC_ENTITY_ID and CUR_DOC_ENTITY_ID |
| 10 | `DOC_FORMAT_CD` | DOUBLE | NOT NULL |  | CODE SET:23; Allows a potential consumer to know how to render the specific media file format of the document and corresponds to the equivalent MIME type of the document as it was stored in CAMM |
| 11 | `DOC_REFERENCE_STATUS_CD` | DOUBLE | NOT NULL |  | CODE SET:8; Status of the document in the clinical workflow. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:ENCOUNTER_ONLY_SEQ; The primary encounter for the document. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_CD` | DOUBLE | NOT NULL |  | CODE SET:72; Specifies the precise kind of document (e.g. Pulmonary History and Physical, Discharge Summary, Ultrasound Report). |
| 15 | `MDOC_EVENT_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:CLINICAL_EVENT_SEQ; The Event ID of the Parent document that this record is related to.this value is from EVENT_ID in CLINICAL_EVENT. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:PERSON_ONLY_SEQ; The person related to the document. |
| 17 | `ROOT_DOC_ENTITY_ID` | DOUBLE | NOT NULL |  | The ROOT or ORIGINAL tracked version of a document's metadata from table identified in DOC_ENTITY_NAME |
| 18 | `SERVICE_STOP_DT_TM` | DATETIME |  |  | Represents the start time the service being document took place (clinically significant). |
| 19 | `SI_DOCUMENT_METADATA_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_DOCUMENT_IDENT_RELTN](SI_DOCUMENT_IDENT_RELTN.md) | `SI_DOCUMENT_METADATA_ID` |

