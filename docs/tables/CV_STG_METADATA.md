# CV_STG_METADATA

> This table holds the most recent version of metadata for a document sent from external sources (e.g. FHIR). Data retrieved from this table will be fed to other applications such as the reconciliation UI

**Description:** Cardiovascular Staging Metadata  
**Table type:** ACTIVITY  
**Primary key:** `CV_STG_METADATA_ID`  
**Columns:** 32  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORING_ORG` | VARCHAR(255) |  |  | A character filed which identifies the authoring organization. |
| 2 | `AUTHORING_ORG_ID` | DOUBLE |  |  | obsolete column - no longer used |
| 3 | `CATEGORY_TXT` | VARCHAR(255) |  |  | CATEGORY TXT |
| 4 | `CLIENT_ID_TXT` | VARCHAR(255) |  |  | Client ID of the incoming FHIR request |
| 5 | `CONFIDENTIALTY_TXT` | VARCHAR(80) |  |  | The sensitivity of the data held within the document.; |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE |  |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `CV_STG_METADATA_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `DOCUMENT_ACTION_STATUS_CD` | DOUBLE |  |  | Code value that represents the status of the imported document.; |
| 9 | `EFFECTIVE_END_DT_TM` | DATETIME |  |  | The clinically relevant end date and time. |
| 10 | `EFFECTIVE_END_TZ` | DOUBLE |  |  | EFFECTIVE END TIME ZONE |
| 11 | `EFFECTIVE_START_DT_TM` | DATETIME |  |  | The clinically relevant start date and time.; |
| 12 | `EFFECTIVE_START_TZ` | DOUBLE |  |  | EFFECTIVE START TIME ZONE |
| 13 | `ENCNTR_ID` | DOUBLE |  | FK→ | Unique identifier of the encounter.; |
| 14 | `EVENT_CD` | DOUBLE |  |  | Code value that represents the event associated with the diagnostic report.; |
| 15 | `EVENT_ID` | DOUBLE |  |  | Unique identifier of the event. This is from an EVENT_ID in the cinical_event table |
| 16 | `INERROR_REASON_TXT` | VARCHAR(255) |  |  | Reason for the Inerror action taken on the document. |
| 17 | `ISSUED_DT_TM` | DATETIME |  |  | The date and time at which this version of the document was issued.; |
| 18 | `ISSUED_TZ` | DOUBLE |  |  | ISSUED TIME ZONE |
| 19 | `PERSON_ID` | DOUBLE |  | FK→ | Unique identifier for the patient / PERSON |
| 20 | `RESOURCE_IDENT` | DOUBLE |  |  | Unique identifier of the external resource. |
| 21 | `RESOURCE_TYPE_TXT` | VARCHAR(255) |  |  | The FHIR resource type (e.g., DocumentReference, DiagnosticReport).; |
| 22 | `RESULT_STATUS_CD` | DOUBLE |  |  | Code value that represents the status of the diagnostic report.; |
| 23 | `STAGING_REASON_TXT` | VARCHAR(255) |  |  | The reason for staging.; |
| 24 | `TRANSMITTING_ORG` | VARCHAR(255) |  |  | A character filed which identifies the transmitting organization. |
| 25 | `TRANSMITTING_ORG_ID` | DOUBLE |  |  | obsolete column - no longer used |
| 26 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TZ` | DOUBLE |  |  | UPDT TIME ZONE |
| 32 | `VERSION_TXT` | VARCHAR(80) |  |  | Text representation of the Version number to identify the version of document stored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CV_EXT_IDENTIFIER](CV_EXT_IDENTIFIER.md) | `CV_STG_METADATA_ID` |
| [CV_FINDINGS](CV_FINDINGS.md) | `CV_STG_METADATA_ID` |
| [CV_STG_ACTION_ENTITY](CV_STG_ACTION_ENTITY.md) | `CV_STG_METADATA_ID` |
| [CV_STG_DOCUMENT](CV_STG_DOCUMENT.md) | `CV_STG_METADATA_ID` |

