# SI_DOCUMENT_INFO

> Document information for documents sent out from Millennium, this may include CAMM address for generated documents.

**Description:** System Integration Document Information  
**Table type:** ACTIVITY  
**Primary key:** `SI_DOCUMENT_INFO_ID`  
**Columns:** 27  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_QUAL_DT_TM` | DATETIME |  |  | The beginning point for qualifying data for inclusion when asssembling an on demand CDA. |
| 2 | `DOCUMENT_UUID` | VARCHAR(255) |  |  | A system generated Unique Identifier for the document. Only assigned when the custodial organization does not have an OID |
| 3 | `DOC_SET_ROOT_EXTENSION` | VARCHAR(255) | NOT NULL |  | The set id for this CDA document. |
| 4 | `DOC_VERSION_NBR` | DOUBLE |  |  | The version number of current CDA document associated with the event_id. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Encounter Table, used for encounter level documents. |
| 6 | `END_QUAL_DT_TM` | DATETIME |  |  | The ending point for qualifying data for inclusion when asssembling an on demand CDA. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | A unique identifier to an event, used for events level documents. From the CLINICAL_EVENT table EVENT_ID column. |
| 8 | `MEDIA_OBJECT_IDENTIFIER` | VARCHAR(64) |  |  | Identifier of the document object if stored in the multimedia storage. |
| 9 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE | NOT NULL |  | Version of the identified document object in the multimedia storage. |
| 10 | `ON_DEMAND_IND` | DOUBLE | NOT NULL |  | True when the document is to be generated on-demand |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization responsible for stewardship of the document. |
| 12 | `OUTPUT_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | This defines the type of document being registered. |
| 13 | `PARENT_SI_DOCUMENT_INFO_ID` | DOUBLE | NOT NULL | FK→ | The related document in this table |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person related to the document being sent. |
| 15 | `REPORT_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The Template Identifier used by CDG to build the dataset for transformation. |
| 16 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SCH_EVENT table. This will be populated when documents are generated for visits. |
| 17 | `SI_DOCUMENT_INFO_ID` | DOUBLE | NOT NULL | PK | Primary Key to the SI_Document_Info table. |
| 18 | `SI_TEMPLATE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The Template Group used to create the document. This will be used for debugging and reporting purposes. |
| 19 | `START_DT_TM` | DATETIME |  |  | the 388 service call time where we can log the service invoke timestamp. |
| 20 | `SUMMARY_CARE_TYPE_CD` | DOUBLE | NOT NULL |  | This field will be populated if the generated document is marked as a summary of care document by the selected report template. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VALIDATION_VAL` | DOUBLE |  |  | Indicates whether the generated document is a valid document. It will use bit-operators to determine which sections were mandatory and failed validation. |
| 27 | `VALID_FROM_DT_TM` | DATETIME |  |  | Contains the Beginning Point of when the event is valid, used for event level documents. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PARENT_SI_DOCUMENT_INFO_ID` | [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `SI_DOCUMENT_INFO_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REPORT_TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SI_TEMPLATE_GROUP_ID` | [SI_TEMPLATE_GROUP](SI_TEMPLATE_GROUP.md) | `SI_TEMPLATE_GROUP_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SI_DOCUMENT_IDENTIFIER_R](SI_DOCUMENT_IDENTIFIER_R.md) | `SI_DOCUMENT_INFO_ID` |
| [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `PARENT_SI_DOCUMENT_INFO_ID` |
| [SI_DOCUMENT_RECIPIENT_RELTN](SI_DOCUMENT_RECIPIENT_RELTN.md) | `SI_DOCUMENT_INFO_ID` |
| [SI_DOCUMENT_TRANSACTION_LOG](SI_DOCUMENT_TRANSACTION_LOG.md) | `SI_DOCUMENT_INFO_ID` |
| [SI_REPO_REG_RELTN](SI_REPO_REG_RELTN.md) | `SI_DOCUMENT_INFO_ID` |

